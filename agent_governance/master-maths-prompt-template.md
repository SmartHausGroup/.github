# Master MATHS Prompt Template

Use this as the canonical prompt template for governed build/change requests. `MATHS` is a prompt-template style only. It is not part of {{PROJECT_NAME}} (MA), does not define MA phases, and does not replace MA. If a task is separately governed by MA or another methodology, follow that methodology directly and reference it explicitly in the plan/prompt.

This template is governance-locked for this repository and requires compliance with:
- `AGENTS.md` / `CLAUDE.md` (read FIRST — system instructions for all agents)
- `docs/governance/NORTH_STAR.md`
- `docs/governance/EXECUTION_PLAN.md`

---

## Execution Prompt — MATHS Workstream (Governance Locked)

Plan Reference: `plan:<fill-plan-id>`
Parent Plan: `plan:<fill-parent-plan-id>`
North Star: `docs/governance/NORTH_STAR.md`

**Mission:** Produce the full MATHS package for `[INSERT EXACT SCOPE HERE]` with governance compliance and no scope drift. If the active plan separately requires MA, satisfy MA using its own docs and deliverables; do not treat MATHS as the MA process.

Example scope:
- `Search ranking determinism + scoring + invariants + verification gates`

## Model Configuration (for prompt runner)

- Set temperature to 0 (or as low as the platform allows).
- Set top_p to 1.0 (no nucleus sampling truncation).
- Disable any "creative" or "balanced" mode; use "precise" if available.
- If the platform supports a system prompt, paste the Governance Lock and Agent Constraints sections into it.

## Governance Lock (Mandatory)

Before any write/test/command:

1. Read:
- `AGENTS.md` / `CLAUDE.md` (system instructions — read FIRST)
- All applicable `.cursor/rules/**/*.mdc` (if present)
- `docs/governance/NORTH_STAR.md`
- `docs/governance/EXECUTION_PLAN.md`
- When scope is math/algorithm: MA process rules (if `.cursor/rules/ma-process/` exists)

2. Verify alignment + plan linkage:
- Must cite `plan:{plan-id}:{requirement-id}` references.
- Must stop if missing/misaligned.

3. Enforce approval protocol:
- No file edits, no tests, no commands until explicit user approval.
- Present formal change-approval packet and end with:
  `If you're good with this plan, reply "go".`

## Canonical Vocabulary (use these exactly, no synonyms)

| Term | Use for | Do NOT use |
|------|---------|------------|
| invariant | Machine-enforced guarantee (YAML) | constraint, rule, check, guard |
| lemma | Formal claim with proof sketch | theorem, proof, claim, proposition |
| scorecard | Artifact aggregating pass/fail results | report, summary, dashboard |
| artifact | Generated JSON output from notebooks | output file, result, export |
| notebook | Jupyter `.ipynb` verification file | script, program, code file |
| extraction | Moving code from notebook to `.py` | refactoring, porting, copying |
| governing formula | Single input-output relation for the scope | main equation, core formula |
| fail-closed | System halts/rejects on failure | fail-safe, graceful degradation |

Use these terms consistently in all phase outputs. If a term not in this table is needed, define it explicitly in the A phase and use it consistently thereafter.

## Required Output Format (Before Approval)

Use this exact structure:

- `Decision Summary`: Recommended path and why.
- `Options Considered`: Option A / B / C with pros/cons.
- `Evaluation Criteria`:
  - Mathematical soundness
  - Determinism guarantees
  - Invariant enforceability
  - Maintenance overhead
  - Deployment viability
- `Why This Choice`: Context-grounded reasoning.
- `Risks`: Explicit unresolved risks.
- `Next Steps`: Ordered execution steps with plan refs.

## Execution Order (After Approval Only)

1. Complete **M** (Model). Do not start A until M is complete.
2. Complete **A** (Annotate). Do not start T until A is complete.
3. Complete **T** (Tie). Do not start H until T is complete.
4. Complete **H** (Harness). Do not start S until H is complete.
5. Complete **S** (Stress-test). Then fill Required Completion Block and emit GO/NO-GO.
6. Governance closure (action log, execution plan, project status as required).

### Methodology Separation

`MATHS` is a reusable prompt format. It does not define or replace `MA`.

If the active task is governed by `MA`:

- read `agent_governance/mathematical_autopsy:_deterministic_ai_creation.md` directly,
- read the repo-local MA rules directly,
- list the required MA deliverables explicitly in the prompt or plan,
- and do not collapse MA into the MATHS prompt format.

### Phase Transition Protocol

After completing each MATHS phase, emit the phase exit checklist and wait for user confirmation before starting the next phase. Do not batch multiple phases in a single response unless the user explicitly requests it (e.g. "run M through S in one shot").

When emitting a phase exit:
- Use exactly: `[PHASE X COMPLETE — all deliverables met]` or `[PHASE X BLOCKED — missing: {list}]`
- If BLOCKED, do not proceed; wait for user resolution.

### Phase Contract Object (Mandatory — Machine-Verifiable)

Each MATHS phase MUST emit a phase contract artifact before the next phase starts. The next phase MUST consume it. No free-floating reasoning between phases.

**Emit after each phase exit checklist:** Write `configs/generated/maths_phase_output/<phase>.json` (or path declared in Context) with this schema:

```json
{
  "phase": "M",
  "invariants_declared": ["INV-XXXX", "..."],
  "variables_defined": ["var1", "var2"],
  "constraints_declared": ["constraint1", "..."],
  "assumptions": ["assumption1", "..."],
  "artifact_sha256": "<sha256 of this file content before adding this field>",
  "signed_hash": "<sha256 of canonical JSON serialization of all above fields except signed_hash>"
}
```

- Replace `<phase>` with the completed phase letter (M, A, T, H, S).
- Populate arrays from that phase's deliverables; use empty array `[]` when none.
- Next phase MUST read the previous phase's contract and fail-closed if missing or invalid.

### MATHS Lifecycle State Machine (Mandatory)

Agents MUST use only these states and transitions. Do not infer or invent states.

| From State | To State | Condition |
|------------|----------|-----------|
| DRAFT | APPROVED | Owner explicitly approves plan. |
| APPROVED | EXECUTING | Agent begins work with approval ("go"). |
| EXECUTING | BLOCKED | Stop condition fires (missing ref, allowlist violation, schema fail). |
| EXECUTING | FAILED | Invariant/gate failure; deterministic replay fail. |
| EXECUTING | COMPLETE | S phase done; FINAL_DECISION: GO. |
| BLOCKED | APPROVED | Owner updates plan/scope and re-approves only. |
| FAILED | CANCELLED | Owner cancels or re-scopes. |

- Emit current state in Completion Block and in phase_output when applicable.
- BLOCKED → APPROVED transition requires human action; agent MUST NOT assume approval.

### CHECK:C-FILE-SCOPE (Mandatory Before Any Write)

Before committing or staging changes, run:

```bash
git diff --name-only origin/main...HEAD
# or: git diff --name-only <base_ref>...HEAD
```

Assert: every listed file is in the Context **Explicit file allowlist**. If any file is not in the allowlist, or any file in the **Explicit file denylist** appears:

```
STATUS: BLOCKED
TASK: scope_violation
REASON: file not in allowlist | denylist file touched
MISSING: [list of violating paths]
NEXT ALLOWED ACTION: None until scope corrected or allowlist updated by owner.
```

Do not rely on instruction discipline; enforce via this check.

### NEXT_PHASE_PROMPT_TEMPLATE (Self-Reinforcing Loop)

When a task instructs "generate the MATHS prompt for the next phase," use this exact template. Do not improvise.

- **inputs:** `previous_phase_output.json` (the phase contract of the completed phase).
- **must_include:**
  - `invariant_refs`: List of invariant IDs from previous phase contract.
  - `exit_criteria`: Copy of the completed phase's exit checklist with all items checked.
  - `validation_command`: Exact command(s) to verify the next phase's gate (e.g. `npm run compile`, `make ma-validate-quiet`).
- **structure:** Same MATHS sections (M, A, T, H, S) with Governance Lock and Context; reference `plan:<plan-id>:<next-task-id>`.

### Resource Budget Constraints

When the plan or Context specifies resource limits, enforce them. If unspecified, use these defaults unless overridden in Context:

- `max_iterations`: 5 (e.g. retries or refinement loops).
- `max_epochs`: N/A for non-training; when training scope: define in plan.
- `max_duration_seconds`: 3600 (1 hour) for single run unless plan specifies otherwise.
- `max_memory_mb`: N/A unless plan specifies.

IF a budget is exceeded: SET status = BLOCKED; EMIT `budget_exceeded: <which_budget>`; do not continue.

### Confidence Threshold (When Classification/Scoring Applies)

When the scope includes confidence or classification scores, use explicit thresholds. Do not use "low confidence" or "high confidence" without definition.

- IF `max_softmax < 0.60` (or threshold declared in plan): SET `class = "none"` (or fallback class declared in plan).
- IF `confidence >= 0.80`: use authoritative/primary path per plan.
- Define thresholds in A phase or T phase; reference them in H and S. Agents MUST NOT infer thresholds.

### Risk Monitors (Executable)

For each risk listed in the plan or T phase, define an executable monitor. Do not leave risks as prose only.

Format per risk:

```
RISK: <risk_id>
MONITOR: <variable or artifact path to check>
TRIGGER: <condition, e.g. "> 0.05" or "== false">
ACTION: BLOCK | WARN | ESCALATE
```

Example: `RISK: head_degradation` / `MONITOR: existing_head_degradation_max` / `TRIGGER: > 0.05` / `ACTION: BLOCK`

Agents MUST evaluate MONITOR against TRIGGER and perform ACTION when condition is true.

### Scope Violation BLOCKED Format

When a new file is required but not in the allowlist, or a denylist file would be touched:

```
STATUS: BLOCKED
TASK: scope_violation
REASON: file not in allowlist | denylist file touched
MISSING: [path(s)]
NEXT ALLOWED ACTION: None until owner adds path to allowlist or revokes the change.
```

## Determinism Requirements

- Identify all nondeterminism sources.
- Lock seeds (`random`, `numpy`, `torch`, etc.).
- Prove bounded divergence or reject design.
- Fail-closed on invariant/test failure.

## Validation Requirements

- Run required checks per repo rules (`pre-commit run --all-files` or approved fallback).
- No fake/mock-only proofs for math behavior.
- Report all failing gates explicitly.

## Governance Closure (Mandatory)

Update:
- `docs/governance/ACTION_LOG` (local timezone timestamp, plan ref, alignment result)
- `docs/governance/EXECUTION_PLAN.md` (progress/milestones)
- `docs/governance/PROJECT_STATUS.md` (if milestone-related)
- Post-work checklist status (explicit complete/incomplete)

## Stop Conditions

Return `NO-GO` immediately if:
- North Star misalignment
- missing plan mapping
- missing approval
- MATHS phase incomplete (or required external-methodology deliverables not delivered)
- invariant or determinism failure
- file allowlist violated or denylist file touched

## When Blocked (mandatory output format)

When any stop condition or no-go trigger fires, emit this exact structure:

```
STATUS: BLOCKED
PHASE: [current MATHS phase letter]
TASK: [scope_violation | missing_plan_ref | north_star_misalignment | ambiguous_requirement | missing_input | budget_exceeded | …]
REASON: [one-line reason]
MISSING: [specific list of what is needed]
NEXT ALLOWED ACTION: [e.g. "None until plan ref provided" | "Clarify X with owner" | "User must resolve Y"]
```

Do not proceed with writes, tests, or commands after emitting BLOCKED. For file allowlist/denylist violations use `TASK: scope_violation` and list violating paths in MISSING.

---

## MATHS Prompt Template

Use this template for any governed build/change request. If the active plan separately requires MA or another methodology, add those deliverables explicitly; the template itself does not define them.

## Agent Constraints (Re-check Before Every Write)

- Do not edit files, run tests, or run commands until explicit user approval ("go").
- Do not skip or reorder MATHS phases (M → A → T → H → S).
- Do not change thresholds or invariants to make gates green without owner approval.
- Do not proceed if plan reference is missing or North Star is misaligned.
- If scope drifts beyond Context allowlist/denylist, stop and re-scope.
- Do not add sections, fields, or deliverables not listed in this template.
- Do not reorganize the template structure or insert commentary between phases.
- If this prompt is re-run with identical inputs, scope, and model configuration, the output structure, field names, and phase sequence must be identical. Only values derived from the specific scope may differ.

## Response Framing (Mandatory)

- Begin each phase output with `## [Phase Letter] — [Phase Name]`.
- End each phase output with the phase exit checklist.
- Do not include introductions, transitions, summaries of previous phases, or filler between phases.
- Do not summarize what you are "about to do" — produce the deliverables directly.

## Execution Rules (Mandatory)

- Do not proceed past a phase when required inputs are missing.
- Fail closed when invariant, schema, or artifact requirements are ambiguous.
- Do not modify thresholds to "make gates green" without explicit owner approval.
- If deterministic replay fails, stop promotion and resolve before continuing.
- If scope drifts beyond declared boundaries, stop and re-scope first.

**Fill order:** Prompt Run Metadata → Context → M → A → T → H → S → (Assure/Observe only when plan sets `Assure_required: true` or `Observe_required: true`; otherwise omit) → Output Contract → Completion Block.

## Prompt Run Metadata

- Prompt version:
- Task ID:
- Run ID:
- Commit SHA:
- Dataset/version fingerprint:
- Invariant IDs in scope:
- Owners (product/engineering/MA):

## Context

- Task name:
- Domain: `framework | app`
- Owner:
- Dependencies:
- Explicit file allowlist (may touch):
- Explicit file denylist (must not touch):

