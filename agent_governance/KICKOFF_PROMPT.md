# Agent Governance Kit — Installation Kickoff Prompt

> **Drop this prompt into any AI agent to bootstrap the Agent Governance Kit.**
> Copy everything below the line into your agent. The agent will learn the framework, then execute installation.

---

## Execution Prompt — MATHS Workstream (Governance Kit Installation)

Plan Reference: `plan:governance-kit-install`
Parent Plan: `N/A — this is the bootstrap plan`
North Star: `To be created during installation (docs/governance/NORTH_STAR.md)`

**Mission:** Install and configure the Agent Governance Kit for this project. Read every section of this prompt completely before acting. Do not skim. Then execute installation by following `agent_governance/INSTRUCTIONS.md` step by step.

## Model Configuration (for prompt runner)

- Set temperature to 0 (or as low as the platform allows).
- Set top_p to 1.0 (no nucleus sampling truncation).
- Disable any "creative" or "balanced" mode; use "precise" if available.
- If the platform supports a system prompt, paste the Governance Lock and Agent Constraints sections into it.

---

## What You Are Installing

This is a **portable AI agent governance framework** — a set of files and processes that control how AI agents work on this repository. After installation, every AI agent (including you) will operate under a deterministic, plan-driven, approval-gated workflow.

The framework exists because LLMs are probabilistic. 90% accuracy per step yields approximately 59% accuracy over 5 steps and approximately 35% over 10 steps. Without structure, agents drift from scope, fabricate information, skip validation, make unauthorized changes, and produce inconsistent results. This framework pushes reliability into deterministic processes and reserves flexibility for reasoning.

### The Operating Model

| Layer | What It Does | Where It Lives |
|-------|-------------|----------------|
| **Vision** | Defines ultimate goals, metrics, success criteria | `docs/governance/NORTH_STAR.md` |
| **Governance** | Execution plans, action logs, project status | `docs/governance/` |
| **Rules** | Mandatory constraints that shape all agent behavior | `.cursor/rules/**/*.mdc` (if present) |
| **Plans** | Formal execution plans defining WHAT to achieve | `/plans/` via `agent_governance/PLAN_TEMPLATE.md` |
| **Prompts** | Formal task instructions defining HOW to execute | `docs/prompts/` via `agent_governance/master-maths-prompt-template.md` |
| **Tools** | Deterministic scripts, notebooks, validators | `scripts/`, `notebooks/`, `Makefile` |
| **Context** | Domain knowledge, specs, architecture docs | `docs/` |
| **Artifacts** | Generated outputs from validated notebook work | `configs/generated/`, `notebooks/` |

### The Agent's Role

You are the **orchestration layer**. You sit between what needs to happen (plans, prompts) and getting it done (tools, notebooks, artifacts). You read instructions from plans and prompts. You apply rules and governance constraints at every step. You use tools deterministically — never guess what a tool can tell you. You produce artifacts via validated notebooks. You report results via action logs. You escalate when blocked — never work around a problem. You make decisions. Tools execute. Governance validates. The owner approves.

---

## What Is {{PROJECT_NAME}} (MA)

{{PROJECT_NAME}} (MA) is a rigorous, phased process for implementing any code that involves mathematical operations, algorithms, or performance guarantees. It is the core intellectual foundation of this governance framework.

### Why MA Exists

Math and algorithm code has unique risks that general-purpose development practices do not address:

- **Non-determinism**: Floating-point arithmetic, sort stability, and unseeded randomness produce different results across runs. A function can return a slightly different answer every time it is called.
- **Silent failure**: A scoring function can return plausible-looking but incorrect results. Unlike a crash, nobody notices until the damage is done.
- **Undocumented assumptions**: If the developer (or AI) assumes inputs are always positive but does not check, a negative input silently corrupts results.
- **Untestable claims**: "This algorithm is O(n log n)" is meaningless without proof. "This function is monotonic" is a claim that must be formally verified, not asserted.

MA solves this by requiring that every piece of math/algorithm code goes through a formal process: define intent, formalize the math, create machine-enforced guarantees (invariants), write formal claims with proofs (lemmas), implement in notebooks (not directly in code files), generate validation artifacts (scorecards), and only then extract to the codebase.

### The Authoritative MA Standard

**Read this document for the complete, definitive explanation of {{PROJECT_NAME}}:**

