# Use Case 2: Eligibility and Benefits Determination

**Proven implementation of complex policy — for the systems that decide who gets what**

## The Real Problem: When the Eligibility System Has Drifted From the Statute

It's a Tuesday morning at a state Medicaid agency. The Office of the Inspector General has spent six months auditing the eligibility-determination system the state uses to adjudicate Medicaid applications. The audit findings are about to be released. The headline: roughly 4% of approved applications should have been denied, and roughly 7% of denied applications should have been approved, when measured against the state's documented Medicaid eligibility policy. The agency's IT team explains that the system was built 17 years ago, has been patched continuously, and the original developers are long gone. The policy team explains that they have updated eligibility rules approximately 340 times in the last decade. The audit explains that nobody in the agency can demonstrate the production code correctly implements the current policy.

The 4% wrong-approvals will trigger federal recoupment of approximately $87M. The 7% wrong-denials are class-action material — vulnerable populations were denied benefits they were statutorily entitled to. The agency director has 90 days to develop a remediation plan. The IT team's estimate to rebuild the eligibility system from scratch is $40M and four years.

**The current reality:** This pattern is not limited to Medicaid. SNAP eligibility, housing voucher determination, unemployment insurance, disability determinations, lending eligibility, insurance claims adjudication — every high-stakes eligibility system runs on code that has evolved over years through patches, with policy that has evolved in parallel, with no mechanism that demonstrates the code correctly implements the policy. The systems work in production because they pass functional tests; they fail when an outside auditor measures them against the documented policy.

**The hidden cost:** Beyond the immediate audit exposure, agencies and organizations running drift-prone eligibility systems face cumulative liability that grows with each policy change. Each patch is an opportunity for new drift. Each policy update widens the gap between intent and implementation. The cost is paid as remediation, recoupment, litigation, and the human cost of incorrect determinations.

## Why Traditional Systems Fail

### Functional Tests Sample; Conformance Requires Universal Coverage

Functional tests verify the system behaves correctly on the test cases the team has written. Eligibility policies are complex enough that no realistic test set covers all the cases. The system passes the tests; the audit finds the cases the tests did not cover. The gap is structural.

**The mathematical reality:** Eligibility decisions are functions over complex input spaces (applicant demographics, household composition, income sources, asset categories, jurisdictional rules). Sampling the input space with tests provides finite coverage. Mathematical proof of conformance provides universal coverage. Auditors increasingly demand the latter.

### Policy Documentation Is Prose; Code Is Executable

The eligibility policy is documented in natural-language prose — federal regulations, state implementation guidelines, internal interpretations. The code is executable logic in a programming language. The translation from prose to code is performed by developers who may or may not interpret the prose the same way the policy team intended. The translation is not proven correct; it is reviewed and accepted.

**The organizational cost:** Policy teams discover implementation drift during audits, after years of incorrect determinations have accumulated. The corrective workflow — update the spec, update the code, validate the change — happens reactively rather than preventively.

### Legacy System Rebuilds Are Multi-Year Projects

The standard answer to "the system has drifted from the policy" is "we'll rebuild it." Multi-year rebuilds cost tens of millions, miss go-live dates, and ship with the same architectural absence of policy-conformance proof that the legacy system had. The rebuild may move the implementation closer to current policy at go-live; the drift starts accumulating again immediately.

### Vendor Eligibility Engines Inherit the Vendor's Interpretation

When agencies license vendor eligibility engines (NextGen, Conduent, Maximus, Deloitte solutions), the vendor's implementation reflects the vendor's interpretation of the policy. The agency cannot easily customize without forking the vendor's logic. Vendor updates may or may not reflect changes in the agency's specific policy. The conformance gap moves from agency-developed code to vendor-developed code, but it doesn't close.

## Current Solutions: Functional Testing, Rebuilds, Vendor Reliance, and Audit Cycles

### How the Market Currently Handles This

Four approaches dominate today:

