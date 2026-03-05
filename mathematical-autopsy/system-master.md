# MA System Master

**Status:** Active  
**Owner:** @smarthaus  
**System of Record:** Mathematical Autopsy operating model  
**Last Updated:** 2026-02-19

---

## 1) Purpose

This document is the canonical system specification for Mathematical Autopsy (MA).  
It defines how MA converts intent into mathematically governed, reproducible, and auditable execution.

This file is the single source of truth for:

- End-to-end MA operating model
- Governance and decision boundaries
- Notebook-first implementation doctrine
- Deterministic validation and release controls
- Alignment to Agile, DevOps, and SRE practices

---

## 2) Relationship to Existing Governance Docs

This master spec does not replace core governance artifacts. It integrates them.

- Strategic intent: `docs/governance/NORTH_STAR.md`
- Authorized work map: `docs/governance/EXECUTION_PLAN.md`
- Current progress: execution milestones and artifact evidence in `docs/governance/EXECUTION_PLAN.md`
- Agent runtime guardrails: `AGENTS.md`
- Enforcement rules: `.cursor/rules/`

If this document conflicts with the North Star or execution plan, those governance documents win until this file is updated.

---

## 2.1 File Naming Contract (Deterministic)

To prevent path drift and agent ambiguity, MA documentation and template assets use one naming rule:

- `lowercase-kebab-case` for `.md`, `.yaml`, `.json`, and `.ipynb` files inside `framework/docs/`, `framework/prompts/`, `framework/plans/`, and `framework/notebooks/`.

Explicit exceptions:

- repository-standard control files (`README.md`, `LICENSE`, `CODEOWNERS`, and similar)
- invariant IDs (`INV-*.yaml`) and invariant index (`INDEX.yaml`)
- fixed log/system artifact names (for example `CODEX_ACTION_LOG`)

If a filename conflicts with this contract, it must be renamed and all references updated in the same change.

---

## 2.2 Repository Boundary Model (Framework vs Application)

MA has two distinct concerns that must remain separated:

- **Framework:** methodology and assurance system
- **Application:** runtime product implementation

### Framework Scope

Owns:

- Mathematical definitions and process (`framework/docs/ma-methodology.md`, `framework/docs/math/`)
- Invariants and contracts (`framework/invariants/`, `framework/contracts/`)
- Verification notebooks and artifacts (`framework/notebooks/`, `framework/configs/generated/`)
- Validation gates and scorecard orchestration (`framework/scripts/`, `framework/tools/`, `Makefile`)
- Reusable verification patterns (`framework/patterns/`)

### Application Scope

Owns:

- Native UI and client UX (`app/src/native_app/`)
- Runtime orchestration and service lifecycle (`app/src/ma_platform/`)
- IDE bridge and runtime tools (`app/src/mcp_server/`)
- Runtime launch/integration scripts (`app/scripts/ma_service_launcher.py`)
- Application integration tests (`app/tests/integration/`)

### Boundary Rule

Framework changes must not require app runtime changes unless they alter integration contracts.  
Application changes must not redefine framework guarantees without updating formal docs/invariants and re-running validation.

### Separation Entry Points

- Framework boundary marker: `framework/readme.md`
- Application boundary marker: `app/readme.md`

### Root Policy

Root is repository scaffolding only. Domain-owned assets must live in `framework/` or `app/`.

---

## 3) Core System Principle

**MA is an assurance architecture for AI development.**

It enforces:

- **Traceability:** every meaningful output links to formal math and explicit requirements
- **Determinism:** verification outputs are reproducible under controlled inputs
- **Governance:** no high-impact execution outside approved policy and validated gates

Operationally:

1. Formalize math and constraints
2. Encode guarantees as invariants and lemmas
3. Implement and verify in notebooks
4. Generate artifacts and scorecards
5. Permit extraction and promotion only when gates pass

---

## 4) MA Execution Stack

### 4.1 Strategic Layer

- North Star defines mission, architecture direction, and non-negotiable properties.
- Execution Plan defines what work is authorized now.

### 4.2 Formal Layer

- Mathematics documents define equations, domains, assumptions, and bounds.
- Invariants define enforceable guarantees and acceptance checks.
- Lemmas provide human-readable proof framing linked to invariant IDs.

### 4.3 Implementation Layer

- Notebooks are the implementation source for math-sensitive logic.
- Code is extracted from notebooks after validation; codebase is downstream artifact.

### 4.4 Validation Layer

- CI and local gates verify determinism, artifact validity, invariant alignment, and quality score.
- Promotion decisions are based on gate outcomes and scorecard policy.

### 4.5 Governance Layer

- MGE-backed policy decisions govern what actions are allowed.
- Action logs, receipts, and artifacts provide forensic evidence.

---

## 4.6 MATHS + Assure/Observe Execution Loop (Mandatory)

MA uses a MA-aligned loop derived as the operating model.

**Loop:** `M -> A -> T -> H -> S` with optional overlays `Assure` and `Observe`.