`agent_governance/mathematical_autopsy:_deterministic_ai_creation.md`

This whitepaper covers:
- The probabilistic crisis in AI development and why it matters
- The foundational inversion: intent before code
- The human-AI formalization loop
- Operator theory as engineering substrate
- Invariants as the structural skeleton of systems
- Lemmas and executable proof
- Notebook-centered verification
- The validation pipeline and build orchestration
- Falsification as a safety mechanism
- Governance layering (North Star, execution plans, action logs)
- Team topology and agent specialization
- How MA compares to traditional TDD, formal methods, and MLOps

This is the most important document in the governance kit for understanding the "why" behind every process.

### Key MA Concepts

- **Invariant**: A machine-enforced guarantee defined in a YAML file. Example: "Scoring produces bit-identical outputs given identical inputs and seeds." Invariants are tested automatically and block deployment if violated.
- **Lemma**: A formal mathematical claim with a proof sketch. Example: "The composite score is strictly monotone in each sub-score given positive weights." Lemmas provide the mathematical reasoning that invariants enforce.
- **Scorecard**: A JSON artifact generated by running a verification notebook. Contains pass/fail results for every invariant, seed-lock verification, and a GO/NO-GO decision.
- **Notebook-first development**: All math/algorithm code is written and tested in Jupyter notebooks first, then extracted to Python files only after the scorecard is green. This ensures code is validated before it enters the codebase.
- **Fail-closed**: When an invariant is violated (e.g., NaN detected in a score), the system rejects the result rather than silently proceeding. This is a core safety principle.

### When MA Applies

MA is **required** when the work involves: new mathematical operations or algorithms, new performance guarantees (latency, throughput, accuracy thresholds), changes to existing math that affect correctness, or any code involving computation with determinism requirements.

MA is **not required** for: trivial bug fixes that do not change mathematical behavior, documentation-only changes, configuration changes that do not affect algorithms, or pure infrastructure (CI pipelines, deployment scripts).

---

## What Is the MATHS Framework

MATHS is a reusable prompt-template structure for structured work. It stands for **Model, Annotate, Tie, Harness, Stress-test**. It is not the MA process.

### The Five Phases

| Phase | Name | Purpose |
|-------|------|---------|
| **M** | Model | Define the problem, stakeholders, success metrics, constraints, and boundaries |
| **A** | Annotate | Define formal rules, assumptions, and data contracts |
| **T** | Tie | Define dependencies, failure modes, and go/no-go criteria |
| **H** | Harness | Create the implementation and validation harness plan |
| **S** | Stress-test | Run tests, validate, and certify against explicit acceptance gates |

If a task separately requires MA, include the MA deliverables explicitly in the prompt and execute MA directly. Do not treat the MATHS letters as MA phases.

### Phase Protocol

Each phase must be completed before the next begins. After completing a phase, emit an exit checklist and wait for user confirmation. If blocked, emit a BLOCKED signal and do not proceed. Never batch phases unless explicitly told to.

---

## Files in This Kit

You are working with the `agent_governance/` directory. Here is every file and what it does:

### System Instructions

| File | What It Is | Where It Goes After Install |
|------|-----------|----------------------------|
| `AGENTS.md` | System instructions for all AI agents. Defines the operating model, mandatory rules, process architecture, hard constraints, workflow, canonical vocabulary, and escalation protocol. This is the first file any agent reads. | Project root: `<project-root>/AGENTS.md` |
| `CLAUDE.md` | Identical to AGENTS.md except for the title. Exists because Claude-family models read `CLAUDE.md` by convention. | Project root: `<project-root>/CLAUDE.md` |

### Templates and Schemas

| File | What It Is | Where It Stays |
|------|-----------|----------------|
| `PLAN_TEMPLATE.md` | Master template for execution plans. Every unit of work requires a formal plan created from this template. Contains 22 sections covering everything from objectives to rollback procedures. | `agent_governance/PLAN_TEMPLATE.md` |
| `PLAN_TEMPLATE_SCHEMA.yaml` | YAML schema for validating plan files. Machine-readable structure that mirrors the Markdown template. | `agent_governance/PLAN_TEMPLATE_SCHEMA.yaml` |
| `PLAN_TEMPLATE_SCHEMA.json` | JSON Schema for programmatic plan validation. Use for automated CI checks. | `agent_governance/PLAN_TEMPLATE_SCHEMA.json` |
| `master-maths-prompt-template.md` | Master prompt template using the MATHS structure. Use this when creating prompts for structured governed work. | `agent_governance/master-maths-prompt-template.md` |

