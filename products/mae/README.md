# MAE — Mathematical Autopsy Engine

**Status: Foundation in place. Deployment build under construction.**

---

## What it is

MAE is the build authority for everything SMARTHAUS ships. It is the engine that runs our development discipline — **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** — and enforces that every claim in our codebase is backed by a checked artifact: a lemma, an invariant, a notebook proof, a signed receipt, or a CI gate.

If a property cannot be proven, MAE refuses to mark it shippable. There is no demo path that bypasses the gates.

This is the difference between marketing a system as "responsible" and building a system whose responsibility is mechanically verified before any code leaves a development machine.

## The failures it closes

MAE is the answer to two of the [Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md):

- **BIND** — Lab benchmarks famously do not bind production behavior. MAE production-bound proofs eliminate the gap: the property verified in development is the property enforced in production.
- **SPECIFY** — When courts (Lokken v. UnitedHealth, March 2026) order disclosure of the decision criteria behind an AI system, MAE-built systems produce Lean specifications — readable, auditable, defensible documents that describe what the system is allowed to decide and how it must justify each decision.

It also contributes to **LEAD** — MAE specifications are the format regulators are converging on under the EU AI Act and SR 26-2.

## Use cases

MAE applies wherever a high-stakes capability needs to be **proven before it ships** — and where the customer wants to own the proven code outright, with no SMARTHAUS runtime in their production stack. Four canonical deployments documented in depth:

1. **[Medical-Necessity Logic in Payer Adjudication Systems](./use-cases/01_medical_necessity_logic/README.md)** — The nH Predict pattern done correctly. Proven medical-necessity rules embedded in the customer's coverage engine. The plaintiff and the regulator can re-verify the proof on open-source toolchain.
2. **[Eligibility and Benefits Determination](./use-cases/02_eligibility_benefits/README.md)** — Government benefits programs, insurance claims, lending eligibility. Proven decision logic the customer owns outright. Independent re-verifiability of each determination.
3. **[Regulatory Disclosure and Submission Generation](./use-cases/03_disclosure_submission/README.md)** — Auto-generated regulatory disclosures (Reg Z, GDPR, FDA labeling, capital reports) where the property "compliant with rule X" is mathematically proven before the disclosure ships.
4. **[Capital, KYC, and AML Calculations with Regulatory Boundaries](./use-cases/04_capital_kyc_aml_calculations/README.md)** — Embedded proven logic for high-stakes financial calculations. Auditor and examiner can re-verify each output without trusting the vendor.

**[See all MAE use cases →](./use-cases/README.md)**

## How it works (the short version)

Mathematical Autopsy is a 9-phase pipeline, CI-bound, template-first:

1. **Intent** — what must the system do, and what must it never do.
2. **Mathematical foundation** — formalize the problem.
3. **Lemmas** — proof obligations.
4. **Invariants** — properties that must hold at all times.
5. **Notebook verification** — executable proofs.
6. **Scorecards** — pass/fail evidence.
7. **CI binding** — `release` and `extract-runtime` targets refuse to run unless the aggregate scorecard is green.
8. **Signed receipts** — every artifact carries cryptographic provenance.
9. **Deployment** — bind production behavior to the proven properties.

Across the SMARTHAUS active codebase, this discipline produces **~75 named lemmas, ~700 machine-enforced invariants, ~880 runnable notebook proofs**. Every one of them is in CI. None of them are decorative.

## What ships today

- The 9-phase pipeline is canonical and CI-bound.
- The `release` and `extract-runtime` make targets enforce the green-scorecard gate.
- All current SMARTHAUS products (UCP, SAID, MAIA, CAIO) ship under MAE governance.
- MAE deployment build (the externalized service for customer use) is under construction.

## How to engage

MAE is currently the substrate beneath our shipping products, not yet a standalone customer-facing product. Engagement happens through **Applied-MA** — an embedded engagement with customer teams to bring their own systems under Mathematical Autopsy discipline. Reach out via **[smarthaus.ai](https://smarthaus.ai)**.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
