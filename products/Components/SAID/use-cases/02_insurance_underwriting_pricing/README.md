# Use Case 2: Insurance Underwriting and Pricing

**AI-derived risk factors that satisfy state rate filings**

## The Real Problem: When the Model's Risk Factor Cannot Be Filed

It's a Thursday afternoon at a regional auto insurance carrier. The product team has spent six months building a sophisticated AI model that improves loss-ratio prediction by 14% — material money on a $400M book. The actuarial team is enthusiastic. Then the rate-filing meeting happens. The Chief Pricing Actuary asks the question that should have been asked on day one: *can we file this with the states?*

The answer is no. State insurance regulators require filed rates to be deterministic, explainable, and reproducible. The AI model's risk factor varies across runs on the same input. The model's reasoning cannot be expressed in a single closed-form filing. The actuarial defense — "the model behaves predictably in aggregate" — does not satisfy filed-rate review under the National Association of Insurance Commissioners' (NAIC) AI principles or under any of the 38 state-specific AI insurance regulations adopted between 2024 and 2026.

The carrier has two options. Deploy the model in unregulated workflows (marketing optimization, agent productivity tools, internal reporting) and absorb the lost loss-ratio value. Or rebuild the model's factor as a deterministic look-up table with a 4-6% loss-ratio improvement instead of 14%, throwing away the value that justified the project.

**The current reality:** This is the central frustration of AI in regulated insurance. The capability exists; the regulatory architecture does not yet accept the output. Carriers are running parallel tracks — sophisticated models for internal analytics, simpler deterministic models for filed rates — and the value gap is widening.

**The hidden cost:** Every state that adopts the NAIC AI Model Bulletin or a state-specific equivalent narrows the deployable surface for non-deterministic AI in insurance. Carriers without an architectural answer are watching their analytical advantage stay locked in unregulated workflows while their filed-rate competitiveness erodes.

## Why Traditional Systems Fail

### Non-Deterministic Inference Fails Filed-Rate Compliance

State filed-rate review requires the rate filing to specify how rates are computed from defined inputs. Deterministic formulas (e.g., a multivariate GLM on observable variables) satisfy this directly. Probabilistic AI outputs do not — the same input produces variable outputs, and the variation cannot be specified in a filing. Reviewing actuaries reject filings that cannot demonstrate reproducibility.

**The mathematical reality:** The variance the AI inference stack introduces is not a defect from the model's perspective; it is the cost of using a stochastic decoder. From the regulator's perspective, the variance is incompatible with filed-rate principles. The two frameworks are not negotiating; they are speaking different languages.

### Approximation Layers Lose the Value

The standard engineering response is to deploy the AI model as a "decision-support tool" and have a deterministic system emit the actual rate. The deterministic system approximates the AI's behavior with rules, lookups, or simpler models. The approximation loses most of the value the AI was supposed to provide — by construction, because the value came from the AI capturing patterns the approximation cannot.

**The organizational cost:** The carrier funds the AI model development, deploys it as decision support, and ships a deterministic approximation as the filed rate. The 14% loss-ratio improvement collapses to 4-6%. The actuarial team and the data-science team disagree about whether the model deployment was a success.

### "Constructive Conservatism" Hides Bias

When carriers do deploy AI directly in pricing — for example, in customer-segmentation overlays — they often add "constructive conservatism" margins to handle the non-determinism. These margins systematically overpredict risk for some segments and underpredict for others, introducing the disparate-impact pattern that the NAIC AI Model Bulletin and state regulations are specifically designed to prevent. The margin meant to protect the carrier from variance becomes the basis for an unfair-discrimination examination.

### Vendor Pricing Engines Do Not Solve This

The major insurance pricing engine vendors (Earnix, Akur8, Pricewell, Quantee) provide GLM and gradient-boosting tools that produce deterministic outputs. They do not (today) provide a way to deploy LLM-derived risk factors in a way that satisfies filed-rate compliance. The vendor's answer is "use our deterministic algorithms"; the carrier's question is "we want to use LLM outputs in our pricing without losing filed-rate compliance."

## Current Solutions: GLMs, Approximation Layers, and Parallel-Track Modeling

### How the Market Currently Handles This

Four approaches dominate today:

