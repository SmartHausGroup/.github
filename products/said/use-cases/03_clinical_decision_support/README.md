# Use Case 3: Clinical Decision Support and Coverage Determinations

**The same patient profile produces the same recommendation — replayable in court**

## The Real Problem: When the AI Denied Coverage and Nobody Can Prove Why

It is 2026. A federal court in Minnesota has just ordered a major health insurer to produce its post-acute coverage AI for plaintiff inspection. The discovery order names the algorithm, the model artifacts, the validation records, and the per-decision evidence. The insurer's general counsel reviews the request. The insurer has model cards. It has validation studies. It has policy documents. It has aggregate performance dashboards. What it does not have — what it cannot produce — is a per-patient, per-decision artifact that demonstrates the algorithm behaved the same way for this patient on that day as the algorithm behaves now in the laboratory environment.

The plaintiffs allege roughly 90% reversal rates on appeal of AI-driven denials. The insurer's response is structurally weak: the model "passed validation," the rate of denials "is consistent with prior years," the algorithm is "subject to clinical override." None of this answers the discovery question: prove, for this patient on August 14, that the algorithm produced the recommendation the carrier acted on, and that the same algorithm would produce the same recommendation today.

**The current reality:** This is the post-nH-Predict litigation environment. Every health insurer running AI in coverage determinations is exposed to the same discovery posture. Every clinical decision-support vendor selling AI to providers faces the same question from purchasers' counsel. The carriers and vendors that build per-decision reproducibility into the architecture from the start are in a different position from those who didn't.

**The hidden cost:** Beyond the litigation itself, the regulatory landscape is moving. The FDA AI/ML guidance (updated 2025), CMS rules on AI in Medicare Advantage coverage decisions, and state-level legislation on AI in health insurance all converge on a common requirement: the carrier must be able to demonstrate that a specific decision on a specific date was consistent with the carrier's documented practice. Non-deterministic inference cannot satisfy this requirement. The cost of not solving it is the cost of every coverage decision the carrier defends with testimony rather than evidence.

## Why Traditional Systems Fail

### Clinical AI Cannot Reproduce Its Decisions

The same architectural pattern that makes AI non-deterministic in credit and insurance applies in clinical decision support. The model output for the same patient profile varies across runs — by small amounts in average conditions, by clinically-relevant amounts in the tails. When the carrier reconstructs a six-month-old coverage denial, the reconstructed recommendation may differ from the original. The insurer cannot affirmatively prove the original decision was made by the algorithm the carrier described in its policy documentation.

**The mathematical reality:** Clinical workflows include retrieval (chart history, clinical guidelines, formulary data), sampling decisions (in models that produce ranked recommendations), and ordering effects in how clinical context is assembled. Each is a source of variance. The variance is small enough that the model's quality metrics look stable; the variance is large enough that one specific patient's recommendation could differ across runs.

### Model Cards and Validation Reports Are Aggregate Evidence

The standard regulatory evidence — model cards (Mitchell et al.), validation reports (TRIPOD, CONSORT-AI), bias audits — describe the model's behavior across populations. They do not bind a specific patient to a specific recommendation. The carrier's compliance posture is "the model behaves correctly on average"; the court's question is "prove the model behaved correctly for this patient." The aggregate evidence does not answer the per-decision question.

### Clinical Override Is Documented, Not Architectural

The standard defense is that the AI recommendation is "subject to clinical override" — a human clinician makes the final decision. In practice, override rates run low; the AI's recommendation is the action in most cases. The override mechanism is documented in policy but does not produce per-decision evidence that the override happened (or didn't). When the plaintiff asks for evidence that the override mechanism was functional for the patient in question, the carrier produces aggregate override statistics — again, not per-decision evidence.

**The organizational cost:** Clinical AI deployments operate in a posture of "we trust the validation; we have human-in-the-loop overrides." This posture worked when AI was decision support for niche workflows; it does not work in 2026 when AI is making coverage determinations affecting millions of decisions and class-action discovery is naming specific patients.

### EHR-Integrated AI Inherits the EHR's Audit Architecture

Clinical AI deployed inside Epic, Cerner, Meditech, or Athena inherits the EHR's audit logging. The EHR audit log shows the AI's recommendation, the timestamp, and the clinician's action. It does not show the AI's reasoning, the inputs to the recommendation, or evidence that the recommendation is reproducible. The EHR is the workflow system; it was not designed to be the per-decision evidence system for AI.

