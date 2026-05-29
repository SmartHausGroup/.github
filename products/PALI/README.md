# PALI — Personal AI Layer Interface

**The category SMARTHAUS is defining: portable AI that travels with the user across every device.**

---

## What PALI is

PALI — **Personal AI Layer Interface** — is the category name SMARTHAUS is staking for portable, mathematically-governed personal AI. The way "operating system" was once a category name somebody had to define, and the way "smartphone" was once a category that did not exist until somebody named it.

A category needs three things to exist:
- A **shape** — what the category is, distinct from adjacent categories.
- A **necessity** — why the category needs to exist now, when it didn't have to before.
- A **product** — something operational that delivers the category, so the category is not a theoretical placeholder.

PALI has all three.

## The shape

PALI is a portable AI layer that travels with the user across every device — one identity, one memory, one governance plane, on whatever device the user happens to be using at the moment. Phone, laptop, tablet, headset, web. The PALI experience is *continuity*: a conversation started on iPhone continues on Windows without re-introducing yourself. A research thread from Tuesday evening on iPad shows up Wednesday morning on a work MacBook. Preferences, permissions, history — all travel with you.

The infrastructure underneath is *portability by construction*:

- **Identity** — one cryptographic identity for *you*, signed under your control, recognized on every device.
- **Memory** — your context lives in a substrate that is yours to read, yours to revoke, yours to take with you. Not in a vendor's silo.
- **Governance** — the same admission policies, the same proof obligations, the same audit chain, regardless of which device the AI happens to be running on at a given moment.

PALI is distinct from:

- **Cloud assistants** (Siri, Alexa, Google Assistant) — single-platform, vendor-owned data, no cross-device continuity outside the vendor's ecosystem.
- **Productivity AI** (Copilot, Gemini in Workspace) — tied to a specific productivity platform, not portable across the user's full device footprint.
- **Chatbots** (ChatGPT, Claude.ai, Gemini app) — useful but not memory-resident across devices, governance-light, identity-vendor-mediated.
- **Agent platforms** (autoGPT-style frameworks) — automation-focused, not user-companion-focused, no consumer-facing surface.

PALI is the consumer-facing personal AI category. It is what users experience when their AI is *theirs* and follows them.

## The necessity

Personal AI is the most consequential consumer technology of the next decade. The three companies positioned to own it — Apple, Google, Microsoft — *cannot* deliver it across the devices people actually use.

- **Apple Intelligence** is locked to Apple silicon. It does not exist on the Android phone your spouse uses, the Windows laptop you got at work, the Chromebook your kid has at school.
- **Gemini** favors Pixel and the Google ecosystem. It is not native to your iPhone, your Mac, your Surface.
- **Microsoft Copilot** is built into Windows and Microsoft 365. It cannot follow you onto iOS or into a Google Workspace.

Each of the three platform owners is racing to own your personal AI inside their own walls. None of them can credibly own it across all of them. **The walls are their business model.**

SMARTHAUS is not a platform. We can deliver across the walls because we are not protecting any walls.

The PALI category exists because the user's reality is multi-device, multi-vendor, multi-context — and no platform-owner-controlled AI can serve that reality. The category is necessary now, not in five years, because the user's reality is already multi-device; the only question is whether somebody fills the gap with a portable layer or whether the user lives with three or four siloed AIs that don't talk to each other.

## The product — TAI

The product that delivers the PALI category is **[TAI — Tutelarius Auxilium Intellectus](./TAI/README.md)**. Voice-first personal assistant with mathematical guarantees. Cross-device by construction. Built on the SMARTHAUS substrate — [RFS](../Substrate/RFS/README.md) for memory, [SAID](../Components/SAID/README.md) for deterministic inference, [UCP](../Components/UCP/README.md) for governance, [MAE](../Components/MAE/README.md) for proven properties.

TAI is in active development with platform foundations (Rust daemon, voice subsystem, IPC layer, packaging for macOS and Windows) already built. The Y1 H2 milestone is the first cross-device personal AI experience that doesn't depend on any platform owner's permission to exist on every device the user touches.

**[Read the TAI product page →](./TAI/README.md)**

## What this means for SMARTHAUS

PALI is the category. TAI is the product. The Components (UCP, SAID, MAE, MAIA, MGE, CAIO, VEE) are the mathematical-governance infrastructure underneath. The Substrate (RFS, NME) is the integration layer everything reads and writes into.

A reader of the SMARTHAUS vision can see the architecture in one direction or the other:

- **Top-down:** PALI is what the user touches. TAI is the product that delivers PALI. Under TAI are the Components. Under the Components is the Substrate.
- **Bottom-up:** The Substrate integrates everything. The Components operate on the Substrate. PALI is the consumer-facing surface those Components converge into. TAI is the PALI product.

The category exists because the architecture supports it. The architecture exists because the category needs it. They co-define each other.

---

**[Read TAI — the PALI product →](./TAI/README.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
