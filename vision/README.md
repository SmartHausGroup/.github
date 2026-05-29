# The SMARTHAUS Vision

**Every AI decision should come with a receipt.**

SMARTHAUS is building the substrate underneath enterprise AI — the layer that makes AI decisions provable, replayable, and verifiable by anyone outside the company that ran them. We're building it because the enterprise AI category is structurally incomplete without it, the regulators are no longer waiting, and the failures that prove the need are already in court.

This page is the entire end-to-end view of what we're building. Investors, partners, and technical readers who want the full picture instead of the per-product slice — this is for you.

---

## The condition

We are not the first to claim AI needs governance. We are one of the first to argue that governance built as a wrapper around AI is itself a guess — and that **you cannot govern a guess with another guess.** That sentence is the wedge underneath the company.

Enterprise AI fails in six distinct, structural ways. None of them are bad-vendor problems. None of them are solved by the safety tools the market is currently selling. Each one converges on the same missing artifact: a verifiable record of a specific decision, made at the moment of decision, that an outside party can replay and confirm. We call them **The Six Failures** — PROVE, REPLAY, BIND, PREVENT, SPECIFY, LEAD — and each one has a real court case behind it from January 2025 forward. **[Read the full breakdown →](../six-failures/README.md)**

Three things have changed at once.

- **The failures are now in court.** Mobley v. Workday certified as a nationwide collective action. Cursor's hallucinating support bot. Replit's autonomous coding agent dropping a production database. UnitedHealth's nH Predict facing court-ordered algorithm disclosure.
- **The regulators have stopped waiting.** EU AI Act enforcement live February 2, 2025. SR 26-2 finalized April 2026 (replacing the 2011 SR 11-7 model-risk framework). State AI laws stacking through 2025–2026.
- **The dollars are following.** Gartner now projects **$2.5 trillion in global AI spending in 2026**. The category is forming around the missing artifact, and the companies that build with it already in the architecture pay no retrofit bill.

---

## The architecture — three categories

SMARTHAUS is not a product. It's three categories of product, organized around a shared mathematical [Substrate](../products/Substrate/README.md), composed through [Components](../products/Components/README.md), and surfaced through a portable [PALI](../products/PALI/README.md) layer.

### Substrate — the mathematical foundation

Two primitives form the substrate. Neither is sold standalone; both ship as the integration layer every Component reads and writes into.

- **[RFS — Resonant Field Storage](../products/Substrate/RFS/README.md).** Field-theoretic memory. Information is stored as wave patterns in a 4D Fourier field; retrieval works through matched-filter probing rather than brute-force vector cosine.
- **[NME — Nota Memoria Engine](../products/Substrate/NME/README.md).** The encoder that extracts structured meaning from text and projects it into the RFS field.

The point of a substrate is what it replaces. APIs connect *behavior*; substrates integrate *state*. In a chained architecture, behavior fires step-by-step and small errors compound until the system drifts out of sync. In a substrate-integrated architecture, every step writes into the same field and is bounded by the same rules. The math holds the system together. Substrate productization ships Y2 H2.

### Components — the seven mathematical-governance products

Seven Components compose into the SMARTHAUS architecture. Three are pilot-ready and signed for distribution today; four are in active development.