## Current Solutions: Model Cards, Validation Reports, Override Logs, and EHR Audits

### How the Market Currently Handles This

Four approaches dominate today:

1. **Validation and approval frameworks** (FDA SaMD AI/ML, TRIPOD-AI, CONSORT-AI) — Pre-deployment evidence that the model performs adequately.
2. **Model documentation** (Model Cards, Datasheets for Datasets, AI Use Inventories) — Static documentation of model design and behavior.
3. **EHR audit logging** (Epic, Cerner, Meditech audit trails) — Workflow-level records of AI recommendations and clinician actions.
4. **AI governance platforms in healthcare** (Holistic AI for healthcare, RegASK, Beekeeper AI) — Compliance workflow tooling.

**What this provides:**
- Validation frameworks establish baseline performance.
- Model documentation supports regulatory submission and procurement.
- EHR audit logs trace recommendations through clinician workflows.
- Governance platforms automate compliance workflows.

### Why These Solutions Fall Short

**1. Validation Is Pre-Deployment; The Question Is Per-Decision**
FDA approval and TRIPOD-AI validation establish that the model performs adequately at the time of approval. They do not bind individual deployment-time decisions to the approved model behavior. The court's question — *"prove this specific decision was made by the model you described in your approval submission"* — is not answered by approval-time validation.

**2. Model Cards Are Static; Behavior Is Dynamic**
The model card describes what the model is intended to do. The model's actual behavior on a specific input on a specific day requires per-decision evidence. The card and the per-decision evidence are different artifact types; only the latter answers discovery.

**3. EHR Audit Logs Lack Reasoning**
The Epic audit log shows the AI recommended a specific course of action. It does not show *why* the AI recommended that course of action, what inputs the recommendation considered, what the model's confidence was, or whether the model would make the same recommendation today on the same inputs.

**4. Governance Platforms Address Workflow, Not Evidence**
Compliance workflow automation routes approvals and tracks documentation. It does not produce per-decision cryptographic evidence that an outside party can verify independently.

**5. None Provide Replayable Per-Decision Envelopes**
The structural gap is the same as in credit and insurance: there is no per-decision artifact that an outside party can take to their own hardware, re-run, and verify byte-for-byte that the carrier's record of the AI's recommendation matches what the AI would produce today.

## How SAID Is Different

**1. Per-Patient Deterministic Recommendations**
SAID makes the AI's recommendation for a specific patient profile reproducible across runs. The same patient + same clinical context + same model version → same recommendation. Every time.

**2. Cryptographically Signed Per-Decision Envelopes**
Every coverage determination, every clinical recommendation produces a signed envelope. The envelope is the per-decision evidence artifact.

**3. Byte-Identical Replay on the Plaintiff's Hardware**
SAID's open-source replay tooling lets the plaintiff's expert re-derive the carrier's historical recommendation independently. The carrier's claim about what the AI did is verifiable, not testimonial.

**4. The FDA-Approved Model the Carrier Deployed, Not a Forked Version**
SAID's determinism guarantee comes from the inference architecture, not from forking the model. The FDA-approved model artifact deploys directly; the determinism is layered on top.

**5. Clinical Override Logged in the Envelope**
The envelope includes whether the recommendation was a final action or a candidate for clinician review. The override mechanism's behavior is per-decision evidence, not aggregate statistics.

**6. EHR Integration Preserves Workflow**
SAID integrates with Epic, Cerner, Meditech, and Athena through their standard AI integration APIs. The clinician workflow does not change; the envelope is generated alongside the recommendation and stored in the carrier's compliance vault.

**7. CMS, FDA, and State AI Health Regulations**
SAID envelopes are the artifact format that CMS coverage rules, FDA SaMD guidance, and state-level AI health regulations are converging on as the expected evidence shape.

## The SAID Solution: Replayable Coverage Determinations

### What If Every Coverage Decision Could Be Re-Derived in Court?

Imagine a coverage-determination workflow where every AI-driven recommendation — every prior authorization decision, every medical-necessity determination, every clinical decision-support output — ships with a cryptographically signed envelope that the plaintiff's expert can take to their laptop and re-run, producing the exact same recommendation the carrier acted on. The carrier's posture in litigation moves from defensive testimony to evidentiary demonstration. The plaintiff's allegation that the AI behaved inconsistently can be tested against verifiable artifacts.

