---
title: System Map
sidebar_position: 1
---

# System Map

The single diagram of what exists and who talks to whom in SMARTHAUS.

Nine systems. One shared field. Every system is either the memory substrate (RFS), something that routes or orchestrates using that substrate (MAIA, CAIO, TAI, VEE), something that feeds or uses it (NME, VFE), or governance (MGE).

---

## System Decomposition

| System | Repositories | Role |
|--------|-------------|------|
| **RFS** | rfs-core, ResonantFieldStorage, rfs-sdk | Memory substrate: 4-D resonant field; exact recall + associative resonance + proactive discovery. |
| **MAIA** | MAIA | Intent engine: semantic intent resolution, routing to VFE/RFS/marketplace via master equation. |
| **CAIO** | caio-core, caio, caio-sdk | Universal AI orchestration; deterministic policy; contract-gated execution. |
| **TAI** | tai-core, tai, tai-sdk | Product: voice-first personal assistant; integrates CAIO, VFE, RFS, NME, MAIA, VEE. |
| **AIVA** | Archetype specification | Enterprise assistant archetype; triadic AIOS/AQL/AEF architecture; RFS as memory substrate. |
| **VFE** | vfe-core, VerbumFieldEngine, vfe-sdk | Inference: model API gateway; OpenAI-compatible; model selection calculus $S_{total}$. |
| **NME** | NotaMemoriaEngine | Memory structuring: trait extraction; encoding into RFS via $E(\text{Extract}(\Psi_t))$. |
| **VEE** | VoluntasEngine | Intent classification: native C++/pybind11; RL-based intent parsing. |
| **MGE** | mge-core, MathematicalGuaranteeEngine, mge-sdk | Mathematical Governance Engine: rules-as-code; compliance API; MA enforcement sidecar. |

---

## Cross-System Coupling

How state flows between systems:

| Producer | Consumes | Emits | Signal Form |
|----------|----------|-------|-------------|
| **RFS** | Bytes, embeddings (ingest); query vectors (associate) | Field state $\Psi$; matched-filter response $r = E^H \Psi$; recall bytes; quality metrics $Q$, $\eta$, capacity | Field state; vectors; metrics |
| **MAIA** | Query $q$, context $C$, market $M$; RFS resonance $W$ | Route decision (VFE / RFS / marketplace) | Discrete choice + scores |
| **NME** | Raw user input | Trait structures; encoded waves for RFS | Structured records; $E(\text{Extract}(\Psi_t))$ |
| **VFE** | Request, model selection weights | $S_{total}$; token stream | Scalar score; tokens |
| **CAIO** | Request, policy | Adapter choice; response | Contract-satisfying I/O |
| **VEE** | Context (e.g. from RFS) | Intent classification (RL policy) | Label or distribution |
| **MGE** | Rules (.mdc, .yaml), request/action | `/check` result | Pass/fail + reasons |
| **TAI** | User input; responses from CAIO, VFE, RFS, NME, MAIA, VEE | Requests to subsystems; final user response | Requests/responses; voice; embeddings |

### RFS as the Memory Substrate

RFS is the connective tissue. MAIA needs RFS to compute resonance $W(q, C)$ for routing decisions. NME writes trait waves into RFS. TAI uses RFS for both associative and exact recall. VFE may use RFS for context retrieval. CAIO may read RFS metrics for policy decisions.

If RFS were removed, MAIA's resonance term $W$ would be undefined, NME would have nowhere to store trait waves, and TAI would lose its memory. The field is not optional infrastructure — it is the integration substrate.

### MAIA as the Router

TAI and other consumers send query + context to MAIA. MAIA's master equation combines intent $I$, alignment $A$, reinforcement learning $RL$, and RFS resonance $W$ to produce a route decision. Replacing this with "call an LLM to decide" removes the same-input-same-route guarantee.

### CAIO as the Orchestrator

Requests pass through CAIO for policy enforcement. Contract pass/fail is deterministic — same request and policy always produce the same enforcement decision. CAIO ensures that governance is executable, not advisory.

---

## Determinism Boundaries

Not everything in the system is deterministic. The architecture explicitly separates where determinism is enforced from where probabilistic behavior is permitted.

### Enforced Determinism (same inputs → same outputs)

- **RFS** encode/recall (seeded $E$, $\Pi_{assoc}$)
- **RFS** byte channel (AEAD encryption)
- **MGE** rule evaluation
- **CAIO** policy application
- **VFE** model selection calculus (same request + weights → same $S_{total}$ and model choice)

### Permitted Stochasticity

- **MAIA** RL component (learning evolves policy)
- **VEE** RL policy learning
- **LLM inference** via VFE (token sampling)
- **NME** trait extraction (if model-based)
- **TAI** inference responses (downstream of LLM sampling)

The design principle: learned or stochastic components operate *on top of* or *beside* deterministic ones. MAIA's route uses deterministic $I$, $A$, $W$ terms and a stochastic $RL$ term. VFE's model selection is deterministic; the inference through the selected model is stochastic. Invariants and gates apply to the deterministic surfaces. Probabilistic components are bounded, not eliminated.

---

## Why Not LangChain + a Vector Database?

This is a fair question. The answer is structural, not preferential:

- **Single field, multiple channels.** RFS provides exact recall, vector similarity, interference-aware (corpus-aware) search, and proactive discovery from one state $\Psi$. A vector database stores isolated points. It has no superposition, no $Q$/$\eta$ guardrails, no band separation between exact and associative channels.

- **Equations govern behavior.** Invariants and lemmas pin capacity, recall error, stability, and resonance to formal bounds. CI pipelines enforce them on every change. LangChain + vector DB do not ship formal operator calculus with CI-bound verification artifacts.

- **Intent and routing are math.** MAIA's $\text{Route}(\cdot)$ is a defined function of $I$, $A$, $RL$, $W$, where $W$ couples directly to the RFS field. Replacing this with "call an LLM to decide the route" removes same-input-same-route guarantees.

- **Memory is structured and trait-aware.** NME encodes traits as field contributions $E(\text{Extract}(\Psi_t))$ into the same RFS field. A vector database stores vectors and optionally blobs — no 4-D resonant field with band separation and interference-aware scoring.

- **Proactive discovery before any query.** RFS can reveal clusters, anomalies, and field topology without a user query. Vector databases are query-reactive only.

- **Determinism with rollback.** MA defines rollback criteria per invariant. Scorecard gates block release when guarantees fail. There is no equivalent in a generic orchestration + retrieval stack.
