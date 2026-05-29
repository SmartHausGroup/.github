# MAE — Mathematical Autopsy Engine

**Status: Foundation in place. Deployment build under construction.**

---

## What it is

MAE is the build authority for everything SMARTHAUS ships. It is the engine that runs our development discipline — **[Mathematical Autopsy](../mathematical-autopsy/)** — and enforces that every claim in our codebase is backed by a checked artifact: a lemma, an invariant, a notebook proof, a signed receipt, or a CI gate.

If a property cannot be proven, MAE refuses to mark it shippable. There is no demo path that bypasses the gates.

This is the difference between marketing a system as "responsible" and building a system whose responsibility is mechanically verified before any code leaves a development machine.

## The failures it closes

MAE is the answer to two of the [Six Failures](../six-failures/):

- **BIND** — Lab benchmarks famously do not bind production behavior; vendors game public scores while deployed systems fall apart. MAE production-bound proofs eliminate the gap: the property verified in development is the property enforced in production. The LMArena benchmark-gaming pattern is structurally unavailable to a MAE-built system.
- **SPECIFY** — When courts (Lokken v. UnitedHealth, March 2026) order disclosure of the decision criteria behind an AI system, most vendors can produce only model weights. MAE-built systems produce Lean specifications — readable, auditable, defensible documents that describe *what* the system is allowed to decide and *how* it must justify each decision.

It also contributes to **LEAD** — MAE specifications are the format regulators are converging on under the EU AI Act and SR 26-2.

## How it works (the short version)

Mathematical Autopsy is a 9-phase pipeline, CI-bound, template-first:

1. **Intent** — what must the system do, and what must it never do
2. **Mathematical foundation** — formalize the problem
3. **Lemmas** — proof obligations
4. **Invariants** — properties that must hold at all times
5. **Notebook verification** — executable proofs
6. **Scorecards** — pass/fail evidence
7. **CI binding** — `release` and `extract-runtime` targets refuse to run unless the aggregate scorecard is green
8. **Signed receipts** — every artifact carries cryptographic provenance
9. **Deployment** — bind production behavior to the proven properties

Across the SMARTHAUS active codebase, this discipline produces **~75 named lemmas, ~700 machine-enforced invariants, ~880 runnable notebook proofs**. Every one of them is in CI. None of them are decorative.

## What ships today

- The 9-phase pipeline is canonical and CI-bound (`UCP/configs/ma_phases.yaml`).
- `release` and `extract-runtime` make targets enforce the green-scorecard gate.
- All current SMARTHAUS products (UCP, SAID, MAIA, CAIO) ship under MAE governance.
- MAE deployment build (the externalized service for customer use) is under construction.

## How to engage

MAE is currently the substrate beneath our shipping products, not yet a standalone customer-facing product. Engagement happens through **Applied-MA** — an embedded engagement with customer teams to bring their own systems under Mathematical Autopsy discipline. Reach out via **[smarthaus.ai](https://smarthaus.ai)**.

---

**[← Back to SMARTHAUS](https://github.com/SmartHausGroup)** · **[The Six Failures](../six-failures/)** · **[Mathematical Autopsy →](../mathematical-autopsy/)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
