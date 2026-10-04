#!/usr/bin/env python3
"""Audit SmartHausGroup/.github public profile and committed SMARTHAUS CI policy."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

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
        ".github/rulesets/release-approval.json",
        ".smarthaus/automation.yaml",
        ".smarthaus/ci.json",
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

    if load_json(ROOT / '.github/rulesets/protected-branches.json') != {'bypass_actors': [], 'conditions': {'ref_name': {'exclude': [], 'include': ['~DEFAULT_BRANCH', 'refs/heads/development', 'refs/heads/staging', 'refs/heads/main']}}, 'enforcement': 'active', 'name': 'protected-branches', 'rules': [{'type': 'deletion'}, {'type': 'non_fast_forward'}, {'type': 'required_signatures'}, {'parameters': {'allowed_merge_methods': ['merge'], 'dismiss_stale_reviews_on_push': True, 'require_code_owner_review': False, 'require_last_push_approval': False, 'required_approving_review_count': 0, 'required_review_thread_resolution': True}, 'type': 'pull_request'}], 'target': 'branch'}:
        audit.fail(".github/rulesets/protected-branches.json differs from approved signed-CI protection policy")
    if load_json(ROOT / '.github/rulesets/release-approval.json') != {'bypass_actors': [], 'conditions': {'ref_name': {'exclude': [], 'include': ['refs/heads/main']}}, 'enforcement': 'active', 'name': 'release-approval', 'rules': [{'parameters': {'allowed_merge_methods': ['merge'], 'dismiss_stale_reviews_on_push': True, 'require_code_owner_review': False, 'require_last_push_approval': False, 'required_approving_review_count': 1, 'required_review_thread_resolution': True}, 'type': 'pull_request'}], 'target': 'branch'}:
        audit.fail(".github/rulesets/release-approval.json differs from approved signed-CI protection policy")
    ci = load_json(ROOT / ".smarthaus/ci.json")
    if (ci.get("schema_version") != "smarthaus-ci-v1" or ci.get("baseline_version") != "2.0.0"
            or not {"syntax", "tests", "static_security", "dependencies", "build"} <= set(ci.get("checks", {}))):
        audit.fail("signed CI policy is missing required checks")
    if any((ROOT / ".github/workflows").glob("*.y*ml")):
        audit.fail("GitHub Actions workflows are present; this repository uses SMARTHAUS CI")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local", action="store_true", help="run local repository checks (the default)")
    parser.parse_args()
    audit = Audit()
    audit_local(audit)
    return audit.finish()


if __name__ == "__main__":
    raise SystemExit(main())
