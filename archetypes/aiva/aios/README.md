# AIOS — Artificial Intelligence Operating System

**Biology layer of AIVA: Central Nervous System (CNS)**

Part of the **AIVA** archetype. [← Back to AIVA](../README.md)

## Role

AIOS is the **Biology layer** of the triadic AIVA system. It implements a **Central Nervous System (CNS)** that works like a living body: a brain (COE), voluntary execution (SNS), and autonomic self-care (ANS), with **RFS (Resonant Field Storage)** as the mathematical memory substrate. AIOS receives natural-language or structured intent, evaluates it using mathematical calculus, coordinates execution through the somatic subsystem, and monitors health through the autonomic subsystem. Memory and context are provided by RFS—the same mathematical memory substrate used in both TAI and AIVA.

## Why a nervous system (and why three subsystems)

We model AIOS as a CNS because **intent, execution, and self-care are different jobs** that need different guarantees. A single “orchestrator” that both decides and runs and monitors would either micromanage (bottleneck, latency) or handwave (no accountability). Biology separates these for good reason: the brain plans and remembers; the somatic system carries out voluntary actions; the autonomic system keeps the organism alive without conscious control. We get the same benefits: **COE** can focus on reward, risk, memory, and policy without being tied to execution latency; **SNS** can optimize sequencing and resource flow locally; **ANS** can monitor and fail-close without waiting for the “brain” to poll. Violations (risk over threshold, entropy overrun) trigger **A3 fail-close** and audit—no silent degradation. All behavior is governed by **lattice cognitive calculus** and **runtime function contracts**, so every emission is canonical and reproducible (A1 determinism, A10 auditability). The result is semi-autonomous cooperation: think, do, and watch are separate, but they share contracts and axioms so the system stays provable and safe.

## The three subsystems (each has its own page)

AIOS is structured as a **nervous system** with three semi-autonomous subsystems. Each has a well-defined mathematical contract and works together without a single central dictator—like a human body.

| Subsystem | Role | Page |
|-----------|------|------|
| **COE** — Cognitive Orchestration Engine | The brain: intent parsing, policy gating, memory (RFS), anomaly detection, DAG tuning. Thinks; does not execute or monitor. | [COE](coe/README.md) |
| **SNS** — Somatic Nervous System | Voluntary execution: molecule → DAG → run. Coordinates the “doing” path (COE → AQL → AEF). Does; does not decide or monitor. | [SNS](sns/README.md) |
| **ANS** — Autonomic Nervous System | Self-care: monitors execution health, anomaly/alerting, policy tuning. Feeds telemetry back into COE. Watches and modulates; does not execute or decide. | [ANS](ans/README.md) |

## How they work together (semi-autonomous, like a body)

- **COE** receives intent and produces plans and blueprints. It uses brain regions (Prefrontal Cortex, Basal Ganglia, Thalamus, Hippocampus, Amygdala, Corpus Callosum, Cerebellum) with mathematical contracts (reward \(R_t\), risk \(\Sigma_t\), entropy \(H(G)\), memory similarity \(M(q,\Phi)\)). It does **not** micromanage execution or monitoring.
- **SNS** takes the plan and runs it: molecule → AQL (compile to DAG) → AEF (execute particles). It coordinates resources and sequencing semi-autonomously; only when thresholds or policies are violated does COE/ANS intervene.
- **ANS** monitors execution state and telemetry, detects anomalies, triggers fail-close (A3) when needed, and feeds feedback into the COE so that policies and gates can adapt. It runs in the background, like heart rate and stress response.

**End-to-end flow**: Intent → **COE** (orchestrate_intent) → blueprint → **SNS** (coordinate_sns) → AQL → AEF → execution state → **ANS** (monitor_ans) → feedback → COE (learning, policy tuning). All steps are governed by lattice cognitive calculus, runtime function contracts, and lattice axioms (e.g. determinism, A3 fail-close).

## COE brain regions (inside the COE)

The COE is composed of region modules; each has a `process()` contract and emits canonical fields. See [COE](coe/README.md) for detail.

- **Prefrontal Cortex** — Intent parsing, constraint prioritization, disambiguation
- **Basal Ganglia** — Policy gating and execution path selection
- **Thalamus** — Inter-module signal routing and relay
- **Hippocampus** — Short- and long-term memory (RFS-backed)
- **Amygdala** — Alert escalation and anomaly detection (A3 fail-close)
- **Corpus Callosum** — Cross-subsystem coordination (autonomic ↔ somatic)
- **Cerebellum** — DAG tuning and execution optimization

## Integration

- **RFS** — Memory substrate for holographic memory (Hippocampus, episodic/system memory)
- **AQL** — Intent parsed by AIOS is compiled to AQL DAGs (via SNS)
- **AEF** — Execution telemetry from AEF feeds back to AIOS (via SNS/ANS) for learning
- **External** — Systems like TAI integrate via CAIO; no direct code dependencies

Working toward measurable integrated information (Φ) as a metric for system-wide awareness.

## Why these contracts and axioms

AIOS (and the whole AIVA stack) is governed by **LATTICE axioms** and **runtime function contracts**. That isn’t bureaucracy—it’s how we get **determinism, safety, and auditability**. Same inputs and config → same outputs (A1). Execution units are stateless; state is explicit (A2). When risk Σ_t or entropy H(G) or latency Λ exceeds thresholds, we halt or fall back—no silent degradation (A3). Only symbol-mapped fields are emitted (A4); risk increases monotonically with anomaly and latency (A6). So: every decision and emission is **reproducible with provenance** (A10). Orchestration latency is bounded (e.g. Λ_total ≤ 50ms in contracts); fail-close is enforced at region boundaries. The “why” is simple: we want a system that can be **proven correct and audited**, not just tested. The nervous-system split (COE / SNS / ANS) plus these contracts is what makes that possible.
