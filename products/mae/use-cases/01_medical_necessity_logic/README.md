# Use Case 1: Medical-Necessity Logic in Payer Adjudication Systems

**The nH Predict pattern, done correctly — proven coverage criteria embedded in the carrier's own software**

## The Real Problem: When the AI Denies and Nobody Can Defend the Denial

It is 2026. A federal court in Minnesota has compelled a major Medicare Advantage carrier to produce the AI behind its nursing-facility coverage decisions. The discovery order names the algorithm, the medical-necessity criteria it implements, and the per-patient evidence of conformance. The carrier's general counsel reads the order. The carrier has model cards. It has validation studies. It has clinical-team-developed criteria documents. What it cannot produce — what no carrier in the industry can produce today — is a mathematical proof that the implementation in production code correctly translates the carrier's documented medical-necessity criteria into a decision.

The plaintiffs allege the algorithm overrode physician recommendations and denied coverage at roughly 90% reversal-on-appeal rates. The carrier's defense rests on the criteria being clinically appropriate, on the validation studies showing the algorithm performs adequately in aggregate, and on the human-review override mechanism. None of this answers the discovery question: prove the *implementation* of the *documented criteria* in *production code* correctly reflects the carrier's stated coverage policy. Without that proof, the gap between policy and implementation becomes the legal theory of the case.

**The current reality:** This is the post-nH-Predict litigation environment. Every health insurer running AI in coverage determinations is exposed to the same structural question. The defense available today — model cards, validation reports, override logs — does not answer it. The defense required tomorrow — mathematical proof that the implementation correctly implements the policy — does not yet exist in any production health-insurance carrier's stack.

**The hidden cost:** Beyond the litigation cost, the carrier's coverage operations are constrained. New AI capabilities cannot deploy because clinical-affairs and legal cannot defend them. Existing AI capabilities operate under elevated scrutiny. Settlement reserves grow. The carrier's posture moves from offensive (using AI to make coverage decisions consistent and explainable) to defensive (using AI minimally and absorbing the inconsistency cost of manual processes).

## Why Traditional Systems Fail

### "We Validated the Algorithm" Is Aggregate Evidence

Validation studies (TRIPOD-AI, CONSORT-AI, FDA SaMD validation) demonstrate the algorithm performs adequately in aggregate. They do not demonstrate that the production implementation correctly translates the carrier's documented coverage criteria. A validated algorithm whose code drifts from the spec it validates against can pass validation and fail conformance.

**The mathematical reality:** Validation tests sampled behavior. Mathematical proof of conformance tests the implementation against the specification universally. The two evidence types serve different purposes; the latter is what discovery in 2026 is asking for.

### Code Reviews Are Human Pattern-Matching

The standard engineering process — pull request reviews, design reviews, clinical-team sign-off — is human pattern-matching. Skilled humans catch many implementation drifts; they do not catch all of them; nobody can prove they caught the relevant ones. The reviewer's signature on the PR is not evidence that the implementation conforms to the spec under all inputs.

**The organizational cost:** Clinical-affairs teams spend large fractions of their time reviewing implementation choices made by engineering teams who do not have the clinical context to know whether the implementation matches the carrier's medical-necessity intent. Reviews ship anyway because the alternative is paralysis. The drift between policy and implementation accumulates.

### Vendor Validation Does Not Transfer to In-House Workflow

When the carrier licenses a vendor coverage-determination AI (vendor-developed nH Predict and competitors), the vendor's validation evidence covers the vendor's claims. The carrier's specific coverage policy may differ from the vendor's documentation. The carrier's downstream workflow — how the AI recommendation flows to dispositioners and clinicians — is not covered by vendor validation. The gap between vendor evidence and carrier operations is the gap discovery exploits.

### Override Logs Show Workflow, Not Conformance

The carrier's evidence that "humans can override the AI" is workflow evidence. It does not show whether the AI's recommendations conform to the carrier's coverage criteria for the cases that are not overridden. When override rates are low (typically 5-15%), the AI is making the decision in 85-95% of cases. The conformance evidence for those decisions is missing.

## Current Solutions: Validation Studies, Clinical Governance, and Vendor Reliance

### How the Market Currently Handles This

Four approaches dominate today:

1. **Pre-deployment validation studies** (TRIPOD-AI, CONSORT-AI, FDA SaMD validation) — Aggregate evidence of model performance.
2. **Clinical governance committees** — Periodic review of AI behavior and recommendation patterns.
3. **Vendor-provided validation** (vendor white papers, vendor model cards, vendor compliance attestations) — Vendor's claims about model behavior.
4. **In-house coverage policy documentation** — The carrier's documented medical-necessity criteria, maintained in policy databases.

**What this provides:**
- Validation studies establish baseline performance.
- Clinical governance reviews aggregate behavior.
- Vendor evidence supports vendor model use.
- Documented criteria define what the carrier intends.

### Why These Solutions Fall Short

**1. Validation Studies Are Pre-Deployment Aggregate Evidence**
They do not demonstrate post-deployment conformance, do not prove the code matches the spec, and do not provide per-decision evidence.

**2. Clinical Governance Reviews Are Periodic**
Quarterly or annual review of aggregate AI behavior cannot catch per-decision conformance failures in real time. The drift between policy and implementation accumulates between reviews.

**3. Vendor Validation Does Not Cover Carrier Customization**
Every carrier customizes coverage policy. Vendor validation does not cover the customer's customizations. The gap between vendor claims and carrier implementation is the legal exposure.

**4. Documented Criteria Are Inputs to Validation, Not Evidence of Conformance**
Having the policy documented is necessary but not sufficient. The question is whether the implementation faithfully translates the policy — and the documentation does not answer this question.

**5. None Produce Mathematical Proof of Implementation Conformance**
No combination of the above produces the artifact that 2026 discovery is converging on: a formal, machine-checkable proof that the production code correctly implements the documented medical-necessity policy.

## How MAE Is Different

**1. Mathematical Proof of Policy-to-Code Conformance**
MAE produces formal proofs that the implementation correctly implements the documented medical-necessity policy. The proof is machine-checkable on open-source toolchain (Lean 4). The plaintiff, the FDA, the CMS reviewer, and the state insurance examiner can all verify the proof independently.

**2. The Carrier Owns the Result**
Applied-MA delivers the proven code, the proofs, and the build process as deliverables. The carrier owns them outright. No SMARTHAUS runtime in production. No vendor-lock-in. The vendor-AI gap (what the vendor proved vs. what the carrier deploys) is eliminated by carrier ownership.

**3. The Implementation Is the Specification**
Under MAE, the production code IS the proven implementation of the policy. There is no drift between policy and implementation, because the proof artifact binds them. Changes to either trigger re-proof; un-reproven changes do not ship.

**4. Per-Decision Conformance Is Architectural**
Because the implementation is proven to conform to the policy, every decision the implementation produces is — by construction — a faithful application of the policy. Per-decision conformance evidence is the proof itself, applied universally.

**5. The Lokken-Class Litigation Defense Becomes Affirmative**
The defense moves from "we believe the implementation correctly implements the policy" to "here is the mathematical proof that the implementation correctly implements the policy; verify it yourself." This is the structural shift in litigation posture.

**6. The Carrier's Coverage Policy Stays Authoritative**
The carrier's clinical-affairs team continues to define the medical-necessity policy. Applied-MA translates the policy into formal specifications and proves the implementation conforms. The clinical authority does not move; the proof of correct implementation becomes available.

**7. CMS, FDA, and State AI Health Regulation Compliance**
The MAE proof artifact is the format CMS coverage rules, FDA SaMD guidance, and state-level AI health regulations are converging on as the expected evidence shape. Carriers operating with MAE-built coverage logic are ahead of the regulatory curve.

## The MAE Solution: Proven Coverage Criteria, Carrier-Owned

### What If the Coverage Adjudication Code Carried Its Own Proof?

Imagine a coverage-determination system where the production code that implements medical-necessity criteria ships with a formal mathematical proof that the code correctly implements the documented policy. The proof is part of the deliverable. When the plaintiff's expert challenges a denial, the expert can examine the proof — running it independently on Lean 4 — to verify that the implementation faithfully reflects the carrier's stated policy. The defense is structural: the implementation cannot diverge from the policy because the proof binding them is part of the build.

This is MAE applied to medical-necessity adjudication. The implementation drift that creates the legal exposure is the architectural problem MAE solves.