- **M (Model):** define problem, user, success criteria, constraints
- **A (Annotate):** formalize data/contracts/equations/assumptions
- **T (Tie):** validate dependencies, interfaces, policy checks, and readiness
- **H (Harness):** implement via notebook-first process
- **S (Stress-test):** verify behavior under functional and edge conditions
- **Assure (optional for production):** strengthen security/compliance/unit rigor
- **Observe (optional for production):** enforce runtime observability and incident response

No MA-scoped change is complete unless it has passed MATHS step gates and produced required outputs.

### 4.6.1 MATHS Step Mapping to MA


| MATHS Step         | MA Phase / System Layer                           | Required Outputs                                                                         | Gate to Proceed                                                      |
| ------------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Model              | Phase 1 Intent + North Star/Execution Plan checks | Problem statement, user, measurable success, constraints, plan reference                 | North Star alignment confirmed and work authorized in execution plan |
| Annotate           | Phase 2 Mathematics + Phase 3 preconditions       | Notation, equations, assumptions, data/interface contracts, candidate invariants         | Math and contracts are explicit enough to verify deterministically   |
| Tie                | Governance preflight + tool/dependency validation | Connection checks, path validity, policy checks, required artifacts and notebook targets | All required dependencies/checks green; no unresolved blockers       |
| Harness            | Phase 4 Verification (notebook-first)             | Notebook implementation, assertions, generated artifacts, extraction candidate           | Notebook executes successfully and outputs valid artifacts           |
| Stress-test        | Phase 5 CI enforcement + scorecard                | Gate results, stress outcomes, failure-mode evidence, scorecard decision                 | Required gates pass and scorecard policy permits promotion           |
| Assure (optional)  | Release hardening controls                        | Security checks, stricter tests, edge-case coverage, input sanitization evidence         | Hardening criteria complete for release class                        |
| Observe (optional) | SRE operations and reliability loop               | Telemetry map, alert thresholds, runbooks, rollback/kill-switch readiness                | Operational readiness signed off                                     |


### 4.6.2 Required Output Contract per Step

Each MATHS step must emit a concrete output record.

- **Model output**
  - Problem
  - User/persona
  - Success metrics
  - Constraints
  - North Star and execution-plan reference
- **Annotate output**
  - Formal spec elements (equations, assumptions, bounds)
  - Integration/data contract map
  - Invariant candidates and lemma linkage intent
- **Tie output**
  - Dependency and connection validation checklist
  - Governance preflight status (including MGE where applicable)
  - "Ready for assembly" decision with unresolved risk list (if any)
- **Harness output**
  - Notebook implementation references
  - Artifact generation evidence
  - Extraction candidate scope
- **Stress-test output**
  - Functional and edge-case results
  - Deterministic replay evidence
  - Scorecard and gate outcomes
- **Assure output (optional)**
  - Hardening report and residual risk statement
- **Observe output (optional)**
  - Operational telemetry, alerting, rollback, and autopsy workflow references

### 4.6.3 MATHS Prompt Pack (Mandatory Conversation Prompts)

For consistent prompting and execution, use these questions at each step.

**Model**

- What exact problem are we solving?
- Who is the specific user or stakeholder?
- What measurable outcome defines success?
- What constraints (time, cost, stack, compliance) are non-negotiable?

**Annotate**

- What equations/rules define correctness?
- What assumptions must hold?
- What data and integration contracts exist?
- Which invariants and lemmas should govern this work?

**Tie**

- Are all dependencies and interfaces validated?
- Are required services/tools reachable and configured?
- Are policy/governance checks satisfied?
- What can fail before implementation and how is it prevented?

**Harness**

- Is implementation occurring in notebook-first flow where required?
- Which artifacts must be produced?
- What extraction boundary is authorized?

**Stress-test**

- What functional checks prove expected behavior?
- What edge/adversarial checks prove robustness?
- Are results deterministic and replayable?
- Does scorecard policy permit promotion?

**Assure (optional)**

- What additional release hardening is required for this risk class?
- Are security/compliance checks complete?

**Observe (optional)**

- Which telemetry signals indicate health or drift?
- What triggers rollback or kill-switch?
- Is incident autopsy workflow ready?

### 4.6.4 Go/No-Go Rules

- **No-Go:** Any MATHS step missing required outputs.
- **No-Go:** Any unresolved governance mismatch (North Star, plan, MGE policy where applicable).
- **No-Go:** Any required gate failure or non-permissive scorecard decision.
- **Go:** Only when all required step outputs and gates are satisfied for the change class.

### 4.6.5 Naming Crosswalk (Behavior Unchanged)

- Model = Architect
- Annotate = Trace
- Tie = Link
- Harness = Assemble
- Stress-test = Stress-test
- Assure = Validate
- Observe = Monitor

---

## 5) Notebook-First Doctrine (Hard Requirement)

MA implementation logic follows this sequence:

1. Define math and invariants
2. Implement in notebook cells
3. Execute and verify invariant checks
4. Export artifacts to `framework/configs/generated/`
5. Validate gates and scorecard
6. Extract code to runtime modules only after validation

Implications:

- Production logic must not bypass notebook-first flow for MA-scoped work.
- Artifact quality gates are mandatory inputs to release confidence.
- "Code-only" changes without MA traceability are non-compliant for math-governed behavior.

