# SAID — Deterministic Inference

**Current release: [SAID Runtime v0.2.5](https://github.com/SmartHausGroup/said-core/releases/tag/said-runtime-v0.2.5) · Signed for distribution · Pilot-ready**

---

## What it is

SAID is a GPU-first model inference engine that makes frontier models **interchangeable** underneath your application logic — and **deterministic** when you need them to be.

Most inference stacks treat the model as the application: a Llama prompt is different from a Claude prompt is different from a GPT prompt, and switching providers means rewriting half the system. SAID flips that. Application logic talks to SAID's contract; SAID talks to whichever backend is appropriate. Backends today include MLX, llama.cpp, transformers, HuggingFace, plus API providers (Anthropic, OpenAI, Cohere, Mistral, Groq) and our own `verbum_gpu` runtime.

Determinism is enforced where it matters: same inputs, same fixed context, same outputs. Every time. Every model. The same conversation can be replayed three months later in a courtroom and produce the same words.

## The failures it closes

SAID is the answer to one of the [Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md) outright and contributes to a second:

- **REPLAY** — Reproducibility is the bedrock of every regulated engineering discipline, and most AI deployments don't have it.
- **LEAD** — SAID's deterministic-inference output is the model-lineage artifact regulators now require under SR 26-2.

## Who buys it

- **CTO or VP Engineering** with significant model spend or production-determinism requirements.
- **Budget origin:** infrastructure, not "AI R&D."
- **Typical trigger:** model-vendor lock-in is now a procurement risk, or a compliance team is asking questions about reproducibility nobody can currently answer.

## Use cases

SAID applies wherever inference outputs feed regulated, high-stakes, or auditable decisions. Four canonical deployments documented in depth:

1. **[Credit Decisioning Under Fair Lending](./use-cases/01_credit_decisioning_fair_lending/README.md)** — ECOA, FCRA, SR 26-2. Same applicant profile → same score → same adverse-action notice. Auditor replays any historical denial on their own laptop.
2. **[Insurance Underwriting and Pricing](./use-cases/02_insurance_underwriting_pricing/README.md)** — NAIC AI principles + state rate-filing requirements. Same risk profile → same premium decision, every time, replayable on demand.
3. **[Clinical Decision Support and Coverage Determinations](./use-cases/03_clinical_decision_support/README.md)** — FDA AI/ML guidance + the nH Predict precedent. Same patient profile → same recommendation, with per-decision signed envelopes.
4. **[Fraud, Sanctions, and AML Adjudication](./use-cases/04_fraud_sanctions_aml/README.md)** — Bank-grade model risk regime. Same transaction → same risk verdict → same disposition. Reproducible under examiner replay.

**[See all SAID use cases →](./use-cases/README.md)**

## What ships today

- SAID Runtime v0.2.5 — macOS arm64, signed under release key `runtime-release-2026q2`.
- Built distributions: `.dmg`, tarball, Python wheel.
- 10 Rust crates spanning CLI, inference, server, parity verification, and Python bridge.
- Multi-backend routing across MLX, llama.cpp, transformers, HuggingFace, Anthropic, OpenAI, Cohere, Mistral, Groq, and a native GPU runtime.
- Certified through the readiness harness (`said-sdk certify-runtime`).
- Public-attestation verified. SDK published at `said-sdk 0.2.0`.

## How to engage

Pilot deployments are open to a small cohort. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with your inference-volume context and determinism requirements.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