1. **Deterministic GLM/GBM pricing engines** (Earnix, Akur8, Pricewell) — File the deterministic algorithm; the AI never reaches the filed rate.
2. **AI as decision support only** — Use AI to inform pricing strategy; the algorithm in the filing is deterministic.
3. **Approximation distillation** — Train a smaller deterministic model to mimic the AI; file the smaller model.
4. **Constructive conservatism margins** — Deploy the AI with safety margins to bound variance.

**What this provides:**
- GLM/GBM engines satisfy filed-rate compliance unambiguously.
- AI-as-decision-support keeps the AI value capture in analytics and strategy.
- Distillation enables some AI value to reach the filed rate (with significant loss).
- Conservative margins manage risk in the deployable subset.

### Why These Solutions Fall Short

**1. GLM/GBM Engines Cap the Achievable Loss Ratio**
The most sophisticated GLM or boosted-tree model is not the same as the most sophisticated AI model on the same data. The structural ceiling is meaningfully lower. Carriers betting on GLM/GBM are betting that the ceiling is high enough; in heavily mature insurance segments (personal auto, home, life), the ceiling is being approached.

**2. AI as Decision Support Leaves Value Locked in Analytics**
The carrier's analytical team produces sophisticated insights; the pricing team cannot file them; the rates ship without the insight. The value capture is incomplete. The data-science team's morale and retention suffer because their best work cannot ship.

**3. Distillation Loses Information Asymmetrically**
The distilled model approximates the AI's average behavior. It loses the AI's behavior in the tail — exactly where loss-ratio outperformance comes from. The carrier files an approximation that systematically underperforms in the segments where the AI most outperforms naive baselines.

**4. Constructive Conservatism Creates Disparate Impact**
The margins introduced to handle non-determinism are not uniformly distributed across customer segments. They concentrate where the AI is most uncertain, which correlates with thin-data segments, which often correlate with protected-class proxies. NAIC reviewers and state regulators flag this pattern. The carrier added the margin to protect itself; the margin becomes the regulatory finding.

**5. Vendor Engines Do Not Bridge the Gap**
The vendor product roadmaps point toward "AI-augmented" GLM rather than "deterministic LLM inference" — a different shape from what carriers actually need to deploy LLM-derived factors at filing-grade reproducibility.

## How SAID Is Different

**1. Deterministic Inference Is the Default**
SAID makes the LLM output the same on every run for the same input. Filed-rate reproducibility becomes architecturally available for AI-derived factors.

**2. Per-Quote Signed Envelopes**
Every underwriting decision and every premium calculation produces a signed envelope tying the input (risk profile) to the output (rate factor). The envelope is the regulatory artifact: filed-rate review can verify the factor's calculation on demand.

**3. The AI Factor Becomes Filable**
A SAID-derived risk factor satisfies the same reproducibility test that a GLM coefficient satisfies. The filing specifies the model artifact (hash), the determinism profile (hash), and the envelope format. The reviewer verifies that quotes generated against the filing produce envelopes matching the filed specification.

**4. NAIC AI Principles Compliance by Construction**
The NAIC AI Model Bulletin requires reproducibility, explainability, and fairness testing. SAID's envelope structure supports each: reproducibility via byte-identical replay; explainability via the model's structured output; fairness via population-level analysis across envelopes for protected-class proxies.

**5. The Carrier Keeps the Model Value**
The AI model's full loss-ratio improvement reaches the filed rate. No distillation loss. No constructive conservatism margin. No parallel-track approximation.

**6. State-by-State Determinism Profiles**
Different states have different filed-rate requirements. SAID's determinism profile abstraction supports per-state configuration — a Texas-filed factor can use one profile, a California-filed factor another, with the underlying model the same.

**7. Vendor-Backend Neutral**
The AI inference can ride on Anthropic, OpenAI, an in-house Llama fine-tune, or a self-hosted MLX model on Apple Silicon. The envelope format is consistent across backends. Vendor switching is not a re-filing event.

## The SAID Solution: Filable AI

### What If LLM Outputs Could Pass Filed-Rate Review?

Imagine a pricing engine where AI-derived risk factors are computed by an LLM, produce identical outputs for identical inputs on every run, and ship with cryptographic envelopes that state insurance examiners can replay on their own laptops to verify the rate they received in the filing. The AI's loss-ratio improvement reaches the filed rate without losing fidelity to approximation. The carrier files the model artifact and the determinism profile alongside the algorithm specification. Examiners replay sample quotes from production and verify byte-for-byte that the production output matches the filed specification.

