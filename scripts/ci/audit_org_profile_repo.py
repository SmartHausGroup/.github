#!/usr/bin/env python3
"""Audit SmartHausGroup/.github public profile and GitHub settings posture."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

EXPECTED_REPO = "SmartHausGroup/.github"
EXPECTED_CONTEXTS = {
    "secret-scan",
    "trufflehog",
    "zizmor",
    "semgrep",
    "ossf-scorecard",
    "org-governance-audit",
}
EXPECTED_PROPERTIES = {
    "conformance": "smarthaus-template-v1",
    "product_family": "governance",
    "criticality": "high",
    "data_classification": "public",
    "release_model": "docs-governance",
    "owner_team": "platform",
    "lifecycle": "active",
}

PUBLIC_COPY_FILES = [
    "README.md",
    "profile/README.md",
    "products/README.md",
    "SECURITY.md",
]
FORBIDDEN_PUBLIC_PATHS = [
    ".agents",
    ".amazonq",
    ".continue",
    ".github/copilot-instructions.md",
    ".github/workflows/agent-files.yml",
    ".github/workflows/conformance.yml",
    ".github/workflows/release-trust.yml",
    ".github/workflows/repo-cicd-conformance.yml",
    ".github/workflows/supply-chain.yml",
    ".junie",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "Makefile.ai",
    "agent_governance",
    "artifacts",
    "compliance",
    "configs",
    "docs/governance",
    "docs/ma",
    "invariants",
    "mathematical-autopsy",
    "notebooks",
    "plans",
    "products/Components",
    "products/PALI",
    "products/Substrate",
    "research",
    "scorecards",
    "scripts/supply_chain_policy.py",
    "six-failures",
    "thesis",
    "tools/agents",
    "vision",
]
STALE_PUBLIC_PATTERNS = [
    (re.compile(r"\bv\d+\.\d+\.\d+\b"), "exact product version claim"),
    (re.compile(r"\bY\d+\s+H[12]\b", re.I), "relative roadmap date"),
    (re.compile(r"\b(pilot-ready|signed for distribution|productizes|lands)\b", re.I), "maturity or roadmap claim"),
    (re.compile(r"\b(75\+|700\+|880\+|~75|~700|~880)\b"), "unverified proof-count claim"),
    (re.compile(r"\b(SOC 2 Type II|PCI DSS|HIPAA compliant|GDPR compliant)\b", re.I), "unverified compliance claim"),
    (re.compile(r"\b555[- )]"), "placeholder phone number"),
    (re.compile(r"security@smarthaus\.group", re.I), "unverified security email domain"),
]


class Audit:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def require_file(self, path: str) -> Path:
        target = ROOT / path
        if not target.is_file():
            self.fail(f"missing required file: {path}")
        return target

    def finish(self) -> int:
        for warning in self.warnings:
            print(f"WARN: {warning}", file=sys.stderr)
        if self.failures:
            print("ORG PROFILE GOVERNANCE AUDIT FAILED:", file=sys.stderr)
            for failure in self.failures:
                print(f"  - {failure}", file=sys.stderr)
            return 1
        print("org profile governance audit passed")
        return 0


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def api_get(path: str, token: str) -> Any:
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def status_contexts_from_ruleset(ruleset: dict[str, Any]) -> set[str]:
    contexts: set[str] = set()
    for rule in ruleset.get("rules", []):
        if rule.get("type") != "required_status_checks":
            continue
        params = rule.get("parameters", {})
        for item in params.get("required_status_checks", []):
            if isinstance(item, dict) and item.get("context"):
                contexts.add(item["context"])
    return contexts


def audit_local(audit: Audit) -> None:
    required = [
        "README.md",
        "profile/README.md",
        "SECURITY.md",
        ".github/CODEOWNERS",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/feature_request.md",
        ".github/ISSUE_TEMPLATE/security_report.md",
        ".github/rulesets/protected-branches.json",
        ".github/workflows/org-governance-audit.yml",
        ".github/workflows/security.yml",
        ".github/workflows/static-analysis.yml",
        ".github/workflows/ossf-scorecard.yml",
        "scripts/ci/audit_org_profile_repo.py",
    ]
    for path in required:
        audit.require_file(path)

    for path in FORBIDDEN_PUBLIC_PATHS:
        if (ROOT / path).exists():
            audit.fail(f"public .github repo contains internal-facing path: {path}")

    for path in PUBLIC_COPY_FILES:
        target = audit.require_file(path)
        if not target.is_file():
            continue
        text = target.read_text(encoding="utf-8")
        for pattern, reason in STALE_PUBLIC_PATTERNS:
            if pattern.search(text):
                audit.fail(f"{path} contains stale or unbacked public copy: {reason}")

    codeowners = (ROOT / ".github/CODEOWNERS").read_text(encoding="utf-8")
    for owner in ["@Siniscalchi13", "@babuvenky76"]:
        if owner not in codeowners:
            audit.fail(f"CODEOWNERS missing {owner}")

    branch_ruleset = load_json(ROOT / ".github/rulesets/protected-branches.json")
    if branch_ruleset.get("bypass_actors") != []:
        audit.fail("protected-branches ruleset contains bypass actors")
    rule_types = {rule.get("type") for rule in branch_ruleset.get("rules", [])}
    for required_rule in ["deletion", "non_fast_forward", "required_linear_history", "required_signatures", "required_status_checks"]:
        if required_rule not in rule_types:
            audit.fail(f"protected-branches ruleset missing {required_rule}")
    contexts = status_contexts_from_ruleset(branch_ruleset)
    missing_contexts = sorted(EXPECTED_CONTEXTS - contexts)
    if missing_contexts:
        audit.fail(f"protected-branches ruleset missing contexts: {missing_contexts}")
    extra_contexts = sorted(contexts - EXPECTED_CONTEXTS)
    if extra_contexts:
        audit.fail(f"protected-branches ruleset contains internal or retired contexts: {extra_contexts}")
    for rule in branch_ruleset.get("rules", []):
        if rule.get("type") == "required_status_checks":
            params = rule.get("parameters", {})
            if params.get("strict_required_status_checks_policy") is not True:
                audit.fail("protected-branches ruleset does not require strict status checks")
            if params.get("do_not_enforce_on_create") is not False:
                audit.fail("protected-branches ruleset does not enforce status checks on branch creation")


def audit_live(
    audit: Audit,
    repo: str,
    require_live: bool,
    require_native_secret_protection: bool,
) -> None:
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        message = "live audit skipped because GH_TOKEN/GITHUB_TOKEN is not set"
        if require_live:
            audit.fail(message)
        else:
            audit.warn(message)
        return

    owner, name = repo.split("/", 1)
    try:
        metadata = api_get(f"/repos/{owner}/{name}", token)
        workflow_permissions = api_get(f"/repos/{owner}/{name}/actions/permissions/workflow", token)
        rulesets = api_get(f"/repos/{owner}/{name}/rulesets", token)
        properties = api_get(f"/repos/{owner}/{name}/properties/values", token)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        message = f"live audit API access failed: {exc}"
        if require_live:
            audit.fail(message)
        else:
            audit.warn(message)
        return

    if metadata.get("full_name") != repo:
        audit.fail(f"live repository mismatch: {metadata.get('full_name')} != {repo}")
    if metadata.get("default_branch") != "main":
        audit.fail("live default branch is not main")
    if metadata.get("visibility") != "public":
        audit.fail("live repository is not public")
    if metadata.get("delete_branch_on_merge") is not True:
        audit.fail("live delete_branch_on_merge is not enabled")
    if metadata.get("allow_merge_commit") is not False:
        audit.fail("live merge commits are still enabled")
    if metadata.get("allow_rebase_merge") is not False:
        audit.fail("live rebase merges are still enabled")
    if metadata.get("allow_squash_merge") is not True:
        audit.fail("live squash merges are not enabled")

    if workflow_permissions.get("default_workflow_permissions") != "read":
        audit.fail("live default workflow token permissions are not read-only")
    if workflow_permissions.get("can_approve_pull_request_reviews") is not False:
        audit.fail("live workflow tokens can approve pull request reviews")

    security = metadata.get("security_and_analysis") or {}
    for feature in [
        "secret_scanning",
        "secret_scanning_push_protection",
        "secret_scanning_non_provider_patterns",
    ]:
        status = (security.get(feature) or {}).get("status")
        if status != "enabled":
            message = (
                f"live {feature} is not enabled; native GitHub Secret Protection "
                "requires enterprise approval, so fail-closed CI secret scanners remain required"
            )
            if require_native_secret_protection:
                audit.fail(message)
            else:
                audit.warn(message)
    dependabot_status = (security.get("dependabot_security_updates") or {}).get("status")
    if dependabot_status != "enabled":
        audit.fail("live dependabot_security_updates is not enabled")

    live_contexts: set[str] = set()
    for ruleset in rulesets:
        if ruleset.get("target") != "branch" or ruleset.get("enforcement") != "active":
            continue
        try:
            detail = api_get(f"/repos/{owner}/{name}/rulesets/{ruleset['id']}", token)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            message = f"could not read live ruleset {ruleset.get('name')}: {exc}"
            if require_live:
                audit.fail(message)
            else:
                audit.warn(message)
            continue
        if detail.get("bypass_actors") not in ([], None):
            audit.fail(f"live ruleset {detail.get('name')} contains bypass actors")
        live_contexts.update(status_contexts_from_ruleset(detail))
    missing_live_contexts = sorted(EXPECTED_CONTEXTS - live_contexts)
    if missing_live_contexts:
        audit.fail(f"live rulesets missing required contexts: {missing_live_contexts}")
    extra_live_contexts = sorted(live_contexts - EXPECTED_CONTEXTS)
    if extra_live_contexts:
        audit.fail(f"live rulesets contain internal or retired contexts: {extra_live_contexts}")

    prop_map = {item.get("property_name"): item.get("value") for item in properties}
    for key, expected in EXPECTED_PROPERTIES.items():
        if prop_map.get(key) != expected:
            audit.fail(f"live custom property {key}={prop_map.get(key)!r}, expected {expected!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true", help="run local repository checks")
    parser.add_argument("--live", action="store_true", help="run live GitHub settings checks")
    parser.add_argument("--require-live", action="store_true", help="fail if live GitHub API access is unavailable")
    parser.add_argument(
        "--require-native-secret-protection",
        action="store_true",
        help="fail if GitHub-native Secret Protection is not enabled",
    )
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", EXPECTED_REPO))
    args = parser.parse_args()

    audit = Audit()
    run_local = args.local or not args.live
    if run_local:
        audit_local(audit)
    if args.live:
        audit_live(
            audit,
            args.repo,
            args.require_live,
            args.require_native_secret_protection,
        )
    return audit.finish()


if __name__ == "__main__":
    raise SystemExit(main())
