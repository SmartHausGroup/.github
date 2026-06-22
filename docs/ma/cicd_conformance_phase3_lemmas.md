# SmartHausGroup/.github Repo CI/CD Conformance - Phase 3 Lemmas

## L-GITHUB-ORG-PROFILE-CICD-1 Manifest Binding

If `configs/ucp/repo_cicd.yaml` exists and declares `SmartHausGroup/.github`, profile `org-profile-governance`, required checks, Make targets, MA evidence, and locks, then the repository has enough data for conformance evaluation.

## L-GITHUB-ORG-PROFILE-CICD-2 Branch Non-Bypass

If `.github/rulesets/protected-branches.json` requires signed commits, linear history, no force push, no deletion, strict mechanical required checks, and no bypass actors, then protected branches have a deterministic no-bypass policy without requiring impossible multi-human approval.

## L-GITHUB-ORG-PROFILE-CICD-3 Fail-Closed Required Gates

If `repo-cicd-conformance`, `ai-validate-full`, `ai-evidence-pack`, and `ai-pack-verify` exit non-zero on failure, then required CI contexts cannot pass on failed validation.

## L-GITHUB-ORG-PROFILE-CICD-4 Evidence Traceability

If the MA evidence paths and scorecard exist and are green, then the repository CI/CD adoption is traceable.

## L-GITHUB-ORG-PROFILE-CICD-5 UCP Receipt Binding

If the manifest requires UCP receipts for commit, push, pull request, merge, release, and deploy, then UCP can fail closed when remote CI evidence or provenance receipts are missing.
