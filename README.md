# SmartHausGroup/.github

This repository is the organization-level GitHub control surface for
`SmartHausGroup`.

It has special behavior on GitHub, but only for specific file types. Everything
else in this repository is normal public repository content.

## What This Repository Owns

| Area | Path | Purpose |
|---|---|---|
| Organization profile | `profile/README.md` | Public copy shown on the `SmartHausGroup` organization page. |
| Community defaults | `.github/` | Default issue templates, pull request template, security policy, code of conduct, and CODEOWNERS. |
| Agent instruction bindings | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.amazonq/`, `.continue/`, `.junie/` | One canonical agent instruction set projected into tool-specific files. |
| Repo conformance | `configs/ucp/`, `docs/ma/`, `invariants/`, `notebooks/ma/`, `artifacts/scorecards/` | Evidence that this repository conforms to SMARTHAUS repo CI/CD rules. |
| Shared workflow examples | `.github/workflows/` | Workflows for this repo and patterns for other repos. Workflows here do not automatically run in other repositories. |
| Governance audit | `scripts/ci/` | Deterministic local checks for repo, policy, and live GitHub settings drift. |
| Supply-chain policy | `compliance/`, `scripts/supply_chain_policy.py` | Pinned-tool and scanning policy for this repo. |

## What This Repository Does Not Own

This repository is not the source of truth for:

- product code;
- product release status;
- production deployment secrets;
- cross-product standards;
- Marketplace package feeds;
- SharePoint product knowledge;
- customer commitments;
- per-repository branch protection enforcement outside this repo.

Authoritative locations:

- `SmartHausGroup/standards` - cross-product standards and GitHub governance rules.
- `SmartHausGroup/smarthaus-repo-template` - reusable repository baseline.
- product repositories - product code, product-specific docs, releases, and evidence.
- SharePoint Products site - browsable internal copies derived from governed sources.

## Special GitHub Behavior

GitHub treats some files in this repository specially:

- `profile/README.md` renders on the organization profile.
- community health files under `.github/` can be used as defaults by repositories
  that do not define their own.
- `SECURITY.md` can appear as the default security policy.

GitHub does not automatically apply these to every repo:

- workflows under `.github/workflows/`;
- ruleset JSON files under `.github/rulesets/`;
- scripts under `scripts/`;
- agent instructions;
- product documentation.

Those must be referenced, copied, enforced by rulesets, or applied through the
repo factory.

## Operating Rules

- Do not make product maturity, release, compliance, or security claims here
  unless they are current and backed by product evidence.
- Do not store secrets or private customer information here.
- Do not edit generated agent bind files directly. Edit `AGENTS.md`, then run
  `make agents-sync`.
- Do not use this repo as a product documentation dump. Public product copy here
  should be high-level and pointer-based.
- Keep this repo public-safe at all times.

## Local Commands

```bash
make validate
make repo-cicd-conformance
make ai-evidence-pack
make ai-pack-verify
make agents-check
make github-settings-audit
```

## Current Priority

The highest-priority governance work for this repository is keeping local
evidence, live GitHub settings, organization defaults, and public profile copy in
sync.

The live GitHub settings must match the committed policy. If a ruleset JSON,
workflow, security policy, or custom property exists only as a file but is not
applied in GitHub, it is evidence of intent, not enforcement.

GitHub-native Secret Protection is treated as an enterprise approval and cost
decision. Until it is approved and enabled, this repository must keep
fail-closed CI secret scanners active through the required `secret-scan` and
`trufflehog` checks.
