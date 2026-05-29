# Use Case 1: Cross-Device Personal AI for Knowledge Workers

**One identity, one memory, every device — the continuous-thread experience consultants, analysts, and executives don't get from platform-owned AI.**

## The Real Problem: Four Devices, Four Strangers

It's 7:14 AM. The management consultant pulls up her phone on the train, opens her AI assistant, and asks a follow-up question about a client analysis she was working on yesterday afternoon. The phone's AI has no idea what analysis she's referring to. She types it out again. The model generates a response. She makes mental notes.

8:42 AM. She arrives at the client site, opens her MacBook in the conference room, and tries to continue. Her MacBook's AI is a different account, a different vendor, a different context. The morning's iPhone conversation is unreachable. She types the analysis context again. The model generates a different response — different framing, different examples, different recommendations. She is now reconciling two AI conversations about the same client, neither of which knows the other exists.

11:30 AM. She's in a working session with the client team. She wants to pull up a note she made yesterday about the engagement scope. The note is somewhere — Notes app on her phone? Document on her MacBook? A message in the team chat? She spends three minutes finding it.

2:15 PM. She's on a video call with her partner back at the firm. He references a client document she has open on her iPad in the next room. She has to walk over, pick it up, and bring it to the call. Her AI assistants have no concept of which device is "current" or what's loaded on each one.

5:00 PM. End of day. She has had four different AI-assisted conversations about the same engagement. None of them are connected. Tomorrow she will start over on whichever device she picks up first.

**The current reality:** This is the standard knowledge-worker experience with platform-owned AI in 2026. Apple Intelligence does not see her work MacBook context. Microsoft Copilot does not see her iPhone context. Google Gemini does not see her iPad context. Each platform's AI assumes the user lives on that platform. The consultant lives on four platforms across the day.

**The hidden cost:** Knowledge work is fundamentally context-dependent. The value the AI assistant can provide scales with how much of the relevant context it has. Fragmenting context across device-locked AIs caps the assistant's value at "what each device's AI happens to know about that moment." Most of the consultant's cognitive load through the day is re-establishing context the AI should have carried for her.

## Why Traditional Systems Fail

### Platform AI Is Walled-Garden AI

Apple Intelligence runs on Apple silicon. It does not exist on the user's Android phone, Windows laptop, Chromebook, or Linux workstation. Gemini favors Pixel and Workspace; Copilot favors Windows and Microsoft 365. Each platform owner's AI assumes the user is single-platform — an assumption that breaks within an hour of observing a real knowledge worker's day.

The walls are not accidental. They are the business model. Each platform owner is competing for the user's primary device commitment; cross-platform AI would undermine that competition. The user's reality (multi-platform, multi-device, all-day-context) does not align with what the platforms can deliver.

### Cloud Chatbots Have No Cross-Device Memory

ChatGPT, Claude.ai, Gemini app — the major cloud chatbots — are device-agnostic in the sense that the user can open them on any browser. They are not device-aware: opening Claude.ai on your phone doesn't know that you also have Claude.ai open on your MacBook with five tabs of context. Cross-device continuity for cloud chatbots means "log in and your conversation history is the same," which is not the same thing as a continuous personal AI thread that travels with you.

The chatbots' value is per-interaction. The continuous-thread value is structurally absent.

### Per-App AI Loses the Cross-App Reality

The knowledge worker's day spans email, calendar, documents, chat, presentations, browsing, file management, code, video calls. Each application increasingly has its own AI. Per-app AI helps within the app but cannot see across apps. The cross-app reality of the work — which is most of the work — falls into the gap between apps.

### Custom Integrations Don't Scale to Personal Use

Enterprise organizations sometimes build custom integration layers that pull context from multiple systems into a unified AI surface. These integrations cost real engineering effort, target specific enterprise workflows, and do not scale down to "the consultant's individual cross-device life." Personal AI continuity is too small a use case to justify enterprise integration spend; too large a use case to ignore.

## Current Solutions: Platform AIs, Cloud Chatbots, Per-App AIs, Custom Integrations

### How the Market Currently Handles This

Four approaches dominate today:

1. **Platform-native AI** (Apple Intelligence, Gemini on Pixel, Copilot on Windows) — Polished, well-integrated, single-platform.
2. **Cloud chatbots** (ChatGPT, Claude.ai, Gemini app) — Cross-browser-accessible, conversation-history-aware, not continuous across the day.
3. **Per-application AI** (in-app assistants in Slack, Notion, Office, Google Workspace, etc.) — Helpful within the app, blind across apps.
4. **Custom enterprise integration** — Where the budget exists, IT teams glue some of this together for specific workflows.

**What this provides:**
- Platform AIs are well-polished for users who live in one platform.
- Cloud chatbots provide reliable per-interaction AI.
- Per-app AIs provide useful in-context assistance.
- Custom integrations deliver value where they exist.