| Component | Function | Status |
|---|---|---|
| **[UCP — Universal Control Plane](../products/Components/UCP/README.md)** | Runtime governance. Nothing executes that hasn't been admitted by policy. Signed record every time. | Pilot-ready (v0.6.3) |
| **[SAID — Deterministic Inference Engine](../products/Components/SAID/README.md)** *(Latin: Sermo Arbiter Inferentiae Determinata)* | GPU-first deterministic inference with constraint gates. Same input, same output, replayable, integrity-verified. | Pilot-ready (v0.2.5) |
| **[MAE — Mathematical Autopsy Engine](../products/Components/MAE/README.md)** | Math-first build discipline applied inside customer applications. Customer owns the proven code. | Pilot-ready (MVP) |
| **[MAIA — Intent Engine](../products/Components/MAIA/README.md)** *(Latin: Mens Animus Intentio Anima)* | Figures out what the user actually wants. | Active development |
| **[MGE — Mathematical Governance Engine](../products/Components/MGE/README.md)** | Governance running as a sidecar inside customer applications. | Active development |
| **[CAIO — Orchestrator](../products/Components/CAIO/README.md)** *(Latin: Coordinatio Auctus Imperium Ordo)* | Orchestrates services and controls access across Components. | Active development |
| **[VEE — Math, Privacy, RL Kernel](../products/Components/VEE/README.md)** *(Latin: Voluntas Engine)* | Lyapunov stability, quantum-inspired compute, differential privacy. Consumed by other Components. | Active development |

Each Component is a *mathematical operator on AI behavior* — a contract the action has to satisfy, a verdict, and a signed record anyone can verify later. Each ships independently and composes with the others.

### PALI — the consumer surface

**[PALI — Personal AI Layer Interface](../products/PALI/README.md)** is the category SMARTHAUS is defining: portable, mathematically-governed personal AI that travels with the user across every device.

A category needs three things to exist: a shape, a necessity, and a product. PALI has all three.

The **shape** is a portable AI layer with one identity, one memory, and one governance plane that follows the user across phone, laptop, tablet, headset, web — distinct from cloud chatbots (no cross-device continuity), platform AIs (single-vendor), per-app AIs (single-app), and agent platforms (no consumer surface).

The **necessity** is that the three platform owners trying to own personal AI — Apple, Google, Microsoft — cannot deliver it across the devices people actually use. Apple Intelligence is locked to Apple silicon. Gemini favors Pixel. Copilot favors Windows. The walls are their business model. SMARTHAUS is not a platform; we can deliver across the walls because we are not protecting any walls.

The **product** is **[TAI — Tutelarius Auxilium Intellectus](../products/PALI/TAI/README.md)**. Voice-first personal AI with mathematical guarantees. Cross-device by construction. Built on the SMARTHAUS Component stack with platform foundations (Rust daemon, voice subsystem, IPC, macOS arm64 packaging) already shipping. Y1 H2 pilot milestone delivers the first cross-device PALI experience.

---

## The discipline — Mathematical Autopsy

How we build is upstream of what we build. **MA — Mathematical Autopsy** is the development discipline that produces every piece of software SMARTHAUS ships, and the structural reason the seven by-construction properties hold.

Conventional development goes: write the code, run the tests, iterate, debug, ship, monitor, hope. The artifact you ship is a guess you have checked. SMARTHAUS inverts the sequence.

1. **Define.** State what the system must do, must never do, and must guarantee.
2. **Validate.** Confirm the definitions with the people who own them.
3. **Prove.** Each rule is proven to hold, in math, using our proof engine. No proof, no progress.
4. **Convert.** Once the rules are proven, they become code in the target language.
5. **Notebook.** The code runs in a notebook and is tested against the proven contract. Green or nothing.
6. **Extract.** When and only when the notebook is green, the code is extracted as runtime, with validating metadata in the header — signing chain, rule references, proof identifiers, version pins.

The artifact we ship is a contract we have proven and a runtime that enforces it. There is no demo path that bypasses the gates.

Across our active codebase: **75+ named lemmas, 700+ machine-enforced invariants, 880+ runnable notebook proofs** — every one of them in CI. **[Read more about Mathematical Autopsy →](../mathematical-autopsy/README.md)**

---

## What we sell today — the three plays

The Components land in customer hands through three named plays. Each one closes a different shape of failure in a different part of the customer's stack.

**Prevent — MGAI (Mathematically Governed AI), built on UCP.** We stop your AI agents from taking actions they shouldn't, *before* they fire. Signed record either way. Closes the **PREVENT** and **PROVE** failures primarily; also closes drift, eval rot, and regulatory exposure in the agent layer. **[See use cases for UCP →](../products/Components/UCP/use-cases/README.md)**

