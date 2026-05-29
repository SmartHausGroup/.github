# TAI — The PALI Product

**Tutelarius Auxilium Intellectus · Voice-first personal AI with mathematical guarantees · Cross-device by construction**

---

## What TAI is

TAI is the SMARTHAUS product that delivers the [PALI](../README.md) category: a portable, voice-first personal AI that travels with the user across every device they own. Same identity. Same memory. Same governance. On phone, on laptop, on tablet, in the web, via voice or text — wherever the user happens to be.

The substrate underneath TAI is the SMARTHAUS Component stack: [UCP](../../Components/UCP/README.md) for runtime governance, [SAID](../../Components/SAID/README.md) for deterministic inference, [MAE](../../Components/MAE/README.md) for proven embedded properties, [MAIA](../../Components/MAIA/README.md) for intent classification, [CAIO](../../Components/CAIO/README.md) for service orchestration, [VEE](../../Components/VEE/README.md) for math primitives, [RFS](../../Substrate/RFS/README.md) for memory, [NME](../../Substrate/NME/README.md) for meaning extraction. The user does not see these Components. The user sees TAI.

TAI is what happens when the SMARTHAUS architecture is shaped into a consumer-facing surface and made portable across every platform.

## What TAI does today

TAI is in **active development with platform foundations already shipping**:

- **`tai-engine`** — Rust workspace, three crates (daemon, IPC, voice). Built daemon binary on macOS arm64. Process-isolated runtime with cryptographically-signed engine identity. Phase 5 (runtime integration execution) closed. Last commit May 2026.
- **`tai-sdk`** — Python SDK published to PyPI (`tai-sdk`). Voice-first API with async/await support. Type-safe. Service discovery for CAIO/VFE auto-detection. Used by integrators building applications on TAI's surface.
- **`tai`** — The legacy Python orchestration layer (precedes the Rust daemon; superseded for runtime work; documentation reference for the historical orchestration model).

The TAI Y1 H2 pilot milestone integrates the Rust runtime daemon with CAIO orchestration to deliver the first end-to-end PALI experience: voice-in on one device, memory + context resolution via RFS, mathematically-governed action via UCP, deterministic inference via SAID, response surfaced wherever the user is at the moment.

## Core capabilities

- **Voice-first interface.** Speech-to-text and text-to-speech as primary inputs, with text-based interaction as the secondary modality. On-device transcription preferred for privacy; cloud fallback for languages and accents the on-device model doesn't cover.
- **Cross-device memory.** Conversations, documents, preferences, and context persist in the user's RFS-backed memory substrate. The substrate is the user's — taking it from one device to another requires no migration.
- **Document upload and query.** Store documents in TAI's memory and retrieve context-relevant content during interaction. Documents flow into the same RFS substrate as conversations.
- **Model routing.** JSON-configured model selection with per-conversation choice. The application logic (in TAI) is decoupled from the inference engine (SAID); switching backends is configuration, not code.
- **Session persistence.** Conversations persist across application restarts, device switches, and time gaps. Coming back to TAI on a different device picks up where the last interaction left off.
- **Standalone deployment.** Runs as a desktop application (currently macOS arm64; Windows packaging in build) with an accompanying API for integration into other surfaces.
- **Mathematical guarantees.** Every action TAI takes flows through UCP admission and produces a signed record. Every inference TAI runs flows through SAID and produces a deterministic envelope. Every proven property TAI enforces was built through MAE.

## What TAI is not

- **Not a chatbot.** Chatbots respond to inputs; TAI is a persistent personal AI that maintains state, runs in the background, and has long-term memory and goals.
- **Not platform-locked.** TAI does not depend on Apple, Google, Microsoft, or any platform owner's infrastructure to function on their devices. The architecture is cross-platform by construction.
- **Not a wrapper around a single model.** TAI is the user-facing surface over a substrate of Components and a Substrate. The substrate determines TAI's properties; the underlying model (Claude, GPT, Llama, in-house) is a backend choice routed through SAID.
- **Not consumer-only.** The same TAI runtime can deploy into enterprise contexts (where it composes with the customer's deployment of UCP, SAID, MAE), into research contexts (where it composes with the Princeton-style use of RFS as a research substrate), and into the consumer PALI context (where it is the default).

## Use cases

TAI applies wherever a user wants a personal AI that follows them across devices, that they actually own, that has mathematical accountability for what it does on their behalf. Four canonical deployments documented in depth:

1. **[Cross-Device Personal AI for Knowledge Workers](./use-cases/01_cross_device_knowledge_worker/README.md)** — The consultant whose phone, laptop, and tablet each have their own context but who needs one continuous thread. TAI is the thread.
2. **[Voice-First AI in Hands-Busy Workflows](./use-cases/02_voice_first_hands_busy/README.md)** — Clinicians in surgery, field service technicians, drivers, accessibility users. Voice as primary input, hands and eyes occupied elsewhere.
3. **[Personal AI With Provable Privacy](./use-cases/03_provable_privacy/README.md)** — Sensitive personal and professional contexts (mental health, legal counsel, financial advisors) where the user needs proof of what the AI did and did not do with their information.
4. **[Family and Household AI With Permission Boundaries](./use-cases/04_family_household_permissions/README.md)** — Multi-user households where different family members have different access scopes, parental controls are mathematically enforced, and shared family context coexists with private individual contexts.

**[See all TAI use cases →](./use-cases/README.md)**

## What ships when

- **Today:** Platform foundations shipping in `tai-engine` and `tai-sdk`. Process-isolated Rust daemon. Voice subsystem. IPC transport. macOS arm64 packaging. Phase 5 runtime integration execution closed.
- **Y1 H2:** First end-to-end TAI pilot — cross-device personal AI experience delivered on macOS, iOS, Windows, and Android, with CAIO orchestration over the full SMARTHAUS Component stack.
- **Y2:** Substrate productization (RFS + NME standalone) expands TAI's memory surface; new Components (MGE, expanded MAIA) deepen the in-application governance and intent classification.
- **Y3+:** Marketplace ecosystem ramps. Third-party publishers (privacy lawyers, financial advisors, healthcare advocates, family-safety nonprofits) build packs that drop into TAI through the validated extension surface.

## How to engage

- **Early access list** for the Y1 H2 pilot is open. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with the device footprint you'd want to test TAI across.
- **Enterprise deployment** that composes TAI with customer-deployed UCP / SAID / MAE — engage through the Components pilot programs.
- **Integration partners** building applications on the `tai-sdk` — see the SDK documentation at the published PyPI package.

---

**[PALI category overview](../README.md)** · **[See all TAI use cases](./use-cases/README.md)** · **[Components](../../Components/README.md)** · **[Substrate](../../Substrate/README.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
