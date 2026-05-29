# Use Case 4: Capital, KYC, and AML Calculations with Regulatory Boundaries

**Proven implementation of bank-grade regulatory formulas — independently verifiable**

## The Real Problem: When the Examiner Asks "Prove the Calculation"

It's Wednesday morning at a regional bank. The Federal Reserve examiner is in week three of a quarterly capital adequacy examination. She has been reviewing the bank's risk-weighted assets calculation. The bank uses an internal RWA system that has been updated dozens of times across multiple regulatory transitions (Basel II, Basel III, Basel IV phase-ins). The examiner asks: prove that the implementation correctly computes RWA per the current applicable framework, for a specific portfolio segment, on a specific date.

The bank's response involves documentation, validation reports, prior examination findings, and the bank's own representation that the calculation conforms to the framework. The examiner reviews. She finds: model risk governance documentation that describes the calculation; validation evidence that the calculation passes test scenarios; nothing that constitutes a mathematical proof that the implementation correctly implements the Basel framework for all inputs the framework covers. Her finding: inadequate evidence of calculation conformance with regulatory framework.

The bank's RWA calculation is critical. It directly determines required regulatory capital. An understatement of risk-weighted assets understates required capital. The examiner's finding requires the bank to develop conformance evidence infrastructure within a defined remediation period. The work is multi-quarter and involves both engineering and model risk capacity.

**The current reality:** Bank-grade calculations under SR 26-2 and successor model-risk frameworks are increasingly examined for conformance with the underlying regulatory formula. Capital adequacy (RWA, LCR, NSFR, leverage ratio), customer-identity verification (CIP, CDD, EDD), AML risk-scoring, sanctions screening hit-evaluation, and several others all face this question. Banks demonstrating conformance with documentation, validation, and representation are operating at the bottom of the evidentiary hierarchy. Banks demonstrating conformance with mathematical proof are operating at the top.

**The hidden cost:** Beyond direct examination findings, banks operating without conformance proof face elevated model-risk capital requirements (regulators assign higher uncertainty to less-evidenced models), longer examination cycles, higher legal reserves for calculation-related litigation, and the compounding cost of every drift event that occurs between formal validation cycles.

## Why Traditional Systems Fail

### Validation Tests Sample; Conformance Requires Universal Coverage

Validation tests confirm the calculation produces correct results for the test scenarios. Regulatory formulas cover input spaces too large for exhaustive testing. The validation passes; the examiner asks about cases outside the test set; the bank cannot affirmatively answer.

**The mathematical reality:** Bank-grade calculations (RWA, LCR, NSFR) are functions over complex input spaces (portfolio composition, exposure types, counterparty types, jurisdictional considerations). Testing samples the space. Mathematical proof covers the space universally. SR 26-2's reference to "decision provenance" and "model lineage" is converging on the universal-coverage standard.

### Implementation Drift Across Regulatory Phase-Ins

Basel III phased in over years. Basel IV is phasing in now. CCAR, DFAST, CECL all impose calculation requirements that have evolved through multiple revisions. Implementation drift accumulates across phase-ins: code written for one regime gets patched for the next; the original implementer is gone; the documentation lags. The drift is rarely caught until an examination samples a calculation the implementation gets wrong.

### Vendor Risk Engines Inherit Vendor Interpretation

