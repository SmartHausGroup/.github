# SNS — Somatic Nervous System

**Voluntary execution: the “doing” path of AIOS**

Part of the **AIOS** (Biology layer) in the **AIVA** archetype. [← Back to AIOS](../README.md) · [← Back to AIVA](../../README.md)

## Role

The **Somatic Nervous System (SNS)** is the voluntary execution arm of AIOS. Like the body’s somatic system carrying out deliberate actions, the SNS takes the plans and blueprints produced by the COE and turns them into actual execution: molecule → DAG → run. It **coordinates** the “doing” path: intent → COE → blueprint → **AQL** (Chemistry) → **AEF** (Physics). It does not decide *what* to do (that’s the COE) or *how healthy* the system is (that’s the ANS)—it executes.

## Why voluntary execution is separate

We separate **execution** from **intent** and **monitoring** so that (1) the COE doesn’t micromanage every step—it hands off a plan and the SNS runs it; (2) execution can optimize sequencing and resources locally (molecule → DAG → run) without round-tripping to the “brain”; (3) failure in execution doesn’t corrupt the COE—the ANS detects it and feeds back, and the COE can adapt policy. In biology, the somatic system carries out voluntary actions; the spinal cord and cerebellum coordinate motion without the cortex micromanaging every muscle. We do the same: `coordinate_sns()` and `execute_tasks()` run under **resource and latency budgets** (A9); if they overrun, the ANS and A3 fail-close kick in. So the SNS is “voluntary” in the sense that it executes what the COE decided—but it’s still **contract-bound** and **deterministic** (A1), so every run is reproducible and auditable.

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

**From COE:** The SNS receives parsed intent, plans, and blueprints from the COE. It does not second-guess or reinterpret intent; it executes what the COE produced. The handoff is contract-based: the COE’s output conforms to the runtime symbol map, and the SNS consumes it to drive AQL and AEF.

**To AQL:** The SNS sends molecule blueprints to AQL for compilation into DAGs. AQL type-checks, resolves contracts, and verifies invariants; the SNS does not perform structure verification—it coordinates the flow from blueprint to compiled graph.

**To AEF:** Compiled DAGs are sent to AEF for execution as particle instructions. AEF schedules and runs particles, enforces resource budgets (A9), and returns execution state and telemetry. The SNS does not run particles itself; it drives the execution path and collects results.

**To ANS:** Execution state \(E_t\) and telemetry from AEF are fed to the ANS for monitoring and feedback. The ANS uses this to detect anomalies, trigger fail-close (A3) when needed, and generate feedback \(F_t\) for the COE. The SNS is the conduit: execution outcomes flow through it to the ANS so that the autonomic subsystem can watch and modulate without participating in execution.

## Semi-autonomous behavior

The SNS runs in a semi-autonomous way relative to the COE: it receives a plan and carries it out without constantly asking the “brain” for permission at each step. Coordination and resource flow are computed locally where possible; only when thresholds or policies are violated does the ANS/COE intervene (e.g. fail-close, policy tuning). This mirrors the body: voluntary motion is coordinated by the spinal cord and cerebellum without the cortex micromanaging every muscle.