**Replay — DI (Deterministic Inference), built on SAID.** We make your AI give the same answer to the same question, every time — with a record anyone can replay to verify. Closes the **REPLAY** failure primarily; also closes compounding error, eval rot, governance-by-watching, and regulatory replay demands. **[See use cases for SAID →](../products/Components/SAID/use-cases/README.md)**

**Specify — Applied-MA (Applied Mathematical Autopsy), built on MAE.** We write your high-stakes capability's rules in math, prove them, and embed the proven code inside your software. You own it outright — no SMARTHAUS runtime in your production stack. Closes the **SPECIFY** and **BIND** failures primarily; closes all six, scoped to one workload. **[See use cases for MAE →](../products/Components/MAE/use-cases/README.md)**

The customer outcome is consistent across all three: software that meets the **seven by-construction properties** of Mathematically Governed Deterministic AI — *Reproducible, Traceable, Explainable, Replayable, Auditable, Falsifiable, Verifiable*. Each property answers a different question a regulator, auditor, or court will ask. Collapsing them would mean leaving one of those questions unanswered.

---

## The endgame

Where this leads in 36–60 months:

**Components land in regulated industries first.** Financial services, insurance, healthcare, life sciences, defense — the industries that feel the failure pressure before anyone else and have the budget to close it. By the time the same failures pierce non-regulated industries (and they will), the Components are proven, scaled, and the play motions are repeatable.

**The Substrate becomes the integration layer.** As more Components land at the same customer, the Substrate (RFS + NME) goes from "what makes the products work together internally" to "what makes the customer's whole AI estate cohere." The pricing model captures the network effect.

**The marketplace compounds.** Y3+ the two-sided ecosystem ramps. Enterprises and individual users browse a single catalog of sealed, signed, version-pinned packs that drop into UCP, SAID, MAE, TAI, or any future Component. Third-party publishers — privacy lawyers, fraud-prevention firms, parental-safety nonprofits, financial advisors, healthcare advocates — build packs that inherit the same mathematical guarantees because the validation gate does not care who wrote the code. AWS-shape leverage with a SMARTHAUS-shape gate.

**TAI brings the Substrate into the user's experience.** The same Substrate that runs enterprise governance also runs cross-device personal AI through TAI. The wedge in is the enterprise; the destination is everyone with a phone.

**The category is named.** *Mathematically Governed Deterministic AI* — defined by the seven by-construction properties, structurally distinct from wrappers, guardrails, MLOps, model audit, and chatbots. The category SMARTHAUS owns by virtue of having built it.

---

## The wager

The bet is that enterprise AI gets governed by math, or it doesn't get governed at all — and that the company that builds the math substrate first, ships the Components that prove it works, and opens the marketplace that compounds it, becomes the unavoidable layer for any AI deployment that has to answer to a regulator, an auditor, a board, a customer, or a court. And that the same architecture, surfaced through TAI, becomes the personal AI users actually own — not the one platform owners rent to them.

We're already shipping. Two Components are pilot-ready and signed for distribution — UCP v0.6.3 and SAID v0.2.5. The third (MAE) is at minimum viable product. Three patents are filed (RFS, UCP, MA). Princeton Physics is collaborating on substrate validation in real laboratory data. TAI platform foundations are shipping in Rust. The Substrate productizes Y2 H2. The marketplace ramps Y3+.

You cannot govern a guess with another guess. We are the company building the proof.

---

**[The Six Failures](../six-failures/README.md)** · **[Products](../products/README.md)** · **[PALI](../products/PALI/README.md)** · **[Mathematical Autopsy](../mathematical-autopsy/README.md)** · **[Princeton Research](../research/princeton.md)** · **[Patents](../research/patents.md)** · **[Math Thesis](../thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