### Reference Documents

| File | What It Is | Where It Stays |
|------|-----------|----------------|
| `mathematical_autopsy:_deterministic_ai_creation.md` | **The definitive standard on {{PROJECT_NAME}}.** A comprehensive whitepaper covering the theory, practice, and rationale behind the MA process. Read this to fully understand why the framework exists and how every piece connects. | `agent_governance/mathematical_autopsy:_deterministic_ai_creation.md` |
| `INSTRUCTIONS.md` | Step-by-step installation and customization guide. This is the operational document you will execute. | `agent_governance/INSTRUCTIONS.md` |
| `KICKOFF_PROMPT.md` | This file. The bootstrapping prompt that brings an agent up to speed and triggers installation. | `agent_governance/KICKOFF_PROMPT.md` |

---

## Process Architecture (Post-Installation)

After installation, all work in this repository flows through this process:

```
User Request
    ↓
Agent reads AGENTS.md / CLAUDE.md (system instructions)
    ↓
Agent reads North Star (docs/governance/NORTH_STAR.md)
    ↓
Agent reads Execution Plan (docs/governance/EXECUTION_PLAN.md)
    ↓
Plan exists for this work?
  ├── YES → Follow plan, get change approval from user
  └── NO  → Create plan using agent_governance/PLAN_TEMPLATE.md, get approval
    ↓
Math/Algorithm scope?
  ├── YES → Execute the required methodology directly (MA when required by scope/plan)
  │         Prompt-template selection, including MATHS, is independent
  │         Authoritative MA reference: agent_governance/mathematical_autopsy:_deterministic_ai_creation.md
  └── NO  → Execute per plan with standard change approval
    ↓
Implementation (notebook-first for math/algo, standard for other)
    ↓
Validation (tests, lints, invariant checks, scorecard)
    ↓
Post-Work (action log entry, execution plan update, governance closure)
```

---

## Agent Constraints (Active During Installation)

Even during installation, these constraints apply:

- Do not guess, fabricate, or assume information you do not have. If uncertain, ask.
- Do not write to files without explicit user approval ("go"). Present your plan and wait.
- Do not skip steps in the installation process.
- Do not modify the template files in ways not specified by INSTRUCTIONS.md.
- If a directory or file already exists, check its contents before overwriting.
- If you encounter something unexpected (existing governance docs, conflicting structure), stop and ask.
- Use tools (file read, grep, glob) to verify state. Never assume a path exists or a file has specific content.

---

## M — Model

### Problem Statement

This project does not have a formal AI agent governance framework. Without one, AI agents operating on the codebase will lack structured workflows, mandatory validation gates, plan-driven execution, and the {{PROJECT_NAME}} process for math/algorithm work. This leads to scope drift, unauthorized changes, inconsistent outputs, and undocumented work.

### Stakeholders

- **Project owner**: Needs deterministic, traceable, approval-gated AI agent behavior.
- **All AI agents**: Need clear operating instructions, constraints, and workflows.
- **Future contributors**: Need to understand how AI agents are governed in this project.

### Success Metrics

- `agents_md_at_root == true` — AGENTS.md exists at project root with project-specific content.
- `claude_md_at_root == true` — CLAUDE.md exists at project root, identical to AGENTS.md except title.
- `governance_docs_exist == true` — All four governance documents exist in `docs/governance/`.
- `directory_structure_complete == true` — All required directories exist (`plans/`, `docs/prompts/`, etc.).
- `all_placeholders_replaced == true` — No `<FILL:...>` placeholders remain in any installed file.
- `templates_in_agent_governance == true` — All template files remain in `agent_governance/`.

### Constraints

- Do not delete or overwrite existing project files without explicit approval.
- Do not modify the governance kit templates beyond what INSTRUCTIONS.md specifies (placeholder replacement and customization).
- Do not create governance documents (North Star, Execution Plan) without understanding the project's actual goals — ask the user.

### Out of Scope

- Implementing project features or writing application code.
- Creating `.cursor/rules/` files (these are optional and project-specific).
- Running tests, linting, or CI pipelines (the project may not have them yet).
- Modifying any files outside the governance kit and governance directories.