This is SAID applied to insurance underwriting and pricing. The non-determinism that previously disqualified LLM outputs from filed rates is the architectural problem SAID solves.

### Per-Quote Signed Envelopes

Every underwriting decision and every premium calculation generates an envelope:

```
{
  "envelope_id": "uuid",
  "timestamp": "2026-05-29T14:23:01Z",
  "product": "personal_auto_2026_filing_v2",
  "state": "TX",
  "model": {
    "name": "carrier-fine-tune-2026q2",
    "version_hash": "sha256:...",
    "filed_artifact_id": "TX-FL-2026-04-22"
  },
  "determinism_profile": "regulated-pricing-v1",
  "input": {
    "risk_profile_hash": "sha256:...",
    "feature_set_version": "personal-auto-v4.1"
  },
  "output": {
    "ai_derived_factor": 1.143,
    "factor_explanation": ["telematics_score", "claims_frequency_5yr", "vehicle_safety_class"],
    "computed_premium_subcomponent": 247.31,
    "output_hash": "sha256:..."
  },
  "envelope_signature": "ed25519:..."
}
```

The envelope is the artifact for state insurance examiner verification. The filed artifact ID anchors back to the rate filing the carrier submitted; the production envelope must verify against the same specification.

### Filing-Compatible Determinism Profiles

Determinism profiles bundle the inference settings required to satisfy filed-rate compliance: pinned seed, deterministic kernel selection, ordered context assembly, sampling controls (typically greedy decoding for adjudication workloads). Profiles are versioned and hashed. The carrier files the profile hash alongside the model artifact; the examiner verifies that production envelopes carry the filed profile.

### NAIC AI Model Bulletin Alignment

The NAIC AI Model Bulletin requires:

- **Governance** — Documented oversight of AI in pricing. SAID envelopes are the auditable artifact stream.
- **Risk management** — Demonstration that the model behaves within bounds. Envelope replay provides per-quote evidence.
- **Testing and validation** — Pre-deployment and ongoing testing. Envelope-based testing extends to production monitoring with the same evidence format.
- **Third-party AI** — Vendor model accountability. SAID's backend-agnostic envelope format supports third-party model use with the same compliance artifacts as in-house models.

A carrier deploying SAID-backed AI pricing produces the artifact stream NAIC reviewers are converging on as the expected evidence format.

### Population-Level Fairness Testing

Per-quote envelopes enable population-level fairness analysis: query the envelope vault for all quotes in a protected-class proxy segment, compare factor distributions, identify potential disparate impact before the regulator does. The same envelope evidence that satisfies reproducibility also satisfies fairness review.

## Real-World Impact: The Numbers That Matter

### For Pricing and Actuarial

**Loss-Ratio Improvement Capture:** The full AI-model loss-ratio improvement reaches the filed rate. Carriers typically report retaining 90-95% of the AI-modeled improvement in the filed version (vs. 30-50% under approximation-distillation approaches).

**Time-to-Filing:** AI-derived factor inclusion in rate filings drops from 18-24 months (build, distill, validate, refile) to 6-9 months (build, file with envelope evidence).

**State Coverage:** A carrier with state-by-state determinism profiles can deploy AI-derived factors across the full multi-state book rather than restricting to states with the most permissive filed-rate frameworks.

### For Compliance and Regulatory

**Filed-Rate Examination:** State examinations of AI-derived factors close on envelope evidence; the examiner replays sample quotes; the production matches the filing; the exam closes.

**NAIC Compliance Posture:** Carriers can demonstrate Model Bulletin alignment with the artifact stream the Bulletin is converging on — proactively, not after the next adoption cycle of state regulations forces it.

**Unfair-Discrimination Defense:** Population-level fairness analysis on the envelope vault provides ongoing evidence that the AI-derived factor does not produce disparate impact across protected classes. The carrier's posture moves from defensive to evidentiary.

### For the Underwriting Operation

**Vendor Flexibility:** The carrier can switch model vendors (Anthropic ↔ in-house fine-tune ↔ third-party specialist provider) without re-filing. The vendor change is an inference-stack change, not a regulatory event.

**Product Velocity:** New product lines can deploy AI-derived factors faster because the regulatory architecture is solved. The pricing team's iteration cycle compresses.

**Talent Retention:** Actuarial and data-science teams can ship their best work into production rather than into decision-support dashboards. The morale and retention benefit is real.

## The Architecture: How It Works

