# Use Case 1: Credit Decisioning Under Fair Lending

**The same applicant always gets the same answer, replayable on the regulator's laptop**

## The Real Problem: When the Same Application Gets Different Answers

It's Tuesday morning at a regional bank. A customer service representative pulls up an applicant's record to explain an adverse-action notice from last week — the applicant has called, frustrated, asking why she was denied. The representative re-runs the model with the same application data to confirm the explanation. The model returns a score 14 points higher than the original decision. With this score, the applicant would have been approved.

The representative does not know what to say. The applicant is on the line. The original denial was based on the original score; the explanation in the adverse-action notice cited factors that the new score does not weight the same way. Did the model change? It is the same version. Did the data change? The application is identical. Why is the score different?

It is different because the model is non-deterministic. Sampling temperature, GPU non-determinism, retrieval-order randomness in the credit-bureau attribute lookup — any of these could have produced the variance. The bank cannot reproduce the original decision. The bank cannot explain the original decision. The bank is one CFPB inquiry away from a finding.

**The current reality:** Non-deterministic credit decisioning is the default state of AI-assisted lending today. Banks and fintechs deployed AI into adverse-action workflows believing the model would behave the way deterministic credit scorecards (FICO, VantageScore) behave: same applicant, same score, same decision, every time. That assumption is incorrect for AI-driven systems by default. The non-determinism shows up the moment somebody tries to re-derive a historical decision.

**The hidden cost:** The Equal Credit Opportunity Act (ECOA), the Fair Credit Reporting Act (FCRA), and the new Federal Reserve SR 26-2 supervisory letter all assume the lender can reproduce a specific decision when challenged. Without determinism, the lender's compliance posture is "trust us, the model usually behaves this way." That posture is not what examiners, plaintiffs, or class-action attorneys are willing to accept in 2026.

## Why Traditional Systems Fail

### Probabilistic Inference Is Architecturally Non-Reproducible

The default inference stack uses temperature-based sampling, top-k or nucleus filtering, GPU operations with non-deterministic reductions, and asynchronous retrieval that does not pin ordering. Each of these introduces variance. Running the same input twice produces outputs that differ in ways the lender cannot predict and cannot explain. The variance is small in average conditions and catastrophic in regulatory ones — *one* applicant's score moving across the approve/deny threshold between two runs is the basis for a discrimination claim.

**The mathematical reality:** Production AI inference is non-deterministic by construction. The lender did not choose this; it is the default of every inference framework shipped today. The lender either accepts the variance (and the regulatory exposure) or adds custom pinning code (and accepts the engineering cost and ongoing maintenance burden).

### "We Pinned the Seeds" Is Insufficient

The standard engineering answer is to pin random seeds. This is necessary but not sufficient. Pinning seeds does not eliminate GPU non-determinism (atomic adds in floating-point reductions produce different results based on thread scheduling). Pinning seeds does not eliminate retrieval-order non-determinism in the credit-bureau attribute pipeline. Pinning seeds does not eliminate variance from the inference framework's autograd-mode optimizations, attention-implementation choices, or kernel-fusion strategies.

A lender that pins seeds and declares the system "deterministic" is making a claim the auditor will eventually disprove by running the system on different hardware or under a different framework version.

### The Adverse-Action Notice Cannot Be Verified Against the Model

Adverse-action notices under ECOA and FCRA must cite the principal reasons for denial. When the lender generates the notice from model outputs (feature importance, SHAP values, attention weights), the notice is a snapshot of the model's reasoning at the time of decision. Months later, when the applicant or the CFPB requests verification, the lender cannot re-derive the same feature importances on the same input. The notice and the model are decoupled.

**The organizational cost:** Compliance teams spend forensic effort reconstructing decisions that should have been queryable. When reconstruction fails — which it does — the bank settles disputes on the bank's exposure profile rather than on the actual merits of the decision.

### Custom Determinism Infrastructure Diverges From the Model Vendor

Banks that build custom determinism layers — pinned seeds, deterministic kernel selection, ordered retrieval — are running a non-standard version of the model. The vendor's documentation, support, performance benchmarks, and accuracy claims no longer apply directly. The bank has effectively forked the model stack. Every model upgrade requires re-validating the custom determinism layer. The engineering burden is permanent.

## Current Solutions: Model Pinning, Audit Logs, and Decision Capture

### How the Market Currently Handles This

Four approaches are widely deployed today:

1. **Model versioning and pinning** (MLflow, Weights & Biases, SageMaker) — Track which model produced which decision.
2. **Inference framework determinism flags** (`torch.use_deterministic_algorithms`, similar in TensorFlow, JAX) — Vendor-provided settings to reduce non-determinism.
3. **Decision-record capture** (Decision-record vendors, in-house audit pipelines) — Store the input, output, and model version for each decision.
4. **Model risk governance platforms** (ValidMind, Yields.io, Datatron) — Pre-deployment validation of model behavior.

**What this provides:**
- Model versioning enables back-tracing which model was in production at a given time.
- Determinism flags reduce some sources of variance.
- Decision-record capture provides the data needed to attempt reconstruction.
- Model risk platforms validate aggregate behavior before deployment.

### Why These Solutions Fall Short

**1. Model Pinning Tells You What, Not Why**
Knowing which model version made the decision does not let you re-derive the decision. You also need the exact inputs (already captured), the exact random state (often not captured), the exact hardware (rarely controllable), and the exact framework version with all dependencies pinned (rarely maintained over months).

**2. Determinism Flags Are Incomplete**
PyTorch's `use_deterministic_algorithms(True)` covers some operations and explicitly fails on others ("non-deterministic operation encountered"). The lender must rewrite parts of the model graph or accept that the flag is not a guarantee. CUDA's atomic-add behavior cannot be made deterministic without significant performance cost.

**3. Decision-Record Capture Is Post-Hoc, Not Replayable**
Storing the decision after the fact does not let the auditor independently verify it. The auditor must trust the lender's stored record. ECOA examination increasingly demands independent verification — meaning the auditor wants to re-run the model themselves and confirm the output matches.

**4. Model Risk Platforms Validate Aggregate Behavior**
They confirm the model behaves correctly in aggregate. They do not bind a specific input to a specific output in a way the lender can prove later. The aggregate validation does not transfer to the per-decision evidence question.

**5. None Produce a Replayable Signed Envelope Per Decision**
The structural gap is the same across all four solutions: there is no per-decision artifact that an outside party can take to their own hardware, re-run, and verify byte-for-byte that the output matches.

## How SAID Is Different

**1. Determinism Is the Default, Not a Flag**
SAID inference is deterministic out of the box. Same input + same fixed context → same output. The lender does not opt in; the determinism is the architecture.

**2. Cryptographically Signed Envelopes Per Decision**
Every inference output ships with a signed envelope: model version hash, input hash, configuration hash, output hash, and a cryptographic signature. The envelope is portable; the regulator can verify it without contacting SAID or the lender.

**3. Byte-Identical Replay on Any Hardware**
SAID's deterministic-replay tooling re-derives any historical decision on any supported hardware. The auditor downloads the envelope, runs the open-source replay tool, gets the same bytes the lender got months ago.

**4. The Same Model the Lender Bought, Not a Fork**
SAID uses the vendor's model directly. The determinism guarantee comes from SAID's inference architecture, not from forking the model. Model upgrades from the vendor flow through without re-validating a custom determinism layer.

**5. Backend-Agnostic at the Application Layer**
The application talks to SAID via an OpenAI-compatible API. Switching from Anthropic to a local llama.cpp model to MLX on Apple Silicon does not change the application code. The same envelope format applies across backends.

**6. Adverse-Action Notice Generation Is Coupled to the Envelope**
The notice citing principal reasons for denial is generated from the same envelope that produced the score. Months later, the notice and the model output are still tied to the same envelope hash. Verification is one query.

**7. Build Discipline Anchors the Claim**
SAID is built under Mathematical Autopsy. The determinism contract is mathematically proven before each release ships. The customer can independently verify the proof.

## The SAID Solution: Replay Is the Architecture

### What If Every Decision Carried Its Own Proof?

Imagine a lending platform where every credit decision — every score, every approval, every denial, every adverse-action notice — ships with a cryptographically signed envelope that an outside party can take to their own laptop and re-run, producing byte-identical output every time. The lender's claim "we ran this model on this applicant on this date and got this answer" stops being a representation and starts being a verifiable artifact.

This is SAID applied to credit decisioning. The inference layer produces the same output for the same input under any verification harness. The envelope is the evidence.

### The Deterministic Inference Layer

SAID's inference layer enforces determinism through coordinated control of every variance source:

- **Seed pinning** at the inference framework, the tokenizer, the sampler, and the retrieval pipeline.
- **Deterministic kernel selection** at the GPU/CPU level — the same kernels run for the same operations, regardless of optimizer choice or runtime conditions.
- **Ordered context assembly** — system prompt, retrieved documents, and user input are concatenated in a pinned canonical order.
- **Sampling control** — temperature, top-p, top-k are pinned to the values that bind the model to a specific decision path; for adjudication workloads, greedy (temperature 0) is the default with controlled exceptions.
- **Floating-point reduction policy** — atomic operations are configured for reproducibility, accepting the performance cost where the regulatory requirement is non-negotiable.