This is SAID applied to clinical decision support. The non-determinism that undermines per-decision evidence is the architectural problem SAID solves.

### Per-Coverage-Decision Envelope

Every coverage determination generates an envelope:

```
{
  "envelope_id": "uuid",
  "timestamp": "2026-05-29T11:14:23Z",
  "decision_type": "post_acute_coverage_determination",
  "patient": {
    "patient_id_hash": "sha256:...",
    "clinical_context_hash": "sha256:..."
  },
  "model": {
    "name": "post-acute-coverage-v3",
    "version_hash": "sha256:...",
    "fda_clearance_id": "K231234"
  },
  "determinism_profile": "regulated-clinical-decision-v1",
  "input": {
    "diagnosis_codes": [...],
    "service_request_hash": "sha256:...",
    "policy_version": "post-acute-coverage-2026-q2"
  },
  "output": {
    "recommendation": "approve_with_modifications",
    "modifications": ["alternative_facility_required"],
    "rationale_codes": ["clinical_necessity_threshold_met", "alt_site_appropriate"],
    "clinician_review_required": true,
    "output_hash": "sha256:..."
  },
  "downstream_action": {
    "clinician_decision": "concur",
    "decision_timestamp": "2026-05-29T11:18:42Z",
    "decision_id": "..."
  },
  "envelope_signature": "ed25519:..."
}
```

The envelope is the artifact for litigation discovery, FDA post-market surveillance, CMS coverage review, and state insurance examination. It carries the inputs, the recommendation, the clinician action, and the cryptographic proof tying them together.

### Determinism Profile for Clinical Adjudication

The `regulated-clinical-decision-v1` profile pins every variance source: seed, sampling (greedy decoding for adjudication; controlled exceptions for clinical-summary generation), context assembly (chart sections in deterministic order), retrieval (clinical-guideline references pinned by version).

### FDA-Approved Model, Deterministic Inference

The carrier or vendor's FDA-cleared model artifact deploys directly. SAID's determinism layer wraps the inference. The model the FDA approved is the model that runs in production; the determinism guarantee comes from the inference architecture above the model.

### Clinical Override and Workflow Capture

The envelope captures the clinical override mechanism: did the recommendation flag for clinician review, did the clinician concur or override, what was the time-to-decision. This is per-decision evidence about whether the human-in-the-loop architecture functioned for the specific patient.

### Population-Level Disparity Analysis

Per-decision envelopes enable population-level analysis: are reversal rates uniform across protected-class proxy segments, do recommendation patterns differ by geography or facility type, are clinician override rates consistent. The same envelope evidence that satisfies per-decision verification also enables ongoing disparity analysis the carrier can present to regulators and to its own clinical governance committees.

## Real-World Impact: The Numbers That Matter

### For Compliance

**Discovery Response Time:** Median time from court order to delivered per-decision evidence drops from months (often impossible to produce) to days (envelope vault query + replay).

**Per-Decision Verifiability:** Every coverage determination and clinical recommendation is structurally reproducible. The carrier's evidentiary posture moves from "we have aggregate statistics" to "here is the specific decision, here is the model that made it, here is the replay tooling you can run yourself."

**FDA Post-Market Surveillance:** Reports submitted to the FDA under post-market obligations carry envelope evidence supporting performance claims. FDA reviewers can verify claims independently.

### For Risk

**Litigation Posture:** Class actions alleging systemic AI bias or systemic AI denial-rate problems are tested against verifiable per-decision evidence. Settlement economics reflect actual liability rather than the inability-to-prove penalty.

**Regulatory Penalty Exposure:** State AI health regulations carrying per-decision evidence requirements are satisfied by architecture rather than by promised process. Penalty exposure narrows.

**Reinsurance and Capital:** Reinsurers and rating agencies underwriting carriers with significant AI footprints distinguish carriers with replayable evidence. The capital-cost differential reflects the structural difference.

### For Clinical Operations

**Clinician Trust:** Clinicians who can be shown the AI's exact recommendation and the inputs that produced it trust the system more than clinicians told "the AI considered the chart." Trust drives appropriate use; lack of trust drives systematic override (which costs the AI's value) or systematic concurrence (which costs the clinical-judgment layer).