---

## M — Model

### Required fields (use these exact headings)

- `problem_statement`: 1-3 sentences. What is broken or missing, and why it matters.
- `stakeholders`: Bullet list of who is affected.
- `success_metrics`: List, each with a numeric threshold or boolean gate.
- `constraints`: Bullet list (time, cost, stack, compliance).
- `out_of_scope`: Bullet list of what this work explicitly does NOT cover.

### Optional formal-method overlay (include only when the active plan separately requires it)

- `determinism_definition`: 1-2 sentences defining what "deterministic" means for this scope.
- `guarantees_required`: Bullet list of formal guarantees the implementation must provide.
- `boundaries`: What the system must NOT do (non-goals, failure modes to prevent).

### Inline example (math-scoped)

```
- problem_statement: The search ranking function permits non-deterministic candidate
  ordering when two candidates have equal composite scores. This violates INV-RANK-DETERMINISM
  and blocks promotion to production.
- stakeholders: Search pipeline, CI gate system, quality assurance.
- success_metrics: deterministic_replay_pass == true; score_ordering_stable == true across
  seeds [42, 123, 256]; scorecard green on all INV-RANK-* invariants.
- constraints: No external dependencies beyond numpy; must run in < 2s on CI hardware.
- out_of_scope: Indexing pipeline changes; embedding model modifications; UI changes.
- determinism_definition: Given identical input data, seeds, and configuration, the ranking
  function must produce bit-identical output arrays on every run.
- guarantees_required: Monotonic score ordering; fail-closed on NaN/Inf; seed-locked RNG.
- boundaries: Must not modify indexing pipeline or embedding model.
```

### Anti-drift examples

**DO:** "The ranking function permits non-deterministic ordering when two candidates have equal composite scores. This violates INV-RANK-DETERMINISM."

**DON'T:** "We need to improve the ranking system to make it more reliable."

**DO:** `success_metrics: deterministic_replay_pass == true; score_ordering_stable == true across seeds [42, 123, 256]`

**DON'T:** `success_metrics: ranking should be consistent and reliable`

### M exit checklist

- [ ] `problem_statement` written (specific, 1-3 sentences)
- [ ] `stakeholders` listed
- [ ] `success_metrics` listed with numeric thresholds or boolean gates
- [ ] `constraints` and `out_of_scope` listed
- [ ] When a formal-method overlay is required: `determinism_definition`, `guarantees_required`, `boundaries` written
- Emit: `[PHASE M COMPLETE — all deliverables met]` or `[PHASE M BLOCKED — missing: {list}]`

---

## A — Annotate

### Required fields (use these exact headings)

- `formal_rules`: Equations, decision logic, or algorithmic rules governing this scope.
- `assumptions`: What must be true for these rules to hold.
- `data_contracts`: Input/output schemas (with types, required fields, value ranges).
- `invariants_impacted`: List of invariant IDs affected by this work.
- `required_artifacts`: List of artifact JSON files this work must produce.

### Optional formal-method overlay (include only when the active plan separately requires it)

- `governing_formula`: The single governing input-output relation. Must include domain, range, operators, and constraints. Use LaTeX or precise notation.
- `variable_definitions`: Every variable used in the governing formula, with type, domain, and units.
- `operator_properties`: Properties of each operator (linearity, commutativity, idempotency, etc.).
- `boundary_conditions`: What happens at domain edges, empty inputs, degenerate cases.
- `convergence_stability`: Convergence criteria, stability bounds, or proof that the operation is single-pass.
- `deterministic_assumptions`: Explicit list of what must hold for determinism (seed locking, input ordering, floating-point treatment).

### Inline example (math-scoped)

```
- governing_formula: |
    S(c) = w_r · r(c) + w_d · d(c) + w_a · a(c)
    where c ∈ Candidates, S: Candidates → R, r: relevance score [0,1],
    d: decay factor [0,1], a: associative boost [0,1],
    w_r + w_d + w_a = 1.0, all w_i > 0.
- variable_definitions:
    - c: candidate item, type: data object
    - S(c): composite score, type: float64, domain: [0, 1]
    - r(c): relevance score, type: float64, domain: [0, 1]
    - d(c): temporal decay factor, type: float64, domain: [0, 1]
    - a(c): associative boost, type: float64, domain: [0, 1]
    - w_r, w_d, w_a: weight parameters, type: float64, domain: (0, 1), constraint: sum = 1.0
- operator_properties: S is a linear combination; monotone in each component given positive weights.
- boundary_conditions: If Candidates is empty, return empty array. If any score is NaN, fail-closed.
- convergence_stability: Single-pass computation; no iteration; O(n) in candidate count.
- deterministic_assumptions: Input candidate order must not affect output ranking (break ties by
  stable secondary key). Seeds locked for any stochastic component. float64 arithmetic throughout.
```

### Anti-drift examples

**DO:** `S(c) = w_r · r(c) + w_d · d(c) + w_a · a(c)` with full variable definitions, domains, and types.

**DON'T:** "We'll use a weighted scoring approach combining relevance, decay, and association."

**DO:** `boundary_conditions: If Candidates is empty, return empty array. If any score is NaN, fail-closed.`

**DON'T:** "Edge cases will be handled appropriately."

### A exit checklist

- [ ] `formal_rules` written with equations or precise logic
- [ ] `assumptions` listed explicitly
- [ ] `data_contracts` include input/output schemas with types
- [ ] `invariants_impacted` lists specific IDs
- [ ] `required_artifacts` lists specific file paths
- [ ] When a formal-method overlay is required: `governing_formula` with domain/range/operators, `variable_definitions`, `operator_properties`, `boundary_conditions`, `convergence_stability`, `deterministic_assumptions` all written
- Emit: `[PHASE A COMPLETE — all deliverables met]` or `[PHASE A BLOCKED — missing: {list}]`

---

## T — Tie

### Required fields (use these exact headings)

- `dependency_checks`: What must be available/working before implementation.
- `service_readiness`: API, MCP, service, or environment prerequisites.
- `confidence_protocol`: What to do when uncertain about a dependency or requirement.
- `known_failure_modes`: List of ways this can fail, with prevention for each.
- `go_no_go`: Explicit go/no-go decision for proceeding to H.

### Optional formal-method overlay (include only when the active plan separately requires it)

- `lemma_list`: Each lemma with these exact sub-fields:
  - `id`: Lemma number (e.g. L1)
  - `name`: Short descriptive name
  - `claim`: Formal statement of what is guaranteed
  - `assumptions`: What must hold for the claim
  - `proof_sketch`: 2-5 sentence outline of why the claim holds
  - `io`: Input/output specification
  - `boundaries`: When/how the lemma can be violated
