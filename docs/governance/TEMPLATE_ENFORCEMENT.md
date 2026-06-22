# Enforcing template use across the org

**There is no GitHub setting that forces every new repository to be created from a template.**
"Mark as template" only makes it *available* in the creation dropdown. Real enforcement is a combination:

## 1. Substantive enforcement (active for conformant repos)
Org-level **rulesets** apply the conformance/security gates to every repo carrying the org custom
property `conformance=smarthaus-template-v1`.

Active ruleset: `smarthaus-conformant-repos`.

Required controls:
- required status checks: `verify`, `validate`, `secret-scan`, `zizmor`,
  `supply-chain-policy`, `sbom-vulnerability-budget`, `trufflehog`, `semgrep`,
- signed commits,
- linear history,
- protected default branch,
- zero bypass actors.

Tag-scoped release controls:
- `release-provenance` creates a deterministic source archive, SHA-256 digest manifest, keyless
  Cosign bundle, and SLSA provenance for `refs/tags/v*`.
- `protected-release-tags` prevents release tag update and deletion.

Solo-operator policy:
- Human-review gates (`2 approvals`, required CODEOWNERS review, last-push approval) are **not**
  enforced while the org has a single active engineering operator. In that state they deadlock the
  organization instead of improving governance.
- `CODEOWNERS` still declares ownership boundaries and can be made required once enough eligible
  reviewers exist.

Owner-only controls still blocked by enterprise settings:
- GitHub Code Security / GHAS,
- GitHub secret scanning and push protection.

The template ships Gitleaks and TruffleHog as active fail-closed secret-scanning fallbacks until
GHAS-native secret scanning and push protection are enabled.

## 2. Operational enforcement of template origin
- **Repo-factory** (active workflow, credential-blocked until `FACTORY_TOKEN` is set): a GitHub App
  or fine-grained token path that creates repos from this template on request
  (`gh repo create --template SmartHausGroup/smarthaus-repo-template`). It preserves self-service and
  guarantees origin. Missing conformance tagging or team assignment fails closed.
- **Lock + funnel** (strongest, high blast radius): set org `members_can_create_repositories = false` so only admins / the factory can create repos. ⚠️ Removes self-serve repo creation for all members — get explicit owner sign-off before flipping.

## 3. Discoverability (weakest, default)
- Mark this repo as a **template** (`is_template: true`) and pin it as a recommended template so it appears in the dropdown.

Current operating mode: #1 is active for tagged repos; #2 is implemented and has `FACTORY_TOKEN`
configured; #3 is active because this repo is marked as a template. Direct org-wide creation
lock remains a separate owner decision because it removes member self-service.
