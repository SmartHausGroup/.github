# MAIA — Intent Engine

**Latin: Mens Animus Intentio Anima · Status: Active development · Y1 H2 pilot target**

---

## What MAIA is

MAIA is the **intent engine** of the SMARTHAUS substrate. It figures out what the user actually wants — converting raw input (voice, text, gestures, structured signals) into intent records that the rest of the substrate can act on.

Intent classification is not a new problem. Conversational AI has been classifying intent for a decade through trained classifiers over fixed taxonomies. MAIA's contribution is what it produces: **intent records with confidence bounds, classification provenance, and refinement history** — structured artifacts that downstream Components (UCP, SAID, CAIO) can evaluate against policy and act on with cryptographic accountability.

## What MAIA does

- **Multi-modal intent extraction.** Voice, text, structured inputs (calendar events, document signals, agent triggers) all flow into the same intent-classification pipeline.
- **Confidence-bounded outputs.** Every intent classification ships with explicit confidence bounds. Low-confidence classifications are flagged for clarification rather than acted on with false certainty.
- **Refinement through reinforcement learning.** When user feedback (correction, confirmation, override) is available, the intent engine refines its model. The refinement is bounded by the substrate's invariants — improvements that violate the contract are rejected.
- **Provenance-preserving classification.** Every intent record carries the chain of reasoning that produced it. Downstream components have explanatory access to *why* the intent was classified the way it was.

## How MAIA fits with the other Components

MAIA is the intent layer that other Components consume:

- **[UCP](../UCP/README.md)** receives intent records and evaluates them against policy before admitting actions. "User wants to draft an email" is admissible; "User wants to drain the bank account" hits a denial.
- **[CAIO](../CAIO/README.md)** orchestrates Component invocation based on the intent classification. Intent → routing decision → Component dispatch.
- **[SAID](../SAID/README.md)** receives intent records as part of its inference context, ensuring inference is consistent with what the user actually asked for.
- **[TAI](../../PALI/TAI/README.md)** is the user-facing surface that MAIA's intent classifications drive. The user's voice or text → MAIA classification → orchestrated Component response.

## Status

MAIA is in **active development**. The intent-classification core is built; the reinforcement-learning refinement layer is in research; the productization for TAI integration is on the Y1 H2 timeline.

Repos: `maia-core`, `maia-sdk`.

---

**[Other Components](../README.md)** · **[Substrate](../../Substrate/README.md)** · **[PALI](../../PALI/README.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