1. **Functional and regression testing** — Manual and automated test suites that exercise documented scenarios.
2. **Periodic legacy modernization projects** — Multi-year, multi-million-dollar rebuilds.
3. **Vendor eligibility engines** — Licensed platforms with vendor-developed policy implementations.
4. **Post-hoc audit and remediation cycles** — OIG, GAO, internal auditors find drift; agencies remediate.

**What this provides:**
- Testing catches the cases tested for.
- Rebuilds close some of the accumulated gap at go-live.
- Vendor engines transfer some of the implementation burden.
- Audits eventually surface drift.

### Why These Solutions Fall Short

**1. Testing Provides Sampled Coverage**
The cases not in the test set are the cases the audit will find. Test-driven development is essential; it is not sufficient for universal-coverage policy conformance.

**2. Rebuilds Are Slow and Recurrent**
A four-year rebuild ships into a policy environment that has changed materially during the rebuild. Re-drift begins immediately. The rebuild does not solve the architectural problem; it resets the drift counter at high cost.

**3. Vendor Reliance Transfers, Doesn't Eliminate**
Vendor solutions shift the implementation responsibility but not the conformance question. The agency still bears the consequence of any drift between vendor implementation and agency-specific policy.

**4. Post-Hoc Audits Find Drift After Harm**
The audit cycle is the agency's existing mechanism. Its weakness is that it operates after the wrong decisions have been made — recoupment, litigation, and harm to vulnerable populations are downstream of the audit, not prevented by it.

**5. None Produce Mathematical Proof of Policy Conformance**
The structural gap is the same: no mechanism produces a formal, verifiable proof that the implementation correctly implements the documented policy under all inputs the policy covers.

## How MAE Is Different

**1. Mathematical Proof of Policy-to-Code Conformance**
MAE produces formal proofs that the eligibility-determination code correctly implements the documented policy. Verifiable on open-source Lean 4 toolchain.

**2. Agency-Owned Implementation**
The proven code is the agency's. No vendor lock-in. No SMARTHAUS runtime in production. The agency owns the source code, the proofs, and the build process.

**3. Universal Input Coverage**
The proof covers every input the policy covers — not a sampled subset, every input. The OIG or class-action plaintiff cannot find a case the proof does not address (within the scope of the documented policy).

**4. Drift-Resistant by Construction**
Policy changes trigger re-proof. The build pipeline blocks deployment of code that has drifted from the proven policy version. Drift becomes architecturally hard to introduce.

**5. Reverse-Engineering as a Starting Point**
Applied-MA can start from the existing implementation (not just from a clean policy spec): formalize the policy, formalize the existing code, identify the gaps, propose the corrections. The agency does not need to start from scratch.

**6. The Implementation Becomes the Specification**
Under MAE, the production code IS the proven implementation. There is no separate specification document that can drift from the code. The proof binds the two; the code and the spec evolve together.

**7. Audits Move From Forensic to Routine**
OIG, GAO, federal auditors, and internal auditors verify the proofs as a routine step. The audit cycle changes character: from "find the drift" to "verify the proof and move on."

## The MAE Solution: Proven Policy Implementation, Agency-Owned

### What If the Eligibility Code Came With a Proof?

Imagine an eligibility-determination system where the production code that decides who is eligible for what ships with a formal mathematical proof that the code correctly implements the documented policy. When OIG audits the system, the audit verifies the proof — not the cases-tested-yesterday, the universal coverage of the proof. When policy changes, the code change ships only when the new proof is green. When a class-action plaintiff challenges a denial, the agency produces the proof showing the implementation matches the policy; the question shifts to whether the policy itself is correct.

This is MAE applied to eligibility determination. The decades of implementation drift that audits find are the architectural problem MAE solves.

### The Applied-MA Engagement for Eligibility

For eligibility-determination systems, Applied-MA typically follows this pattern:

**Specify (2 weeks).** The agency's policy team works with SMARTHAUS to translate the eligibility policy into formal Lean 4 specifications. The specs cover the case logic, threshold tests, exclusions, exceptions, and special-case provisions in the policy. The policy team reviews and approves the formal specs.

**Reverse-Engineer (concurrent with Specify, 1-2 weeks).** SMARTHAUS analyzes the existing implementation, identifies the implementation's logic, and maps it onto the formal spec. Gaps and divergences are surfaced for the policy team's review: *the implementation does X; the policy says Y; which is intended?*

**Prove (4 weeks).** SMARTHAUS proves the (corrected) implementation correctly implements the formal spec. Counterexamples found during proof construction surface remaining implementation gaps; the team iterates. Output: a complete set of proofs tying the implementation to the policy.

**Compile (2 weeks).** The proven specifications generate executable code in the agency's target language. The generated code replaces (or augments) the legacy implementation. Integration with the surrounding eligibility-determination system (data inputs, downstream notifications, case-management workflow) is performed by the agency's engineering team.

### Drift Prevention

The build pipeline blocks deployment of code that does not pass the proof. Routine policy changes follow the workflow: update the formal spec, update the implementation (or regenerate from spec), verify the proof, deploy. The proof step is automatic in CI. A policy change cannot ship as code without a corresponding proof update.

### Agency Ownership

Applied-MA delivers the proven code, the proof artifacts, the build configuration, and the documentation as deliverables. The agency owns them. No SMARTHAUS runtime is added to production. The agency's IT team maintains the system; the MA Assurance retainer (optional) provides ongoing proof-support and re-proof for policy changes.

### Independent Verifiability

Auditors, plaintiffs, advocates, and the public (where appropriate) can install Lean 4 and verify the proofs. The agency's claim that the implementation conforms to the documented policy is verifiable, not testimonial. This is the structural shift in audit and litigation posture.

## Real-World Impact: The Numbers That Matter

### For Audit and Compliance

**Drift Detection Rate:** Drift between policy and implementation is detected at the policy-change step (immediately), not at the audit step (months or years later).

**Audit Findings Reduction:** Audit findings tied to policy-implementation drift drop to near-zero for systems under MAE governance.

**Recoupment Exposure:** Federal recoupment exposure tied to incorrect eligibility determinations narrows. The agency can demonstrate conformance; recoupment based on "your system was wrong" does not apply.

### For Operations

**Time to Implement Policy Changes:** Policy update → code deployment cycle compresses. The formal spec is updated, the implementation is generated or modified, the proof is verified, the change deploys. Routine.

**Reduced Litigation Risk:** Class actions alleging systemic incorrect determinations are answered with proof evidence. The structural defense is in place before the litigation arrives.

**Legacy Modernization Avoided:** The multi-year, multi-million-dollar legacy rebuild is replaced by an 8-week Applied-MA engagement plus integration work. Total cost is materially lower.

### For Beneficiaries and Stakeholders

**Determination Accuracy:** Beneficiaries receive correct determinations consistent with the documented policy. The 4%/7% drift class disappears for the categories under MAE governance.

**Appeal Volume Reduction:** Appeals tied to incorrect determinations drop materially. The agency's appeal-processing capacity stretches.

**Public Trust:** The agency can demonstrate to the public, the legislature, and federal oversight that the system implements policy correctly — and provide the proof for independent verification.

## The Architecture: How It Works

### The Specify and Reverse-Engineer Phase

SMARTHAUS works with the policy team to translate documented policy into formal Lean 4 specifications. Concurrently, SMARTHAUS analyzes the existing implementation and maps it onto the spec. Gaps surface for the policy team's review.

### The Prove Phase

SMARTHAUS proves the (corrected) implementation correctly implements the formal spec. Lean 4 proof artifacts are committed to the agency's repository. The proof kernel is small, audited, and open-source.

### The Compile and Integrate Phase

The proven specifications generate executable code in the agency's target language (typically TypeScript, Python, Java, or .NET). The agency's engineering team integrates the generated code into the existing eligibility-determination system.