### The Applied-MA Engagement

For medical-necessity logic, Applied-MA follows the 8-week engagement structure:

**Specify (2 weeks).** The carrier's clinical-affairs subject-matter experts define the medical-necessity criteria precisely. SMARTHAUS translates the criteria into formal specifications in Lean 4. The clinical-affairs team reviews the formal specs and confirms they accurately capture the policy. Common patterns: criteria with case logic ("if X and Y, then Z"), criteria with quantitative thresholds ("LOS > threshold"), criteria with clinical-judgment hooks ("requires physician concurrence"), criteria with regulatory deference ("per CMS LCD").

**Prove (4 weeks).** SMARTHAUS uses Lean 4 (with AI-assisted proof construction) to prove each criterion holds the property of correctly implementing the carrier's stated policy. A separate program checks every line of every proof. Counterexamples surface implementation gaps; the team iterates. Output: a complete set of Lean 4 proofs, each tied to a specific policy criterion.

**Compile (2 weeks).** The proven specifications generate executable code (target language: the customer's application stack — typically TypeScript, Python, or Rust). The generated code preserves the proof property: a verifier can confirm that the executable produces outputs consistent with the proven specifications. The code embeds in the customer's coverage-adjudication system.

### Proof-Bound Production Code

The production code is structured so the proof artifact and the executable are linked:

```
// Generated under Applied-MA proof PL-2026-04-22
// Proof artifact: lean_proofs/medical_necessity_v3.lean
// Verified property: complies with Coverage_Policy_v4.2

@proven(spec="MedicalNecessity.policy_v4_2")
function determine_post_acute_coverage(patient: PatientContext): CoverageDecision {
  // ... generated code ...
}
```

The `@proven` annotation is not a comment; it is a link to the Lean 4 proof. Build-time verification confirms the executable's behavior matches the proof. Runtime invocations carry metadata referencing the proof artifact ID.

### Open-Source Replay and Verification

The carrier ships the proof artifacts alongside the executable. Plaintiff's experts, FDA reviewers, CMS auditors, and state insurance examiners can install Lean 4 (open-source), download the proof artifacts, and verify the proofs independently. The carrier does not need to provide any infrastructure; the verification runs on the verifier's hardware.

### Policy Evolution and Re-Proof

When the carrier updates the medical-necessity policy (which happens routinely), the proof must be re-derived. The MA Assurance retainer (optional, monthly) supports this co-evolution: clinical-affairs documents the policy change, the proof is updated, the new proven code ships. The re-proof cycle is faster than the original engagement because the proof scaffolding is already established.

## Real-World Impact: The Numbers That Matter

### For Litigation

**Defense Posture:** Class actions alleging systemic coverage-denial problems shift from "the carrier cannot prove its implementation matches its policy" to "the carrier can prove — and the plaintiff can verify — that the implementation matches the policy." The defense moves from testimonial to evidentiary.

**Discovery Response Time:** Median time from court order to delivered conformance evidence drops from months to days. The proof artifacts are the evidence.

**Settlement Economics:** Cases that previously settled on the inability-to-prove penalty now settle on actual exposure — typically materially lower.

### For Compliance

**CMS Coverage Determination Reviews:** CMS oversight of Medicare Advantage coverage decisions is increasingly focused on the AI layer. Carriers producing proof of policy-conformance can answer CMS inquiries directly with proof artifacts.

**FDA SaMD Post-Market Surveillance:** For FDA-cleared coverage-AI components, MAE proofs provide post-market evidence that the implementation continues to conform to the cleared specification.

**State AI Health Regulation:** State regulations adopting NAIC-aligned AI principles for health insurance increasingly require evidence of policy-to-implementation conformance. MAE produces it.

### For Operations

**Clinical-Affairs and Engineering Collaboration:** The structural disconnect between clinical-affairs (owns policy) and engineering (owns implementation) is mediated by Applied-MA: clinical-affairs defines, SMARTHAUS formalizes and proves, engineering deploys. The drift between intent and execution narrows.

**Faster New-Product Launches:** New coverage products previously gated by "we can't defend the AI" can launch under MAE proven logic. Time-to-market compresses.

**Talent Retention:** Clinical-affairs and engineering teams operate with clearer roles and verifiable outcomes. The collaboration stops being adversarial.

## The Architecture: How It Works

### The Specify Phase

Clinical-affairs subject-matter experts work with SMARTHAUS to translate medical-necessity criteria into formal specifications. Common output: Lean 4 specification files defining the criteria as mathematical propositions over typed patient-context structures.

### The Prove Phase

SMARTHAUS proof engineers, supported by AI-assisted proof construction (e.g., Leanstral or similar), prove each specification holds. Proofs are checked by Lean 4's kernel — a small, audited piece of trusted code. Counterexamples produced during proof construction reveal specification ambiguity; the team iterates with clinical-affairs to disambiguate.

### The Compile Phase

The proven specifications generate executable code in the customer's target language. The generation preserves the proof property: the executable's behavior is provably consistent with the specification. Generated code includes structured metadata linking to the proof artifact IDs.

### The Deployment

The customer's engineering team integrates the generated code into the coverage-adjudication system. The integration is straightforward — the generated code is a normal library in the customer's language stack. No SMARTHAUS runtime is added to production; the customer owns the binary.

### The Verification Surface

Proof artifacts are committed to the customer's repository. Verification is a make-target away: `make verify-proofs` runs Lean 4 against all proof artifacts and confirms they check. External parties (plaintiff experts, regulators) install Lean 4 themselves and run the same verification.

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The Lokken-Class Discovery

**The Situation:** A federal court orders the carrier to produce per-patient evidence of AI conformance with documented coverage policy for 3,200 class members.

**Before MAE:** The carrier produces model cards, validation studies, and per-decision audit logs. The plaintiffs argue (correctly) that none of this evidence demonstrates the implementation correctly implements the documented policy. The court orders production of source code; the plaintiffs' experts review the code; ambiguities and apparent divergences between code and policy become the basis for adverse findings.

**With MAE:** The carrier produces the proof artifacts. Plaintiffs' experts install Lean 4 and verify the proofs. The proofs demonstrate the implementation conforms to the documented coverage policy for every input the policy covers. The discovery question is structurally answered: the implementation cannot diverge from the policy without breaking the proof. The case proceeds on whether the policy itself is consistent with statutory and regulatory requirements — which is a different (and narrower) legal theory.

**The Impact:** Discovery costs collapse. Settlement reflects actual policy-related exposure rather than implementation-uncertainty exposure.

### Scenario 2: The CMS Audit

**The Situation:** CMS conducts a Medicare Advantage program audit including review of AI-driven coverage decisions. The audit team requests evidence that the carrier's AI implements coverage criteria consistent with the carrier's filed coverage documentation.

**Before MAE:** The carrier produces aggregate evidence and per-decision audit logs. The audit team finds inadequate evidence of policy-to-implementation conformance. The audit issues findings requiring the carrier to develop conformance evidence infrastructure. The remediation period extends 12-18 months.

**With MAE:** The carrier produces the proof artifacts. CMS auditors verify the proofs on CMS hardware. The audit closes on policy-to-implementation conformance without findings. The carrier's MA Star Rating and CMS relationship strengthen.

**The Impact:** CMS compliance posture moves from defensive to proactive. The carrier becomes a model the CMS holds up to peers.

### Scenario 3: The New Coverage Product

**The Situation:** The carrier wants to launch a new AI-assisted coverage product in a regulated line. Clinical-affairs has the policy. Legal is concerned about post-Lokken exposure. Engineering can build it but cannot defend it.

**Before MAE:** The product is delayed pending resolution of the defensibility concern. The competing carrier launches first. The market share opportunity is lost.

**With MAE:** Applied-MA delivers the proven coverage logic in 8 weeks. The product launches with structural defensibility. Clinical-affairs, legal, and engineering all sign off because the proof gives each team what they need: clinical-affairs gets implementation faithful to policy; legal gets defensible documentation; engineering gets generated code they can integrate cleanly.

**The Impact:** The carrier captures the market opportunity. The competing carrier — operating without MAE — either follows (incurring the same engagement) or absorbs the disadvantage of slower defensible product launches.

## Key Metrics & KPIs: Measuring What Matters

### Conformance Metrics

- **Proof Coverage:** Percentage of medical-necessity criteria covered by Lean 4 proof artifacts.
  - **Target:** 100% within the engagement scope.
  - **Impact:** Policy-to-implementation drift is structurally bounded.

- **Verification Time:** Time required to verify all proof artifacts on customer infrastructure.
  - **Target:** ≤ 60 minutes for a typical coverage-determination engagement.
  - **Impact:** Verification is operationally routine, not a forensic project.

- **Re-Proof Cycle Time:** Median time from policy change to updated proven code.
  - **Target:** ≤ 4 weeks for typical policy updates under MA Assurance retainer.
  - **Impact:** Policy evolution does not stall product velocity.

### Litigation and Compliance Metrics

- **Discovery Response Time:** Median time from court order to delivered conformance evidence.
  - **Target:** ≤ 5 business days.
  - **Impact:** Discovery posture collapses.

- **CMS and State Audit Closure Rate:** Percentage of policy-to-implementation conformance audits closing without findings.
  - **Target:** ≥ 95%.
  - **Impact:** Regulatory capital compounds.

- **Settlement Cost Per Class Member:** Cost per affected class member in resolved litigation.
  - **Target:** Materially lower vs. industry baseline for non-MAE carriers.
  - **Impact:** Litigation reserves reduce.

### Operations Metrics

- **Time to New Coverage Product Launch:** Median time from product concept to defensible AI deployment.
  - **Target:** ≥ 40% reduction vs. pre-MAE baseline.
  - **Impact:** Product velocity accelerates.

- **Clinical-Affairs Override Rate on Engineering Implementation:** Percentage of engineering implementations that clinical-affairs requires re-work on prior to deployment.
  - **Target:** Near-zero under MAE-generated code.
  - **Impact:** Cross-team friction reduces.

## Integration Points: Fitting Into Your Workflow

### Coverage Adjudication Systems

- **Major UM/coverage platforms (Allscripts UM, MCG, InterQual):** MAE-generated code integrates as decision logic.
- **In-house coverage adjudication systems:** MAE-generated code in the customer's primary language stack.

### Policy Management

- **Carrier policy repositories:** Policy documentation → Lean 4 specs (via Applied-MA Specify phase).
- **Clinical-content vendors (Hayes, MCG, InterQual):** Vendor criteria → proven implementations of vendor criteria the carrier deploys.

### Compliance and Audit

- **CMS reporting:** Proof artifacts available for CMS audit verification.
- **FDA SaMD post-market:** Proof artifacts as conformance evidence in post-market submissions.
- **State insurance department exams:** Proof artifacts for state-level AI health regulation compliance.

### Engineering Integration

- **Customer engineering CI/CD:** Proof verification as a build gate in the customer's pipeline.
- **Issue tracking:** Policy change → proof update → code deployment as a linked workflow.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of unverified policy-to-implementation conformance is the litigation exposure of every coverage denial the carrier issues under AI assistance, the regulatory exposure under CMS and state AI health regulations, and the operational cost of clinical-affairs/engineering disputes that arise from implementation ambiguity. The cost is large, growing, and structurally tied to the carrier's reliance on AI in coverage adjudication.

### The Value of Having This

MAE turns coverage-AI from a defensibility risk into a defensibility asset. The carrier's posture moves from "we cannot prove what our AI does" to "we can prove exactly what our AI does, and the plaintiff/regulator can verify our proof." This is the structural shift that converts AI-coverage decisions from a litigation exposure into a competitive advantage.

### The Competitive Advantage

Carriers operating MAE-built coverage logic deploy AI at scale in regulated lines that other carriers cannot enter at scale. The first-mover advantage compounds in regulatory relationship, in product velocity, and in the cost-of-capital differential that flows from a defensible compliance posture.

## Learn More

- **MAE Overview:** [Mathematical Autopsy Engine README](https://github.com/SmartHausGroup/.github/blob/main/products/mae/README.md)
- **Other MAE Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/mae/use-cases/README.md)
- **The Six Failures:** [The SPECIFY Failure in Context](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **Mathematical Autopsy:** [The Build Discipline Behind MAE](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)

---

**MAE transforms medical-necessity logic in payer adjudication from a structural litigation exposure into proven, customer-owned, independently-verifiable code — the policy and the implementation provably bound to each other, with the proof part of the deliverable.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
