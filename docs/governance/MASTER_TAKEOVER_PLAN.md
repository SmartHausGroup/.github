# SMARTHAUS Repository Governance Master Takeover Plan

**Plan ID:** `ma-plan-smarthaus-repo-governance-master-v1`
**Status:** `approved-for-execution`
**Execution rule:** continue through every unblocked step; stop only for a hard blocker that requires owner, enterprise, or external service action.
**Primary reference implementation:** `SmartHausGroup/smarthaus-repo-template`
**First conformant child repo:** `SmartHausGroup/sage-core`
**Normative standard repo:** `SmartHausGroup/standards`

## Phase 0 - Intent Definition

We are building a governed repository admission system for SMARTHAUS repos.

The system solves four concrete problems:

- new repos can be created outside the template unless a factory and ruleset path exist,
- required controls drift unless the template, standards repo, and live org ruleset are reconciled,
- single-operator human review gates can deadlock delivery,
- child repos can claim conformance before their workflows and scorecards prove it.

Boundaries and non-goals:

- this plan does not implement product runtime code,
- this plan does not bypass UCP/AICP admission or claim AICP authority from instruction files alone,
- this plan does not claim GHAS, CodeQL, GitHub secret scanning, or push protection are active until GitHub owner/enterprise settings prove they are active,
- this plan does not disable member repo creation without explicit owner sign-off because that changes org-wide self-service behavior.

Required guarantees:

- every conformant repo has the canonical agent-file layer, file index, MA plans, invariants, scorecards, and required workflows,
- every hot workflow action is full-SHA pinned,
- required CI gates fail closed,
- org rulesets require only mechanical gates in solo-operator mode,
- release tags are protected from mutation and deletion,
- child repos are not tagged conformant until the required status contexts exist and pass.

Success criteria:

- template local gates pass,
- template PR merges green,
- `sage-core` receives the same proven controls and merges green,
- live org ruleset matches the committed required contexts for conformant repos,
- standards repo records the policy update,
- portfolio audit classifies every org repo before broader rollout.

Determinism:

For fixed tracked files and fixed GitHub API responses, the plan state is deterministic. Generated scorecards exclude timestamps and host-specific paths. Any nondeterministic external service state is classified as `BLOCKED` until verified.

## Phase 1 - Governing Formula

Let:

- `T` be the tracked template state,
- `S` be the tracked standards state,
- `C` be the set of conformant child repos,
- `O` be the live GitHub org ruleset/property state,
- `G(x)` be the local deterministic gate result for repo `x`,
- `H(x)` be the required GitHub status-check vector for repo `x`,
- `R(T,O)` be committed-ruleset/live-ruleset equivalence,
- `P` be the portfolio classification map.

The takeover is accepted iff:

```text
ACCEPT(T,S,C,O,P) =
  G(T)
  AND H(T)
  AND for every active child c in C: G(c) AND H(c)
  AND standards_reference_matches(S,T)
  AND R(T,O)
  AND portfolio_classification_complete(P)
```

Range:

- `GO`: all predicates true,
- `NO_GO`: a predicate is false and can be remediated in repo code or GitHub config under current authority,
- `BLOCKED`: a predicate requires owner/enterprise/external action.

## Phase 2 - Formal Calculus

Operators:

- `gate(repo, name)`: required command or GitHub check exits zero.
- `sha_pinned(workflow)`: all external `uses:` refs are 40-character commit SHAs.
- `context_set(ruleset)`: required status check contexts declared in ruleset JSON.
- `equiv(policy, live)`: semantic equivalence after ignoring GitHub API metadata not governed by the policy.
- `classify(repo)`: one of `conformant`, `near-conformant`, `legacy`, `archive`, `blocked`.

Boundary conditions:

- default-branch human-review gates are disabled while there is only one eligible engineering operator,
- release-trust gates are tag-scoped and are not default-branch required checks,
- GHAS-native controls are separate owner/enterprise enablement items,
- direct org repo creation lock is not flipped without explicit owner approval.

## Phase 3 - Lemmas

### L1 - Template Proof Before Propagation

Controls are first implemented in the template and accepted only after local scorecards and GitHub checks are green.

### L2 - Child Repo Inheritance