- `invariant_yamls`: Each invariant with these exact sub-fields matching `invariants/INV_TEMPLATE.yaml`:
  - `id`: INV-XXXX
  - `name`: Descriptive name
  - `owner`: `<team or individual>`
  - `status`: proposed
  - `description`: What this invariant guarantees
  - `equations`: List of equations
  - `thresholds`: Key-value pairs
  - `acceptance_checks`: List of artifact.json.path == value checks
  - `producer`: Notebook path
  - `artifacts`: List of artifact paths
  - `rollback_criteria`: When to rollback
- `ci_gate_mapping`: Which CI gates enforce which invariants.
- `fail_closed_semantics`: What happens when each invariant is violated.

### Inline example (math-scoped)

```
- lemma_list:
  - id: L1
    name: Score monotonicity
    claim: For all candidates c, if r(c) increases and d(c), a(c) are held constant,
           then S(c) strictly increases (given w_r > 0).
    assumptions: w_r > 0; r(c) is well-defined float64 in [0,1].
    proof_sketch: S(c) = w_r·r(c) + w_d·d(c) + w_a·a(c). Since w_d·d(c) and w_a·a(c)
                  are constant, ∂S/∂r = w_r > 0. Therefore S is strictly increasing in r.
    io: input: candidate with r(c) in [0,1]; output: S(c) in [0,1].
    boundaries: Violated if w_r = 0 or r(c) is NaN.

- invariant_yamls:
  - id: INV-RANK-DETERMINISM
    name: Ranking deterministic replay
    owner: <team>
    status: proposed
    description: >
      Given identical inputs and seeds, the ranking function produces
      bit-identical outputs on every run.
    equations:
      - "f(x, seed) == f(x, seed) for all x, seed"
    thresholds:
      max_replay_divergence: 0
    acceptance_checks:
      - ranking_scorecard.json.deterministic_replay_pass == true
    producer: notebooks/math/ranking_verification.ipynb
    artifacts:
      - configs/generated/ranking_scorecard.json
    rollback_criteria: >
      Any non-zero divergence between seeded runs triggers rollback.
```

### Anti-drift examples

**DO:** Lemma with `id`, `claim`, `assumptions`, `proof_sketch`, `io`, `boundaries` all filled.

**DON'T:** "We'll add a lemma to guarantee monotonicity."

**DO:** Invariant YAML with all fields from `INV_TEMPLATE.yaml` filled, `status: proposed`.

**DON'T:** "We'll create an invariant later once the code is working."

### T exit checklist

- [ ] `dependency_checks` and `service_readiness` verified
- [ ] `confidence_protocol` defined
- [ ] `known_failure_modes` listed with prevention
- [ ] `go_no_go` decision stated
- [ ] When a formal-method overlay is required: `lemma_list` with all sub-fields per lemma; `invariant_yamls` with all sub-fields per invariant; `ci_gate_mapping` defined; `fail_closed_semantics` defined
- Emit: `[PHASE T COMPLETE — all deliverables met]` or `[PHASE T BLOCKED — missing: {list}]`

---

## H — Harness

### Required fields (use these exact headings)

- `implementation_plan`: Ordered list of steps.
- `files_to_create_or_update`: Explicit file paths.
- `extraction_boundary`: Which code comes from notebooks vs. written directly (infrastructure only for direct).

### Optional formal-method overlay (include only when the active plan separately requires it)

- `notebook_path`: Path to the notebook (e.g. `notebooks/math/<scope>_verification.ipynb`).
- `notebook_structure`: Ordered list of cells, each with:
  - `cell_type`: markdown | code
  - `purpose`: What this cell does (1 sentence)
  - `lemma_mapping`: Which lemma this cell implements or verifies (if any)
  - `invariant_mapping`: Which invariant this cell validates (if any)
  - `assertion_type`: What assertion is made (if code cell)
- `alternatives_rejected`: Approaches considered and explicitly rejected, with rationale.
- `correctness_criteria`: Per-cell definition of what "correct" means.

Extraction happens ONLY after S is fully green:
- Extract runtime code from notebook exactly.
- Preserve traceability: lemma → invariant → function.
- No translation-only edits outside approved extraction process.

### Inline example (math-scoped)

```
- notebook_path: notebooks/math/ranking_scoring_verification.ipynb
- notebook_structure:
  - cell_type: markdown
    purpose: Notebook overview — scope, success criteria, lemma/invariant references.
  - cell_type: code
    purpose: Imports and seed locking (numpy seed=42, random seed=42).
    assertion_type: assert np.random.get_state()[1][0] == 42
  - cell_type: markdown
    purpose: Document compute_composite_score function — what, why, expected I/O.
  - cell_type: code
    purpose: Implement compute_composite_score(candidates, weights) -> scores array.
    lemma_mapping: L1 (score monotonicity)
    assertion_type: assert scores.shape == (len(candidates),)
  - cell_type: code
    purpose: Unit test for compute_composite_score — monotonicity, boundary, NaN handling.
    invariant_mapping: INV-RANK-DETERMINISM
    assertion_type: assert np.all(scores_run1 == scores_run2)  # deterministic replay
  - cell_type: code
    purpose: VERIFY:L1 — formal monotonicity check across sweep.
    lemma_mapping: L1
    assertion_type: assert monotonicity_violations == 0
  - cell_type: code
    purpose: Export scorecard artifact to configs/generated/.
    assertion_type: assert artifact_path.exists()
- alternatives_rejected:
  - "Use torch for scoring" — rejected: unnecessary dependency, numpy sufficient for linear combination.
  - "Skip tie-breaking" — rejected: violates INV-RANK-DETERMINISM.
- correctness_criteria:
  - compute_composite_score: output shape matches input count; all values in [0,1]; NaN inputs trigger fail-closed.
  - VERIFY:L1: zero monotonicity violations across 1000-sample sweep.
  - Scorecard: all acceptance_checks from invariant YAML pass.
```

### Anti-drift examples

**DO:** Notebook structure with per-cell purpose, lemma mapping, invariant mapping, and assertion type.

**DON'T:** "We'll create a notebook that tests the scoring function."

**DO:** `alternatives_rejected: "Use torch for scoring" — rejected: unnecessary dependency.`

**DON'T:** Silently choosing an approach without documenting what was considered and rejected.

### H exit checklist

- [ ] `implementation_plan` written (ordered steps)
- [ ] `files_to_create_or_update` lists specific paths
- [ ] `extraction_boundary` defined
- [ ] When a formal-method overlay is required: `notebook_path` specified; `notebook_structure` lists all cells with purpose, lemma/invariant mapping, and assertions; `alternatives_rejected` documented; `correctness_criteria` defined per cell
- [ ] Notebook runs end-to-end with zero errors (validated before moving to S)
- Emit: `[PHASE H COMPLETE — all deliverables met]` or `[PHASE H BLOCKED — missing: {list}]`

---

## S — Stress-test

### Required fields (use these exact headings)

- `functional_tests`: What is tested and expected result.
- `edge_adversarial_tests`: Edge cases, adversarial inputs, degenerate cases.
- `determinism_replay_checks`: Seed-locked runs with comparison.
- `acceptance_gates`: List of gates with pass/fail criteria.

