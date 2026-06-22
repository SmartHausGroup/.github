#!/usr/bin/env python3
"""SMARTHAUS supply-chain policy checks.

This script is intentionally dependency-light: PyYAML is available in the local and GitHub-hosted
Python runtimes used by the template. It emits deterministic scorecards without timestamps.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import pathlib
import re
import sys
from typing import Any

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
SPDX_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9.+-]*")


def load_yaml(path: pathlib.Path) -> Any:
    return yaml.safe_load(path.read_text()) or {}


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text())


def walk_values(node: Any):
    if isinstance(node, dict):
        for key, value in node.items():
            yield key, value
            yield from walk_values(value)
    elif isinstance(node, list):
        for item in node:
            yield from walk_values(item)


def workflow_files() -> list[pathlib.Path]:
    return sorted((ROOT / ".github" / "workflows").glob("*.yml"))


def semver_pinned(value: Any) -> bool:
    return isinstance(value, str) and bool(SEMVER_RE.fullmatch(value))


def workflow_text(name: str) -> str:
    path = ROOT / ".github" / "workflows" / name
    return path.read_text() if path.is_file() else ""


def file_exists(path: str) -> bool:
    return (ROOT / path).is_file()


def check_action_pinning(results: list[dict[str, Any]]) -> None:
    failures: list[str] = []
    for workflow in workflow_files():
        data = load_yaml(workflow)
        for key, value in walk_values(data):
            if key != "uses" or not isinstance(value, str):
                continue
            if value.startswith("./") or value.startswith("docker://"):
                continue
            if "@" not in value:
                failures.append(f"{workflow}: {value} has no ref")
                continue
            ref = value.rsplit("@", 1)[1]
            if not SHA_RE.fullmatch(ref):
                failures.append(f"{workflow}: {value} is not full-SHA pinned")
    results.append(
        {
            "name": "actions_sha_pinned",
            "pass": not failures,
            "detail": "all external actions are full-SHA pinned"
            if not failures
            else "; ".join(failures),
        }
    )


def check_checkout_hardening(results: list[dict[str, Any]]) -> None:
    failures: list[str] = []
    for workflow in workflow_files():
        data = load_yaml(workflow)
        jobs = data.get("jobs", {})
        for job_name, job in jobs.items():
            for step in job.get("steps", []):
                uses = step.get("uses")
                if isinstance(uses, str) and uses.startswith("actions/checkout@"):
                    with_block = step.get("with", {})
                    if with_block.get("persist-credentials") is not False:
                        failures.append(f"{workflow}:{job_name}: checkout persists credentials")
    results.append(
        {
            "name": "checkout_credentials_do_not_persist",
            "pass": not failures,
            "detail": "checkout persist-credentials=false everywhere"
            if not failures
            else "; ".join(failures),
        }
    )


def check_workflow_hardening(results: list[dict[str, Any]]) -> None:
    failures: list[str] = []
    for workflow in workflow_files():
        data = load_yaml(workflow)
        if "concurrency" not in data:
            failures.append(f"{workflow}: missing workflow concurrency")
        for job_name, job in data.get("jobs", {}).items():
            if "name" not in job:
                failures.append(f"{workflow}:{job_name}: missing job name")
    results.append(
        {
            "name": "workflow_concurrency_and_names",
            "pass": not failures,
            "detail": "all workflows have concurrency and named jobs"
            if not failures
            else "; ".join(failures),
        }
    )


def check_zizmor_gate(results: list[dict[str, Any]]) -> None:
    security = load_yaml(ROOT / ".github" / "workflows" / "security.yml")
    failures: list[str] = []
    text = (ROOT / ".github" / "workflows" / "security.yml").read_text()
    if "scripts/supply_chain_policy.py --zizmor-sarif" not in text:
        failures.append("security.yml does not parse zizmor SARIF")
    for job_name, job in security.get("jobs", {}).items():
        for step in job.get("steps", []):
            if "zizmor" in str(step.get("run", "")) and step.get("continue-on-error") is True:
                failures.append(f"security.yml:{job_name}: zizmor step is continue-on-error")
    results.append(
        {
            "name": "zizmor_is_gated",
            "pass": not failures,
            "detail": "zizmor SARIF is parsed and not soft-failed"
            if not failures
            else "; ".join(failures),
        }
    )


def check_supply_chain_files(results: list[dict[str, Any]]) -> None:
    required = [
        "compliance/supply-chain-tools.json",
        "compliance/vulnerability-budget.yml",
        "compliance/vulnerability-waivers.json",
        "compliance/license-policy.json",
        ".github/workflows/supply-chain.yml",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    tools = load_json(ROOT / "compliance" / "supply-chain-tools.json") if not missing else {}
    versions_pinned = semver_pinned(tools.get("syft")) and semver_pinned(tools.get("grype"))
    if not versions_pinned:
        missing.append("syft/grype versions must be semver-pinned")
    workflow_text = (
        (ROOT / ".github" / "workflows" / "supply-chain.yml").read_text()
        if file_exists(".github/workflows/supply-chain.yml")
        else ""
    )
    for needle in ["sha256sum -c -", "dir:.", "grype", "sbom:", "--vulnerability-budget"]:
        if needle not in workflow_text:
            missing.append(f"supply-chain workflow missing {needle}")
    results.append(
        {
            "name": "supply_chain_files_and_tools",
            "pass": not missing,
            "detail": "policy files and checksum-verified Syft/Grype workflow present"
            if not missing
            else "; ".join(missing),
        }
    )


def check_security_scanning_policy(results: list[dict[str, Any]]) -> None:
    failures: list[str] = []
    required = [
        "compliance/security-scanning-policy.json",
        ".gitleaks.toml",
        ".semgrep.yml",
        ".github/workflows/static-analysis.yml",
        ".github/workflows/security.yml",
    ]
    for path in required:
        if not file_exists(path):
            failures.append(f"missing {path}")

    tools = (
        load_json(ROOT / "compliance" / "supply-chain-tools.json")
        if file_exists("compliance/supply-chain-tools.json")
        else {}
    )
    for tool in ["gitleaks", "trufflehog", "semgrep"]:
        if not semver_pinned(tools.get(tool)):
            failures.append(f"{tool} version must be semver-pinned")

    policy = (
        load_json(ROOT / "compliance" / "security-scanning-policy.json")
        if file_exists("compliance/security-scanning-policy.json")
        else {}
    )
    if policy.get("semgrep_config") != ".semgrep.yml":
        failures.append("security-scanning policy must bind Semgrep to .semgrep.yml")
    if policy.get("gitleaks_config") != ".gitleaks.toml":
        failures.append("security-scanning policy must bind Gitleaks to .gitleaks.toml")
    for gate in ["secret-scan", "trufflehog", "semgrep"]:
        if gate not in policy.get("required_gates", []):
            failures.append(f"security-scanning policy missing required gate {gate}")

    static_text = workflow_text("static-analysis.yml")
    static = (
        load_yaml(ROOT / ".github" / "workflows" / "static-analysis.yml")
        if file_exists(".github/workflows/static-analysis.yml")
        else {}
    )
    semgrep_job = static.get("jobs", {}).get("semgrep", {})
    if semgrep_job.get("name") != "semgrep":
        failures.append("static-analysis workflow must expose semgrep job/context")
    for needle in [
        "SEMGREP_VERSION=$(python3 -c",
        'pipx run "semgrep==${SEMGREP_VERSION}"',
        "scan --config .semgrep.yml --error",
    ]:
        if needle not in static_text:
            failures.append(f"static-analysis workflow missing {needle}")

    security_text = workflow_text("security.yml")
    security = (
        load_yaml(ROOT / ".github" / "workflows" / "security.yml")
        if file_exists(".github/workflows/security.yml")
        else {}
    )
    if security.get("jobs", {}).get("secret-scan", {}).get("name") != "secret-scan":
        failures.append("security workflow must expose secret-scan job/context")
    if security.get("jobs", {}).get("trufflehog", {}).get("name") != "trufflehog":
        failures.append("security workflow must expose trufflehog job/context")
    for needle in [
        "gitleaks_${GITLEAKS_VERSION}_checksums.txt",
        "--config .gitleaks.toml",
        "trufflehog_${TRUFFLEHOG_VERSION}_checksums.txt",
        "sha256sum -c -",
        "--only-verified",
        "GIT_LFS_SKIP_SMUDGE=1",
        "RUNNER_TEMP/smarthaus-secret-tools",
    ]:
        if needle not in security_text:
            failures.append(f"security workflow missing {needle}")

    results.append(
        {
            "name": "security_scanning_policy",
            "pass": not failures,
            "detail": "Semgrep, Gitleaks, and TruffleHog gates are pinned and fail-closed"
            if not failures
            else "; ".join(failures),
        }
    )


def check_release_trust_policy(results: list[dict[str, Any]]) -> None:
    failures: list[str] = []
    for path in [
        "compliance/release-trust-policy.json",
        "compliance/reproducible-build-policy.json",
        ".github/workflows/release-trust.yml",
        ".github/rulesets/protected-tags.json",
    ]:
        if not file_exists(path):
            failures.append(f"missing {path}")

    tools = (
        load_json(ROOT / "compliance" / "supply-chain-tools.json")
        if file_exists("compliance/supply-chain-tools.json")
        else {}
    )
    if not semver_pinned(tools.get("cosign")):
        failures.append("cosign version must be semver-pinned")

    policy = (
        load_json(ROOT / "compliance" / "release-trust-policy.json")
        if file_exists("compliance/release-trust-policy.json")
        else {}
    )
    expected_true = [
        "require_slsa_provenance",
        "require_keyless_cosign_bundle",
        "require_digest_manifest",
        "require_protected_release_tags",
    ]
    for key in expected_true:
        if policy.get(key) is not True:
            failures.append(f"release-trust policy must set {key}=true")
    if policy.get("protected_tag_pattern") != "refs/tags/v*":
        failures.append("release-trust policy must protect refs/tags/v*")

    workflow = (
        load_yaml(ROOT / ".github" / "workflows" / "release-trust.yml")
        if file_exists(".github/workflows/release-trust.yml")
        else {}
    )
    text = workflow_text("release-trust.yml")
    release_job = workflow.get("jobs", {}).get("release-provenance", {})
    permissions = release_job.get("permissions", {})
    if permissions.get("id-token") != "write":
        failures.append("release-provenance job must grant id-token: write")
    if permissions.get("attestations") != "write":
        failures.append("release-provenance job must grant attestations: write")
    if release_job.get("name") != "release-provenance":
        failures.append("release-trust workflow must expose release-provenance job/context")
    for needle in [
        "cosign-release: v",
        "cosign sign-blob --yes --bundle",
        "actions/attest-build-provenance@",
        "actions/upload-artifact@",
        "sha256sum source.tar.gz > SHA256SUMS",
        "--mtime='UTC 1970-01-01'",
    ]:
        if needle not in text:
            failures.append(f"release-trust workflow missing {needle}")

    tag_ruleset = (
        load_json(ROOT / ".github" / "rulesets" / "protected-tags.json")
        if file_exists(".github/rulesets/protected-tags.json")
        else {}
    )
    if tag_ruleset.get("target") != "tag":
        failures.append("protected-tags ruleset must target tag")
    include = tag_ruleset.get("conditions", {}).get("ref_name", {}).get("include", [])
    if "refs/tags/v*" not in include:
        failures.append("protected-tags ruleset must include refs/tags/v*")
    if tag_ruleset.get("bypass_actors") != []:
        failures.append("protected-tags ruleset must have zero bypass actors")

    results.append(
        {
            "name": "release_trust_policy",
            "pass": not failures,
            "detail": (
                "release provenance, keyless signing, deterministic source archive, and "
                "protected tags are declared"
            )
            if not failures
            else "; ".join(failures),
        }
    )


def check_compliance_policy_files(results: list[dict[str, Any]]) -> None:
    failures: list[str] = []
    required = [
        "compliance/eol-support-policy.json",
        "compliance/vex-policy.json",
        "compliance/access-review-policy.json",
        "docs/governance/MASTER_TAKEOVER_PLAN.md",
    ]
    for path in required:
        if not file_exists(path):
            failures.append(f"missing {path}")
    license_policy = (
        load_json(ROOT / "compliance" / "license-policy.json")
        if file_exists("compliance/license-policy.json")
        else {}
    )
    if license_policy.get("default_decision") != "deny_unknown":
        failures.append("license policy must deny unknown licenses by default")
    for field in [
        "allowed_license_ids",
        "blocked_license_ids",
        "review_required",
        "unknown_license_allowlist",
    ]:
        if not isinstance(license_policy.get(field), list):
            failures.append(f"license policy missing list field {field}")
    manifest_policy = license_policy.get("unresolved_license_manifest", {})
    manifest_path = manifest_policy.get("path")
    manifest_sha = manifest_policy.get("sha256")
    if not isinstance(manifest_path, str) or not manifest_path:
        failures.append("license policy missing unresolved_license_manifest.path")
    elif not (ROOT / manifest_path).is_file():
        failures.append(f"missing {manifest_path}")
    if not isinstance(manifest_sha, str) or not SHA256_RE.fullmatch(manifest_sha):
        failures.append("license policy missing unresolved_license_manifest.sha256")
    elif isinstance(manifest_path, str) and (ROOT / manifest_path).is_file():
        actual_sha = sha256_file(ROOT / manifest_path)
        if actual_sha != manifest_sha:
            failures.append(
                f"{manifest_path} hash mismatch: policy={manifest_sha} actual={actual_sha}"
            )

    results.append(
        {
            "name": "compliance_policy_files",
            "pass": not failures,
            "detail": "license, VEX, EOL, access-review, and master plan policy files are present"
            if not failures
            else "; ".join(failures),
        }
    )


def check_ossf_scorecard_policy(results: list[dict[str, Any]]) -> None:
    failures: list[str] = []
    if not file_exists(".github/workflows/ossf-scorecard.yml"):
        failures.append("missing .github/workflows/ossf-scorecard.yml")
    workflow = (
        load_yaml(ROOT / ".github" / "workflows" / "ossf-scorecard.yml")
        if file_exists(".github/workflows/ossf-scorecard.yml")
        else {}
    )
    job = workflow.get("jobs", {}).get("ossf-scorecard", {})
    if job.get("name") != "ossf-scorecard":
        failures.append("OSSF Scorecard workflow must expose ossf-scorecard job/context")
    permissions = job.get("permissions", {})
    for key in ["contents", "issues", "pull-requests", "checks"]:
        if permissions.get(key) != "read":
            failures.append(f"ossf-scorecard job must grant {key}: read for private-repo analysis")
    text = workflow_text("ossf-scorecard.yml")
    for needle in [
        "ossf/scorecard-action@",
        "publish_results: false",
        "results_format: sarif",
    ]:
        if needle not in text:
            failures.append(f"OSSF Scorecard workflow missing {needle}")
    results.append(
        {
            "name": "ossf_scorecard_policy",
            "pass": not failures,
            "detail": (
                "OSSF Scorecard evidence workflow has private-repo read permissions and "
                "does not publish"
            )
            if not failures
            else "; ".join(failures),
        }
    )


def check_scanner_workspace_isolation(results: list[dict[str, Any]]) -> None:
    workflow = ROOT / ".github" / "workflows" / "supply-chain.yml"
    text = workflow.read_text() if workflow.is_file() else ""
    failures: list[str] = []
    required_needles = [
        "RUNNER_TEMP/smarthaus-tools",
        "RUNNER_TEMP/smarthaus-downloads",
        'SBOM_PATH="$RUNNER_TEMP/sbom.spdx.json"',
        'GRYPE_PATH="$RUNNER_TEMP/grype.json"',
    ]
    for needle in required_needles:
        if needle not in text:
            failures.append(f"supply-chain workflow missing isolated path {needle}")
    forbidden_needles = [
        "mkdir -p .tools",
        " -C .tools",
        ".tools/syft",
        ".tools/grype",
        "artifacts/sbom/sbom.spdx.json",
        "artifacts/sbom/grype.json",
    ]
    for needle in forbidden_needles:
        if needle in text:
            failures.append(
                f"supply-chain workflow scans or stores generated tooling in checkout via {needle}"
            )
    results.append(
        {
            "name": "scanner_workspace_isolated",
            "pass": not failures,
            "detail": "scanner tools, downloads, SBOM, and reports stay outside the checkout"
            if not failures
            else "; ".join(failures),
        }
    )


def check_renovate(results: list[dict[str, Any]]) -> None:
    renovate = load_json(ROOT / "renovate.json")
    failures: list[str] = []
    if renovate.get("rangeStrategy") != "pin":
        failures.append("rangeStrategy must be pin")
    if renovate.get("lockFileMaintenance", {}).get("enabled") is not True:
        failures.append("lockFileMaintenance must be enabled")
    if renovate.get("vulnerabilityAlerts", {}).get("enabled") is not True:
        failures.append("vulnerabilityAlerts must be enabled")
    action_rules = [
        rule
        for rule in renovate.get("packageRules", [])
        if "github-actions" in rule.get("matchManagers", [])
    ]
    if not any(rule.get("pinDigests") is True for rule in action_rules):
        failures.append("GitHub Actions must pin digests")
    results.append(
        {
            "name": "renovate_policy",
            "pass": not failures,
            "detail": "Renovate pins ranges/actions and enables vulnerability alerts"
            if not failures
            else "; ".join(failures),
        }
    )


def parse_zizmor_sarif(path: pathlib.Path) -> int:
    sarif = load_json(path)
    failures: list[str] = []
    for run in sarif.get("runs", []):
        for result in run.get("results", []):
            if result.get("level") == "error":
                failures.append(
                    f"{result.get('ruleId')}: {result.get('message', {}).get('text', '')}"
                )
    if failures:
        print("zizmor error findings:\n" + "\n".join(failures), file=sys.stderr)
        return 1
    return 0


def enforce_vulnerability_budget(grype_json: pathlib.Path, budget_path: pathlib.Path) -> int:
    report = load_json(grype_json)
    budget = load_yaml(budget_path)
    fail_on = {str(item).lower() for item in budget.get("fail_on", [])}
    waiver_path = ROOT / budget.get("allow_waivers_file", "compliance/vulnerability-waivers.json")
    waivers = load_json(waiver_path).get("waivers", [])
    required_fields = set(budget.get("waiver_required_fields", []))
    malformed = [w for w in waivers if not required_fields.issubset(w)]
    if malformed:
        print(f"malformed vulnerability waiver(s): {malformed}", file=sys.stderr)
        return 1
    waived = {(w.get("vulnerability_id"), w.get("package_name")) for w in waivers}
    failures: list[str] = []
    for match in report.get("matches", []):
        vuln = match.get("vulnerability", {})
        artifact = match.get("artifact", {})
        severity = str(vuln.get("severity", "")).lower()
        key = (vuln.get("id"), artifact.get("name"))
        if severity in fail_on and key not in waived:
            failures.append(f"{vuln.get('id')} {artifact.get('name')} {vuln.get('severity')}")
    if failures:
        print("vulnerability budget exceeded:\n" + "\n".join(failures), file=sys.stderr)
        return 1
    return 0


def license_expr_tokens(expr: str) -> set[str]:
    if expr in {"", "NOASSERTION", "NONE"}:
        return set()
    tokens = set(SPDX_TOKEN_RE.findall(expr.replace("(", " ").replace(")", " ")))
    return {token for token in tokens if token not in {"AND", "OR", "WITH"}}


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_purls(package: dict[str, Any]) -> list[str]:
    return sorted(
        str(item.get("referenceLocator"))
        for item in package.get("externalRefs", [])
        if item.get("referenceType") == "purl" and item.get("referenceLocator")
    )


def unresolved_license_identity(package: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": str(package.get("name", "UNKNOWN")),
        "version": str(package.get("versionInfo") or ""),
        "purls": package_purls(package),
    }


def unresolved_license_key(identity: dict[str, Any]) -> str:
    return json.dumps(identity, sort_keys=True, separators=(",", ":"))


def unresolved_license_manifest_identities(
    manifest: dict[str, Any],
) -> set[str]:
    packages = manifest.get("packages", [])
    if not isinstance(packages, list):
        return set()
    return {
        unresolved_license_key(
            {
                "name": str(item.get("name", "UNKNOWN")),
                "version": str(item.get("version") or ""),
                "purls": sorted(str(purl) for purl in item.get("purls", [])),
            }
        )
        for item in packages
        if isinstance(item, dict)
    }


def load_unresolved_license_manifest(policy: dict[str, Any]) -> tuple[set[str], list[str]]:
    manifest_policy = policy.get("unresolved_license_manifest", {})
    manifest_path = manifest_policy.get("path")
    manifest_sha = manifest_policy.get("sha256")
    failures: list[str] = []
    if not isinstance(manifest_path, str) or not manifest_path:
        return set(), ["license policy missing unresolved_license_manifest.path"]
    path = ROOT / manifest_path
    if not path.is_file():
        return set(), [f"missing unresolved license manifest {manifest_path}"]
    if not isinstance(manifest_sha, str) or not SHA256_RE.fullmatch(manifest_sha):
        failures.append("license policy missing unresolved_license_manifest.sha256")
    else:
        actual_sha = sha256_file(path)
        if actual_sha != manifest_sha:
            failures.append(
                f"{manifest_path} hash mismatch: policy={manifest_sha} actual={actual_sha}"
            )
    manifest = load_json(path)
    if manifest.get("schema_version") != "smarthaus.unresolved-license-manifest.v1":
        failures.append("unresolved license manifest schema_version mismatch")
    identities = unresolved_license_manifest_identities(manifest)
    if not identities and manifest_policy.get("allow_empty") is not True:
        failures.append("unresolved license manifest must contain package identities")
    return identities, failures


def unknown_license_allowed(package_name: str, policy: dict[str, Any]) -> bool:
    for item in policy.get("unknown_license_allowlist", []):
        pattern = item.get("package_name_pattern")
        reason = item.get("reason")
        if isinstance(pattern, str) and reason and fnmatch.fnmatch(package_name, pattern):
            return True
    return False


def enforce_license_policy(sbom_path: pathlib.Path, policy_path: pathlib.Path) -> int:
    sbom = load_json(sbom_path)
    policy = load_json(policy_path)
    allowed = set(policy.get("allowed_license_ids", []))
    blocked = set(policy.get("blocked_license_ids", []))
    review_required = set(policy.get("review_required", []))
    failures: list[str] = []
    unresolved_identities, manifest_failures = load_unresolved_license_manifest(policy)
    failures.extend(manifest_failures)

    for package in sbom.get("packages", []):
        name = str(package.get("name", "UNKNOWN"))
        expression = str(
            package.get("licenseConcluded") or package.get("licenseDeclared") or "NOASSERTION"
        )
        if expression == "NOASSERTION":
            expression = str(package.get("licenseDeclared") or "NOASSERTION")
        tokens = license_expr_tokens(expression)
        if not tokens:
            if unknown_license_allowed(name, policy):
                continue
            identity = unresolved_license_identity(package)
            if unresolved_license_key(identity) not in unresolved_identities:
                failures.append(
                    f"{name}: unknown license ({expression}) not present in unresolved manifest"
                )
            continue
        blocked_hits = sorted(tokens & blocked)
        if blocked_hits:
            failures.append(f"{name}: blocked license(s) {', '.join(blocked_hits)}")
        review_hits = sorted(tokens & review_required)
        if review_hits:
            failures.append(f"{name}: review-required license(s) {', '.join(review_hits)}")
        unknown_hits = sorted(
            token
            for token in tokens
            if token not in allowed and token not in blocked and token not in review_required
        )
        if unknown_hits:
            failures.append(f"{name}: unclassified license token(s) {', '.join(unknown_hits)}")

    if failures:
        print("license policy failed:\n" + "\n".join(failures), file=sys.stderr)
        return 1
    return 0


def write_unresolved_license_manifest(
    sbom_path: pathlib.Path, policy_path: pathlib.Path, output_path: pathlib.Path
) -> int:
    sbom = load_json(sbom_path)
    policy = load_json(policy_path)
    identities: dict[str, dict[str, Any]] = {}
    for package in sbom.get("packages", []):
        name = str(package.get("name", "UNKNOWN"))
        expression = str(
            package.get("licenseConcluded") or package.get("licenseDeclared") or "NOASSERTION"
        )
        if expression == "NOASSERTION":
            expression = str(package.get("licenseDeclared") or "NOASSERTION")
        tokens = license_expr_tokens(expression)
        if tokens or unknown_license_allowed(name, policy):
            continue
        identity = unresolved_license_identity(package)
        identity["reason"] = (
            "Syft SPDX output reports NOASSERTION for this manager-derived package; "
            "the package identity is frozen so newly unresolved packages fail closed."
        )
        identities[unresolved_license_key(identity)] = identity
    payload = {
        "schema_version": "smarthaus.unresolved-license-manifest.v1",
        "policy": "allow_only_committed_current_spdx_noassertion_identities",
        "packages": [identities[key] for key in sorted(identities)],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "path": str(output_path.relative_to(ROOT)),
                "package_count": len(payload["packages"]),
                "sha256": sha256_file(output_path),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def policy_scorecard() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    check_action_pinning(results)
    check_checkout_hardening(results)
    check_workflow_hardening(results)
    check_zizmor_gate(results)
    check_supply_chain_files(results)
    check_scanner_workspace_isolation(results)
    check_security_scanning_policy(results)
    check_release_trust_policy(results)
    check_compliance_policy_files(results)
    check_ossf_scorecard_policy(results)
    check_renovate(results)
    return {
        "schema_version": "smarthaus.scorecard.v1",
        "plan_id": "plan:github-org-profile-conformance-rollout",
        "overall": "GO" if all(item["pass"] for item in results) else "NO_GO",
        "determinism": {
            "timestamps_excluded": True,
            "randomness_used": False,
            "stable_inputs": [
                ".github/workflows/*.yml",
                "compliance/*.json",
                "compliance/*.yml",
                ".github/rulesets/*.json",
                ".semgrep.yml",
                "docs/governance/MASTER_TAKEOVER_PLAN.md",
                "renovate.json",
            ],
        },
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-scorecard", action="store_true")
    parser.add_argument("--zizmor-sarif")
    parser.add_argument("--grype-json")
    parser.add_argument("--vulnerability-budget")
    parser.add_argument("--license-spdx")
    parser.add_argument("--license-policy")
    parser.add_argument("--write-unresolved-license-manifest")
    args = parser.parse_args()

    if args.zizmor_sarif:
        return parse_zizmor_sarif(pathlib.Path(args.zizmor_sarif))
    if args.grype_json:
        if not args.vulnerability_budget:
            print("--vulnerability-budget is required with --grype-json", file=sys.stderr)
            return 2
        return enforce_vulnerability_budget(
            pathlib.Path(args.grype_json), ROOT / args.vulnerability_budget
        )
    if args.license_spdx:
        if not args.license_policy:
            print("--license-policy is required with --license-spdx", file=sys.stderr)
            return 2
        if args.write_unresolved_license_manifest:
            return write_unresolved_license_manifest(
                pathlib.Path(args.license_spdx),
                ROOT / args.license_policy,
                ROOT / args.write_unresolved_license_manifest,
            )
        return enforce_license_policy(pathlib.Path(args.license_spdx), ROOT / args.license_policy)

    scorecard = policy_scorecard()
    if args.write_scorecard:
        out = ROOT / "scorecards" / "supply_chain_scorecard.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(scorecard, indent=2, sort_keys=True) + "\n")
    print(json.dumps(scorecard, indent=2, sort_keys=True))
    return 0 if scorecard["overall"] == "GO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
