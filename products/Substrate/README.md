# SMARTHAUS Substrate

**The mathematical foundation underneath the [Components](../Components/README.md) and the [PALI](../PALI/README.md) experience.**

---

## What the Substrate is

The Substrate is the shared mathematical layer that the SMARTHAUS Components read and write into. APIs connect *behavior*; substrates integrate *state*. In a chained AI architecture, behavior fires step-by-step and small errors compound until the system drifts out of sync. In a substrate-integrated architecture, every Component writes into the same field and is bounded by the same mathematical rules. The math holds the system together.

Two Substrate primitives form the foundation. Neither is sold standalone — both ship as the shared layer underneath the Components.

## The primitives

### [RFS — Resonant Field Storage](./RFS/README.md)

Field-theoretic memory. Information is stored as wave patterns in a 4D Fourier field; retrieval works through matched-filter probing rather than brute-force vector cosine.

**What this enables:**
- **Unified storage and exact recall.** A single field substrate provides similarity retrieval, interference-based pattern completion, AEAD-authenticated exact recall, and proactive discovery — all from the same underlying state.
- **Built-in explainability.** Every retrieval produces per-query metrics (resonance quality Q in decibels, interference η as a ratio) that explain why the retrieval matched and with what confidence.
- **Constant-time retrieval.** Query cost depends on the field dimension, not on the number of stored documents. Whether the field contains 1,000 or 1,000,000 patterns, retrieval cost is the same.
- **Falsifiable by construction.** Every theoretical guarantee maps to a measurable invariant validated continuously in CI.

Eight current deployments documented as use cases: [incident memory for on-call teams](./RFS/use-cases/01_incident_memory_oncall/README.md) · [RAG with proofs](./RFS/use-cases/02_rag_with_proofs/README.md) · [code intelligence](./RFS/use-cases/03_code_intelligence/README.md) · [compliance and legal archive](./RFS/use-cases/04_compliance_legal_archive/README.md) · [research knowledge graphs](./RFS/use-cases/05_research_knowledge_graph/README.md) · [pharmaceutical discovery](./RFS/use-cases/06_pharmaceutical_discovery/README.md).

**[Read the RFS overview →](./RFS/README.md)**

### [NME — Nota Memoria Engine](./NME/README.md)

The encoder layer that extracts structured meaning from text and projects it into the RFS field. Where RFS is the storage substrate, NME is the meaning-extraction layer that turns input content into the structured complex-valued waveforms that RFS stores.

NME decomposes text into the 10 components of meaning the SMARTHAUS thesis identifies (structure, content, modality, affect, relationships, reference, intent, context, world knowledge, ambiguity resolution) and produces FHRR-encoded waveforms suitable for RFS storage.

**[Read the NME overview →](./NME/README.md)**

## How the Substrate connects

RFS provides the storage; NME provides the meaning extraction. Together they form the integration layer the SMARTHAUS Components depend on:

- **[UCP](../Components/UCP/README.md)** writes signed admission records into the Substrate and reads them back for audit verification.
- **[SAID](../Components/SAID/README.md)** writes per-decision envelopes into the Substrate alongside the inferences they describe.
- **[MAE](../Components/MAE/README.md)** writes proof artifacts and verifies their relationships to the Substrate-stored code they prove.
- **[MAIA](../Components/MAIA/README.md)** writes intent classifications into the Substrate's associative channel.
- **[CAIO](../Components/CAIO/README.md)** orchestrates Component access to the Substrate through formal contracts.
- **[VEE](../Components/VEE/README.md)** provides math primitives (Lyapunov stability, differential privacy, quantum-inspired compute) that Substrate operators rely on.

The result: a SMARTHAUS deployment is not a collection of independent products. It is a Substrate-integrated set of Components whose state, decisions, and proofs all live in the same shared mathematical layer — and whose composition is governed by the wave physics and information-theoretic invariants the [Mathematical Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md) develops.

## Ship status

- **RFS** ships as research substrate today (in continuous use by SAID's runtime and inside the Princeton research collaboration). Standalone Substrate productization Y2 H2.
- **NME** ships as the early-active encoder for RFS. Productization on the same Y2 H2 timeline as the RFS standalone offering.

## How to engage on the Substrate

Substrate engagement runs through research collaborations and through deployment of Substrate-consuming Components (UCP, SAID, MAE). For direct Substrate access — joint research, academic collaboration, custom encoder development — reach out via **[smarthaus.ai](https://smarthaus.ai)** and see the [Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md) page for the model collaboration shape.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