### The Pricing Engine Integration

SAID integrates with the carrier's pricing engine through an OpenAI-compatible API. The pricing engine calls SAID for AI-derived factors; SAID returns the factor and the envelope. The pricing engine combines the AI factor with deterministic GLM/GBM components per the filing.

### The Filed Artifact

The rate filing includes the model artifact (or its hash, with the model available via secure download to authorized reviewers), the determinism profile, the input feature schema, and the envelope format specification. The reviewer can verify the filing against any production envelope.

### The Multi-State Profile Manager

Different states have different filing requirements. SAID's profile manager maintains state-by-state determinism profiles, each filed separately. The pricing engine selects the appropriate profile based on the policy's state of issue.

### The Fairness Analytics Surface

Periodic population-level analysis runs against the envelope vault, computing factor distributions across protected-class proxy segments, flagging anomalies for actuarial review. The analysis is part of standard ongoing compliance, not a periodic special project.

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The First-Filed AI-Derived Factor

**The Situation:** A carrier wants to file the first AI-derived risk factor in its commercial auto product. The Pricing Actuary needs to convince the Chief Pricing Actuary that the filing will pass state review.

**Before SAID:** The Pricing Actuary cannot make a credible reproducibility claim. The Chief Pricing Actuary blocks the filing. The factor stays in decision-support dashboards.

**With SAID:** The Pricing Actuary demonstrates envelope-based replay on the model's outputs. The Chief Pricing Actuary's reproducibility concern is structurally addressed. The filing is submitted in three states as a pilot. Two states approve; one state requests additional fairness analysis (provided from envelope-vault analytics within the cycle). All three approve. The factor goes live across the multi-state book over the next two filing cycles. Loss-ratio improvement in the AI-factor segments lands within 5% of the AI-modeled forecast.

**The Impact:** The carrier captures the AI value at filing grade. The Pricing Actuary and Chief Pricing Actuary develop a repeatable playbook for AI-factor inclusion in subsequent filings.

### Scenario 2: The State Examination

**The Situation:** A state insurance department examines the carrier's first AI-derived factor 18 months after filing. The examiner requests evidence that production quotes match the filed specification for a sample of 500 policies.

**Before SAID:** The carrier reconstructs each quote, attempting to demonstrate reproducibility. Reconstruction succeeds for most; fails for the 12% of quotes where the model version, the framework patches, or the dependency versions had drifted. The examination issues a finding requiring the carrier to invest in reproducibility infrastructure. The MRA takes 18 months to close.

**With SAID:** The carrier produces the envelopes for all 500 sample policies. The examiner runs envelope replay on examiner hardware; every output matches. The examination closes on schedule with no MRA. The carrier's relationship with the state department strengthens because the carrier moved first into the architecture the department is moving toward.

**The Impact:** The architectural investment that solves the structural problem also solves the immediate compliance problem. The carrier earns the examination capital that compounds across future state interactions.

### Scenario 3: The Vendor Switch

**The Situation:** The carrier has been running its AI factor on Anthropic's Claude. A pricing-engine vendor offers a domain-specific underwriting model that promises a 3-4 point additional loss-ratio improvement. The actuarial team wants to test it; the compliance team is worried about the filing implications.

**Before SAID:** Switching the model vendor requires re-filing in 18 states. The compliance burden is multi-quarter. The actuarial team's hypothesis ("the new vendor's model is better") cannot be tested at filing grade for 12-18 months. The switch is shelved.

**With SAID:** The carrier configures the new vendor as an alternate backend. The same envelope format applies. The actuarial team can A/B test the two models in production-equivalent environments using envelope-based comparison. The model that wins (or the segment where each wins) becomes a re-filing event — but the comparison happens in months, not years.

**The Impact:** Vendor switching becomes a normal product-development event rather than a multi-year compliance project. The carrier's pricing edge stays current with the state of the model market.

## Key Metrics & KPIs: Measuring What Matters

### Filing Compliance Metrics

- **Envelope Coverage:** Percentage of AI-derived premium components producing a signed envelope.
  - **Target:** 100% (mathematically enforced).
  - **Impact:** Every production quote is reproducible.

- **Replay Match Rate:** Percentage of envelope replays producing byte-identical output.
  - **Target:** 100% on supported hardware.
  - **Impact:** Filed-rate compliance is structural.

