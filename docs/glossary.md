# Glossary

Short definitions of the terms used across the SMARTHAUS documentation.

---

## Architecture

**PALI** — Personal AI Layer Interface. A portable AI layer that travels with the user across every device they own, anchored on one identity, one memory, and one governance plane. The consumer-facing surface SMARTHAUS is building on top of the substrate. See **[PALI](/pali/)**.

**Substrate** — The mathematical layer underneath SMARTHAUS products. Composed of three things shipping today: governance (UCP), inference (SAID), and the discipline that produces both (MAE / Mathematical Autopsy).

**Federated composable architecture** — The internal architectural model: hosts (TAI, UCP) embed primitives (SAID, MAE, others); primitives stay first-class products while composing into a unified user experience.

---

## Products

**UCP** — Universal Control Plane. Runtime governance product. Nothing executes that hasn't been admitted by policy. Every admitted action carries a cryptographically signed authority chain. Current release: v0.6.3. See **[UCP](/products/ucp)**.

**SAID** — Deterministic inference engine. Makes frontier models interchangeable underneath application logic. Same inputs + same fixed context → same outputs. Current release: v0.2.5. See **[SAID](/products/said)**.

**MAE** — Mathematical Autopsy Engine. The build authority that enforces the MA discipline across SMARTHAUS products. Deployment build under construction. See **[MAE](/products/mae)**.

**TAI** — The canonical integration host for cross-device personal AI. The shell inside which PALI renders on every device.

---

## Methodology

**Mathematical Autopsy (MA)** — The development discipline used to build SMARTHAUS products. A 9-phase pipeline that proves mathematical properties of a system before any code is written. CI-bound. Template-first. See **[Mathematical Autopsy](/mathematical-autopsy/overview)**.

**The Six Failures** — The six distinct ways enterprise AI breaks in production: PROVE, REPLAY, BIND, PREVENT, SPECIFY, LEAD. Each has a real court case behind it. Each is closed by construction in our architecture. See **[The Six Failures](/six-failures/)**.

**By-construction** — A property is "by construction" if it holds because of how the system is built, not because of testing, monitoring, or human discipline. SMARTHAUS systems are built so seven properties hold by construction: **Reproducible, Traceable, Explainable, Auditable, Replayable, Falsifiable, Verifiable**.

---

## Substrate technology

**RFS** — Resonant Field Storage. The mathematical memory substrate. Information is stored as wave patterns in a 4D Fourier field; retrieval works by matched-filter probing rather than vector cosine. See **[RFS](/rfs/overview)**.

**NME** — Nota Memoria Engine. The encoder layer that transforms text into structured complex-valued waveforms suitable for RFS. Currently in active research.

**FHRR** — Fourier Holographic Reduced Representations (Plate 1995). The vector-algebra framework underneath NME's complex-valued encoding.

**MCP** — Model Context Protocol. The standard interface SMARTHAUS products use to communicate with AI clients (Claude Code, IDE plugins, agent frameworks). UCP ships a local MCP broker.

---

## Governance & compliance

**Admission gate** — A UCP construct: a policy check that runs *before* an action executes. If policy denies, the action does not happen. There is no application-layer override.

**Signed receipt** — A cryptographically signed record of an action: who attempted it, what was attempted, what authority admitted it, what was decided. Portable, replayable, and admissible.

**Invariant** — A property that must hold at every point in a system's lifetime. SMARTHAUS invariants are YAML-defined and CI-verified. Roughly 700 of them across our active codebase.

**Lemma** — A formal mathematical claim with a proof obligation. SMARTHAUS lemmas are numbered (L1, L2, …) and tied to executable verification notebooks.

**Scorecard** — The aggregate pass/fail evidence for a phase or component, cryptographically pinned. Release targets refuse to run unless the scorecard is green.

**SR 26-2** — Federal Reserve supervisory letter on AI/ML model risk management, finalized April 17, 2026. Supersedes SR 11-7. Requires model lineage and decision provenance — the format SMARTHAUS already produces.

**EU AI Act** — European Union AI regulation, enforcement live February 2, 2025.

---

## Research

**Princeton collaboration** — Joint research applying RFS + NME methods to single-particle fluorescence spectroscopy data developed by Puchalla et al. (2008). Joint paper in preparation. See **[Princeton Research](/research/princeton)**.

**Math Thesis** — The formal mathematical foundation underneath the SMARTHAUS substrate. Currently at v8. See **[Math Thesis](/thesis/framework)**.

---

**[← Back to SMARTHAUS](https://github.com/SmartHausGroup)**