### Optional formal-method overlay (include only when the active plan separately requires it)

Scorecard artifact at the path declared in T-phase invariant YAML, with this exact JSON schema. Every artifact MUST include `artifact_sha256` (SHA-256 of the artifact file content at write time) for replay verification:

```json
{
  "type": "object",
  "required": ["invariant_results", "notebook_hash", "seed_lock", "deterministic_replay_pass", "final_decision", "artifact_sha256"],
  "properties": {
    "artifact_sha256": {
      "type": "string",
      "description": "SHA-256 of this artifact file content (excluding this field) at write time; recompute on replay and assert identical."
    },
    "invariant_results": {
      "type": "object",
      "description": "One key per invariant ID, value is boolean pass/fail",
      "additionalProperties": { "type": "boolean" }
    },
    "notebook_hash": {
      "type": "string",
      "description": "SHA-256 of the notebook file at validation time"
    },
    "seed_lock": {
      "type": "object",
      "required": ["seeds_used", "all_locked"],
      "properties": {
        "seeds_used": { "type": "object", "additionalProperties": { "type": "integer" } },
        "all_locked": { "type": "boolean" }
      }
    },
    "deterministic_replay_pass": { "type": "boolean" },
    "final_decision": { "type": "string", "enum": ["GO", "NO-GO"] }
  }
}
```

Example scorecard output:

```json
{
  "invariant_results": {
    "INV-RANK-DETERMINISM": true,
    "INV-RANK-MONOTONICITY": true,
    "INV-RANK-FAILCLOSED": true
  },
  "notebook_hash": "sha256:a1b2c3d4e5f6...",
  "seed_lock": {
    "seeds_used": { "numpy": 42, "random": 42 },
    "all_locked": true
  },
  "deterministic_replay_pass": true,
  "final_decision": "GO"
}
```

### Anti-drift examples

**DO:** Scorecard JSON with every field filled, `final_decision` as exactly `"GO"` or `"NO-GO"`.

**DON'T:** "All tests passed, we're good to go."

**DO:** `edge_adversarial_tests: empty candidate list → returns empty array; NaN score → fail-closed; 10M candidates → completes in < 2s`

**DON'T:** "Edge cases were tested and handled."

### S exit checklist

- [ ] `functional_tests` listed with expected results
- [ ] `edge_adversarial_tests` listed with specific inputs and expected behavior
- [ ] `determinism_replay_checks` run across declared seeds
- [ ] `acceptance_gates` listed with pass/fail
- [ ] When a formal-method overlay is required: scorecard artifact generated at declared path; JSON matches schema above; `final_decision` is `GO` or `NO-GO`
- Emit: `[PHASE S COMPLETE — all deliverables met]` or `[PHASE S BLOCKED — missing: {list}]`
- Emit: `FINAL_DECISION: GO` or `FINAL_DECISION: NO-GO`

---

## Optional — Assure (Production Hardening)

- Security checks:
- Input validation:
- Additional test coverage:

## Optional — Observe (Production Operations)

- Telemetry/signals:
- Alert thresholds:
- Rollback/kill-switch:

## Output Contract

- Deliverables:
- Artifacts generated (with full paths):
- Artifact JSON schema: (reference the schema in S phase, or define inline if non-math scope)
- Validation result:
- Residual risks:
- Evidence links (files/paths only):
- Blocking decisions taken:
- Follow-up actions with owners/dates:

## No-Go Triggers (Mandatory)

- Missing required artifact file(s).
- Artifact schema mismatch against declared contract.
- Invariant checks missing or failing.
- Deterministic replay check is false.
- Unapproved threshold/config drift.
- Security/compliance gate failure (when Assure is in scope).
- File outside Context allowlist modified, or any denylist file modified.

## Required Completion Block

- `M` complete? (yes/no) Evidence:
- `A` complete? (yes/no) Evidence:
- `T` complete? (yes/no) Evidence:
- `H` complete? (yes/no) Evidence:
- `S` complete? (yes/no) Evidence:
- `Assure` required? (yes/no) Evidence:
- `Observe` required? (yes/no) Evidence:
- Final Decision: `GO` | `NO-GO`
- Approved by:
- Timestamp (UTC):

## Before Each Response, Re-check

1. Am I still within scope and the Context file allowlist/denylist?
2. Do I have explicit approval for the next write (or am I only proposing)?
3. Is the current MATHS phase complete per its exit checklist (and any explicitly declared scope-specific deliverables)?
4. Am I using canonical vocabulary from the table above?
5. If uncertain, emit BLOCKED (using the When Blocked format) and do not proceed.

## Crosswalk (Legacy Naming)

- Model = Architect
- Annotate = Trace
- Tie = Link
- Harness = Assemble
- Stress-test = Stress-test
- Assure = Validate
- Observe = Monitor

**MATHS vs. MA:** `MATHS` is a prompt template. `MA` is a separate methodology. If a task uses both, that is a task-level choice documented by the plan and prompt, not a built-in relationship.

---

## MATHS Prompt Example 1 — Real AI App (Non-Math Scope)

Use this as a practical prompt example for a familiar product: an AI customer support assistant for an ecommerce company. This example uses the MATHS template on its own; no separate methodology overlay is required.

## Prompt Run Metadata

- Prompt version: `v1.3`
- Task ID: `MA-SAFE-ANS-001`
- Run ID: `run-2026-02-19-safe-answer-01`
- Commit SHA: `<fill-at-runtime>`
- Dataset version: `support-safe-answer-golden-v3`
- Invariant IDs in scope: `INV-APP-SAFE-001`, `INV-APP-SAFE-002`, `INV-APP-SAFE-003`, `INV-APP-SAFE-004`
- Owners:
  - Product: Support Product Lead
  - Engineering: Support AI Lead Engineer
  - MA: MA Framework Maintainer

## Context

- Task name: Add "safe answer mode" to support AI assistant
- Domain: `app + framework`
- Owner: product engineer + MA maintainer
- Product scenario:
  - Assistant answers order questions.
  - Current issue: policy hallucinations when evidence is weak.
  - Required behavior: low-confidence fallback + escalation.
- Primary dependencies:
  - App API handler for support responses
  - Retrieval layer (policy + order FAQ docs)
  - Framework invariant contracts
  - Artifact output for safety metrics

## Developer Brief (Copy/Paste)

Implement low-confidence protection in the support assistant so it stops inventing policy answers. If confidence is below threshold, return a safe fallback and offer escalation. Keep latency within SLA, keep behavior deterministic in verification runs, and wire results into framework artifacts/gates.

Acceptance goals:
- `false_confident_answers <= 1.0%`
- `helpful_answer_rate >= 85.0%`
- `p95_latency_ms <= 2000`
- `deterministic_replay_pass == true`

## M — Model

### Problem we are solving
The support assistant gives fluent answers, but some are overly confident when evidence is weak.

### Who this is for
- End users
- Support operations team
- Engineering owners