Major bank risk-engine vendors (FIS, Moody's, S&P Risk Engines, Wolters Kluwer OneSumX) implement regulatory formulas in their products. The vendor's interpretation reflects the vendor's read of the regulation. The bank may customize for specific jurisdiction, portfolio, or risk-management approach. Vendor validation does not cover customer customization. The customer bears responsibility for conformance of the customized calculation.

### Model Validation Is Periodic; Conformance Should Be Continuous

Model validation operates on annual or multi-year cycles. Conformance can drift continuously between validation events. The validation establishes a baseline; the operational reality drifts; the next validation finds the drift; the remediation cycle ensues. The cost of each remediation cycle, plus the regulatory exposure during the drift period, is the cumulative cost of validation-based evidence.

## Current Solutions: Vendor Engines, Validation Cycles, Internal Models, and Examination Cycles

### How the Market Currently Handles This

Four approaches dominate today:

1. **Vendor risk and regulatory calculation engines** (FIS, Moody's RiskFrontier and Origination Solutions, S&P, Wolters Kluwer OneSumX, Fenergo for KYC) — Licensed platforms with vendor-implemented calculation logic.
2. **Internal model development and validation** — Bank-developed calculation models passed through model-risk validation cycles.
3. **Regulatory governance and documentation** — Model risk management frameworks, model inventories, validation reports, governance committees.
4. **Examination response and remediation** — Reactive cycles addressing examiner findings.

**What this provides:**
- Vendor engines transfer implementation responsibility to vendors.
- Internal models support custom risk management approaches.
- Governance documentation establishes oversight structure.
- Remediation cycles address findings after they occur.

### Why These Solutions Fall Short

**1. Vendor Engines Cover Vendor Standard Configurations**
The bank's customizations and the bank's specific risk management approach are not covered by vendor validation. The bank's compliance team owns the conformance responsibility for any customization.

**2. Internal Models Inherit the Universal-Coverage Problem**
Bank-developed models pass validation on tested scenarios. The examination's "prove conformance for this specific exposure" question is not answered by aggregate validation.

**3. Documentation Describes Intent, Not Conformance**
Model risk documentation describes what the model is intended to compute. It does not prove the implementation correctly computes the intended formula.

**4. Reactive Remediation Is Expensive**
The remediation cycle after an examination finding consumes engineering and model-risk capacity, often for multiple quarters. The cost is paid in addition to any direct regulatory exposure.

**5. None Provide Mathematical Proof of Regulatory-Formula Conformance**
The structural gap is the same as the other MAE use cases: no mechanism produces a formal, verifiable proof that the bank's implementation correctly implements the documented regulatory formula.

## How MAE Is Different

**1. Mathematical Proof of Formula-to-Code Conformance**
MAE produces formal proofs that the implementation correctly computes the documented regulatory formula. Verifiable on open-source Lean 4 toolchain by the bank's model-risk team, by internal audit, and by external examiners.

**2. Bank-Owned Implementation**
Applied-MA delivers the proven calculation code to the bank. The bank owns the source, the proofs, and the build. No SMARTHAUS runtime in production.

**3. Universal Input Coverage**
The proof covers every input the regulatory formula covers — every portfolio composition, every exposure type, every counterparty, every jurisdiction. The examiner cannot find a case the proof does not address (within the scope of the regulatory framework version).

**4. Regulatory Framework Versioning**
Basel phase-ins, CCAR revisions, CECL clarifications all trigger framework versioning. The proof is bound to a framework version. Updates to the framework trigger re-proof; old calculations remain verifiable against the framework version in force at the time.

**5. Continuous Conformance, Not Periodic Validation**
The build pipeline blocks deployment of code that has not been re-proven against the current framework. Conformance is enforced continuously, not validated periodically.

**6. SR 26-2 Decision Provenance Built In**
Every calculation result the system produces traces back to the proof artifact, the framework version, the implementation version, and the specific calculation path through the formula. Decision provenance is the structure, not an add-on.

**7. Cross-Calculation Consistency**
The same underlying regulatory primitive (e.g., the credit conversion factor for off-balance-sheet items under Basel III) implements once and contributes to multiple calculation aggregates (RWA for credit risk, LCR for unutilized commitments, etc.) with provable consistency.

## The MAE Solution: Proven Calculation, Bank-Owned

### What If the Capital Calculation Came With a Proof?

Imagine a capital calculation system where the production code that computes RWA, LCR, NSFR, and leverage ratio ships with formal mathematical proofs that the code correctly implements the documented Basel formulas. When the Federal Reserve examiner asks "prove the calculation conforms to the framework," the bank produces the proof artifacts. The examiner installs Lean 4 and verifies the proofs on examiner hardware. The conformance question is answered structurally, not testimonially.

This is MAE applied to bank-grade calculations. The implementation drift that creates the regulatory exposure is the architectural problem MAE solves.

### The Applied-MA Engagement for Bank Calculations

For bank-grade calculations, Applied-MA typically follows this pattern:

**Specify (2 weeks).** Bank model-risk and quantitative-analytics teams work with SMARTHAUS to translate the regulatory framework into formal Lean 4 specifications. The specs cover the calculation formulas, the parameter values, the conditional rules, the jurisdictional variations, and the temporal versioning. The model-risk team reviews and approves.

**Reverse-Engineer (concurrent with Specify, 1-2 weeks).** SMARTHAUS analyzes the existing calculation implementation, maps it onto the formal spec, surfaces divergences for the model-risk team's review. Common patterns: implementation choices that interpret regulatory ambiguity in specific ways; implementation simplifications that approximate complex formulas; implementation drift across phase-in cycles.

**Prove (4 weeks).** SMARTHAUS proves the (corrected) implementation correctly implements the formal spec. Counterexamples produced during proof construction surface remaining implementation gaps; the team iterates. Output: a complete set of Lean 4 proofs.

**Compile (2 weeks).** The proven specifications generate executable code in the bank's target language. The generated code embeds in the bank's calculation system. The bank's engineering team integrates with surrounding infrastructure (data sources, reporting, downstream consumers).

### Universal Coverage of the Regulatory Formula

The proof covers every input the regulatory formula covers. For RWA, this means every exposure type, every counterparty type, every collateral configuration, every jurisdictional adjustment that the Basel framework specifies. The examiner's "prove conformance for this specific exposure" question has a structural answer: the implementation conforms by construction.

### Framework Versioning and Phase-Ins

Basel III phase-in dates, Basel IV transition rules, CECL implementation phase-ins all flow through MAE's framework versioning. The proof artifact carries the framework version; the calculation result carries the framework version; historical calculations remain verifiable against the version in force at the time. As phase-ins progress, the framework version updates; the spec updates; the proof is re-derived; the new calculation deploys with structural conformance to the new version.

### Continuous Conformance Enforcement

The build pipeline blocks deployment of calculation code that has not been re-proven against the current framework specification. Code drift from the proven specification cannot ship. The model-risk team's posture moves from "validate periodically and hope nothing drifts" to "the architecture prevents drift between validations."

### Independent Verification

The bank's model-risk function, internal audit, external auditors, and regulatory examiners can all install Lean 4 and verify the proofs independently. The bank's claim about its calculation conformance is verifiable, not testimonial. This is the structural shift in examination posture.

## Real-World Impact: The Numbers That Matter

### For Examination Posture

**Examination Cycle Time:** Median examination duration on calculation-conformance topics drops materially (proof verification is faster than reconstruction).

**Examination Findings Reduction:** Findings tied to calculation conformance drop to near-zero for systems under MAE governance.

**Model Risk Capital Posture:** Regulators assigning capital based on model uncertainty assign less capital to MAE-evidenced models. The capital differential is real money.

### For Operations

**Implementation Drift Detection:** Drift is detected at the deployment gate (immediately) rather than at validation cycle (months or years later).

**Phase-In Implementation Velocity:** Basel and CCAR phase-in implementations ship faster because the spec-to-proof cycle compresses the implementation effort.

**Engineering and Model-Risk Capacity:** Capacity previously consumed by remediation cycles redeploys to higher-judgment work.

### For Strategic Position

**Regulatory Relationship:** Banks operating MAE-governance have proactive relationships with primary regulators on calculation conformance. The bank moves first into the architecture the regulator is converging on.

**M&A Diligence:** Acquirers performing technical diligence on bank targets include calculation-conformance evidence as a structural diligence item.

**Insurance and Counterparty Posture:** Counterparties and insurers evaluating bank risk include calculation-evidence quality as part of structural assessment.

## The Architecture: How It Works

### The Specify and Reverse-Engineer Phase

Model-risk subject-matter experts work with SMARTHAUS to translate the regulatory framework into Lean 4 specifications. SMARTHAUS reverse-engineers the existing implementation. The two are mapped; divergences surface for the model-risk team's review.

### The Prove Phase

SMARTHAUS proves the implementation correctly implements the formal spec. Proofs are committed to the bank's repository.

### The Compile and Integrate Phase

Proven specifications generate executable code in the bank's primary language. The bank's engineering team integrates with calculation infrastructure (data sources, reporting, downstream consumers).

### The Continuous-Conformance Pipeline

The build pipeline enforces the re-prove gate on every change. Framework updates → spec updates → re-prove → re-generate → re-validate → deploy.

### The Verification Surface

Model-risk, internal audit, external auditors, and regulatory examiners verify proofs independently using open-source Lean 4. The bank's compliance documentation includes proof artifacts as the evidence baseline.

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The RWA Examination

**The Situation:** The Federal Reserve examiner from the opening scenario asks for proof that the bank's RWA implementation conforms to Basel framework.

**Before MAE:** The bank produces validation evidence and documentation. The examiner finds inadequate evidence of conformance; the finding requires conformance-evidence infrastructure within a defined remediation period; multi-quarter remediation ensues.

**With MAE:** The bank produces the proof artifacts. The examiner installs Lean 4 and verifies the proofs on examiner hardware. Conformance is demonstrated. The examination closes on schedule without an MRA on calculation conformance.

**The Impact:** The structural conformance posture is in place before the examination. The examination capital compounds — subsequent examinations build on the trust established here.

### Scenario 2: The Basel IV Phase-In

**The Situation:** Basel IV phase-in requires the bank to update RWA calculations for credit-risk operational-risk components by specified dates. The update involves new conditional logic, new parameter values, and revised aggregations.

**Before MAE:** The bank engineering team plans 9 months of implementation. The model-risk team plans 6 months of post-implementation validation. The implementation ships under the standard testing-confidence; future examinations will discover any drift.

**With MAE:** The model-risk team updates the formal spec for Basel IV requirements. The implementation is regenerated where the changes are mechanical; manually modified where the changes require structural revision. Proofs are re-derived. The change ships in 4 months with structural conformance to Basel IV. Subsequent examinations verify the proofs; no Basel IV-related findings.

**The Impact:** Phase-in implementation cycle time halves. The bank stays ahead of regulatory phase-ins rather than behind.

### Scenario 3: The KYC Customer Risk-Scoring

**The Situation:** The bank's KYC customer risk-scoring system has been updated across multiple BSA/AML regime updates. An examiner asks for proof that the risk-scoring correctly implements the bank's documented CDD/EDD criteria for a sample of 400 customers across risk classes.

**Before MAE:** The bank produces documentation and validation evidence. The examiner identifies inconsistencies in implementation across customer segments. The finding requires CDD/EDD implementation remediation across the affected segments.

**With MAE:** The bank produces the proof artifacts for the KYC risk-scoring system. The examiner verifies the proofs; the implementation correctly implements the documented CDD/EDD criteria for the full input space. The examination closes on KYC implementation conformance; the focus shifts to whether the documented criteria are themselves appropriately calibrated (a different and narrower question).

**The Impact:** KYC examination posture moves from defensive (reconstruct each customer's risk-scoring) to proactive (the structural evidence is in place). The compliance team's capacity redeploys.

## Key Metrics & KPIs: Measuring What Matters

### Conformance Metrics

- **Proof Coverage:** Percentage of regulatory calculations covered by Lean 4 proof artifacts.
  - **Target:** 100% within engagement scope.
  - **Impact:** Calculation drift architecturally bounded.

- **Continuous Conformance Detection Rate:** Percentage of attempted code drift detected and blocked at the build gate.
  - **Target:** 100%.
  - **Impact:** Validation cycle becomes confirmation, not discovery.

- **Examination Findings Rate:** Findings per examination on calculation conformance.
  - **Target:** Near-zero for systems under MAE governance.
  - **Impact:** Examination posture transforms.

### Operations Metrics

- **Phase-In Implementation Velocity:** Time from regulatory phase-in publication to deployed implementation.
  - **Target:** ≥ 50% reduction.
  - **Impact:** Bank stays ahead of regulatory evolution.

- **Remediation Cycle Cost:** Engineering and model-risk capacity consumed by post-examination remediation.
  - **Target:** ≥ 70% reduction.
  - **Impact:** Capacity redeploys to higher-value work.

- **Re-Proof Cycle Time:** Median time from regulatory framework update to deployed re-proven calculation.
  - **Target:** ≤ 8 weeks under MA Assurance retainer.
  - **Impact:** Bank stays current with regulatory framework evolution.

### Strategic Metrics

- **Model Risk Capital Posture:** Regulator-assigned capital tied to model uncertainty.
  - **Target:** Material reduction vs. pre-MAE baseline.
  - **Impact:** Real-money capital benefit.

- **Examination Capital:** Quality of relationship with primary regulators on calculation evidence.
  - **Target:** Proactive vs. defensive engagement.
  - **Impact:** Cumulative benefit across examination cycles.

## Integration Points: Fitting Into Your Workflow

### Calculation Systems

- **Capital adequacy systems (FIS, Moody's, S&P, Wolters Kluwer OneSumX, in-house):** MAE-generated code as the calculation core, vendor systems as the data integration and reporting wrapper.
- **Liquidity systems (LCR, NSFR):** Same pattern; calculation core proven, vendor wrapper continues.
- **CECL allowance systems:** Same pattern; CECL calculation proven.
- **CCAR / DFAST stress-testing:** Calculation primitives proven; scenario engines continue.

### KYC / AML Calculations

- **KYC platforms (Fenergo, Encompass, Quantexa):** Customer risk-scoring proven; platform workflow continues.
- **AML transaction-monitoring scoring:** Risk-scoring components proven (separate from the alert-disposition AI covered under SAID UC4).

### Sanctions Screening Hit Evaluation

- **Hit-evaluation logic** (alphanumeric matching, fuzzy matching, entity resolution): Proven implementation of sanctions matching rules.
- **OFAC, EU, UK, UN sanctions list interpretation:** Proven implementation of list-application rules.

### Model Risk and Audit

- **Model risk management platforms (Yields.io, ValidMind, Datatron):** Proof artifacts as evidence baseline.
- **Internal audit and external auditor workflows:** Proof verification as routine audit step.
- **Regulatory examination preparation:** Proof artifacts as examination-ready evidence.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of unverified calculation-to-formula conformance is the elevated model-risk capital, the longer examination cycles, the larger legal reserves for calculation-related litigation, and the cumulative cost of every drift event that occurs between formal validation cycles. The cost is large, growing, and structurally tied to the bank's reliance on automated regulatory calculations.

### The Value of Having This

MAE turns regulatory calculations from a perpetually-uncertain evidence base into proven, bank-owned, independently-verifiable infrastructure. The model-risk capital benefit alone is material; the examination posture benefit compounds across cycles; the operational capacity redeployment frees engineering and model-risk teams for higher-judgment work.

### The Competitive Advantage

Banks operating MAE-governance on capital and KYC calculations operate with structural regulatory advantages competitors cannot match through validation cycles. The capital differential, the examination differential, and the regulatory-relationship differential all compound in ways material to ROE.

## Learn More

- **MAE Overview:** [Mathematical Autopsy Engine README](https://github.com/SmartHausGroup/.github/blob/main/products/mae/README.md)
- **Other MAE Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/mae/use-cases/README.md)
- **The Six Failures:** [Why SR 26-2 Examinations Demand Proven Calculations](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **Mathematical Autopsy:** [The Build Discipline Behind MAE](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)

---

**MAE transforms bank-grade regulatory calculations from a validation-cycle-evidenced compliance posture into proven, bank-owned, independently-verifiable infrastructure — every RWA, LCR, NSFR, KYC, and AML calculation structurally guaranteed to conform to the documented regulatory framework, with universal input coverage and continuous conformance enforcement.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