### Why These Solutions Fall Short

**1. The User Doesn't Live on One Platform**
The structural assumption of platform-native AI is wrong. The platforms know this; they cannot solve it without surrendering the walls that monetize their ecosystems.

**2. Cloud Chatbots Are Sessions, Not Continuity**
A chatbot conversation history is not the same as a continuous personal AI thread. The chatbot doesn't know what the user is doing right now on another device, doesn't proactively surface relevant context, doesn't maintain background state.

**3. Per-App AI Aggregates Friction**
N applications with N built-in AIs means N AI surfaces the user has to context-switch between. Each one is locally helpful; the aggregate is harder to use than fewer, more capable surfaces would be.

**4. Custom Integrations Don't Cover Personal Use**
The knowledge worker's personal AI experience is not what enterprise integration projects target. Personal continuity is a structural absence in the integration landscape.

**5. None Provide a User-Owned Continuous Thread**
The structural gap is the same: no existing offering provides a personal AI that travels with the user across every device they use, with continuous memory and consistent behavior, that the user owns rather than rents from a platform.

## How TAI Is Different

**1. One Identity Across Every Device**
The user's TAI identity is one cryptographic identity, signed under the user's control, recognized on every device TAI runs on. The phone, the MacBook, the iPad, the Windows desktop, the web — all the same TAI, all the same identity.

**2. RFS-Backed Memory the User Owns**
The user's context lives in the RFS substrate — the user's own field of stored conversations, documents, preferences. The substrate is the user's data layer, not the vendor's. Taking it to a new device means taking the user's memory layer with them.

**3. Continuous Background Thread**
TAI is not a session-based chatbot. It runs as a persistent process (the `tai-engine` daemon) on each device, maintaining background state, proactively surfacing relevant context, and continuing the user's thread across device switches.

**4. Voice-First, Text-Always-Available**
The primary input is voice (with on-device transcription preferred). Text is available everywhere voice is available. Switching modalities is seamless within a conversation.

**5. Mathematical Accountability**
Every action TAI takes on the user's behalf passes through UCP admission and produces a signed record. The user can review what TAI did, why, and under what authority — for every action, on every device.

**6. Platform-Independent**
TAI does not depend on Apple, Google, or Microsoft for any aspect of its function. It runs on macOS, Windows, Linux, iOS, and Android by virtue of cross-platform packaging, not by virtue of any platform owner's blessing.

**7. Backend-Agnostic Inference**
The model that powers a given TAI interaction is a backend choice (Claude, GPT, Llama, in-house) routed through SAID. Switching the underlying model is a configuration change, not a re-architecting event.

## The TAI Solution: The Continuous Thread

### What If Your AI Followed You?

Imagine an AI assistant that you started a conversation with on your phone in the morning, continued on your laptop at the office, referenced from your tablet in the conference room, and resolved at your desk — without ever re-introducing the context. The AI knows what you were working on yesterday because it was with you yesterday. The AI knows the document you have open on your iPad because the document is in your shared memory substrate. The AI knows you're now on a video call with your partner because you told it once and the device transition didn't fragment the context.

This is what TAI delivers. The continuous thread is the architecture.

### The TAI Daemon

On each device the user runs TAI, the `tai-engine` daemon runs as a persistent process. The daemon maintains the user's identity, holds session state, runs the voice subsystem, and mediates between the user-facing surface (voice interaction, app integration, conversation UI) and the SMARTHAUS Component stack underneath.

The daemon is cryptographically identity-bound: the user's TAI identity signs every action, the daemon runs under that signature, and other devices' daemons recognize the same identity. Device transitions are not auth events; they are continuity events.

### The Shared Memory Substrate

The user's memory — conversations, documents, preferences, contextual notes, working state — lives in an RFS-backed substrate that is portable across devices. When the user moves from MacBook to iPad, the iPad's TAI reads from the same user-owned substrate the MacBook's TAI wrote into.

The substrate is the user's. Backup, export, migration, deletion — all under the user's control. The user can take their memory layer with them, hand it to a different AI provider, or destroy it. SMARTHAUS does not hold the data hostage; the substrate is yours.

### Cross-Device Orchestration

When the user starts an interaction on one device and continues on another, the orchestration is mathematical, not magical: the TAI on each device reads from the same memory substrate, coordinates through CAIO for any required Component invocation, and produces consistent behavior because the substrate and the Components are consistent. There is no "syncing" period or "loading" delay tied to device transition; the transition is transparent because the architecture is shared.

### Voice + Text + Visual

TAI's primary input is voice. The on-device transcription handles ambient interaction without sending raw audio to the cloud. Text input is always available. Visual context (document on screen, presentation slide, scene captured by camera) integrates with the conversation when the user invokes it.