### What success looks like
- Low-confidence responses do not fabricate policy.
- Safe fallback and escalation are always available.
- Metrics are artifacted and replayable.

### Constraints
- Keep latency within SLA.
- No leakage of private/internal data.
- Keep UX stable.

### Out of scope
- Full retrieval rewrite
- Broad UI redesign
- Multilingual expansion

`[PHASE M COMPLETE — all deliverables met]`

## A — Annotate

### Product rules
1. High evidence score -> answer with citations.
2. Low evidence score -> fallback + escalation.
3. Never present guessed policy text as fact.

### Assumptions
- Retrieval confidence is available.
- Decision metadata can be logged.

### Input Schema (strict)

```json
{
  "message": "Where is my package?",
  "customer_id": "cust_123",
  "intent": "order_status",
  "retrieval": {
    "confidence": 0.62,
    "evidence_count": 2,
    "snippets": [
      {"doc_id": "policy_shipping_1", "score": 0.73, "text": "..."}
    ]
  }
}
```

### Output Schema (strict)

```json
{
  "answer_text": "I am not fully certain from available policy details. I can connect you to support.",
  "decision_mode": "fallback",
  "confidence_score": 0.62,
  "escalation_offered": true,
  "citations": ["policy_shipping_1"],
  "policy_claim_level": "non_authoritative"
}
```

### Required artifact
- `configs/generated/support_safe_answer_metrics.json`
  - `hallucination_rate`
  - `fallback_rate`
  - `false_confident_answers`
  - `deterministic_replay_pass`
  - `helpful_answer_rate`
  - `p95_latency_ms`

`[PHASE A COMPLETE — all deliverables met]`

## T — Tie

### Decision policy matrix

| Condition | Decision Mode | Policy Claim Level | Escalation |
|---|---|---|---|
| `confidence >= 0.80` and evidence consistent | `answer` | `authoritative` | `false` |
| `0.60 <= confidence < 0.80` and partial evidence | `answer` with caution | `non_authoritative` | `true` |
| `confidence < 0.60` | `fallback` | `non_authoritative` | `true` |
| contradiction detected in top evidence | `fallback` | `non_authoritative` | `true` |
| retrieval unavailable | `escalate` | `non_authoritative` | `true` |

`[PHASE T COMPLETE — all deliverables met]`

## H — Harness

1. Add confidence decision branch in response layer.
2. Extend verification notebook dataset (answerable + ambiguous + adversarial).
3. Emit metrics artifact.
4. When plan requires new or changed invariants: Add/update invariant YAML per T-phase list; `validation_command` MUST be an executable command (no "manual review").
5. Re-run gates.

Expected command sequence:

```bash
make dev-verify
make notebooks-plan
make notebooks-run
make quality-gate
```

`[PHASE H COMPLETE — all deliverables met]`

## S — Stress-test

- Functional: high-confidence answers stay useful.
- Edge/adversarial: ambiguity, contradiction, missing KB, injection phrasing.
- Replay: fixed-seed runs produce stable metric distributions.
- Acceptance: hallucination/safety/helpfulness/latency gates pass together.

`[PHASE S COMPLETE — all deliverables met]`
`FINAL_DECISION: GO`

## Optional — Assure

- Red-team set for policy-sensitive intents.
- PII guardrails in logs/artifacts.
- Unit tests for decision branch + output contract.

## Optional — Observe

- Track fallback rate, escalation acceptance, dissatisfaction signals.
- Alerts on false-confidence spikes and latency regression.
- Incident playbook with rollback/strict fallback mode.

## Output Contract

- Deliverables:
  - safe-answer behavior implemented
  - verification coverage for low-confidence paths
  - escalation messaging flow
- Artifact:
  - `configs/generated/support_safe_answer_metrics.json`
- Done when:
  - safety threshold met
  - usefulness threshold met
  - deterministic replay pass
  - required gates green

## Required Completion Block (Filled Example)

- `M` complete? `yes` — problem, stakeholders, metrics, constraints, out-of-scope defined
- `A` complete? `yes` — rules, schemas, assumptions, artifact path defined
- `T` complete? `yes` — decision matrix with thresholds defined
- `H` complete? `yes` — implementation plan, command sequence, files listed
- `S` complete? `yes` — functional, edge, replay, acceptance gates defined
- `Assure` required? `yes` — red-team, PII, unit tests scoped
- `Observe` required? `yes` — telemetry, alerts, rollback scoped
- Final Decision: `GO (conditional on gates passing in active run)`
- Approved by: Product engineer + MA maintainer
- Timestamp (UTC): `2026-02-19T00:00:00Z`

---

## MATHS Prompt Example 2 — Math-Scoped (MA Governed Separately)

This example demonstrates a math-scoped task that uses the MATHS prompt structure while separately including MA-governed deliverables. The formal-method content appears because the task requires it, not because MATHS defines MA.

## Prompt Run Metadata

- Prompt version: `v1.0`
- Task ID: `RANK-SCORE-001`
- Run ID: `run-2026-02-22-ranking-scoring-01`
- Commit SHA: `<fill-at-runtime>`
- Dataset/version fingerprint: `ranking-golden-v1`
- Invariant IDs in scope: `INV-RANK-DETERMINISM`, `INV-RANK-MONOTONICITY`, `INV-RANK-FAILCLOSED`
- Owners:
  - Product: Search quality maintainer
  - Engineering: Ranking lead
  - MA: MA framework maintainer

## Context

- Task name: Search ranking scoring determinism and monotonicity guarantees
- Domain: `framework`
- Owner: ranking lead + MA maintainer
- Dependencies:
  - `src/<project>/ranking.py` (target extraction file)
  - `notebooks/math/ranking_scaffold.ipynb` (source notebook)
  - `invariants/INV-RANK-DETERMINISM.yaml`
- Explicit file allowlist (may touch):
  - `notebooks/math/ranking_*`
  - `invariants/INV-RANK-*`
  - `configs/generated/ranking_*`
  - `docs/math/RANKING_*`
  - `src/<project>/ranking.py`
- Explicit file denylist (must not touch):
  - `src/<project>/indexing/` (indexing pipeline)
  - `src/<project>/core/` (core engine)
  - `configs/policy/` (policy configs)

## M — Model (with MA intent)

- `problem_statement`: The search ranking function permits non-deterministic candidate ordering when two candidates have equal composite scores. This violates INV-RANK-DETERMINISM and blocks promotion to production.
- `stakeholders`: Search pipeline, CI gate system, quality assurance.
- `success_metrics`: `deterministic_replay_pass == true`; `score_ordering_stable == true` across seeds [42, 123, 256]; scorecard green on all `INV-RANK-*` invariants.
- `constraints`: No external dependencies beyond numpy; must run in < 2s on CI hardware.
- `out_of_scope`: Indexing changes; embedding model modifications; UI changes.
- `determinism_definition`: Given identical input data, seeds, and configuration, the scoring function must produce bit-identical output arrays on every run.
- `guarantees_required`: Monotonic score ordering; fail-closed on NaN/Inf; seed-locked RNG.
- `boundaries`: Must not modify indexing pipeline or core engine.

