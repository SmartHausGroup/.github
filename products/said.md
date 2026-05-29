# SAID — Deterministic Inference

**Current release: [SAID Runtime v0.2.5](https://github.com/SmartHausGroup/said-core/releases/tag/said-runtime-v0.2.5) · Signed for distribution · Pilot-ready**

---

## What it is

SAID is a GPU-first model inference engine that makes frontier models **interchangeable** underneath your application logic — and **deterministic** when you need them to be.

Most inference stacks treat the model as the application: a Llama prompt is different from a Claude prompt is different from a GPT prompt, and switching providers means rewriting half the system. SAID flips that. Application logic talks to SAID's contract; SAID talks to whichever backend is appropriate. Backends today include MLX, llama.cpp, transformers, HuggingFace, plus API providers (Anthropic, OpenAI, Cohere, Mistral, Groq) and our own `verbum_gpu` runtime.

Determinism is enforced where it matters: same inputs, same fixed context, same outputs. Every time. Every model. The same conversation can be replayed three months later in a courtroom and produce the same words.

## The failures it closes

SAID is the answer to one of the [Six Failures](../six-failures/) outright and contributes to a second:

- **REPLAY** — Reproducibility is the bedrock of every regulated engineering discipline, and most AI deployments don't have it. Cursor's April 2025 incident — bot invents nonexistent company policy, subscriptions canceled, trust collapses — happened because the vendor couldn't replay the conversation to find the failure point. SAID makes that replay structurally available.
- **LEAD** — SAID's deterministic-inference output is the model-lineage artifact regulators now require under SR 26-2.

## Who buys it

- **CTO or VP Engineering** with significant model spend or production-determinism requirements.
- **Budget origin:** infrastructure, not "AI R&D."
- **Typical trigger:** model-vendor lock-in is now a procurement risk, or a compliance team is asking questions about reproducibility nobody can currently answer.

## What ships today

- SAID Runtime v0.2.5 — macOS arm64, signed under release key `runtime-release-2026q2`.
- Built distributions: `.dmg`, tarball, Python wheel.
- 10 Rust crates spanning CLI, inference, server, parity verification, and Python bridge.
- Multi-backend routing across MLX, llama.cpp, transformers, HuggingFace, Anthropic, OpenAI, Cohere, Mistral, Groq, and a native GPU runtime.
- Certified through the readiness harness (`said-sdk certify-runtime`).
- Public-attestation verified.
- SDK published at `said-sdk 0.2.0`.

## How to engage

Pilot deployments are open to a small cohort. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with your inference-volume context and determinism requirements.

---

**[← Back to SMARTHAUS](https://github.com/SmartHausGroup)** · **[The Six Failures](../six-failures/)** · **[← UCP](./ucp.md)** · **[MAE →](./mae.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
