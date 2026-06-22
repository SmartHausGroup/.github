# Master Plan Template

Use this as the canonical template for all execution plans in `/plans/`. Every plan MUST use this structure to ensure consistency, traceability, and deterministic agent execution. Plans are created in three formats (`.md`, `.yaml`, `.json`) with identical content; this template defines the Markdown format with inline examples and anti-drift guidance.

**Governance lock:** This template requires compliance with:
- `AGENTS.md` / `CLAUDE.md` (read FIRST — system instructions for all agents)
- `docs/governance/NORTH_STAR.md`
- `docs/governance/EXECUTION_PLAN.md`

**Schema:** See `agent_governance/PLAN_TEMPLATE_SCHEMA.yaml` and `agent_governance/PLAN_TEMPLATE_SCHEMA.json` for the machine-readable structure.

### CHECK:C-PLAN-SCHEMA (Mandatory)

Before execution, validate the plan file against the schema. The agent MUST run:

```bash
.venv/bin/python scripts/validate_plan_schema.py plans/<plan-name>/<plan-name>.yaml
```

Or the project's equivalent (e.g. `make validate-plan PLAN=plan-name`). If the command fails (non-zero exit or schema violation), the agent MUST NOT proceed; emit BLOCKED with `TASK: plan_schema_invalid`. This prevents plan drift over time.

---

## How to use this template

1. Copy `agent_governance/PLAN_TEMPLATE.md` to `plans/{plan-name}/{plan-name}.md`.
2. Fill every section. If a section does not apply, write `N/A — [reason]` (do not delete the section).
3. Create matching `.yaml` and `.json` files using `agent_governance/PLAN_TEMPLATE_SCHEMA.yaml` / `.json` as the structure.
4. Set `status: draft`. Get user approval. Only then change to `status: approved` and begin execution.
5. During execution, update Section 19 (Execution Outcome) as tasks complete.
6. On completion, update Section 18 (Governance Closure) and set `status: complete`.

**Agent constraint:** Do not add sections, fields, or tasks not in this template without explicit owner approval.

---

## Section 1: Plan Header

**Plan ID:** `plan:<fill-kebab-name>`
**Parent Plan ID:** `<fill or null if top-level>`
**Title:** `<fill human-readable title>`
**Version:** `<fill semver, e.g. 1.0>`
**Status:** `<draft | approved | in-progress | complete | blocked | cancelled | failed>` — Use only these values; see Lifecycle State Machine below.
**Owner:** `<fill team or individual>`
**Date Created:** `<fill YYYY-MM-DD>`
**Date Updated:** `<fill YYYY-MM-DD>`
**North Star Ref:** `docs/governance/NORTH_STAR.md`
**Execution Plan Ref:** `<fill section/item in docs/governance/EXECUTION_PLAN.md>`
**Domain:** `<framework | app | infrastructure | governance>`
**Math/Algorithm Scope:** `<true | false>`

### Inline example

```
Plan ID: plan:search-ranking-determinism
Parent Plan ID: plan:search-v2
Title: Search Ranking Determinism
Version: 1.0
Status: draft
Owner: Search Team
Date Created: 2026-02-22
Date Updated: 2026-02-22
North Star Ref: docs/governance/NORTH_STAR.md
Execution Plan Ref: docs/governance/EXECUTION_PLAN.md § Search Ranking v2
Domain: framework
Math/Algorithm Scope: true
```

### Anti-drift

**DO:** Fill every field. Use exact enum values for `status` and `domain`.

**DON'T:** Leave `version` blank. Don't omit `execution_plan_ref`. Don't use free-text for `status`.

### Plan Lifecycle State Machine (Mandatory)

Use only these states and transitions. Do not infer or invent states.

| From State | To State | Condition |
|------------|----------|-----------|
| draft | approved | Owner explicitly approves plan. |
| approved | in-progress | Agent begins execution with approval ("go"). |
| in-progress | blocked | Stop condition (missing ref, allowlist violation, schema fail). |
| in-progress | failed | Invariant/gate failure; deterministic replay fail. |
| in-progress | complete | All tasks done; gates pass. |
| blocked | approved | Owner updates plan/scope and re-approves only. |
| failed | cancelled | Owner cancels or re-scopes. |

- BLOCKED → approved requires human action; agent MUST NOT assume approval.

---

## Section 2: North Star Alignment

### Alignment

- **Source:** `docs/governance/NORTH_STAR.md`
- **Principles served:**
  - `<list specific North Star principles this plan advances>`