`[PHASE M COMPLETE — all deliverables met]`

## A — Annotate (with MA governing formula + calculus)

- `formal_rules`:
  1. Composite score is a weighted linear combination of three sub-scores.
  2. Tie-breaking uses stable secondary key (candidate insertion order).
  3. NaN or Inf in any sub-score triggers fail-closed (return empty result + error flag).

- `assumptions`:
  - All sub-scores are finite float64 in [0, 1].
  - Weights are positive float64 summing to 1.0.
  - Candidate list has a stable insertion order.

- `data_contracts`:
  - Input: `List[Candidate]` each with `.relevance: float64`, `.decay: float64`, `.boost: float64`
  - Output: `np.ndarray` of float64 composite scores, shape `(n,)`, sorted descending with stable tie-breaking
  - Error: If any input is NaN/Inf, return `(empty_array, error_flag=True)`

- `invariants_impacted`: `INV-RANK-DETERMINISM`, `INV-RANK-MONOTONICITY`, `INV-RANK-FAILCLOSED`

- `required_artifacts`: `configs/generated/ranking_scorecard.json`

- `governing_formula`:

  ```
  S(c) = w_r · r(c) + w_d · d(c) + w_b · b(c)
  where c ∈ Candidates, S: Candidates → [0,1]
  r: relevance ∈ [0,1], d: decay ∈ [0,1], b: boost ∈ [0,1]
  w_r, w_d, w_b ∈ (0,1), w_r + w_d + w_b = 1.0
  ```

- `variable_definitions`:
  - `c`: candidate item
  - `S(c)`: composite score, float64, [0, 1]
  - `r(c)`: relevance score, float64, [0, 1]
  - `d(c)`: temporal decay factor, float64, [0, 1]
  - `b(c)`: boost factor, float64, [0, 1]
  - `w_r, w_d, w_b`: weight parameters, float64, (0, 1), sum = 1.0

- `operator_properties`: S is a linear combination; monotone in each component given positive weights; commutative in candidate order (output ranking is order-independent).

- `boundary_conditions`: Empty candidate list → empty array. Any NaN/Inf sub-score → fail-closed. Single candidate → trivially ordered.

- `convergence_stability`: Single-pass O(n) computation. No iteration. Stable sort for ranking.

- `deterministic_assumptions`: float64 arithmetic throughout; stable sort; seeds locked; candidate input order does not affect output ranking.

`[PHASE A COMPLETE — all deliverables met]`

## T — Tie (with MA lemmas + invariants)

- `dependency_checks`: numpy available; candidate data structures defined; invariant template available.
- `service_readiness`: No external services required; pure computation.
- `confidence_protocol`: If any sub-score type is ambiguous, emit BLOCKED and request schema clarification.
- `known_failure_modes`:
  - NaN propagation through weighted sum → prevented by fail-closed check before computation.
  - Unstable sort producing different orderings → prevented by using `np.argsort(kind='stable')`.
  - Float precision edge cases → prevented by float64 and rounding to 15 significant digits.
- `go_no_go`: GO — all dependencies available, failure modes have prevention.

- `lemma_list`:
  - `id`: L1
    `name`: Score monotonicity
    `claim`: For all candidates c, if r(c) increases while d(c) and b(c) are held constant, S(c) strictly increases.
    `assumptions`: w_r > 0; r(c) ∈ [0,1]; no NaN.
    `proof_sketch`: ∂S/∂r = w_r > 0, so S is strictly increasing in r. Same argument holds for d and b with their respective weights.
    `io`: input: candidate with sub-scores in [0,1]; output: S(c) in [0,1].
    `boundaries`: Violated if w_r = 0 or r(c) is NaN.

  - `id`: L2
    `name`: Deterministic replay
    `claim`: f(X, seed) == f(X, seed) for all valid input sets X and seeds.
    `assumptions`: float64 arithmetic; stable sort; all seeds locked; no external state.
    `proof_sketch`: The function is a pure computation with no I/O, no threading, no external state. Given identical inputs and seeds, numpy operations produce identical results. Stable sort preserves insertion order for ties.
    `io`: input: candidate list + seeds; output: sorted score array.
    `boundaries`: Violated if unseeded RNG is used or sort is unstable.

- `invariant_yamls`:
  - `id`: INV-RANK-DETERMINISM
    `name`: Ranking deterministic replay
    `owner`: <team>
    `status`: proposed
    `description`: Given identical inputs and seeds, ranking produces bit-identical outputs.
    `equations`: ["f(x, seed) == f(x, seed) for all x, seed"]
    `thresholds`: { max_replay_divergence: 0 }
    `acceptance_checks`: ["ranking_scorecard.json.deterministic_replay_pass == true"]
    `producer`: notebooks/math/ranking_scoring_verification.ipynb
    `artifacts`: ["configs/generated/ranking_scorecard.json"]
    `rollback_criteria`: Any non-zero divergence triggers rollback.

  - `id`: INV-RANK-MONOTONICITY
    `name`: Ranking score monotonicity
    `owner`: <team>
    `status`: proposed
    `description`: Composite score is strictly increasing in each sub-score given positive weight.
    `equations`: ["∂S/∂r >= 0", "∂S/∂d >= 0", "∂S/∂b >= 0"]
    `thresholds`: { max_monotonicity_violations: 0 }
    `acceptance_checks`: ["ranking_scorecard.json.monotonicity_pass == true"]
    `producer`: notebooks/math/ranking_scoring_verification.ipynb
    `artifacts`: ["configs/generated/ranking_scorecard.json"]
    `rollback_criteria`: Any monotonicity violation triggers rollback.

  - `id`: INV-RANK-FAILCLOSED
    `name`: Ranking fail-closed on invalid input
    `owner`: <team>
    `status`: proposed
    `description`: NaN or Inf in any sub-score produces empty result with error flag.
    `equations`: ["isnan(x) or isinf(x) → ([], error=True)"]
    `thresholds`: { false_accepts_on_nan: 0 }
    `acceptance_checks`: ["ranking_scorecard.json.failclosed_pass == true"]
    `producer`: notebooks/math/ranking_scoring_verification.ipynb
    `artifacts`: ["configs/generated/ranking_scorecard.json"]
    `rollback_criteria`: Any NaN/Inf accepted without error triggers rollback.

- `ci_gate_mapping`: `scripts/ci/ranking_contract_gate.py` validates all three invariants against scorecard artifact.
- `fail_closed_semantics`: Any invariant failure → CI gate fails → merge blocked → rollback to last green scorecard.

`[PHASE T COMPLETE — all deliverables met]`

## H — Harness (with MA notebook-first implementation)