`[PHASE M COMPLETE — all deliverables met]`

---

## A — Annotate

### Formal Rules

1. **File placement rule**: `AGENTS.md` and `CLAUDE.md` go to the project root. All other kit files remain in `agent_governance/`.
2. **Customization rule**: Every `<FILL:...>` placeholder in every file must be replaced with project-specific values. No placeholder may remain.
3. **Governance document rule**: Four governance documents must be created in `docs/governance/`: North Star, Execution Plan, Action Log, Project Status. These are NOT included in the kit — they must be created with project-specific content.
4. **Directory creation rule**: All required directories must exist before files are placed in them.
5. **Idempotency rule**: If a directory or file already exists, do not overwrite unless the existing content is empty or a placeholder. Ask the user before overwriting non-empty files.

### Assumptions

- The `agent_governance/` directory exists and contains all kit files.
- The user has approval authority over this project.
- The user can provide project-specific information (vision, goals, metrics) for governance documents.
- The project uses Python (if math/algorithm work applies). If not, MA-specific directories (`notebooks/`, `invariants/`, `configs/generated/`) may be skipped.

### Data Contracts

**Input:** The `agent_governance/` directory containing these files:

```
agent_governance/
├── INSTRUCTIONS.md              ← installation guide (read and execute)
├── KICKOFF_PROMPT.md            ← this prompt
├── AGENTS.md                    ← system instructions template
├── CLAUDE.md                    ← system instructions template (Claude variant)
├── PLAN_TEMPLATE.md             ← execution plan template
├── PLAN_TEMPLATE_SCHEMA.yaml    ← plan schema (YAML)
├── PLAN_TEMPLATE_SCHEMA.json    ← plan schema (JSON Schema)
├── master-maths-prompt-template.md  ← MATHS prompt template
└── mathematical_autopsy:_deterministic_ai_creation.md  ← MA whitepaper (authoritative standard)
```

**Output:** A fully configured project with this structure:

```
<project-root>/
├── AGENTS.md                           ← customized system instructions
├── CLAUDE.md                           ← customized system instructions (Claude variant)
├── agent_governance/                   ← templates + reference docs (unchanged except customization)
├── docs/
│   ├── governance/
│   │   ├── NORTH_STAR.md               ← project vision (created)
│   │   ├── EXECUTION_PLAN.md           ← authorized work plan (created)
│   │   ├── ACTION_LOG                  ← action history (created, initially empty)
│   │   └── PROJECT_STATUS.md           ← project state (created)
│   ├── math/                           ← if MA applies
│   │   ├── README.md
│   │   └── LEMMAS_APPENDIX.md
│   └── prompts/                        ← prompt storage
├── plans/                              ← execution plans storage
├── invariants/                         ← if MA applies
│   ├── INDEX.yaml
│   └── INV_TEMPLATE.yaml
├── notebooks/math/                     ← if MA applies
└── configs/generated/                  ← if MA applies
```

### Required Artifacts

- No JSON artifacts for this installation task (this is infrastructure, not math).
- The "artifacts" are the installed and customized files themselves.

`[PHASE A COMPLETE — all deliverables met]`

---

## T — Tie

### Dependency Checks

- `agent_governance/` directory exists with all 9 files listed in Section A.
- Project root is accessible and writable.
- User is available to provide project-specific information (vision, goals, metrics).

### Known Failure Modes

| Failure Mode | Prevention |
|-------------|-----------|
| `agent_governance/` directory missing or incomplete | Verify all 9 files exist before starting. If any are missing, emit BLOCKED. |
| Existing `AGENTS.md` or `CLAUDE.md` at project root | Check before overwriting. Ask user whether to replace or merge. |
| Existing `docs/governance/` with populated files | Check contents before overwriting. Ask user whether to replace or merge. |
| User cannot provide project vision/goals | Emit BLOCKED. Governance documents require project-specific content. |
| Project is not Python-based | Skip MA-specific directories (notebooks/, invariants/, configs/generated/). All other installation proceeds normally. |
| Placeholder `<FILL:...>` missed during customization | The S phase (Stress-test) includes a grep for remaining placeholders. |

### Confidence Protocol

If uncertain about any of the following, stop and ask the user:
- Whether existing files should be overwritten
- What the project's vision, goals, and metrics are
- Whether the project involves math/algorithm work (determines whether MA directories are needed)
- Whether the project uses Python