### The Ongoing Operation

Policy changes follow the cycle: update spec, update implementation (or regenerate), verify proof, deploy. The build pipeline enforces the verify-proof gate. MA Assurance retainer (optional, monthly) supports the ongoing co-evolution.

### The Audit Surface

Auditors install Lean 4 and verify the proof artifacts. Verification typically takes minutes. The audit's question shifts from "find the drift" to "verify the proof; verify the policy interpretation is correct."

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The OIG Eligibility Audit

**The Situation:** OIG audits the state's Medicaid eligibility-determination system and finds 4% wrong-approvals and 7% wrong-denials against the documented policy.

**Before MAE:** The agency faces $87M in recoupment and a class-action exposure. The remediation plan is a multi-year rebuild costing $40M.

**With MAE:** The agency has run Applied-MA on the eligibility system over the previous year. Proof artifacts demonstrate the implementation conforms to the documented policy. OIG's audit verifies the proofs and finds no drift class — the 4%/7% figures from peer-state audits do not apply because the architecture prevents the drift. The recoupment exposure does not materialize. The class-action material does not exist.

**The Impact:** A $127M+ exposure (recoupment + remediation) becomes a routine compliance posture. The agency's relationship with OIG and CMS strengthens.

### Scenario 2: The Class-Action Lawsuit on Wrong-Denials

**The Situation:** Legal-aid advocates file a class action alleging the agency's eligibility system denied benefits to thousands of statutorily-entitled applicants. The discovery names specific applicants and asks for evidence that the denials conformed to the documented eligibility policy.

**Before MAE:** The agency produces source code, policy documents, and per-decision logs. The advocates' expert witnesses identify divergences between policy and implementation. The court finds the agency's defense inadequate. The settlement includes back-benefits for the class plus ongoing federal monitoring.

**With MAE:** The agency produces the proof artifacts. The advocates' experts verify the proofs and confirm the implementation conforms to the documented policy. The class-action argument shifts from "the system implemented the policy incorrectly" to "the policy itself was incorrect" — a different (and narrower) legal theory. Where the implementation conformed and the policy was the issue, the case proceeds on policy reform; the agency's implementation is not the failure.

**The Impact:** Litigation posture shifts to actual exposure rather than implementation-uncertainty exposure. Where the policy itself was the issue, the case becomes a policy-reform vehicle rather than an implementation-fault settlement.

### Scenario 3: The New Federal Policy Implementation

**The Situation:** CMS issues new federal Medicaid policy requirements that states must implement within 12 months. The agency must update its eligibility-determination system to reflect the new rules.

**Before MAE:** The implementation requires updates across multiple subsystems. The agency's engineering team plans 9 months of work, tests, and validation. The implementation ships with the standard testing-based confidence; CMS audits in year 2 may find drift.

**With MAE:** The policy team updates the formal spec. The implementation is regenerated where the changes are mechanical; manually modified where the changes require structural revision. Proofs are re-derived. The change ships in 4 months with structural conformance evidence. CMS audits in year 2 verify the proofs; no drift findings.

**The Impact:** Policy implementation cycle time halves. The agency stays ahead of federal policy changes rather than behind. CMS relationship strengthens.

## Key Metrics & KPIs: Measuring What Matters

### Conformance Metrics

- **Proof Coverage:** Percentage of eligibility-determination logic covered by Lean 4 proof artifacts.
  - **Target:** 100% within the engagement scope.
  - **Impact:** Drift is structurally bounded.

- **Re-Proof Cycle Time:** Median time from policy change to deployed proven code.
  - **Target:** ≤ 8 weeks for routine policy updates under MA Assurance retainer.
  - **Impact:** Policy implementation velocity accelerates.

- **Audit Finding Rate:** Findings per audit tied to policy-implementation drift.
  - **Target:** Near-zero for systems under MAE governance.
  - **Impact:** Audit cycle posture transforms.

### Operations Metrics