A child repo may inherit conformant status only after the template-proven controls are adapted without weakening invariant bindings.

### L3 - Ruleset Promotion

Live org rulesets may require a new status context only after that context exists and passes in every currently tagged conformant repo.

### L4 - Standards Reconciliation

The standards repo is updated only after the template implementation is proven, so normative text references actual enforcement rather than desired state.

### L5 - Portfolio Classification Before Broad Rollout

Repos not yet tagged conformant must be classified before requiring the full context set.

### L6 - External Settings Are Blockers, Not Green Claims

Owner/enterprise settings such as GHAS, CodeQL default setup, GitHub push protection, signed-commit org policy, or org-wide repo creation locks remain `BLOCKED` until verified live.

## Phase 4 - Invariants

Machine enforcement is split across:

- `invariants/INV-REPO-TEMPLATE-TAKEOVER.yaml`,
- `invariants/INV-SUPPLY-CHAIN.yaml`,
- child-repo copied invariants after propagation,
- standards CI gates,
- GitHub org rulesets.

Required default-branch contexts after this tranche:

- `verify`,
- `validate`,
- `secret-scan`,
- `zizmor`,
- `supply-chain-policy`,
- `sbom-vulnerability-budget`,
- `trufflehog`,
- `semgrep`.

Tag-scoped release context:

- `release-provenance`.

Evidence-only or non-required until promoted:

- `ossf-scorecard`.

## Phase 5 - Notebook Development

All repo-governance controls must have notebook-backed scorecards before runtime extraction. Current notebooks:

- `notebooks/governance/repo_takeover_verification.py`,
- `notebooks/governance/supply_chain_verification.py`.

Child repos must either retain these notebooks or adapt them with the same lemma and invariant coverage.

## Phase 6 - Scorecard Validation

Required scorecards:

- `scorecards/repo_takeover_scorecard.json`,
- `scorecards/supply_chain_scorecard.json`.

The scorecards must report `overall = GO` before controls are extracted or promoted.

## Phase 7 - Extraction And Rollout Order

1. Template implementation and local validation.
2. Template PR, GitHub checks, merge.
3. Child repo propagation to `sage-core`.
4. Child repo PR, GitHub checks, merge.
5. Live org ruleset promotion for new default-branch contexts.
6. Standards repo reconciliation.
7. Portfolio audit and classification.
8. Broader child-repo rollout by classification.

## Current Execution Status

| Workstream | State | Gate |
|---|---:|---|
| Canonical agent files and binds | Done | `verify` |
| File index | Done | `validate` |
| Repo factory with `FACTORY_TOKEN` | Done | `repo-factory` manual dispatch |
| Solo-operator branch ruleset baseline | Done | GitHub org ruleset |
| SHA-pinned actions and zizmor | Done | `zizmor`, `supply-chain-policy` |
| Syft SBOM and Grype vulnerability budget | Done | `sbom-vulnerability-budget` |
| Semgrep deterministic static analysis | Active | `semgrep` |
| Gitleaks + TruffleHog secret scanning | Active | `secret-scan`, `trufflehog` |
| License policy gate | Active | `sbom-vulnerability-budget` |
| Release trust: deterministic archive, Cosign, SLSA | Active | `release-provenance` on tags |
| Protected release tag descriptor | Active | `.github/rulesets/protected-tags.json` |
| VEX, EOL, reproducible build, access review policies | Active | `supply-chain-policy` |
| OSSF Scorecard | Evidence | `ossf-scorecard` |
| `sage-core` propagation | Pending | child repo PR |
| Live ruleset context promotion | Pending | after child repo green |
| Standards reconciliation | Pending | standards CI |
| Portfolio audit | Pending | org repo classification |

## Hard Blockers

The following are not blockers for this tranche, but remain blocked for full organization hardening until the named owner action is complete:

- GHAS / CodeQL / GitHub secret scanning / push protection: requires GitHub owner or enterprise enablement.
- Org-wide direct repo creation lock: requires explicit owner decision because it removes member self-service.
- Workstation gitsign enforcement: requires explicit developer-machine configuration approval.
- DCO/CLA legal text: requires legal/CTO approval before fail-closed contribution enforcement.