- `implementation_plan`:
  1. Create verification notebook with seed-locked setup.
  2. Implement `compute_composite_score()` in notebook cell.
  3. Implement `validate_inputs()` (NaN/Inf check) in notebook cell.
  4. Unit test each function individually.
  5. Integration test: full pipeline with golden dataset.
  6. VERIFY:L1 cell (monotonicity sweep).
  7. VERIFY:L2 cell (deterministic replay across 3 seeds).
  8. Export scorecard artifact.
  9. After S green: extract to `src/<project>/ranking.py`.

- `files_to_create_or_update`:
  - `notebooks/math/ranking_scoring_verification.ipynb` (create)
  - `configs/generated/ranking_scorecard.json` (generated by notebook)
  - `src/<project>/ranking.py` (extraction target, after S green only)

- `extraction_boundary`: All scoring logic from notebook. Infrastructure (imports, CLI) may be written directly.

- `notebook_path`: `notebooks/math/ranking_scoring_verification.ipynb`

- `notebook_structure`:
  - cell_type: markdown | purpose: Overview, scope, lemma refs (L1, L2), invariant refs (INV-RANK-*)
  - cell_type: code | purpose: Imports + seed lock | assertion: `assert np.random.get_state()[1][0] == 42`
  - cell_type: markdown | purpose: Document validate_inputs — what, why, I/O, fail-closed behavior
  - cell_type: code | purpose: Implement validate_inputs(candidates) -> (valid, error_flag) | invariant_mapping: INV-RANK-FAILCLOSED
  - cell_type: code | purpose: Test validate_inputs with NaN, Inf, empty, valid inputs | assertion: `assert error_flag == True` for NaN case
  - cell_type: markdown | purpose: Document compute_composite_score — governing formula, weights, output shape
  - cell_type: code | purpose: Implement compute_composite_score(candidates, weights) -> scores | lemma_mapping: L1
  - cell_type: code | purpose: Test compute_composite_score — shape, range, monotonicity spot check | assertion: `assert scores.shape == (n,); assert np.all(scores >= 0); assert np.all(scores <= 1)`
  - cell_type: code | purpose: VERIFY:L1 — monotonicity sweep (1000 samples) | lemma_mapping: L1 | assertion: `assert monotonicity_violations == 0`
  - cell_type: code | purpose: VERIFY:L2 — deterministic replay across seeds [42, 123, 256] | lemma_mapping: L2, invariant_mapping: INV-RANK-DETERMINISM | assertion: `assert np.array_equal(run1, run2); assert np.array_equal(run2, run3)`
  - cell_type: code | purpose: Export scorecard to configs/generated/ranking_scorecard.json | assertion: `assert Path(artifact_path).exists()`

- `alternatives_rejected`:
  - "Use torch" — rejected: unnecessary dependency for linear combination; numpy sufficient.
  - "Skip stable sort" — rejected: violates INV-RANK-DETERMINISM when ties exist.
  - "Use float32" — rejected: precision risk; float64 required per deterministic_assumptions.

- `correctness_criteria`:
  - validate_inputs: NaN/Inf → (False, True); valid → (True, False); empty → (True, False) with empty scores.
  - compute_composite_score: shape (n,); values in [0,1]; monotone in each sub-score; deterministic.
  - VERIFY:L1: zero violations in 1000-sample monotonicity sweep.
  - VERIFY:L2: bit-identical results across 3 seeded runs.
  - Scorecard: all acceptance_checks pass; `final_decision: "GO"`.

`[PHASE H COMPLETE — all deliverables met]`

## S — Stress-test (with MA scorecard)

- `functional_tests`:
  - 100 valid candidates → correct scores, correct ordering, correct shape.
  - Single candidate → trivially ordered.
  - All candidates with same sub-scores → stable ordering by insertion order.

- `edge_adversarial_tests`:
  - Empty candidate list → empty array, no error.
  - One candidate with NaN relevance → fail-closed, error flag True.
  - All candidates NaN → fail-closed, error flag True.
  - 100,000 candidates → completes in < 2s.
  - Weights that don't sum to 1.0 → validation error before scoring.

- `determinism_replay_checks`:
  - Seeds [42, 123, 256]: all three runs produce bit-identical output arrays.
  - Candidate input order shuffled: output ranking is identical.

- `acceptance_gates`:
  - `INV-RANK-DETERMINISM`: `deterministic_replay_pass == true`
  - `INV-RANK-MONOTONICITY`: `monotonicity_pass == true`
  - `INV-RANK-FAILCLOSED`: `failclosed_pass == true`
  - All gates must be green for GO.

- Scorecard artifact at `configs/generated/ranking_scorecard.json`:

```json
{
  "invariant_results": {
    "INV-RANK-DETERMINISM": true,
    "INV-RANK-MONOTONICITY": true,
    "INV-RANK-FAILCLOSED": true
  },
  "notebook_hash": "sha256:<computed-at-runtime>",
  "seed_lock": {
    "seeds_used": { "numpy": 42, "random": 42 },
    "all_locked": true
  },
  "deterministic_replay_pass": true,
  "final_decision": "GO"
}
```

`[PHASE S COMPLETE — all deliverables met]`
`FINAL_DECISION: GO`

## Output Contract

- Deliverables:
  - Verification notebook: `notebooks/math/ranking_scoring_verification.ipynb`
  - Scorecard artifact: `configs/generated/ranking_scorecard.json`
  - Invariant YAMLs: `invariants/INV-RANK-DETERMINISM.yaml`, `INV-RANK-MONOTONICITY.yaml`, `INV-RANK-FAILCLOSED.yaml`
  - Lemmas: L1, L2 in `docs/math/LEMMAS_APPENDIX.md`
  - Extracted code (after S green): `src/<project>/ranking.py`
- Artifact JSON schema: see S phase scorecard schema above.
- Validation result: all gates green; deterministic replay pass.
- Residual risks: float64 precision across different CPU architectures (mitigated by rounding to 15 sig digits).
- Evidence links: notebook path, scorecard path, invariant paths.
- Blocking decisions taken: none.
- Follow-up actions: promote invariant status from `proposed` to `accepted` after merge.

## Required Completion Block

- `M` complete? `yes` — problem, stakeholders, metrics, constraints, out-of-scope, determinism definition, guarantees, boundaries all defined
- `A` complete? `yes` — governing formula, variable definitions, operator properties, boundary conditions, convergence, deterministic assumptions all defined
- `T` complete? `yes` — lemmas L1/L2 with all sub-fields; 3 invariant YAMLs with all fields; CI gate mapping; fail-closed semantics defined
- `H` complete? `yes` — notebook structure with per-cell purpose/mapping/assertions; alternatives rejected; correctness criteria defined; notebook runs end-to-end
- `S` complete? `yes` — functional, edge, replay, acceptance tests defined; scorecard artifact generated; all gates green
- `Assure` required? `no`
- `Observe` required? `no`
- Final Decision: `GO`
- Approved by: Ranking lead + MA maintainer
- Timestamp (UTC): `2026-02-22T00:00:00Z`