- **Anti-alignment (what this plan does NOT change):**
  - `<list what is explicitly preserved/unchanged>`

### Inline example

```
- Principles served:
  - Result quality (ranking must be accurate and reproducible)
  - Fail-closed determinism (scoring must be bit-reproducible)
  - Performance within SLA (< 200ms p95 latency)
- Anti-alignment:
  - Does NOT change indexing pipeline
  - Does NOT modify embedding model
  - Does NOT relax existing accuracy thresholds
```

### Anti-drift

**DO:** List specific principles by name from your North Star document.

**DON'T:** "This plan aligns with the North Star." (vague, no specifics)

---

## Section 3: Intent Capture

The plan MUST capture the user's stated requirements.

- **User's stated requirements:**
  - `<list each requirement in the user's words or unambiguous paraphrase>`
- **Intent doc ref:** `<path to intent doc, or "captured in this plan" if no separate doc>`
- **Intent verification:** `<"Plan requirements R1-Rn explicitly capture user's stated requirements listed above.">`

### Inline example

```
- User's stated requirements:
  - "Ranking must be deterministic — identical queries produce bit-identical results every run."
  - "NaN or Inf in any score component must fail-closed, not silently propagate."
  - "Monotonic in each score component given positive weights."
- Intent doc ref: captured in this plan (no separate intent doc)
- Intent verification: Plan requirements R1-R3 explicitly capture the three user-stated
  requirements above. R1 maps to determinism. R2 maps to fail-closed. R3 maps to monotonicity.
```

### Anti-drift

**DO:** Use the user's actual words or an unambiguous paraphrase. Trace each user requirement to an Rx.

**DON'T:** Rewrite the user's intent in vague terms. Don't skip this section.

---

## Section 4: Objective

- **Objective:** `<1-3 sentences: what this plan delivers>`
- **Current state:** `<what is broken or missing right now, with evidence>`
- **Target state:** `<what "done" looks like, with measurable outcomes>`

### Inline example

```
- Objective: Implement deterministic, monotonic, fail-closed ranking for the search system
  and validate via notebook-first verification with scorecard artifact.
- Current state: Ranking function exists but permits non-deterministic ordering on equal
  scores and does not check for NaN/Inf. No invariants or verification notebook exist.
- Target state: Ranking produces bit-identical results across seeded runs; NaN/Inf triggers
  fail-closed; monotonicity proven across 1000-sample sweep; scorecard artifact green on
  all three invariants; runtime module extracted from notebook.
```

### Anti-drift

**DO:** State current state with evidence (what's broken, what's missing). State target state with measurable outcomes.

**DON'T:** "Improve the ranking system." (no current state, no measurable target)

---

## Section 5: Scope

### In scope (conceptual)

- `<list of what work is included>`

### Out of scope (conceptual)

- `<list of what is explicitly excluded>`

### File allowlist (agent MAY touch these)

- `<exact paths or globs>`

### File denylist (agent MUST NOT touch these)

- `<exact paths or globs>`

### Scope fence rule

Agent must STOP and re-scope if any file outside the allowlist is needed. Do not proceed; emit BLOCKED.

### Inline example

```
In scope:
- Implement ranking function with determinism, monotonicity, fail-closed guarantees
- Create verification notebook
- Create invariants and lemmas
- Extract runtime module after scorecard green

Out of scope:
- Indexing pipeline changes
- Embedding model modifications
- UI changes
- Threshold recalibration for other components

File allowlist:
- notebooks/math/search_ranking_verification.ipynb
- invariants/INV-RANK-*.yaml
- invariants/INDEX.yaml
- configs/generated/search_ranking_scorecard.json
- docs/math/RANKING_MATHEMATICS.md
- docs/math/LEMMAS_APPENDIX.md (append only)
- src/<project>/ranking.py (extraction target only, after S green)

File denylist:
- src/<project>/indexing/** (indexing pipeline)
- src/<project>/core/** (core engine)
- configs/policy/** (policy configs)
- Any file not in allowlist
```

### Anti-drift

**DO:** List every file the agent may touch, by exact path or narrow glob.

**DON'T:** "The agent can modify relevant files." (unbounded scope)

---

## Section 6: Requirements

Requirements use `R{n}` format so prompts can reference `plan:{plan-id}:R{n}`.

### R1

- **Ref:** `plan:<plan-id>:R1`
- **Description:** `<1-2 sentences, specific>`
- **Acceptance criteria:** `<measurable: boolean gate or numeric threshold>`
- **Depends on:** `<list of Rx or external prereqs, or "none">`
- **User intent trace:** `<which user stated requirement from Section 3 this satisfies>`