### Go/No-Go

**GO** — provided `agent_governance/` directory is complete and user is available.

`[PHASE T COMPLETE — all deliverables met]`

---

## H — Harness

### Execution Plan

This is the core action phase. Execute these steps in order.

**Step 0: Read the MA whitepaper (background understanding)**

Read `agent_governance/mathematical_autopsy:_deterministic_ai_creation.md` to understand the full theoretical foundation of the governance framework. You do not need to memorize every detail, but you must understand:
- Why intent must come before code (Section 3)
- What invariants are and why they matter (Section 6)
- What notebook-centered verification means (Section 8)
- How governance layering works (Section 14)

This document is the authoritative standard on MA. If anything in the other kit files seems ambiguous or contradictory regarding MA, this whitepaper is the tiebreaker.

**Step 1: Read the installation instructions**

Read `agent_governance/INSTRUCTIONS.md` completely. This document contains the step-by-step installation process. What follows below is a summary — the INSTRUCTIONS document is the detailed operational guide.

**Step 2: Verify kit completeness**

Before any file operations, verify all 9 files exist in `agent_governance/`:

```
INSTRUCTIONS.md
KICKOFF_PROMPT.md
AGENTS.md
CLAUDE.md
PLAN_TEMPLATE.md
PLAN_TEMPLATE_SCHEMA.yaml
PLAN_TEMPLATE_SCHEMA.json
master-maths-prompt-template.md
mathematical_autopsy:_deterministic_ai_creation.md
```

If any file is missing, emit BLOCKED and report which files are missing.

**Step 3: Check for existing governance infrastructure**

Before creating anything, check what already exists:
- Does `AGENTS.md` exist at the project root?
- Does `CLAUDE.md` exist at the project root?
- Does `docs/governance/` exist? If so, what files are in it?
- Does `plans/` exist?
- Does `docs/prompts/` exist?

Report findings to the user. If non-empty governance files exist, ask the user whether to replace, merge, or skip.

**Step 4: Execute INSTRUCTIONS.md Steps 1-7**

Follow `agent_governance/INSTRUCTIONS.md` steps 1 through 7 exactly:

1. **Step 1**: Copy `AGENTS.md` and `CLAUDE.md` to project root.
2. **Step 2**: Verify templates remain in `agent_governance/`.
3. **Step 3**: Create required directory structure.
4. **Step 4**: Create governance documents (North Star, Execution Plan, Action Log, Project Status) — **ask the user for project-specific information**.
5. **Step 5**: Customize all files for this project (replace all `<FILL:...>` placeholders).
6. **Step 6**: Create invariant template if MA applies.
7. **Step 7**: Verify installation using the checklist.

**Critical: Step 4 requires user input.** You cannot create a North Star document or Execution Plan without knowing the project's actual vision, goals, and authorized work. Ask the user. Do not fabricate project details.

**Step 5: Present installation summary to user**

After completing all steps, present a summary:
- Files created (with paths)
- Files customized (with paths)
- Directories created
- Governance documents created
- Any items skipped (with reason)
- Any items that need user follow-up

`[PHASE H COMPLETE — all deliverables met]`

---

## S — Stress-test

### Verification Checklist

After installation, verify every item:

**File Existence**

- [ ] `<project-root>/AGENTS.md` exists and contains project-specific content
- [ ] `<project-root>/CLAUDE.md` exists and is identical to AGENTS.md except title
- [ ] `agent_governance/INSTRUCTIONS.md` exists (unchanged)
- [ ] `agent_governance/KICKOFF_PROMPT.md` exists (unchanged)
- [ ] `agent_governance/PLAN_TEMPLATE.md` exists
- [ ] `agent_governance/PLAN_TEMPLATE_SCHEMA.yaml` exists
- [ ] `agent_governance/PLAN_TEMPLATE_SCHEMA.json` exists
- [ ] `agent_governance/master-maths-prompt-template.md` exists
- [ ] `agent_governance/mathematical_autopsy:_deterministic_ai_creation.md` exists (unchanged)

**Governance Documents**

- [ ] `docs/governance/NORTH_STAR.md` exists with project vision and metrics
- [ ] `docs/governance/EXECUTION_PLAN.md` exists with authorized work
- [ ] `docs/governance/ACTION_LOG` exists
- [ ] `docs/governance/PROJECT_STATUS.md` exists

