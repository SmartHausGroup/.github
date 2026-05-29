# TAI Use Cases — Where the PALI Experience Lives

**Status:** Public Documentation
**Last Updated:** 2026-05

## Overview

This directory contains four in-depth use cases for **TAI**, the [PALI product](../README.md). Each use case is a white paper covering the lived user problem, why existing personal-AI offerings fall short, how TAI's mathematically-governed cross-device architecture closes the gap, and the measurable outcomes for the user and the organization adopting it.

TAI applies wherever a user wants a personal AI that follows them across devices, that they actually own, and that has mathematical accountability for what it does on their behalf. The four documented deployments span professional knowledge work, hands-busy operational contexts, privacy-critical personal and professional uses, and family/household environments with permission boundaries.

## Use Cases

### 1. Cross-Device Personal AI for Knowledge Workers
**Directory:** `01_cross_device_knowledge_worker/`
**Problem:** The consultant's iPhone has its own context. The work MacBook has its own context. The personal iPad has its own context. The conference-room shared workstation has its own context. Each "AI" is a stranger to the others. The user spends their cognitive load re-introducing themselves to each new surface instead of doing work.
**TAI Solution:** One TAI identity that travels with the user. Conversations started on the phone continue on the laptop. Documents loaded on the iPad are available on the workstation. Preferences, permissions, history — all travel.
**Key Value:** Cognitive load reduction (no re-introduction), context continuity across the multi-device work day, mathematically-governed memory the user owns.

### 2. Voice-First AI in Hands-Busy Workflows
**Directory:** `02_voice_first_hands_busy/`
**Problem:** Clinicians in surgery cannot type. Field service technicians have both hands on equipment. Long-distance drivers cannot look at a screen. Accessibility users may not be able to use typing or screens at all. The dominant "AI" surface assumes a keyboard and a screen.
**TAI Solution:** Voice-first as the primary modality. On-device transcription preferred for privacy and latency. Same mathematically-governed substrate as the typing-based interactions; the modality is the difference, the architecture is the same.
**Key Value:** AI accessible in operational contexts where it has been operationally absent. Privacy-preserving voice processing. Mathematical guarantees apply to voice-initiated actions identically to typed actions.

### 3. Personal AI With Provable Privacy
**Directory:** `03_provable_privacy/`
**Problem:** Mental health context, legal counsel context, financial advisor context, attorney-client privileged communication context, medical-history context — all of these are contexts where the user needs to know exactly what the AI did, did not do, and could not do with their information. Trust-based promises ("we don't use your data for training") are insufficient when the stakes are this high.
**TAI Solution:** Per-interaction signed envelopes (via SAID) and per-action admission records (via UCP) that the user can examine independently. The mathematical guarantees the SMARTHAUS substrate provides apply equally to consumer privacy contexts as to enterprise compliance contexts. The user is the auditor.
**Key Value:** Provable rather than promised privacy. User-owned cryptographic evidence of what the AI did with their data. Architecturally-bounded scope on what the AI is allowed to do with sensitive information.

### 4. Family and Household AI With Permission Boundaries
**Directory:** `04_family_household_permissions/`
**Problem:** A family of four sharing a household has different family members with different ages, different responsibilities, different privacy needs. Parental controls in consumer AI today are policy promises with no architectural enforcement. The 8-year-old should not be able to ask about subjects the parent has scoped out; the teen should have access to homework help with bounded autonomy; the parent should have audit visibility into AI interactions with the children.
**TAI Solution:** UCP admission policies enforced per-family-member identity. Shared household context for collaborative work (vacation planning, meal planning, schedule coordination) coexisting with private individual contexts. Mathematical enforcement of parental controls — the model cannot serve content outside the scope the parent has admitted for that family member.
**Key Value:** Family-scale AI that mathematically respects permission boundaries. Parental controls that are not bypassable through prompt engineering. Shared and private contexts coexist with structural separation.

## Quick Comparison

| Use Case | Primary TAI Feature | Key Differentiator | User Value |
|---|---|---|---|
| Knowledge Worker | Cross-device continuity | One identity, one memory, every device | Cognitive load reduction; context preservation |
| Hands-Busy Workflows | Voice-first interface | Privacy-preserving on-device transcription | AI accessible in operational contexts; equivalent guarantees across modalities |
| Provable Privacy | Per-interaction signed evidence | User-owned audit trail of every AI action | Trust based on proof, not promise |
| Family Permissions | Per-identity admission policies | Mathematical enforcement of parental controls | Family-scale AI that respects bounded scopes |

## Common TAI Capabilities Used

Every TAI use case shares the same underlying capabilities:

- **Cross-device identity continuity** — one cryptographic identity for the user that every TAI surface recognizes.
- **RFS-backed memory** — user context lives in a substrate the user owns, taking it to new devices requires no migration.
- **UCP admission gates** — every action TAI takes flows through policy admission, with signed records.
- **SAID deterministic inference** — every inference produces a per-interaction envelope the user can replay.
- **Voice-first primary input** — with text as the secondary modality across all use cases.
- **MAE-proven properties** — properties TAI enforces (privacy scopes, permission boundaries, content limits) are mathematically proven before they ship into the runtime.
- **CAIO orchestration** — Component invocation governed by formal contracts rather than imperative wiring.

## How to Engage

TAI is in active build toward the Y1 H2 pilot. Early access lists are open. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with the use case that best matches your context — and the device footprint across which you'd want TAI to follow you.

---

**[TAI product page](../README.md)** · **[PALI category](../../README.md)** · **[Components](../../../Components/README.md)** · **[Substrate](../../../Substrate/README.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