### R2

- **Ref:** `plan:<plan-id>:R2`
- **Description:**
- **Acceptance criteria:**
- **Depends on:**
- **User intent trace:**

`<add more Rx as needed>`

### Inline example

```
R1
- Ref: plan:search-ranking-determinism:R1
- Description: Ranking function produces bit-identical outputs given identical inputs and seeds.
- Acceptance criteria: deterministic_replay_pass == true across seeds [42, 123, 256].
- Depends on: none
- User intent trace: User requirement 1 ("identical queries produce bit-identical results")

R2
- Ref: plan:search-ranking-determinism:R2
- Description: NaN or Inf in any score component triggers fail-closed (empty result + error flag).
- Acceptance criteria: failclosed_pass == true in scorecard; zero false accepts on NaN test set.
- Depends on: none
- User intent trace: User requirement 2 ("NaN or Inf must fail-closed")

R3
- Ref: plan:search-ranking-determinism:R3
- Description: Composite score is strictly monotone in each component given positive weight.
- Acceptance criteria: monotonicity_violations == 0 across 1000-sample sweep.
- Depends on: R1 (determinism must hold for monotonicity tests to be meaningful)
- User intent trace: User requirement 3 ("monotonic in each score component")
```

### Anti-drift

**DO:** Each requirement has measurable acceptance criteria and traces to a user stated requirement.

**DON'T:** "R1: Make ranking better." (not measurable, no acceptance criteria, no intent trace)

---

## Section 7: Execution Sequence

- **Ordering:** `<list of task IDs in strict execution order>`
- **Stop on first failure:** `true`
- **Strict ordering rule:** Do not start task N+1 until task N exit criteria are met.
- **MATHS phase mapping (if math/algorithm scope):**

| Task | MATHS phase | Description |
|------|-------------|-------------|
| `<task-id>` | `<M / A / T / H / S>` | `<brief>` |

### Inline example

```
- Ordering: [T1, T2, T3, T4, T5, T6, T7]
- Stop on first failure: true
- MATHS phase mapping:
  | Task | MATHS phase | Description |
  |------|-------------|-------------|
  | T1   | M           | Intent + problem definition |
  | T2   | A           | Governing formula + calculus |
  | T3   | T           | Lemmas + invariants |
  | T4   | H           | Verification notebook |
  | T5   | S           | Scorecard + stress test |
  | T6   | H (extract) | Runtime extraction (after T5 green) |
  | T7   | —           | Governance closure |
```

---

## Section 8: Task Breakdown

Repeat this block for every task in the execution sequence.

### T1 — `<task name>`

- **Ref:** `plan:<plan-id>:T1`
- **Description:** `<what this task does, 1-3 sentences>`
- **Requirement refs:** `<which Rx this task satisfies>`
- **Depends on:** `<which tasks must complete first, or "none">`
- **MATHS phase:** `<M / A / T / H / S / N/A>`
- **Deliverables:**
  - `<specific file path or artifact>`
- **Exit criteria:**
  - `<how to know this task is done — command output, artifact existence, assertion result>`
- **Validation command:** `<exact executable command>`. For steps that require human judgment only, set `REQUIRES_HUMAN_APPROVAL: true` and `BLOCK_IF_UNSET: true` in the task; do not use "manual review" as a validation command.
- **Implementation notes:** `<code patterns, approaches, decisions — optional but recommended>`

### Inline example

```
T3 — Create lemmas and invariants

- Ref: plan:search-ranking-determinism:T3
- Description: Define lemmas L1 (monotonicity) and L2 (deterministic replay); create
  invariant YAMLs INV-RANK-DETERMINISM, INV-RANK-MONOTONICITY, INV-RANK-FAILCLOSED;
  register in INDEX.yaml and LEMMAS_APPENDIX.md.
- Requirement refs: R1, R2, R3
- Depends on: T2 (governing formula must be locked before lemmas can reference it)
- MATHS phase: T (Tie)
- Deliverables:
  - invariants/INV-RANK-DETERMINISM.yaml
  - invariants/INV-RANK-MONOTONICITY.yaml
  - invariants/INV-RANK-FAILCLOSED.yaml
  - invariants/INDEX.yaml (updated with 3 new entries)
  - docs/math/LEMMAS_APPENDIX.md (L1, L2 added)
- Exit criteria:
  - All 3 invariant YAML files exist and pass YAML lint.
  - INDEX.yaml contains entries for all 3 invariant IDs.
  - LEMMAS_APPENDIX.md contains L1 and L2 with all required sub-fields.
- Validation command: .venv/bin/python -c "import yaml; [yaml.safe_load(open(f)) for f in ['invariants/INV-RANK-DETERMINISM.yaml', 'invariants/INV-RANK-MONOTONICITY.yaml', 'invariants/INV-RANK-FAILCLOSED.yaml']]"
- Implementation notes: Use invariants/INV_TEMPLATE.yaml as the structure. Status: proposed
  (will be promoted to accepted after T5 scorecard green).
```

