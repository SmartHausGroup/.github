# ANS — Autonomic Nervous System

**Self-care: monitoring, feedback, and fail-close**

Part of the **AIOS** (Biology layer) in the **AIVA** archetype. [← Back to AIOS](../README.md) · [← Back to AIVA](../../README.md)

## Role

The **Autonomic Nervous System (ANS)** is the self-care and monitoring arm of AIOS. Like the body’s autonomic system (heart rate, respiration, stress response), the ANS operates largely in the background: it monitors execution health, detects anomalies, triggers alerts, and feeds telemetry back into the COE for learning and policy tuning. It does **not** execute tasks (that’s the SNS) or decide intent (that’s the COE)—it **watches** and **modulates**: fail-close when thresholds are exceeded, tune policies based on reward and anomaly.

## Why autonomic (and why fail-close is non-negotiable)

We separate **monitoring and self-care** from intent and execution so that (1) the system doesn’t rely on the COE to “poll” for health—the ANS runs continuously and feeds back; (2) **fail-close is enforceable** at the ANS/COE boundary: when risk \(\Sigma_t\) or entropy \(H(G)\) or latency \(\Lambda\) exceeds thresholds (A3), execution halts or routes to a safe fallback—no silent degradation; (3) the COE **learns** from feedback (policy tuning, Basal Ganglia gates, Amygdala sensitivity) so the next intent can be gated or routed differently. In biology, the autonomic system regulates heart rate, respiration, and stress without conscious control; the brain receives the signals and can change behavior over time. We do the same: `monitor_ans()` and `generate_feedback()` produce **canonical feedback** \(F_t\); that feedback is consumed by the COE for learning and by policies for fail-close. So the ANS isn’t “optional”—it’s how we **guarantee** that the system stays within bounds and that violations are auditable (A10) and mitigated (A3).

## Key functions

- **`monitor_ans(E_t)`** — Monitors system performance and generates feedback. Takes execution state \(E_t\); returns feedback \(F_t = f_{\text{feedback}}(A_t, M_t, R_t)\) with canonical fields.
- **Health and anomaly** — Tracks execution health, latency, error rates, anomaly scores. Bounds and thresholds are mathematically defined (e.g. risk \(\Sigma_t\), A3 fail-close).
- **`generate_feedback(anomaly_score, monitoring_state, reward_signal)`** — Generates feedback vector for system modulation; used by COE for learning and policy updates.
- **Policy tuning** — Feeds telemetry and feedback into the COE so that Basal Ganglia and other regions can adapt policies (e.g. when to gate, when to fall back).

## Mathematical contracts

- Feedback \(F_t\) and monitoring outputs conform to the **runtime symbol map** and **runtime function contracts**.
- **A3 fail-close**: if risk or anomaly thresholds are exceeded, execution halts or routes to a safe fallback (legally enforced per lattice axioms).
- Anomaly score \(\in [0,1]\); reward signal finite; monitoring state valid.

## Integration

**From SNS:** The ANS receives execution state \(E_t\) and telemetry from the execution path (AQL and AEF). The SNS is the conduit: it does not interpret or filter telemetry beyond what is needed to pass it through. The ANS consumes this to compute anomaly scores, reward signals, and monitoring state, and to decide when to trigger fail-close (A3) or policy updates.

**To COE:** The ANS feeds feedback \(F_t\) and telemetry into the COE so that each region can adapt. The Amygdala receives alerts and risk; the Hippocampus receives signals for memory updates; the Basal Ganglia receives input for policy tuning; the Corpus Callosum supports cross-subsystem coordination. The COE does not poll the ANS—the ANS pushes feedback when thresholds or events require it, so that learning and fail-close are timely.

**RFS:** Monitoring and feedback can influence what is stored or recalled. Anomaly-triggered memory encoding, reward-weighted consolidation, and policy-driven recall are all possible when the ANS and COE use RFS as the memory substrate—so that the system’s “memory” reflects not only what happened but how healthy and how significant it was.

## Semi-autonomous behavior

The ANS runs semi-autonomously: it continuously monitors and can trigger fail-close or modulation without waiting for the COE to “decide” every time. Thresholds and axioms (e.g. A3) are enforced at the ANS/COE boundary. The COE then uses the feedback to adapt—so the next intent might be gated or routed differently. This mirrors the body: the autonomic system regulates vital functions and stress responses without conscious control, while the brain receives the signals and can alter behavior over time.
