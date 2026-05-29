# SAID Use Cases — Where Deterministic Inference Lives

**Status:** Public Documentation
**Last Updated:** 2026-05

## Overview

This directory contains four in-depth use cases for **SAID — Deterministic Inference**. Each use case is a white paper covering the operational problem, why existing market solutions fall short, how SAID closes the gap by construction, and the measurable outcomes for the organization adopting it.

SAID applies wherever model inference outputs feed regulated, high-stakes, or auditable decisions — credit, insurance, healthcare, fraud, AML. In every one of these domains, the question *"why did the model produce this output?"* is the question that determines whether the system survives a regulator, an examiner, or a court.

## Use Cases

### 1. Credit Decisioning Under Fair Lending
**Directory:** `01_credit_decisioning_fair_lending/`
**Problem:** Banks and fintechs running AI-assisted credit decisioning cannot reliably reproduce the model output for a specific applicant on a specific day, because inference is non-deterministic by default. The Equal Credit Opportunity Act, FCRA, and SR 26-2 all require reproducible decisions and verifiable adverse-action notices. Without determinism, the lender is one regulator inquiry from a finding.
**SAID Solution:** Deterministic inference binds the same applicant profile + same model version to the same score and the same adverse-action language. Every decision ships with a signed envelope. The auditor replays the decision on their own laptop.
**Key Value:** Fair-lending risk drops because identical applicants get identical treatment. Examination cycles shorten because evidence is queryable. The class-action risk of "the model said different things to different protected-class applicants on different days" disappears structurally.

### 2. Insurance Underwriting and Pricing
**Directory:** `02_insurance_underwriting_pricing/`
**Problem:** Insurance carriers using AI in underwriting and rating face a structural mismatch with state insurance regulation, which requires that filed rates be deterministic, explainable, and reproducible. Non-deterministic inference cannot satisfy filed-rate compliance. Carriers either avoid AI in regulated rating (and lose the underwriting edge) or deploy it and absorb the regulatory exposure.
**SAID Solution:** Deterministic inference makes AI-derived risk factors filable as part of the rate filing. Same risk profile → same factor → same premium. Every underwriting decision and every rate calculation ships with a replayable envelope.
**Key Value:** Carriers can deploy AI in rated lines of business — auto, home, life, commercial — with the same architectural rigor as filed deterministic formulas. NAIC AI principles compliance becomes a query, not a forensic project.

### 3. Clinical Decision Support and Coverage Determinations
**Directory:** `03_clinical_decision_support/`
**Problem:** Health insurance carriers and clinical decision-support vendors face the post-nH-Predict environment, where courts are ordering disclosure of AI coverage-denial algorithms and plaintiffs are alleging systemic high-reversal-rate denial patterns. Without deterministic inference, the carrier cannot prove that the same patient profile would have received the same recommendation on a different day.
**SAID Solution:** Deterministic inference binds the same patient + clinical context + model version to the same support recommendation. Every coverage determination ships with a signed envelope. The plaintiff's expert re-verifies the determination on open-source toolchain.
**Key Value:** The nH Predict-class litigation exposure becomes architecturally bounded. The carrier or vendor produces verifiable evidence rather than testimonial defenses. FDA AI/ML guidance compliance is built in.

### 4. Fraud, Sanctions, and AML Adjudication
**Directory:** `04_fraud_sanctions_aml/`
**Problem:** Banks running AI-driven transaction monitoring, sanctions screening, and AML adjudication face bank-grade model-risk regimes (SR 26-2 + revised SR 11-7 replacement). Examiners increasingly demand evidence that the model's decision on a specific transaction on a specific day was reproducible and consistent with the model's documented behavior. Most production transaction-monitoring systems cannot answer this.
**SAID Solution:** Deterministic inference binds the same transaction features + model version to the same risk verdict and disposition path. Every adjudication ships with a replayable envelope. The bank's compliance team queries the envelope vault for examination evidence.
**Key Value:** Model risk management capabilities expand because the model becomes auditable. False-positive disposition becomes consistent across customers and time. SR 26-2 model lineage and decision provenance requirements are satisfied by architecture.

## Quick Comparison

| Use Case | Primary SAID Feature | Key Differentiator | Enterprise Value |
|---|---|---|---|
| Credit Decisioning | Per-applicant deterministic envelopes | Replayable adverse-action notices | Fair-lending risk reduction, class-action exposure structurally bounded |
| Insurance Underwriting | Deterministic risk factors | Filed-rate compatible AI | AI-derived factors deployable in rated lines |
| Clinical Decision Support | Patient + context envelope replay | nH Predict-class evidence | Court-defensible coverage decisions |
| Fraud / Sanctions / AML | Per-transaction signed envelopes | Examiner-replayable risk verdicts | SR 26-2 compliance by architecture |

## Common SAID Capabilities Used

Every SAID use case shares the same underlying capabilities:

- **Deterministic inference at the model layer** — same inputs + same fixed context → same outputs, every time.
- **Cryptographically signed per-decision envelopes** — every output carries the model version, the input hash, the seed pin, and a signature anyone can verify.
- **Byte-identical replay** — the regulator or auditor can re-derive any historical decision on their own hardware using open-source tooling.
- **OpenAI-compatible API surface** — existing application code does not need to be rewritten; SAID drops in behind the API the application already speaks.
- **Backend interchangeability** — Llama, Claude, GPT, Gemini, Mistral, local MLX or llama.cpp models — all behind the same SAID contract.
- **Mathematical Autopsy build discipline** — every SAID release ships under the same proof-closed pipeline as the rest of the SMARTHAUS substrate.

## How to Engage

SAID is pilot-ready and currently deployed in design-partner engagements at banks, insurance carriers, and healthcare organizations. Pilots run 60–90 days with three engagement tiers based on model and region scope. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with the use case that best matches your deployment context.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
