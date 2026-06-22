# SmartHausGroup/.github Conformance Rollout

**Plan ID:** `plan:github-org-profile-conformance-rollout`
**Status:** `complete`
**Date:** 2026-06-22

## Phase 0 - Intent Definition

Build a repository-local conformance layer for `SmartHausGroup/.github` so the org profile repository can be safely tagged with `conformance=smarthaus-template-v1`.

The problem is that this active repository was outside the org conformance ruleset. The solution is to install mechanical CI gates, UCP-readable manifests, MA evidence, agent-file bindings, and supply-chain policy checks before the repo is tagged.

Non-goals: product runtime changes, cloud deployment, MAE publication, and AICP/UCP repin.

Guarantees: required checks fail closed, branch rulesets contain no bypass actors, human-review deadlock is absent, deterministic scorecards are green, and repo admission can be re-evaluated from tracked files.

Determinism: the same git tree and locked standards inputs produce the same conformance decision.

## Phase 1 - Governing Formula

```text
Admissible(.github) =
  ManifestValid
  and RulesetNonBypass
  and RequiredChecksPresent
  and MAEvidenceTraceable
  and ScorecardGreen
  and NoHumanDeadlock
```

Unknown or missing predicates return `NO_GO`.

## Phase 2 - Formal Calculus

`ManifestValid` means `configs/ucp/repo_cicd.yaml` names `SmartHausGroup/.github`, binds the required contexts, and points at the MA evidence set.

`RulesetNonBypass` means signed commits, linear history, no deletion, no force-push, strict required checks, and zero bypass actors.

`NoHumanDeadlock` means no pull-request approval quorum, no required CODEOWNERS review, and no last-push approval requirement for this solo-operator mode.

## Phase 3 - Lemmas

- `L-GITHUB-ORG-PROFILE-CICD-1`: a complete manifest gives UCP enough data to evaluate repo conformance.
- `L-GITHUB-ORG-PROFILE-CICD-2`: mechanical protected-branch rules prevent bypass without requiring impossible human quorum.
- `L-GITHUB-ORG-PROFILE-CICD-3`: required Make targets and workflows fail closed.
- `L-GITHUB-ORG-PROFILE-CICD-4`: MA docs, invariant, notebook, and scorecard provide traceability.
- `L-GITHUB-ORG-PROFILE-CICD-5`: UCP receipt policy keeps publication admission bound to remote CI evidence.

## Phase 4 - Invariants

Machine invariants live in `invariants/cicd_conformance.yaml` and bind to the `repo-cicd-conformance` and `evidence-pack` CI gates.

## Phase 5 - Notebook Development

Notebook evidence lives in `notebooks/ma/cicd_conformance.ipynb`. It is deterministic and seed-locked to `1729`.

## Phase 6 - Scorecard Validation

Scorecard evidence lives in `artifacts/scorecards/cicd_conformance.json` and must remain `GREEN`.

MAE v0.2.1 evidence is allowed only as local unsigned-limited validation context:

- bundle: `/Users/smarthaus/Projects/GitHub/mae/artifacts/releases/mathematical_autopsy_engine/0.2.1/com.smarthaus.mathematical-autopsy-engine-0.2.1.ucp.tar.gz`
- status: `unsigned_limited_local_candidate`
- promotion: blocked until package signing authority exists.

## Phase 7 - Extraction To Runtime

Runtime extraction for this tranche is the committed CI/governance control surface: workflows, rulesets, manifest, policy files, scripts, agent bindings, notebooks, and scorecards. No product runtime code is extracted.

## Acceptance

- Local validation passes. Completed 2026-06-22: repo conformance, evidence pack, agent bind check, supply-chain policy, Semgrep, Zizmor, Gitleaks, TruffleHog filesystem scan, and MAE v0.2.1 bundle digest verification.
- PR checks pass. Completed on PR #1.
- Merge commit is signed and verified: `02c9e67f56e56db94f9377ea868e6ab795ff8bb7`.
- Default-branch checks pass after merge.
- Org custom property is set: `conformance=smarthaus-template-v1`.
