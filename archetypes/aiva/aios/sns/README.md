# SNS — Somatic Nervous System

**Voluntary execution: the “doing” path of AIOS**

Part of the **AIOS** (Biology layer) in the **AIVA** archetype. [← Back to AIOS](../README.md) · [← Back to AIVA](../../README.md)

## Role

The **Somatic Nervous System (SNS)** is the voluntary execution arm of AIOS. Like the body’s somatic system carrying out deliberate actions, the SNS takes the plans and blueprints produced by the COE and turns them into actual execution: molecule → DAG → run. It **coordinates** the “doing” path: intent → COE → blueprint → **AQL** (Chemistry) → **AEF** (Physics). It does not decide *what* to do (that’s the COE) or *how healthy* the system is (that’s the ANS)—it executes.

## Key functions

- **`coordinate_sns(A_t, S_t)`** — Coordinates SNS systems for task execution. Takes actions \(A_t\) and system state \(S_t\); returns execution state \(E_t = f_{\text{execute}}(T_t, R_t, S_t)\) with canonical fields.
- **Molecule → DAG → run** — Converts molecule blueprints to executable DAGs, manages runtime sequencing, and drives execution through AQL (compilation) and AEF (particle execution).
- **`execute_tasks(task_decomposition, resource_allocation, system_state)`** — Executes tasks using SNS systems; returns execution state with performance metrics.
- **`compute_coordination(system_graph, resource_allocation)`** — Computes coordination matrix for system orchestration; resource flow and allocation.

## Mathematical contracts

- Execution state \(E_t\) and coordination outputs conform to the **runtime symbol map** and **runtime function contracts**.
- Resource allocation is non-negative; task decomposition is valid; system state is consistent.
- Determinism: same inputs and config → same execution state (under lattice axioms).

## Integration

- **From COE** — Receives parsed intent, plans, and blueprints. Does not second-guess intent; it executes.
- **To AQL** — Sends molecule blueprints; AQL compiles to DAGs.
- **To AEF** — DAGs are executed as particle instructions; AEF returns telemetry.
- **To ANS** — Execution state \(E_t\) and telemetry are fed to ANS for monitoring and feedback.

## Semi-autonomous behavior

The SNS runs in a semi-autonomous way relative to the COE: it receives a plan and carries it out without constantly asking the “brain” for permission at each step. Coordination and resource flow are computed locally where possible; only when thresholds or policies are violated does the ANS/COE intervene (e.g. fail-close, policy tuning). This mirrors the body: voluntary motion is coordinated by the spinal cord and cerebellum without the cortex micromanaging every muscle.