**Quality Improvement:** Per-decision evidence enables clinical quality improvement: identify recommendation patterns associated with worse outcomes, surface them for clinical-governance committee review, refine the model with envelope-based data.

**Patient Communication:** When patients ask about coverage decisions, the conversation can move from "the AI recommended this" to "here is the specific recommendation, here are the inputs, here is what would change the outcome."

## The Architecture: How It Works

### The EHR Integration

SAID integrates with Epic, Cerner, Meditech, and Athena through their AI integration APIs. The recommendation flows from SAID to the EHR; the envelope flows to the carrier's compliance vault. The clinician sees the recommendation in the workflow; the carrier holds the per-decision evidence.

### The Coverage-Determination Pipeline

For coverage determinations (prior authorization, medical necessity), SAID intercepts the AI recommendation step, generates the envelope, returns the recommendation. The downstream system (UM platform, claims system) records the clinician or systemic action. The envelope captures both.

### The Envelope Vault

Envelopes are written to the vault inside the carrier's environment. The vault is structured, signed, append-only, and portable. Compliance teams query the vault for examination evidence; legal teams export from the vault for litigation discovery; clinical-governance committees use vault analytics for quality improvement.

### The Replay Service

Open-source replay tooling reproduces any historical decision. The plaintiff's expert, the FDA reviewer, the state insurance examiner can all run the replay independently. Byte-identical match verifies the carrier's claim; mismatch identifies the divergence.

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The Discovery Order

**The Situation:** A federal court orders a carrier to produce per-patient AI decision evidence for 2,400 named class members.

**Before SAID:** The carrier attempts to reconstruct each decision. Reconstruction succeeds for some, fails for others (model version drift, framework patches, retrieval-order non-determinism). The court issues an adverse finding on the failed reconstructions. The settlement reflects the carrier's inability to demonstrate consistent behavior.

**With SAID:** The carrier produces the envelopes for all 2,400 class members. The plaintiffs' expert witnesses replay each decision independently. The evidence shows the AI made consistent recommendations across the protected-class and reference segments; clinical override rates were appropriate; the carrier's stated process was actually executed. The case proceeds on actual merits.

**The Impact:** The carrier's litigation posture shifts from "we cannot prove what the AI did" to "we can prove exactly what the AI did, and you can verify it yourselves." Settlement reflects actual exposure.

### Scenario 2: The FDA Post-Market Inquiry

**The Situation:** The FDA initiates post-market surveillance on a cleared clinical decision-support AI. The agency requests evidence that the model performs in production consistent with the performance characteristics stated in the 510(k).

**Before SAID:** The carrier or vendor produces aggregate dashboards. The agency requests per-decision evidence for a sample. Reconstruction fails on a fraction of the sample; the failures correlate with model version updates. The agency issues a Warning Letter on inadequate post-market surveillance practices.

**With SAID:** The carrier or vendor produces envelopes for the sampled decisions. The FDA reviewer runs replay; outputs match. Performance characteristics in production align with the 510(k) submission. The post-market surveillance closes affirmatively.

**The Impact:** FDA relationship strengthens because the carrier or vendor moved first into the evidentiary architecture the agency is converging on.

### Scenario 3: The Clinical Governance Committee

**The Situation:** A health system's clinical governance committee reviews the AI's recommendation patterns in post-acute care. The committee suspects the recommendations may differ across patient subgroups in ways the model card did not predict.

**Before SAID:** The committee reviews aggregate dashboards. The granular question — *do the recommendations differ in identifiable patterns* — cannot be answered without per-decision evidence the system does not retain.

**With SAID:** The committee queries the envelope vault for the cohort of interest. Population-level analysis identifies a recommendation pattern in a specific subgroup the model card did not characterize. The committee escalates to the AI vendor; the vendor adjusts the model; the deployment of the updated model produces new envelopes the committee can compare against the old.

**The Impact:** Clinical governance moves from "we hope the AI is fair" to "we have the evidence to confirm or refute fairness, continuously." This is the posture that converts AI from a clinical-governance risk into a clinical-governance tool.

## Key Metrics & KPIs: Measuring What Matters

### Reproducibility Metrics