The application calls SAID through an OpenAI-compatible API; SAID applies the determinism contract; the model produces an output; the envelope is generated.

### The Per-Decision Signed Envelope

Every inference response ships with a structured envelope:

```
{
  "envelope_id": "uuid",
  "timestamp": "2026-05-29T09:14:23.412Z",
  "model": {
    "name": "claude-opus-4.6",
    "version_hash": "sha256:...",
    "provider": "anthropic"
  },
  "inference_config": {
    "temperature": 0.0,
    "top_p": 1.0,
    "seed": 42,
    "context_assembly_hash": "sha256:...",
    "determinism_profile": "regulated-lending-v1"
  },
  "input": {
    "application_id": "app-2026-05-29-001",
    "input_hash": "sha256:...",
    "feature_set_version": "fair-lending-v3.2"
  },
  "output": {
    "score": 687,
    "decision": "deny",
    "adverse_action_factors": [
      "debt_to_income_ratio",
      "credit_utilization",
      "recent_inquiry_count"
    ],
    "output_hash": "sha256:..."
  },
  "envelope_signature": "ed25519:..."
}
```

The envelope is the per-decision artifact. The bank's adverse-action notice references the envelope. The CFPB inquiry six months later targets the envelope. The plaintiff's expert in a class action re-verifies from the envelope.

### Byte-Identical Replay Tooling

SAID ships open-source replay tooling. The auditor downloads the envelope, downloads the model artifact (or uses an API-provider replay endpoint where applicable), runs the replay command, and gets the same output the bank originally got. If the bytes match: the decision is verified. If they don't: there is a finding, immediately, with structural clarity about what diverged.

The replay tooling runs on the auditor's hardware, with no access to the bank's infrastructure required. This is the difference between "trust the lender" and "verify it yourself."

### Adverse-Action Notice Coupling

Adverse-action notices are generated from the envelope. The notice cites the principal-reason factors that the model produced for the specific applicant. Because the envelope is replayable, the notice's claims are verifiable months later. The applicant who calls Customer Service can be told: *"We can show you the exact decision the model made. We can show you the factors it weighted. We can show you the same model would make the same decision today on the same information. If anything has changed in your situation since then, let's update the application and re-run."*

The conversation shifts from defensive (*"we don't know exactly what happened"*) to substantive (*"here is exactly what happened, let's look at what changed"*).

## Real-World Impact: The Numbers That Matter

### For Compliance

**Adverse-Action Notice Verifiability:** Every notice issued under SAID-backed decisioning is structurally verifiable. The lender's compliance team has a queryable evidence base instead of a forensic reconstruction problem.

**CFPB Inquiry Response Time:** Median time from CFPB request to delivered evidence drops from weeks (reconstruction) to hours (envelope query).

**ECOA Examination Cycles:** Examiners testing fair-lending controls receive envelope evidence with replay tooling. Examinations close on the actual lending behavior rather than on the lender's representations about it.

### For Risk

**Litigation Exposure Reduction:** Class actions alleging disparate treatment in AI-assisted lending shift from "the lender's record is incomplete" to "the lender's record is verifiable." Settlement economics change materially.

**Insurance Posture:** D&O and E&O underwriters writing fair-lending policies for AI-using lenders distinguish lenders with replayable evidence from lenders without. Premium reflects the structural difference.

**Model Risk Posture:** Under SR 26-2, model lineage and decision provenance are required. SAID envelopes are the artifact format that satisfies the requirement.

### For the Lending Operation

**Customer Trust:** Customers who can be shown the exact decision the model made — and who can be told the model would make the same decision today on the same information — trust the institution more than customers told "we don't know exactly what happened."

**Decision Velocity:** Banks can deploy AI-assisted decisioning more aggressively because the regulatory floor is well-defined. The "should we deploy AI in this workflow" conversation moves from compliance vetting to product development.

**Model Vendor Flexibility:** SAID's backend-agnostic architecture means switching from one model vendor to another (Anthropic → OpenAI → in-house) is an inference-stack decision, not an application rewrite. Vendor-lock-in stops being a procurement risk.

## The Architecture: How It Works

### The Inference API

SAID exposes an OpenAI-compatible API. Existing application code that talks to OpenAI, Anthropic, or other model providers routes through SAID instead. The application receives an inference response plus a signed envelope.

### The Determinism Profile