### Anti-drift

**DO:** Per-task exit criteria that are verifiable (command, assertion, file existence). Per-task requirement traceability.

**DON'T:** "T3: Create invariants." (no exit criteria, no requirement refs, no deliverables list)

**DO:** Validation commands use `.venv/bin/python` (per project venv convention).

**DON'T:** `python scripts/...` (may not use project venv)

---

## Section 9: Gate Checks

Gates validate that plan requirements are met. List every gate.

### CHECK:C0 — `<gate name>`

- **Description:** `<what this gate validates>`
- **Task ref:** `<which task(s) this gate validates>`
- **Validation command:** `<exact command to run>`
- **Pass criteria:** `<what output means pass>`
- **Fail action:** `<block | rollback | escalate>`

### Decision rule

- **GO:** All gates pass.
- **NO-GO:** Any gate fails.

### No-go triggers

- `<explicit list of conditions that force NO-GO>`

### Inline example

```
CHECK:C0 — Governance preflight
- Description: All governance files, rules, and plan surfaces present.
- Task ref: T1
- Validation command: ls AGENTS.md docs/governance/NORTH_STAR.md docs/governance/EXECUTION_PLAN.md
- Pass criteria: All files exist (exit code 0).
- Fail action: block

CHECK:C1 — Invariants indexed
- Description: All 3 invariant YAMLs exist and are registered in INDEX.yaml.
- Task ref: T3
- Validation command: .venv/bin/python -c "import yaml; idx=yaml.safe_load(open('invariants/INDEX.yaml')); ids=[i['id'] for i in idx['invariants']]; assert 'INV-RANK-DETERMINISM' in ids and 'INV-RANK-MONOTONICITY' in ids and 'INV-RANK-FAILCLOSED' in ids"
- Pass criteria: Assertion passes (exit code 0).
- Fail action: block

CHECK:C2 — Scorecard green
- Description: Scorecard artifact exists with all invariant checks passing.
- Task ref: T5
- Validation command: .venv/bin/python scripts/ci/scorecard_gate.py --output configs/generated/search_ranking_scorecard.json
- Pass criteria: final_decision == "GO" in output JSON.
- Fail action: block

Decision rule:
- GO: C0, C1, C2 all pass.
- NO-GO: any gate fails.

No-go triggers:
- Missing invariant YAML or INDEX entry.
- Scorecard final_decision != "GO".
- Any invariant check false in scorecard.
- Deterministic replay divergence > 0.
- Unapproved threshold modification.
- File outside allowlist touched.
```

---

## Section 10: Determinism Requirements

*Required when `math_algorithm_scope: true` or when the plan involves computation. Write `N/A` if not applicable.*

- **Seed locking:**
  - `<which libraries, which seeds, what values>`
- **Device policy:**
  - `<CPU / GPU / MPS rules>`
- **Float precision:**
  - `<float32 / float64 / rounding policy>`
- **Replay verification:**
  - `<how many seeds, what comparison method>`
- **Deterministic algorithms:**
  - `<torch.use_deterministic_algorithms(True), np.random.seed(), etc.>`

### Inline example

```
- Seed locking: numpy seed=42, random seed=42. All seeds set before any computation.
- Device policy: CPU only (no GPU/MPS variance). Pure numpy, no torch.
- Float precision: float64 throughout. No float32 intermediate values.
- Replay verification: 3 seeds [42, 123, 256]; bit-identical output arrays required.
- Deterministic algorithms: numpy stable sort (kind='stable') for ranking.
```

---

## Section 11: Artifacts

List every artifact this plan produces.

| Path | Format | Producer | Schema ref | Validation |
|------|--------|----------|------------|------------|
| `<exact path>` | `<JSON/YAML/.pt/.ipynb/.py>` | `<task ID>` | `<link to schema or "inline">` | `<no NaN/Inf, schema match, etc.>` |

### Inline example