- **Determination Accuracy:** Percentage of determinations consistent with documented policy.
  - **Target:** ≥ 99.5% (vs. typical 93-96% for legacy systems).
  - **Impact:** Beneficiary harm and recoupment exposure drop.

- **Appeal Volume:** Number of appeals tied to determination errors.
  - **Target:** ≥ 30% reduction post-MAE deployment.
  - **Impact:** Appeal-processing capacity stretches.

- **Policy Implementation Cycle Time:** Median time from policy change publication to deployed implementation.
  - **Target:** ≥ 50% reduction vs. pre-MAE baseline.
  - **Impact:** Agency stays current with federal and state policy evolution.

### Strategic Metrics

- **Total Cost of Eligibility Modernization:** Total cost of moving from legacy to MAE-governed eligibility.
  - **Target:** ≥ 80% reduction vs. full rebuild estimates.
  - **Impact:** Capital previously committed to multi-year rebuilds redeploys.

- **Federal Oversight Posture:** CMS, HHS, and other federal-agency relationship quality.
  - **Target:** Move from defensive to proactive engagement.
  - **Impact:** Reduced federal scrutiny and faster federal program approvals.

## Integration Points: Fitting Into Your Workflow

### Eligibility Determination Systems

- **State Medicaid Management Information Systems (MMIS):** MAE-generated code replaces or augments the eligibility-determination module.
- **SNAP, TANF, housing voucher systems:** Generated code in the system's primary language stack.
- **Vendor eligibility platforms (Conduent, Maximus, Deloitte solutions):** MAE-generated code as a customer-owned customization layer.

### Policy Management

- **Federal regulation tracking:** Policy team workflow connects federal-rule updates to spec updates.
- **State policy documentation systems:** State-specific policy interpretations feed into formal specs.
- **Internal interpretation memos:** Internal interpretations of ambiguous policy formalized in the proof spec.

### Audit and Oversight

- **OIG, GAO, internal audit:** Auditor workflow includes proof verification as a routine step.
- **Federal oversight (CMS, HHS, USDA, HUD, depending on program):** Proof artifacts provided to federal overseers.
- **State legislative oversight:** Proof artifacts available for legislative-audit inquiries.

### Engineering and CI/CD

- **Agency engineering pipelines:** Proof verification as a build gate.
- **Policy-change workflow:** Spec update → code generation → proof verification → deployment as a linked workflow.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of unverified eligibility-determination logic is the recoupment exposure of every audit cycle, the litigation exposure of every wrong-denial class action, and the cumulative harm to vulnerable populations who receive incorrect determinations under drift-affected systems. The cost is paid in dollars (recoupment, settlements, remediation projects), in regulatory relationship (federal oversight intensifies on agencies with audit findings), and in public trust (the agency's standing in its community).

### The Value of Having This

MAE turns eligibility determination from a structural drift problem into queryable, verifiable infrastructure. The proof artifact is the evidence. The agency owns the implementation. The audits become routine. The policy changes ship cleanly. The beneficiaries receive correct determinations.

### The Competitive Advantage

State agencies, federal programs, and private benefit-administration organizations that adopt MAE-governance early operate in a fundamentally different audit and litigation environment than those that wait for the next OIG audit cycle to force the move. The differentiation compounds in operational efficiency, in regulatory standing, and in public outcomes.

## Learn More

- **MAE Overview:** [Mathematical Autopsy Engine README](https://github.com/SmartHausGroup/.github/blob/main/products/mae/README.md)
- **Other MAE Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/mae/use-cases/README.md)
- **The Six Failures:** [The BIND and SPECIFY Failures in Context](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **Mathematical Autopsy:** [The Build Discipline Behind MAE](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)

---

**MAE transforms eligibility and benefits determination from a drift-prone legacy system perpetually behind documented policy into proven, agency-owned infrastructure — the policy and the implementation provably bound to each other, with the proof verifiable by any auditor, advocate, or oversight body on open-source toolchain.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