- **Envelope Coverage:** Percentage of AI-driven coverage determinations and clinical recommendations producing a signed envelope.
  - **Target:** 100%.
  - **Impact:** Every decision is per-decision evidentiable.

- **Replay Match Rate:** Percentage of envelope replays producing byte-identical output.
  - **Target:** 100% on supported hardware.
  - **Impact:** Court-defensibility is structural.

- **Discovery Response Time:** Median time from court order to delivered per-decision evidence package.
  - **Target:** ≤ 72 hours.
  - **Impact:** Discovery posture compresses.

### Regulatory Posture Metrics

- **FDA Post-Market Sample Closure Rate:** Percentage of FDA-sampled decisions closing on envelope evidence.
  - **Target:** ≥ 95%.
  - **Impact:** Post-market relationship strengthens.

- **State AI Health Examination Closure Rate:** Percentage of state examinations closing without an MRA.
  - **Target:** ≥ 80%.
  - **Impact:** Regulatory capital compounds.

- **Population-Level Disparity Anomaly Detection Rate:** Percentage of disparity anomalies detected internally before regulator inquiry.
  - **Target:** ≥ 95%.
  - **Impact:** Disparate-impact posture moves from defensive to proactive.

### Clinical Operations Metrics

- **Clinician Override Rate:** Track-only metric; baseline pre-SAID vs. post-SAID.
  - **Target:** Trends inform clinical-governance review.
  - **Impact:** Quality improvement signal.

- **Clinical Recommendation Reproducibility:** Patient-level test of recommendation consistency across runs.
  - **Target:** 100% within supported hardware envelope.
  - **Impact:** Clinician trust based on verified consistency.

## Integration Points: Fitting Into Your Workflow

### EHR and Clinical Systems

- **Epic, Cerner, Meditech, Athena:** AI integration via standard EHR AI APIs.
- **Clinical decision-support platforms (NeuroFlow, Bayesian Health, vendors of cleared SaMD AI):** SAID drops in as the deterministic inference layer.

### Utilization Management

- **UM platforms (Allscripts UM, MCG, InterQual systems):** Coverage-determination AI calls route through SAID.
- **Prior-authorization automation (Olive, Notable, Akasa for revenue cycle, vendor-specific UM):** Prior-auth AI generates envelopes.

### Compliance and Regulatory

- **FDA post-market surveillance:** Envelope exports in FDA-aligned formats.
- **CMS coverage decision reporting:** Per-decision envelopes available for CMS review.
- **State insurance department exams:** Envelope vault exports.

### Clinical Governance

- **Clinical-governance platforms (in-house, vendor-specific):** Envelope-based population analysis for quality improvement.
- **Bias and fairness analytics (specialized vendors):** Envelope vault as analytical substrate.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of non-deterministic clinical AI is the litigation exposure of every coverage determination the carrier has issued under AI assistance, every CMS or FDA inquiry ahead, and the class actions that follow the public attention drawn by nH Predict. The carrier or vendor that absorbs this exposure as a "we'll defend when challenged" posture is structurally exposed to the moment the challenge cannot be met.

### The Value of Having This

SAID turns AI-driven coverage determinations and clinical recommendations from a structural litigation exposure into queryable per-decision infrastructure. The model the carrier or vendor cleared with the FDA is the same model that runs in production; the determinism guarantee is the architecture; the envelope is the per-decision evidence.

### The Competitive Advantage

The carriers and clinical AI vendors that produce per-decision evidence at scale are operating in a different regulatory and litigation environment than those that don't. The differentiation is structural: it shows up as faster discovery closure, lower legal reserve, faster FDA post-market resolution, and the ability to participate in coverage and care models that require evidentiary architecture.

## Learn More

- **SAID Overview:** [Deterministic Inference README](https://github.com/SmartHausGroup/.github/blob/main/products/said/README.md)
- **Other SAID Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/said/use-cases/README.md)
- **The Six Failures:** [The Lokken Pattern in Context](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **SMARTHAUS Vision:** [The Full End-to-End View](https://github.com/SmartHausGroup/.github/blob/main/vision/README.md)

---

**SAID transforms AI in clinical decision support from a litigation and regulatory exposure into per-decision infrastructure — every coverage determination, every clinical recommendation, every patient-specific decision verifiable on the plaintiff's expert's laptop, the FDA reviewer's hardware, or the state examiner's workstation, with byte-identical output every time.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