```
| Path | Format | Producer | Schema ref | Validation |
|------|--------|----------|------------|------------|
| configs/generated/search_ranking_scorecard.json | JSON | T5 | See Section 9 scorecard schema | no NaN/Inf; final_decision is "GO" or "NO-GO" |
| invariants/INV-RANK-DETERMINISM.yaml | YAML | T3 | invariants/INV_TEMPLATE.yaml | valid YAML; all required fields present |
| notebooks/math/search_ranking_verification.ipynb | ipynb | T4 | notebook-first rules | runs end-to-end; all assertions pass |
| src/<project>/ranking.py | Python | T6 | notebook extraction | py_compile passes |
```

---

## Section 12: Environment Prerequisites

- **Python version:** `<e.g. >=3.11>`
- **Virtual environment:** `.venv/bin/python`
- **Dependencies beyond requirements.txt:** `<list, or "none">`
- **Hardware requirements:** `<CPU / GPU / MPS / memory, or "standard CI">`
- **External data:** `<datasets, models, APIs needed, or "none">`
- **Pre-notebook check:** `<make pre-notebook-check if notebooks involved, or "N/A">`

---

## Section 13: Implementation Approach

- **Options considered:**
  - Option A: `<description, pros, cons>`
  - Option B: `<description, pros, cons>`
- **Chosen approach:** `<which option and why>`
- **Rejected approaches:** `<what was rejected and why>`
- **ADR ref:** `<link to ADR if architectural decision, or "N/A">`

### Anti-drift

**DO:** Document at least two options with pros/cons, even if one is clearly better. This prevents the agent from re-inventing discarded ideas.

**DON'T:** Skip this section. If you don't document rejected approaches, the agent may try them.

---

## Section 14: Risks and Mitigations

| Risk | Impact | Mitigation | Status |
|------|--------|------------|--------|
| `<description>` | `<high / medium / low>` | `<how to prevent/handle>` | `<open / mitigated / accepted / materialized>` |

### Hard blockers (things that stop the plan entirely)

- `<list>`

### Inline example

```
| Risk | Impact | Mitigation | Status |
|------|--------|------------|--------|
| NaN propagation through weighted sum | high | Fail-closed check before computation | mitigated |
| Unstable sort producing different orderings | high | Use np.argsort(kind='stable') | mitigated |
| Float precision edge cases | medium | float64 throughout + rounding to 15 sig digits | mitigated |

Hard blockers:
- Scorecard final_decision == "NO-GO" (cannot extract until green).
- Any invariant YAML missing or malformed (blocks T5).
```

---

## Section 15: Rollback

- **Rollback procedure:**
  1. `<step-by-step how to undo>`
- **Files to revert:**
  - `<specific paths>`
- **Artifacts to delete:**
  - `<specific paths>`
- **Governance updates on rollback:**
  - `<what to update in action log / execution plan>`

### Inline example

```
Rollback procedure:
1. git revert commits from this plan's branch.
2. Delete generated artifacts (see list below).
3. Remove invariant entries from INDEX.yaml.
4. Remove lemma entries from LEMMAS_APPENDIX.md.
5. Update ACTION_LOG with rollback entry.

Files to revert:
- invariants/INV-RANK-DETERMINISM.yaml (delete)
- invariants/INV-RANK-MONOTONICITY.yaml (delete)
- invariants/INV-RANK-FAILCLOSED.yaml (delete)
- invariants/INDEX.yaml (revert to prior state)
- docs/math/LEMMAS_APPENDIX.md (revert to prior state)

Artifacts to delete:
- configs/generated/search_ranking_scorecard.json
- notebooks/math/search_ranking_verification.ipynb

Governance updates on rollback:
- ACTION_LOG: "Rolled back plan:search-ranking-determinism — [reason]"
- EXECUTION_PLAN.md: Revert progress for this item
- This plan: status → cancelled
```

---

## Section 16: Prompt References

- **MATHS prompt template:** `agent_governance/master-maths-prompt-template.md` (if math/algorithm scope)
- **Prompt doc:** `docs/prompts/{agent}-<plan-name>.md`
- **Prompt kickoff:** `docs/prompts/{agent}-<plan-name>-prompt.txt`
- **Per-task prompts (if plan has multiple execution units):**
  - `<list of prompt paths per workstream/run>`

*Write `N/A` for fields that don't apply. If this plan has a MATHS prompt, ensure the prompt references this plan's Rx IDs in its `plan:{plan-id}:{requirement-id}` references.*

---

## Section 17: Traceability

### Files created by this plan