---

## 6) Deterministic Failure Doctrine

MA follows deterministic failure classification:

- **Contract/Security violation:** terminal, fail-closed behavior
- **Operational/resource failure:** explicit degraded mode with deterministic recovery path

No silent fallback, no hidden self-healing on contract breach, no entropy-dependent transition logic.

All failure transitions must be:

- Explicitly classified
- Logged with canonical records
- Reproducible under identical input and version context

---

## 7) Governance and Authorization Model

No execution is valid unless all are true:

1. Aligned to `docs/governance/NORTH_STAR.md`
2. Authorized in `docs/governance/EXECUTION_PLAN.md`
3. Governed under MGE policy checks where applicable
4. Traceable through logs and artifacts

All meaningful actions should preserve:

- Plan reference
- Decision evidence
- Validation context
- Result status

---

## 8) Alignment with Agile, DevOps, and SRE

MA is not a replacement for Agile, DevOps, or SRE.  
MA is the formal assurance layer that strengthens all three for AI systems.

### 8.1 Agile Alignment

MA incorporates Agile through structured incremental delivery and explicit completion criteria.

- Work is phase- and task-scoped in `docs/governance/EXECUTION_PLAN.md`.
- Each increment has explicit acceptance criteria (invariants, gates, artifacts).
- Progress and transparency are maintained through status and action logs.
- Iteration is disciplined: update math, re-verify, then promote.

**Agile outcome:** predictable, inspectable, requirement-driven increments.

### 8.2 DevOps Alignment

MA incorporates DevOps through automation, reproducibility, and controlled promotion.

- CI/local gates enforce deterministic validation and policy compliance.
- Artifact generation and scorecard evaluation are standardized release checks.
- Promotion flow is controlled by branch and gate policy (feature -> development -> staging -> main).
- Evidence-first release discipline reduces hidden integration risk.

**DevOps outcome:** automated quality enforcement and reliable delivery pipelines.

### 8.3 SRE Alignment

MA incorporates SRE through reliability boundaries, failure handling, and operational evidence.

- Deterministic failure doctrine defines strict failure behavior.
- Scorecards and invariants act as reliability guardrails.
- Fail-closed behavior protects integrity under contract/security breach.
- Incident response uses MA autopsy workflow: capture evidence, identify violated guarantee, remediate, revalidate.

**SRE outcome:** measurable reliability, controlled degradation, and fast root-cause recovery.

### 8.4 MA Crosswalk


| MA Element                                   | Agile                          | DevOps                           | SRE                                    |
| -------------------------------------------- | ------------------------------ | -------------------------------- | -------------------------------------- |
| North Star + execution-plan gating           | Backlog and scope discipline   | Change governance                | Risk-informed planning                 |
| Math -> invariants -> notebooks -> artifacts | Incremental acceptance clarity | Reproducible build/validate flow | Reliability by design                  |
| Invariants and lemmas                        | Definition of Done quality bar | Policy-as-code checks            | Safety boundaries and guardrails       |
| Scorecard decisions                          | Sprint acceptance confidence   | Deployment gating                | Error-budget style quality control     |
| Action logs and receipts                     | Team transparency              | Auditability                     | Incident evidence and postmortem input |


---

## 9) MA Roles and Responsibilities

- **Math Lead:** owns formal definitions, invariants, and thresholds.
- **Gates Owner:** owns CI/local gate health and scorecard integrity.
- **Release Authority:** controls promotion, rollback, and kill-switch decisions.
- **Document Owner:** ensures ADRs, runbooks, and process docs remain current.
- **Agent Operator:** executes approved work under governance and validation policy.

---

## 10) Contracts and Artifacts

Minimum MA contract set:

- Invariants: `framework/invariants/INV-*.yaml`
- Artifact outputs: `framework/configs/generated/*.json`
- Score decision: `framework/scorecard.json`
- Traceability and phase contracts: `framework/contracts/*.yml`
- Receipt/provenance checks: `framework/scripts/ops/verify_receipt.py` and extraction workflow

Every promoted behavior change should have:

- formal reference (equation/lemma/invariant),
- validation evidence (artifact + gates),
- operational trace (logs + plan reference).

---

## 11) Definition of Done

A change is done only when:

1. Authorized by North Star and execution plan
2. Notebook-first implementation and validation path completed (for MA-scoped logic)
3. Required artifacts generated and valid
4. Required gates pass and scorecard policy is satisfied
5. Traceability evidence is recorded
6. Relevant documentation is updated

---

## 12) Adoption Guidance for Future Work

When adding new capabilities:

1. Start with formal intent and mathematical framing
2. Define or update invariants before extraction
3. Build and verify in notebook first
4. Keep deterministic tool boundaries explicit
5. Promote only through gate-backed evidence

This keeps MA consistent as both a methodology and an operationally enforceable platform.

---

## 13) Positioning Statement

Mathematical Autopsy operationalizes:

- **Agile** for iterative, requirement-driven delivery,
- **DevOps** for automated validation and release discipline,
- **SRE** for reliability and deterministic failure handling,

while adding a math-first assurance layer required for trustworthy AI systems.