- **State Coverage Ratio:** Percentage of states where the carrier has filed AI-derived factors successfully.
  - **Target:** Track per filing cycle; goal is to lead the carrier's state footprint, not lag it.
  - **Impact:** AI value capture scales with the regulatory book.

### Value Capture Metrics

- **AI Value Retention in Filed Rate:** Percentage of AI-modeled loss-ratio improvement retained in the filed version.
  - **Target:** ≥ 90% (vs. 30-50% with approximation distillation).
  - **Impact:** Project ROI lands as modeled.

- **Time to AI-Factor Filing:** Median months from AI factor development to first state approval.
  - **Target:** ≤ 9 months (vs. 18-24 with distillation tracks).
  - **Impact:** Product velocity accelerates.

- **Loss-Ratio Improvement in AI-Factor Segments:** Realized improvement in segments where AI-derived factors apply.
  - **Target:** Within 5% of AI-modeled forecast.
  - **Impact:** Modeled value materializes in actuals.

### Regulatory Posture Metrics

- **State Examination Closure Rate:** Percentage of state examinations of AI-derived factors closing without an MRA.
  - **Target:** ≥ 80% (vs. typical 40-50% pre-SAID).
  - **Impact:** Regulatory capital compounds.

- **Fairness Anomaly Detection Rate:** Percentage of population-level fairness anomalies detected internally before regulator inquiry.
  - **Target:** ≥ 95%.
  - **Impact:** Disparate-impact posture moves from defensive to proactive.

## Integration Points: Fitting Into Your Workflow

### Pricing Engines

- **Earnix, Akur8, Pricewell, Quantee:** SAID integrates as the AI-factor source behind the existing pricing-engine deterministic algorithms.
- **In-house pricing engines:** SAID drops in via OpenAI-compatible API.

### Underwriting Platforms

- **Guidewire PolicyCenter, Duck Creek Policy, Majesco Policy:** SAID provides AI-derived underwriting decisions with envelopes that integrate into the underwriting record.
- **Distribution channel platforms (agency portals, MGA platforms):** Real-time underwriting via SAID with envelope evidence retained in policy records.

### Compliance and Regulatory

- **Filing systems (SERFF):** Filed artifact identifiers and determinism profile hashes attach to filings.
- **State examination platforms:** Envelope vault export to examiner-preferred formats.
- **NAIC reporting:** Population-level fairness analysis aligned to Model Bulletin reporting expectations.

### Model Vendors

- **Anthropic, OpenAI, Cohere, Mistral, Groq:** Routed via OpenAI-compatible API with envelope wrapping.
- **Insurance-specialist models (specialist vendors, in-house fine-tunes):** Same envelope format applies; vendor switching is configuration, not architecture change.
- **Self-hosted models (Llama, Mistral, custom fine-tunes):** MLX, llama.cpp, transformers, vLLM, or `verbum_gpu` backends.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of non-deterministic AI in insurance pricing is the loss-ratio gap between what the AI model can produce and what the filed rate can capture. As the AI model improves, the gap widens. Carriers absorbing this gap are systematically ceding margin to the carriers that solve the architecture. The regulatory floor is rising — every additional state adopting NAIC AI Model Bulletin alignment narrows the deployable surface for non-deterministic inference.

### The Value of Having This

SAID turns AI in insurance pricing from a decision-support tool into filed-rate infrastructure. The full AI value capture reaches the production premium. The compliance evidence is the artifact regulators are converging on. The vendor flexibility decouples pricing innovation from filing cycles.

### The Competitive Advantage

The carriers that deploy SAID-class deterministic AI in filed rates capture the AI loss-ratio improvement at scale. The carriers that don't watch their non-AI competitors lose ground to AI competitors with no path to recover the lost margin without architectural change. The differentiation is structural and compounds across rate-filing cycles.

## Learn More

- **SAID Overview:** [Deterministic Inference README](https://github.com/SmartHausGroup/.github/blob/main/products/said/README.md)
- **Other SAID Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/said/use-cases/README.md)
- **The Six Failures:** [Why Determinism Matters in Regulated AI](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **SMARTHAUS Vision:** [The Full End-to-End View](https://github.com/SmartHausGroup/.github/blob/main/vision/README.md)

---

**SAID transforms AI in insurance from a decision-support tool that never reaches the filed rate into filed-rate infrastructure — capturing the full AI loss-ratio improvement with envelope evidence that state examiners replay on their own laptops, NAIC compliance built in by construction.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