Customers configure determinism profiles — named bundles of inference settings (seed, sampling, kernel selection, etc.) — that apply to specific workloads. A `regulated-lending-v1` profile pins everything required for ECOA/SR 26-2 compliance. A `customer-facing-chat-v1` profile permits some sampling variance but pins context assembly. Profiles are versioned and signed.

### The Backend Router

SAID routes inference to the appropriate backend — MLX on Apple Silicon for low-latency local inference, llama.cpp for CPU fallback, HuggingFace transformers for self-hosted models, or API providers (Anthropic, OpenAI, Cohere, Mistral, Groq) for managed inference. The same envelope format applies across backends; the determinism contract is enforced consistently.

### The Envelope Vault

Envelopes are written to a vault inside the customer's environment. The vault is structured (queryable as a database), cryptographically signed, append-only, and portable. Compliance teams query the vault for examination evidence; legal teams export from the vault for litigation discovery.

### The Replay Service

SAID's open-source replay tooling allows any envelope to be replayed on any supported hardware. The replay output is compared byte-for-byte against the envelope's output hash; matches verify the decision, mismatches identify the divergence point.

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The Disputed Adverse-Action Notice

**The Situation:** The applicant from our opening scenario calls about her denial. The CSR pulls up the envelope.

**Before SAID:** The model produces a different score on re-run. The CSR cannot explain. The applicant files a CFPB complaint. The bank's response involves three weeks of reconstruction effort. The complaint settles with the applicant receiving credit and the bank absorbing the cost.

**With SAID:** The CSR replays the envelope. The output matches: same score, same factors, same denial. The CSR explains the principal reasons cited in the adverse-action notice. The applicant acknowledges that her debt-to-income ratio is the issue and asks what would change the outcome. The CSR walks through the path to reapply in 90 days with the corrected ratio. No CFPB complaint. The applicant becomes a customer of an installment product the bank offers in the meantime.

**The Impact:** The conversation that would have escalated to a complaint resolves at the first point of contact. The applicant trusts the institution. The CFPB stat doesn't move.

### Scenario 2: The Fair-Lending Class Action

**The Situation:** Six months after a marketing campaign targeting underserved communities, a plaintiff's firm files a class action alleging that the bank's AI-assisted credit decisioning produced disparate denial rates for protected-class applicants. The plaintiffs demand reproducible decisions for 4,200 named applicants.

**Before SAID:** The bank attempts to reconstruct each decision. Reconstruction fails for hundreds of them — model versions changed, framework updates broke replay, retrieval-order non-determinism cannot be reproduced. The discovery extends 18 months. The settlement reflects the structural inability to demonstrate consistent treatment.

**With SAID:** The bank produces the envelopes for all 4,200 applicants. The plaintiffs' expert witnesses re-verify each decision on their own hardware using the open-source replay tooling. The evidence demonstrates: identical applicant profiles received identical decisions across the protected and reference classes. The disparate-rate claim has to be argued on portfolio composition (which the plaintiffs can argue on real evidence) rather than on inference variance (which they cannot manufacture from verifiable envelopes). The case proceeds on its actual merits.

**The Impact:** The defense moves from "we cannot prove our model behaved consistently" to "here is the verifiable proof that our model behaved consistently." Settlement economics shift accordingly.

### Scenario 3: The SR 26-2 Examination

**The Situation:** The bank's first SR 26-2 examination covers AI-assisted credit decisioning. The examiner requests model-lineage evidence and decision-provenance evidence for a sample of 200 decisions across credit cards, installment loans, and small-business lending.

**Before SAID:** The bank's model-risk team assembles model cards, validation reports, monitoring dashboards, and decision logs. The examiner finds gaps: cannot independently verify any specific decision, cannot confirm model lineage from input to output, cannot reproduce the model's claimed behavior on examiner hardware. The exam closes with MRAs that take 12 months to remediate.

**With SAID:** The model-risk team produces the envelope vault export and the replay tooling. The examiner replays the 200 sample decisions on examiner hardware; every output matches the envelope claim. Model lineage and decision provenance are demonstrated structurally, not testimonially. The exam closes on schedule.

**The Impact:** SR 26-2 compliance moves from "build out new infrastructure" to "we already produce the artifact you're asking for." First-mover advantage compounds across subsequent exams.

## Key Metrics & KPIs: Measuring What Matters

### Decision Reproducibility Metrics

- **Envelope Coverage:** Percentage of model-driven credit decisions producing a signed envelope.
  - **Target:** 100% (mathematically enforced).
  - **Impact:** Every decision is reproducible.

