#!/usr/bin/env python3
"""Fail-closed verifier for SMARTHAUS repo CI/CD conformance."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    "configs/ucp/repo_cicd.yaml",
    "configs/ucp/standard_sources.yaml",
    "configs/ucp/standard_sources.lock",
    "configs/ucp/standard_toolchain.lock",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/repo-cicd-conformance.yml",
    ".github/workflows/org-governance-audit.yml",
    ".github/rulesets/protected-branches.json",
    "SECURITY.md",
    "docs/ma/cicd_conformance_phase0_intent.md",
    "docs/ma/cicd_conformance_phase1_formula.md",
    "docs/ma/cicd_conformance_phase2_calculus.md",
    "docs/ma/cicd_conformance_phase3_lemmas.md",
    "invariants/cicd_conformance.yaml",
    "notebooks/ma/cicd_conformance.ipynb",
    "artifacts/scorecards/cicd_conformance.json",
]


def fail(message: str) -> None:
    print(f"FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        fail(f"missing required files: {missing}")

    workflow = (ROOT / ".github/workflows/repo-cicd-conformance.yml").read_text(encoding="utf-8")
    for token in [
        "repo-cicd-conformance",
        "evidence-pack",
        "make repo-cicd-conformance",
        "make ai-pack-verify",
    ]:
        if token not in workflow:
            fail(f"workflow missing token {token}")

    manifest = (ROOT / "configs/ucp/repo_cicd.yaml").read_text(encoding="utf-8")
    for token in [
        "schema_version: 0.1.0",
        "repo-cicd-conformance",
        "evidence-pack",
        "requires_ucp_receipt: true",
        "blocks_without_remote_ci_evidence: true",
    ]:
        if token not in manifest:
            fail(f"manifest missing token {token}")

    ruleset = json.loads(
        (ROOT / ".github/rulesets/protected-branches.json").read_text(encoding="utf-8")
    )
    rules = ruleset.get("rules", [])
    rule_types = {rule.get("type") for rule in rules}
    for required in [
        "non_fast_forward",
        "deletion",
        "required_linear_history",
        "required_signatures",
        "required_status_checks",
    ]:
        if required not in rule_types:
            fail(f"ruleset missing rule {required}")
    if "pull_request" in rule_types:
        fail("ruleset reintroduces human-review deadlock; mechanical gates are required")
    if ruleset.get("bypass_actors") != []:
        fail("ruleset has bypass actors")
    status_rules = [rule for rule in rules if rule.get("type") == "required_status_checks"]
    if len(status_rules) != 1:
        fail("ruleset must contain exactly one required_status_checks rule")
    params = status_rules[0].get("parameters", {})
    if params.get("strict_required_status_checks_policy") is not True:
        fail("ruleset must require strict status checks")
    if params.get("do_not_enforce_on_create") is not False:
        fail("ruleset must enforce status checks on branch creation")
    contexts = {
        item.get("context")
        for item in params.get("required_status_checks", [])
        if isinstance(item, dict)
    }
    expected_contexts = {
        "repo-cicd-conformance",
        "evidence-pack",
        "verify",
        "validate",
        "secret-scan",
        "zizmor",
        "supply-chain-policy",
        "sbom-vulnerability-budget",
        "trufflehog",
        "semgrep",
        "ossf-scorecard",
        "org-governance-audit",
    }
    missing_contexts = sorted(expected_contexts - contexts)
    if missing_contexts:
        fail(f"ruleset missing required context(s): {missing_contexts}")

    scorecard = json.loads(
        (ROOT / "artifacts/scorecards/cicd_conformance.json").read_text(encoding="utf-8")
    )
    if scorecard.get("status") != "GREEN":
        fail("scorecard is not GREEN")
    determinism = scorecard.get("determinism", {})
    if determinism.get("seed_locked") is not True or determinism.get("seed") != 1729:
        fail("scorecard determinism is not seed locked")
    score = scorecard.get("score", {})
    if score.get("passed") != score.get("total"):
        fail("scorecard did not pass all invariants")

    print("repo CI/CD conformance verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