The modality is the user's choice. The architecture treats voice-driven and text-driven interactions equivalently — the same mathematical governance, the same memory substrate, the same per-interaction evidence.

### Mathematical Accountability for Every Action

Every action TAI takes — every email it drafts, every calendar event it creates, every document it modifies, every external system it touches — passes through [UCP](../../../Components/UCP/README.md) admission and produces a signed record. The user can review the records: what TAI tried to do, what policy admitted (or denied) it, what the resulting authority chain looks like. Every inference TAI runs produces a [SAID](../../../Components/SAID/README.md) envelope the user can replay.

The user is the auditor of their own AI. The accountability is structural.

## Real-World Impact: The Numbers That Matter

### For the User

**Cognitive Load:** Re-introducing context across device transitions consumes a measurable fraction of knowledge workers' cognitive load through the day. TAI eliminates it for AI-assisted work.

**Context Continuity:** Conversations and working state persist across device transitions, across application transitions, and across time gaps. Coming back to TAI on a different device picks up where the last interaction left off.

**Memory Ownership:** The user's working memory is theirs. Migration, backup, and deletion are user-controlled events, not vendor-mediated processes.

### For Knowledge-Work Productivity

**Faster Resumption:** Returning to in-flight work after meetings, travel, or context switches happens at TAI-speed rather than at re-introduction-speed.

**Deeper Context Use:** Because TAI carries the user's full context across devices, the AI assistance available on any given device is the assistance the full context warrants — not the smaller assistance the device-local context warrants.

**Cross-Application Bridging:** TAI sees across the user's applications because the user's context flows through TAI's memory substrate. Bridging email, calendar, documents, and chat happens at the substrate level, not through per-app integration.

### For the Organization

**Knowledge Capture:** The consultant's AI-assisted reasoning across the day is captured in the user's memory substrate — available for review, summarization, or hand-off to colleagues with the user's consent.

**Vendor Independence:** The organization's knowledge workers are not locked into a single platform's AI. TAI deploys across the device mix the workforce actually uses.

**Provable AI Use:** Because every action TAI takes produces a signed record, the organization has structural evidence of how AI was used in client engagements — relevant for professional liability, regulatory exposure, and quality assurance.

## The Architecture: How It Works

### Cross-Device Identity

The user's TAI identity is a cryptographic key pair the user controls. The first-time setup generates the identity locally, secures it through the device's keychain or equivalent, and propagates the public identity to other devices the user adds. Subsequent devices recognize the user via the public identity; private operations sign with the user's controlled private key.

### Memory Substrate Replication

The user's RFS-backed memory replicates across the user's devices through an encrypted synchronization layer. The user's content is encrypted under keys only the user controls; SMARTHAUS infrastructure (if any is used for sync) cannot read the content. The replication is end-to-end encrypted by construction.

### Component Composition

Each device's TAI composes with the SMARTHAUS Component stack through [CAIO](../../../Components/CAIO/README.md) orchestration: voice in → [MAIA](../../../Components/MAIA/README.md) intent classification → CAIO routing → [SAID](../../../Components/SAID/README.md) inference → [UCP](../../../Components/UCP/README.md) admission → action. The Component stack runs locally on the device when possible; cloud Components are invoked when local processing is insufficient (typically for large-model inference on devices without sufficient compute).

### Platform Packaging

The `tai-engine` daemon is packaged for macOS (arm64, current shipping target), with Windows packaging in build. iOS and Android packaging will follow under the Y1 H2 pilot milestone.

## Use Case Scenarios

### Scenario 1: The Cross-Device Engagement

**The Situation:** The consultant from our opening scenario lives across four devices on a typical day.

**With TAI:** She speaks to TAI on the train, asking a question about yesterday's client analysis. TAI surfaces the context she captured yesterday, answers, and notes a follow-up to handle at the client site. At the client site, she opens her MacBook; TAI continues the thread. She references a document in the conversation; TAI knows the document because it's in her memory substrate. The afternoon working session, the partner call, the end-of-day wrap — all the same continuous thread.

**The Impact:** Cognitive load reduces. The AI assistance she gets is consistent with the AI assistance she gave consent to and the context she's actually built. End of day, she has *one* continuous engagement record, not four fragmented ones.

### Scenario 2: The Multi-Day Project

**The Situation:** A multi-week strategy engagement with thousands of pages of client documentation, dozens of interviews, multiple frameworks under development, and a shifting set of recommendations.

**With TAI:** The substrate accumulates the engagement's full context — documents, interview notes, frameworks, recommendation drafts, the consultant's annotations and decisions. At any point in the engagement, on any device, the consultant can ask TAI to bring relevant context forward. The retrieval is RFS-backed; matches surface with explainability metrics so the consultant knows why TAI surfaced what it did.