- **Notebooks:** `<paths to notebooks created>`
- **Invariants:** `<invariant IDs created or modified>`
- **Lemmas:** `<lemma IDs created or modified>`
- **Code files:** `<Python files extracted from notebooks>`
- **Config/artifact files:** `<generated JSON/YAML paths>`

### Index updates required

- **Traceability index:** `docs/CODE_TRACEABILITY_INDEX.md` — `<entries to add, or "N/A">`
- **Invariant index:** `invariants/INDEX.yaml` — `<entries to add, or "N/A">`
- **Math README:** `docs/math/README.md` — `<entries to add, or "N/A">`
- **Lemmas appendix:** `docs/math/LEMMAS_APPENDIX.md` — `<entries to add, or "N/A">`

### Anti-drift

**DO:** List every file this plan creates and every index that needs updating.

**DON'T:** Create files without listing them here. If a file isn't in this section and Section 5 allowlist, it should not exist.

---

## Section 18: Governance Closure

On plan completion, update:

- [ ] `docs/governance/ACTION_LOG` — entry with plan ref, North Star alignment, timestamp (local timezone)
- [ ] `docs/governance/EXECUTION_PLAN.md` — mark related item(s) complete with date
- [ ] `docs/governance/PROJECT_STATUS.md` — update if milestone-related
- [ ] Invariant promotions: `<proposed → accepted, list IDs>`
- [ ] Lemma promotions: `<Draft → Rev X.Y, list IDs>`
- [ ] This plan: `status → complete`, `date_updated → today`

---

## Section 19: Execution Outcome

*Fill this section during and after execution. Do not pre-fill.*

### Task checklist

- [ ] T1 — `<task name>` — Evidence: `<path or result>`
- [ ] T2 — `<task name>` — Evidence: `<path or result>`
- [ ] `<add all tasks>`

### Gate checklist

- [ ] CHECK:C0 — `<gate name>` — Result: `<pass/fail>`
- [ ] CHECK:C1 — `<gate name>` — Result: `<pass/fail>`
- [ ] `<add all gates>`

### Final decision

- **Decision:** `<GO | NO-GO>`
- **Approved by:** `<name/role>`
- **Completion timestamp:** `<YYYY-MM-DD HH:MM:SS TZ>`

---

## Section 20: When Blocked

If any task or gate fails, emit this exact structure:

```
STATUS: BLOCKED
TASK: <task-id or gate-id>
REASON: <description of what failed>
MISSING: <specific list of what is needed to unblock>
NEXT ALLOWED ACTION: <resolution path, e.g. "Fix X and re-run T3" or "Owner must approve Y">
```

Do not proceed past the blocked task. Do not attempt workarounds.

### Escalation path

- **Primary:** `<owner of this plan>`
- **Secondary:** `<team lead or North Star maintainer>`

---

## Section 21: Agent Constraints

These constraints apply to any agent executing this plan:

- Do not touch files outside the Section 5 file allowlist.
- Do not skip or reorder tasks (Section 7 strict ordering).
- Do not modify thresholds or invariants to make gates green without owner approval.
- Do not execute until plan `status` is `approved`.
- Reference `plan:{plan-id}:{task-id}` in all action log entries and commits.
- Do not add tasks, gates, or deliverables not in this plan without owner approval.
- If scope needs to expand, emit BLOCKED and request re-scope approval.
- Use `.venv/bin/python` for all Python commands.
- If math/algorithm scope: follow notebook-first development.

---

## Section 22: References

- **North Star:** `docs/governance/NORTH_STAR.md`
- **Execution Plan:** `docs/governance/EXECUTION_PLAN.md`
- **Applicable rules:**
  - `<list applicable .cursor/rules/ files, or "see .cursor/rules/**/*.mdc">`
- **Related plans:** `<sibling or dependency plan IDs>`
- **Related docs:** `<math docs, intent docs, ADRs>`
- **MATHS prompt template:** `agent_governance/master-maths-prompt-template.md` (if math/algorithm scope)
- **MA whitepaper (authoritative standard):** `agent_governance/mathematical_autopsy:_deterministic_ai_creation.md` (if math/algorithm scope)
- **Installation kickoff prompt:** `agent_governance/KICKOFF_PROMPT.md`

---

## Plan Template Version

- **Template version:** 1.0
- **Last updated:** 2026-02-22
- **Schema files:** `agent_governance/PLAN_TEMPLATE_SCHEMA.yaml`, `agent_governance/PLAN_TEMPLATE_SCHEMA.json`