**Directory Structure**

- [ ] `plans/` directory exists
- [ ] `docs/prompts/` directory exists
- [ ] `docs/math/` directory exists (if MA applies)
- [ ] `invariants/` directory exists (if MA applies)
- [ ] `notebooks/math/` directory exists (if MA applies)
- [ ] `configs/generated/` directory exists (if MA applies)

**Placeholder Verification**

- [ ] No `<FILL:` strings remain in `<project-root>/AGENTS.md`
- [ ] No `<FILL:` strings remain in `<project-root>/CLAUDE.md`
- [ ] No `<FILL:` strings remain in any customized file

Run this command (or equivalent) to verify no placeholders remain:

```bash
grep -r "<FILL:" AGENTS.md CLAUDE.md agent_governance/PLAN_TEMPLATE.md agent_governance/PLAN_TEMPLATE_SCHEMA.yaml agent_governance/PLAN_TEMPLATE_SCHEMA.json agent_governance/master-maths-prompt-template.md
```

If any `<FILL:` strings are found, go back and replace them.

**Cross-Reference Verification**

- [ ] `AGENTS.md` references `agent_governance/PLAN_TEMPLATE.md` correctly
- [ ] `AGENTS.md` references `agent_governance/master-maths-prompt-template.md` correctly
- [ ] `AGENTS.md` references `agent_governance/mathematical_autopsy:_deterministic_ai_creation.md` as the MA standard
- [ ] `AGENTS.md` references all four governance documents with correct paths
- [ ] `CLAUDE.md` matches AGENTS.md (except title)

### Acceptance Gates

- `all_files_exist == true`
- `all_governance_docs_created == true`
- `all_placeholders_replaced == true`
- `cross_references_valid == true`

All gates must be green.

`[PHASE S COMPLETE — all deliverables met]`
`FINAL_DECISION: GO`

---

## Output Contract

- **Deliverables:**
  - Fully installed and customized governance framework
  - AGENTS.md and CLAUDE.md at project root
  - Four governance documents in `docs/governance/`
  - All required directories created
  - All templates customized for the project
  - Installation summary presented to user

- **Done when:**
  - All S phase verification items checked
  - All acceptance gates green
  - No `<FILL:...>` placeholders remain
  - User has confirmed installation is correct

- **Follow-up actions after installation:**
  - Log the installation in `docs/governance/ACTION_LOG` (first entry)
  - For all future work, follow the process architecture defined in AGENTS.md
  - If a task separately requires MA, follow MA directly; use the MATHS template only if that prompt structure is desired
  - For all work, create formal plans using the plan template
  - Refer to `agent_governance/mathematical_autopsy:_deterministic_ai_creation.md` for the complete MA standard

---

## Required Completion Block

- `M` complete? `<fill after phase>` — problem, stakeholders, success metrics, constraints, out-of-scope
- `A` complete? `<fill after phase>` — rules, assumptions, data contracts, input/output structure
- `T` complete? `<fill after phase>` — dependencies, failure modes, confidence protocol, go/no-go
- `H` complete? `<fill after phase>` — INSTRUCTIONS.md read and executed, all steps completed, summary presented
- `S` complete? `<fill after phase>` — all verification items checked, all gates green, no placeholders remain
- `Assure` required? `no`
- `Observe` required? `no`
- Final Decision: `<GO or NO-GO>`
- Approved by: `<project owner>`
- Timestamp (UTC): `<fill-at-runtime>`

---

## Quick Reference — What to Read and When

| Order | Document | Why |
|-------|----------|-----|
| 1 | This prompt (`KICKOFF_PROMPT.md`) | Understand the framework, context, and plan |
| 2 | `mathematical_autopsy:_deterministic_ai_creation.md` | Understand the MA standard (the "why" behind everything) |
| 3 | `INSTRUCTIONS.md` | Execute the installation step by step |
| 4 | `AGENTS.md` (after customization) | Verify the system instructions are complete and correct |
| 5 | `PLAN_TEMPLATE.md` | Understand how plans are structured (for future work) |
| 6 | `master-maths-prompt-template.md` | Understand how prompts are structured (for future work) |

---

**Kit Version:** 1.1
**Last Updated:** 2026-03-15
