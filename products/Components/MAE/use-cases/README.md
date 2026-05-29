# MAE Use Cases — Where Proven Code Lives

**Status:** Public Documentation
**Last Updated:** 2026-05

## Overview

This directory contains four in-depth use cases for **MAE — Mathematical Autopsy Engine**, sold under the **Applied-MA** engagement. Each use case is a white paper covering the operational problem, why existing market solutions fall short, how MAE closes the gap by construction, and the measurable outcomes for the organization adopting it.

MAE applies wherever a high-stakes capability needs to be **mathematically proven before it ships** — and where the customer wants to own the proven code outright, with no SMARTHAUS runtime in their production stack. The proof is the deliverable. The customer's own software embeds the proven code. The regulator, auditor, plaintiff, or court can re-verify the proof on open-source toolchain.

## Use Cases

### 1. Medical-Necessity Logic in Payer Adjudication Systems
**Directory:** `01_medical_necessity_logic/`
**Problem:** Health insurance carriers using AI for coverage determinations face the post-Lokken environment: courts ordering disclosure of decision logic, plaintiffs alleging high-reversal-rate patterns, CMS rules requiring explainability. The carrier needs medical-necessity criteria that are demonstrably consistent with documented coverage policy — not "probably consistent based on training data," but provably consistent by construction.
**MAE Solution:** Applied-MA takes the carrier's coverage policy through the 9-phase pipeline: define the medical-necessity criteria, validate with medical directors, prove each criterion holds the property of being a faithful translation of the policy, embed the proven code in the carrier's coverage adjudication system.
**Key Value:** The nH Predict-class exposure becomes architecturally bounded. The carrier owns the code, the proofs, and the build process. No SMARTHAUS runtime in production; no vendor-lock-in. The auditor verifies the proof on open-source toolchain.

### 2. Eligibility and Benefits Determination
**Directory:** `02_eligibility_benefits/`
**Problem:** Government benefits programs (Medicaid, SNAP, housing vouchers), insurance claims systems, and lending eligibility platforms run high-stakes determination workflows where errors cascade into legal exposure, regulatory penalties, and harm to vulnerable populations. The decision logic is complex; the existing implementation evolved over years; nobody can demonstrate it correctly implements the policy.
**MAE Solution:** Applied-MA reverse-engineers the existing decision logic, formalizes the policy in mathematical notation, proves the implementation matches the policy (or identifies where it does not), produces an embedded version of the proven logic that ships back into the customer's existing system.
**Key Value:** The customer's existing decision system is replaced by a proven version that demonstrably implements the policy. Litigation and regulatory exposure tied to incorrect implementation drops. Independent re-verifiability is built in.

### 3. Regulatory Disclosure and Submission Generation
**Directory:** `03_disclosure_submission/`
**Problem:** Financial institutions, healthcare organizations, and pharmaceutical companies generate enormous volumes of regulatory disclosures, submissions, and filings (Reg Z lending disclosures, GDPR data-subject responses, FDA labeling, capital adequacy reports, EU AI Act conformity assessments). Manual generation is expensive and error-prone; AI generation is fast but lacks proof of regulatory compliance. The penalty for incorrect disclosure can be material.
**MAE Solution:** Applied-MA takes the disclosure or submission template through the 9-phase pipeline: define the regulatory requirements, prove the generation logic produces only outputs that satisfy the requirements, embed the proven generator in the customer's existing workflow.
**Key Value:** Every disclosure or submission the customer ships under MAE-generated logic carries a mathematical guarantee of regulatory compliance with the specific rules cited. The compliance team's posture moves from "we sample-check generation quality" to "the generation cannot produce non-compliant output by construction."

### 4. Capital, KYC, and AML Calculations with Regulatory Boundaries
**Directory:** `04_capital_kyc_aml_calculations/`
**Problem:** Banks running capital adequacy calculations, customer-identity verification, and AML risk-scoring face bank-grade examination of the calculation logic. Examiners want evidence that the calculations correctly implement the regulatory formula, that calculation behavior has not drifted from approval, and that any specific calculation result is reproducible and verifiable.
**MAE Solution:** Applied-MA formalizes the regulatory calculation in mathematical notation, proves the implementation correctly implements the formula, produces an embedded version of the proven calculator that ships into the customer's capital, KYC, or AML platform.
**Key Value:** The bank's calculation evidence moves from "the implementation matches the spec — trust us" to "here is the mathematical proof that the implementation matches the spec — verify it yourself on open-source toolchain." Examination cycles shorten; regulatory capital posture strengthens.

## Quick Comparison

| Use Case | Primary MAE Feature | Key Differentiator | Enterprise Value |
|---|---|---|---|
| Medical-Necessity Logic | Proven coverage criteria | nH-Predict-class exposure bounded | Litigation defensibility; CMS, FDA, state compliance |
| Eligibility Determination | Proven implementation of policy | Policy-to-code provable correspondence | Reduced litigation risk; vulnerable-population protection |
| Disclosure Generation | Proven regulatory compliance | Generation cannot produce non-compliant output | Compliance cost reduction; penalty exposure narrowed |
| Capital/KYC/AML Calculations | Proven regulatory formula implementation | Independent re-verifiability of calculation | SR 26-2 alignment; faster examinations |

## Common MAE Capabilities Used

Every MAE use case shares the same underlying capabilities:

- **9-phase Mathematical Autopsy pipeline** — define, validate, prove, convert, notebook, extract, sign, deploy.
- **Lean 4 proof artifacts** — formal proofs that the implementation has specific properties, verifiable on open-source toolchain.
- **Embedded code, customer-owned** — the proven code is the customer's binary; no SMARTHAUS runtime in production.
- **Independent verifiability** — auditor, regulator, plaintiff, or court can re-verify the proof without trusting SMARTHAUS or the customer.
- **Policy-to-proof traceability** — every proven property traces to a specific clause in the customer's documented policy.
- **CI-bound build discipline** — no proven code ships unless every proof gate is green.

## The Applied-MA Engagement Shape

Applied-MA is the engagement model that delivers MAE-built capabilities. Typical structure:

- **Specify (2 weeks):** Customer subject-matter experts define what the capability must do, must never do, and must guarantee. SMARTHAUS translates into formal statements the experts approve.
- **Prove (4 weeks):** AI-assisted proof tool drafts proofs that each rule holds. A separate program checks every line. Nothing ships without verified proof.
- **Compile (2 weeks):** The proven rules become code embedded directly inside the customer's application.

The customer owns the result entirely — source code, proofs, and build process belong to them. There is no recurring SMARTHAUS runtime license on the production deployment. Optional MA Assurance retainer for ongoing co-evolution and re-proof as policies change.

## How to Engage

Applied-MA engagements run 8 weeks fixed-scope, with three tiers based on workload complexity. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with the high-stakes capability you want to bring under Mathematical Autopsy discipline.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
