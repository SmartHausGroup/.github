# PALI — Personal AI Layer Interface

**Your AI. On every device you own. One identity, one memory, one governance plane.**

---

## The thesis

Personal AI is the most consequential consumer technology of the next decade, and the three companies positioned to own it — Apple, Google, Microsoft — *cannot* deliver it across the devices people actually use.

- **Apple Intelligence** is locked to Apple silicon. It does not exist on the Android phone your spouse uses, the Windows laptop you got at work, the Chromebook your kid has at school.
- **Gemini** favors Pixel and the Google ecosystem. It is not native to your iPhone, your Mac, your Surface.
- **Microsoft Copilot** is built into Windows and Microsoft 365. It cannot follow you onto iOS or into a Google Workspace.

Each of the three platform owners is racing to own your personal AI *inside their walls*. None of them can credibly own it *across* all of them. The walls are their business model.

We are not a platform. We can.

## What PALI is

PALI is a portable AI layer that travels with you. The same identity, the same memory, the same governance — on whatever device you happen to be using at the moment. Phone, laptop, tablet, headset, web.

The user-facing experience is continuity: a conversation you started on your iPhone continues on your Windows machine without re-introducing yourself. A research thread from a Tuesday evening on your iPad shows up Wednesday morning on your work MacBook. Permissions, history, preferences — all travel with you.

The infrastructure underneath is portability by construction:

- **Identity** — one cryptographic identity for *you*, signed under your control, recognized on every device.
- **Memory** — your context lives in a substrate that is yours to read, yours to revoke, yours to take with you. Not in a vendor's silo.
- **Governance** — the same admission policies, the same proof obligations, the same audit chain — regardless of which device the AI happens to be running on at a given moment.

## What's underneath

PALI is not a new model. It is a *layer* on top of the substrate we already ship:

- **[UCP](../products/ucp.md)** provides the governance plane — every action signed, every authority chain admissible.
- **[SAID](../products/said.md)** provides the inference layer — frontier models interchangeable, deterministic when it matters.
- **[MAE](../products/mae.md)** provides the proof discipline — every property the system claims is mechanically checked.

PALI is the consumer-shaped surface those three substrate products converge into.

## What ships today, and when

- **Today:** The substrate (UCP, SAID) is pilot-ready. The discipline (MAE) governs all of it.
- **Next 18 months:** The PALI experience rolls out — portable identity, cross-device memory, the unified surface.

We are not waiting for the platforms to open their walls. We are building the layer that doesn't need them to.

---

**[← Back to SMARTHAUS](https://github.com/SmartHausGroup)** · **[The Six Failures](../six-failures/)** · **[UCP →](../products/ucp.md)** · **[SAID →](../products/said.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/ucp.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