**The Impact:** The engagement's intellectual capital is captured in the consultant's substrate rather than scattered across notebooks, file systems, and human memory. The substrate grows in value as the engagement progresses.

### Scenario 3: The Sensitive Client Conversation

**The Situation:** A confidential client conversation that should never reach cloud AI providers' training data, may not be discoverable by the consultant's employer's IT, and must be reviewable by the consultant later.

**With TAI:** The conversation runs through TAI's on-device transcription (no cloud audio). Inference for sensitive content runs on local models (the inference layer can be configured per-conversation to prefer local backends). Every action produces a signed record the consultant retains; every inference produces a deterministic envelope she can replay. The conversation is private by architecture — the privacy guarantees are not "we promise"; they are "here is the cryptographic evidence of what processed your content."

**The Impact:** Sensitive contexts that have been off-limits to AI assistance because of trust concerns can now be served by TAI under provable privacy bounds.

## Key Metrics & KPIs

### Continuity Metrics

- **Cross-Device Context Continuity Rate:** Percentage of cross-device transitions preserving full conversation context.
  - **Target:** 100%.
  - **Impact:** Cognitive load reduction is structural.

- **Memory Substrate Availability:** Percentage of devices presenting consistent memory substrate within the user's identity.
  - **Target:** 100% on supported platforms.
  - **Impact:** The user's substrate is genuinely user-owned and cross-device.

### User Experience Metrics

- **Re-Introduction Frequency:** Per-day count of times the user must re-establish context with their AI.
  - **Target:** Near-zero post-TAI deployment (vs. dozens with siloed platform AIs).
  - **Impact:** Direct measure of cognitive-load reduction.

- **Conversation Persistence Across Time Gaps:** Percentage of multi-day conversations that resume cleanly after weekend or vacation gaps.
  - **Target:** 100%.
  - **Impact:** TAI is a continuous thread, not session-based.

### Accountability Metrics

- **Per-Action Evidence Coverage:** Percentage of TAI actions producing user-accessible signed records.
  - **Target:** 100%.
  - **Impact:** User is the auditor of their own AI.

- **Per-Inference Replay Availability:** Percentage of TAI inferences producing user-accessible deterministic envelopes.
  - **Target:** 100%.
  - **Impact:** Inference accountability is structural.

## Integration Points

### Devices and Platforms

- **macOS arm64** — current TAI shipping target with full daemon + voice + IPC stack.
- **Windows** — packaging in build under the Y1 H2 pilot.
- **iOS and Android** — native packaging on the Y1 H2 pilot timeline.
- **Web** — browser-accessible interaction surface via the `tai-sdk` API.

### Productivity Surfaces

- **Email, calendar, documents** — TAI integrates with the user's existing productivity tools as a cross-surface assistant rather than a per-app one.
- **Chat platforms** — TAI participates in Slack, Teams, and similar surfaces as a user-aware assistant the user can invoke from any of them.
- **Browser context** — TAI sees what the user has open and can reason across pages with the user's consent.

### Enterprise Composition

- **UCP-deployed enterprises** — TAI composes with customer UCP deployments to enforce enterprise policies on TAI behavior.
- **SAID-deployed enterprises** — TAI uses enterprise SAID for inference when configured, producing enterprise-side envelopes.
- **MAE-deployed enterprises** — Proven properties from MAE engagements ship into TAI as enforced bounds on TAI behavior.

## Why This Matters

### The Cost of Not Having This

The cost of fragmented per-device personal AI is the cognitive load knowledge workers absorb every time they switch devices, the value the AI fails to deliver because it doesn't have the cross-device context, and the structural ceiling on how useful personal AI can be when it is locked to single platforms. The cost scales with how multi-device the user's life is — which is most users, most of the time.

### The Value of Having This

TAI turns personal AI from a per-device tool into a continuous thread that travels with the user. The cognitive-load reduction, the context-continuity benefit, the structural accountability — all compound across the user's day.

### The Competitive Advantage

For the first cohort of knowledge workers (and the organizations employing them) who adopt TAI, the cross-device AI advantage compounds against peers locked into single-platform personal AI. The advantage is not theoretical — it shows up as faster work, better decisions, and lower cognitive cost.

## Learn More

- **[TAI product page](../../README.md)** · **[PALI category overview](../../../README.md)** · **[Other TAI use cases](../README.md)**
- **The supporting Components:** [UCP](../../../../Components/UCP/README.md) · [SAID](../../../../Components/SAID/README.md) · [MAE](../../../../Components/MAE/README.md) · [CAIO](../../../../Components/CAIO/README.md)
- **The Substrate:** [RFS](../../../../Substrate/RFS/README.md) · [NME](../../../../Substrate/NME/README.md)

---

**TAI delivers the cross-device continuous thread for knowledge workers — one identity, one memory, every device, with mathematical accountability for every action the AI takes on the user's behalf.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