- **Byte-Identical Replay Rate:** Percentage of envelope replays producing byte-identical output to the original decision.
  - **Target:** 100% on supported hardware (mathematically enforced).
  - **Impact:** Reproducibility is structural, not best-effort.

- **Decision Replay Latency:** Median time from envelope to verified replay.
  - **Target:** ≤ 30 seconds on commodity hardware.
  - **Impact:** Verification is fast enough to support real-time customer service.

### Compliance and Regulatory Metrics

- **Adverse-Action Notice Verifiability:** Percentage of issued notices that re-verify against the envelope on demand.
  - **Target:** 100%.
  - **Impact:** ECOA and FCRA defensibility is structural.

- **CFPB Inquiry Response Time:** Median time from inquiry to delivered evidence.
  - **Target:** ≤ 24 hours.
  - **Impact:** Inquiries close on schedule rather than escalating.

- **SR 26-2 Audit Sample Closure Rate:** Percentage of examiner-sampled decisions that close on envelope evidence alone.
  - **Target:** ≥ 95%.
  - **Impact:** Exam cycles shorten; MRA backlog reduces.

### Operational Metrics

- **Backend Switching Effort:** Engineering effort to switch the model backend serving a deployed workload.
  - **Target:** ≤ 1 sprint for primary-vendor switch.
  - **Impact:** Vendor lock-in stops being a procurement risk.

- **Customer Service Resolution Rate:** Percentage of adverse-action disputes resolved at first point of contact via envelope verification.
  - **Target:** ≥ 70%.
  - **Impact:** Disputes resolve at lower-cost touch points.

## Integration Points: Fitting Into Your Workflow

### Lending Platforms

- **Loan origination systems (LOS — nCino, Encompass, Blend, Mortgage Cadence):** SAID drops in as the inference layer behind credit-decision API calls.
- **Adverse-action notice generators (FIS, Fiserv, in-house):** Notice generation consumes the envelope; cited factors trace to the envelope output.
- **Credit-bureau attribute providers (Experian, Equifax, TransUnion):** Attribute retrieval pinned to ordered, deterministic pull.

### Model Vendors

- **Anthropic, OpenAI, Cohere, Mistral, Groq:** Routed via OpenAI-compatible API with envelope wrapping.
- **Self-hosted models (Llama, Mistral, in-house):** Run on MLX, llama.cpp, transformers, vLLM, or `verbum_gpu`.
- **In-house fine-tunes:** Deterministic inference applies to fine-tuned variants the same as base models.

### Compliance and Audit

- **Model risk management platforms (ValidMind, Yields.io, Datatron):** Envelope evidence ingested into validation workflows.
- **Audit platforms (AuditBoard, Workiva):** Vault exports into audit workpapers.
- **eDiscovery and litigation hold:** Envelope vault exports to standard formats for legal discovery.

### Customer-Facing

- **Customer service platforms (Salesforce Service Cloud, Zendesk, in-house CRM):** Envelope verification embedded in adverse-action dispute workflows.
- **Member-facing portals:** Optional envelope reference IDs in adverse-action notices for self-service verification.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of non-deterministic credit decisioning is not the cost of a single complaint — it is the structural exposure of every adverse-action notice the bank has issued under AI assistance, every model-risk examination ahead, and every class action a plaintiff's firm decides to file. The lender that absorbs this cost as a "we'll reconstruct it if asked" posture is structurally exposed to the moment the reconstruction fails.

### The Value of Having This

SAID turns AI-assisted credit decisioning from a regulatory risk into queryable infrastructure. The same decision-quality, the same model vendor flexibility, the same operational productivity — with the missing artifact (the per-decision signed envelope) that converts every regulatory question from a forensic project into a database query.

### The Competitive Advantage

The lenders that produce verifiable per-decision evidence at scale will move first into the regulated AI-lending workflows that the lenders without this infrastructure cannot enter at scale. The first-mover advantage compounds in market share, in regulator trust, and in the cost-of-capital differential that flows from a defensible compliance posture.

## Learn More

- **SAID Overview:** [Deterministic Inference README](https://github.com/SmartHausGroup/.github/blob/main/products/said/README.md)
- **Other SAID Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/said/use-cases/README.md)
- **The Six Failures:** [The REPLAY Failure in Context](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **SMARTHAUS Vision:** [The Full End-to-End View](https://github.com/SmartHausGroup/.github/blob/main/vision/README.md)

---

**SAID transforms AI-assisted credit decisioning from a structural regulatory risk into infrastructure that produces per-decision signed envelopes — replayable by the bank, the regulator, the auditor, the plaintiff, and the customer on their own hardware, with byte-identical output every time.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
