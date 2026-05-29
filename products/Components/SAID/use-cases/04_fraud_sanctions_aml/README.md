# Use Case 4: Fraud, Sanctions, and AML Adjudication

**Per-transaction signed envelopes that satisfy bank-grade model risk regimes**

## The Real Problem: When the Examiner Asks "Why This Alert, Why This Disposition"

It's a Monday morning at the bank's transaction-monitoring operations center. The OCC examiner has been on-site for two weeks and is asking pointed questions. She points at a specific transaction from six months ago: a $47,000 wire from a long-time customer to a counterparty in a high-risk jurisdiction. The bank's AI transaction-monitoring system flagged the wire as low-risk and the dispositioner cleared it without escalation. Three weeks later, the same counterparty appeared in OFAC reporting tied to sanctions evasion. The examiner's question: *prove the AI's decision on this wire was consistent with how the AI was supposed to behave at the time, and prove the same AI would not flag it differently today.*

The bank cannot answer. The transaction-monitoring AI is non-deterministic. The model has been updated three times since the wire. The bank's records show the AI's output ("low-risk"), the dispositioner's action ("clear"), and the audit log of the clearance. They do not show whether the AI would produce the same output on the same transaction today, or whether the original output was even reproducible at the time it was made. The examiner finds: inadequate model risk management practices in AI transaction monitoring. The MRA will require 12-18 months and material capital allocation to resolve.

**The current reality:** This pattern is now routine. Every bank deploying AI in fraud detection, sanctions screening, and AML adjudication faces the same examination posture. SR 26-2 (Federal Reserve, April 2026) replaced SR 11-7 with a framework that explicitly requires model lineage and decision provenance — meaning the bank must be able to demonstrate, for any specific transaction on any specific day, that the AI behaved consistent with documented design. Most production AI transaction monitoring systems cannot do this.

**The hidden cost:** Beyond the MRA exposure, banks operating AI transaction monitoring without per-decision evidence face elevated false-positive cost (disposition consistency cannot be enforced), elevated false-negative cost (model drift cannot be detected at decision granularity), and elevated regulatory exposure (the next sanctions enforcement action will name banks that cannot produce per-transaction evidence as the standard the industry is now expected to meet).

## Why Traditional Systems Fail

### Transaction-Monitoring AI Is Non-Deterministic

Production transaction-monitoring AI — graph neural networks for relationship analysis, gradient-boosting for transaction features, LLMs for natural-language sanctions list matching — exhibits the standard non-determinism of production AI inference. The model output for the same transaction varies across runs by small amounts in average conditions and by alert-class-relevant amounts in tails. The bank cannot affirmatively prove that a specific historical transaction would have produced the same disposition recommendation today.

**The mathematical reality:** Bank-grade model risk management was developed for deterministic models (logistic regression, decision trees, deterministic rule sets). AI inference is structurally different. The model-risk framework cannot grade what it cannot reproduce.

### Vendor Audit Trails Lack Reasoning

The standard transaction-monitoring platforms (FICO Falcon, NICE Actimize, SAS, Featurespace, Quantexa, Verafin) provide alert-level audit trails: the alert fired, the disposition was recorded, the case was closed. They do not provide per-transaction evidence that the AI's reasoning was consistent with the model's documented design or that the same model would produce the same alert today. The audit trail is workflow evidence, not decision evidence.

### Model Risk Governance Operates on Aggregate Metrics

Bank model risk management functions assess model performance through aggregate metrics: false-positive rates, true-positive rates, geographic distribution, customer-segment performance. These metrics describe the model's average behavior. They do not bind specific transactions to specific decisions in a way the examiner can verify per-transaction.

**The organizational cost:** Bank model risk teams operate in a posture of "the model performs adequately in aggregate." When the examiner asks about a specific transaction, the team reconstructs from the available audit trail; the reconstruction is incomplete; the exam closes with findings.

### SR 26-2 Raised the Bar

The April 2026 Federal Reserve supervisory letter explicitly references AI-specific requirements that prior frameworks did not address: model lineage from data to decision, decision provenance for individual outputs, and reproducibility of model behavior over time. Banks operating without per-decision evidence are no longer compliant with the framework they're examined against.

## Current Solutions: TMS Platforms, Audit Trails, and Model Risk Functions

### How the Market Currently Handles This

Four approaches dominate today:

1. **Transaction-monitoring platforms** (FICO Falcon, NICE Actimize, SAS AML, Featurespace, Quantexa, Verafin) — Vendor TMS with audit-trail capabilities.
2. **Model risk management platforms** (Yields.io, ValidMind, Datatron) — Pre-deployment and ongoing model validation.
3. **Sanctions screening systems** (LexisNexis Bridger, Refinitiv World-Check, Dow Jones Risk & Compliance) — Watchlist screening platforms.
4. **In-house decision-capture pipelines** — Custom systems that store per-decision input, output, and metadata for later review.

**What this provides:**
- TMS platforms provide workflow, alert-disposition, and case-management capabilities.
- Model risk platforms validate aggregate performance.
- Sanctions screening systems maintain current watchlists and screening logic.
- Decision-capture pipelines store the data needed for attempted reconstruction.

### Why These Solutions Fall Short

**1. TMS Audit Trails Are Workflow Records**
The audit trail shows the alert fired and was dispositioned. It does not show whether the AI reasoning was consistent with the model's documented behavior, whether the same alert would fire today on the same transaction, or whether the AI's confidence was at a level documented as appropriate for that alert class.

**2. Aggregate Validation Does Not Answer Per-Decision Questions**
The model risk function's aggregate validation work demonstrates the model performs at acceptable rates. The examiner's question about a specific transaction is not answered by aggregate evidence. The two evidence types serve different purposes; SR 26-2 requires both.

**3. Sanctions Screening Logic Is Deterministic; AI Enhancements Are Not**
The hard-rules layer of sanctions screening (exact-match, fuzzy-match against watchlists) is typically deterministic and audit-trail-grade. The AI-enhanced layer (name disambiguation, entity resolution, relationship inference) is non-deterministic. The bank's screening evidence is mixed: hard rules are reproducible, AI layers are not.

**4. Decision Capture Without Replay Is Trust-Me Evidence**
A captured decision record shows what the system stored. It does not let the examiner independently re-derive the decision. The capture is data; the replay is evidence.

**5. None Produce Replayable Per-Transaction Envelopes**
The structural gap, again: no per-transaction artifact an outside party can take to their own hardware, replay, and verify byte-for-byte against the bank's record.

## How SAID Is Different

**1. Deterministic AI Inference for Transaction Monitoring**
SAID makes the AI layer of transaction monitoring reproducible: same transaction features + same fixed context → same alert score and disposition recommendation.

**2. Per-Transaction Signed Envelopes**
Every transaction the AI monitors generates an envelope. The envelope carries the transaction features, the model artifact, the decision, and a cryptographic signature.

**3. Byte-Identical Replay for Examiners**
The OCC, the FDIC, the Federal Reserve, and state banking departments can replay any historical transaction's AI decision on examiner hardware. The bank's posture moves from testimony to evidence.

**4. SR 26-2 Compliance by Construction**
Model lineage (which model artifact produced the decision) and decision provenance (the inputs and reasoning) are captured in the envelope structure. SR 26-2 evidentiary requirements are satisfied per transaction, not promised per process.

**5. The Vendor Model the Bank Bought, Not a Fork**
SAID's determinism layer wraps the vendor model directly. The bank does not maintain a forked version of FICO Falcon, NICE Actimize, or any other vendor's AI. The vendor's model upgrades flow through; the bank's compliance posture stays intact.

**6. Cross-Engine Consistency**
The bank's AI fraud detection, AI sanctions screening, AI AML adjudication, and AI risk-rating systems can all run under SAID with the same envelope format. The compliance team queries a single vault for evidence across the AI footprint.

**7. False-Positive Disposition Consistency**
Per-transaction envelopes enable consistency analysis on false-positive dispositions: are similar transactions getting similar treatments, is dispositioner judgment consistent across teams, is the AI surfacing the same patterns over time. False-positive cost reduction follows from disposition consistency.

## The SAID Solution: Per-Transaction Evidence That Replays in Examination

### What If Every AI-Generated Alert Could Be Re-Derived on the Examiner's Laptop?

Imagine a transaction-monitoring environment where every AI alert — every fraud flag, every sanctions hit, every AML escalation — ships with a cryptographically signed envelope that an OCC or Federal Reserve examiner can take to their hardware and replay, producing the exact same alert score the bank's system produced months ago. The model lineage and decision provenance requirements of SR 26-2 are satisfied per alert, not per quarterly model risk report.

This is SAID applied to AI transaction monitoring. The non-determinism that undermines per-transaction evidence is the architectural problem SAID solves.

### Per-Transaction Envelope

Every AI decision in the transaction-monitoring pipeline generates an envelope:

```
{
  "envelope_id": "uuid",
  "timestamp": "2026-05-29T08:14:23.412Z",
  "decision_type": "transaction_risk_scoring",
  "transaction": {
    "transaction_id_hash": "sha256:...",
    "amount": 47000.00,
    "counterparty_id_hash": "sha256:...",
    "feature_set_hash": "sha256:..."
  },
  "model": {
    "name": "transaction_monitoring_v4.2",
    "version_hash": "sha256:...",
    "vendor": "vendor-x",
    "deployed_artifact_id": "deployed-2026-04-15"
  },
  "determinism_profile": "regulated-aml-v1",
  "policy_pack_version": "aml-policy-2026-q2",
  "output": {
    "risk_score": 27,
    "alert_class": "low_risk",
    "disposition_recommendation": "auto_clear",
    "rationale_codes": ["customer_history_consistent", "counterparty_seen_before"],
    "model_confidence": 0.91,
    "output_hash": "sha256:..."
  },
  "downstream_action": {
    "dispositioner_action": "auto_cleared",
    "case_id": null,
    "elapsed_to_action_ms": 124
  },
  "envelope_signature": "ed25519:..."
}
```

The envelope is the per-transaction evidence artifact for SR 26-2 model lineage, decision provenance, BSA/AML examination, OFAC compliance review, and any subsequent investigation tied to the specific transaction.

### Determinism Profile for Bank Adjudication

The `regulated-aml-v1` profile pins every variance source: seed, sampling (greedy decoding for adjudication scoring), context assembly (transaction context, customer history, counterparty graph features in deterministic order), retrieval (sanctions list version pinned, customer-history window pinned).

### Model Lineage and Decision Provenance

The envelope's `model.deployed_artifact_id` traces back to the bank's model deployment records — the specific version, the validation evidence, the approval workflow that put it in production. The envelope's `output.rationale_codes` trace back to the model's documented reasoning categories. Model lineage and decision provenance are baked into the envelope; the SR 26-2 evidentiary requirements are satisfied per transaction.

### Cross-Engine Consistency

The bank may run separate AI engines for fraud detection, sanctions screening, customer risk rating, and AML transaction monitoring. SAID provides a consistent envelope format across all of them. Compliance teams query a single vault; examiners receive evidence in a consistent format; model risk functions analyze patterns across the bank's full AI footprint.

### Disposition Consistency Analytics

Per-transaction envelopes enable population-level analysis: are similar transactions getting similar AI scores, is dispositioner action consistent across teams and over time, is the AI surfacing patterns that match documented model behavior. False-positive disposition consistency is a real money saver — the dispositioner team's capacity stretches when consistency improves.

## Real-World Impact: The Numbers That Matter

### For Compliance and Examinations

**SR 26-2 Examination Closure Rate:** Bank examinations of AI transaction monitoring close on envelope evidence rather than aggregate reports. MRA rate drops materially in the first examination cycle post-deployment.

**Discovery Response Time:** Median time from regulatory or legal request for per-transaction evidence drops from weeks (reconstruction) to hours (envelope query + replay).

**Model Risk Posture:** SR 26-2 model lineage and decision provenance requirements are satisfied per transaction. The model risk function shifts from defending aggregate performance to providing per-decision evidence.

### For Operations

**False-Positive Reduction:** Disposition consistency analysis identifies systematically over-flagged patterns. False-positive rates decline as the dispositioner team's feedback loop tightens. Material operational cost reduction.

**Alert Volume Management:** The bank can deploy more aggressive AI alerting because dispositioner consistency is enforceable. Alert volume increases produce alert quality, not alert noise.

**Cross-Engine Investigation:** Investigators working a case can query envelope evidence across the bank's full AI footprint (fraud, sanctions, AML, customer risk) in a single workflow. Investigation cycle times compress.

### For Risk

**Regulatory Penalty Exposure:** Banks facing the next round of sanctions enforcement actions can produce per-transaction evidence. The "we couldn't reconstruct the decision" defense — which carries severe penalty multipliers — is structurally unavailable as a failure mode.

**Insurance Posture:** Cyber and operational-risk insurers writing policies for banks distinguish those producing per-transaction evidence. Premium reflects the differential.

**M&A Diligence:** Acquirers examining banks' AI infrastructure include per-decision evidence quality as a structural diligence item. The differential is now part of bank valuation.

## The Architecture: How It Works

### The Transaction-Monitoring Integration

SAID integrates with FICO Falcon, NICE Actimize, SAS AML, Featurespace, Quantexa, Verafin, and in-house transaction-monitoring systems through standard AI integration APIs. The alert generation step routes through SAID; the envelope is generated; the alert flows back to the TMS workflow.

### The Sanctions Screening Integration

For AI-enhanced sanctions screening (entity resolution, name disambiguation, relationship inference), SAID wraps the AI layer with deterministic inference. The hard-rules screening layer remains as-is. The composite screening produces a unified envelope per screened entity.

### The Envelope Vault

Envelopes are written to the vault inside the bank's environment. The vault is structured, signed, append-only, and portable. Compliance teams query the vault for examination evidence; legal teams export from the vault for litigation discovery; investigators query the vault for case work; model risk teams analyze patterns for ongoing validation.

### The Replay Service

Open-source replay tooling reproduces any historical AI decision. The OCC examiner, the Federal Reserve examiner, the FDIC examiner, the state banking department examiner, or the bank's own internal audit team can independently verify any historical decision.

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The Sanctions Enforcement Investigation

**The Situation:** OFAC initiates an investigation alleging the bank processed wires for a sanctioned counterparty over a six-month period. The investigation requests per-wire evidence that the bank's AI screening behaved consistent with documented design.

**Before SAID:** The bank produces the alert audit trail. OFAC requests per-wire reconstruction; the AI screening cannot be reconstructed for wires that occurred prior to recent model updates. OFAC issues findings on inadequate AI screening evidence. The settlement reflects the lack of per-decision evidence.

**With SAID:** The bank produces the envelopes for every wire in the investigated period. OFAC replays envelopes; the AI screening behaved as the bank's documented model design described. The investigation focuses on whether the bank's screening criteria were appropriately strict (which is a different question with different answers) rather than on whether the bank can prove what its screening did.

**The Impact:** The investigation outcome reflects actual exposure, not the inability-to-prove penalty multiplier. The bank's relationship with OFAC strengthens because the bank moved first into the evidentiary architecture.

### Scenario 2: The SR 26-2 Examination

**The Situation:** The bank's first examination under SR 26-2 covers the AI transaction-monitoring program. The examiner requests model lineage and decision provenance evidence for a sample of 800 alerts across fraud, AML, and sanctions categories.

**Before SAID:** The model risk team produces model documentation, validation reports, and aggregate performance dashboards. The examiner finds insufficient per-decision evidence to demonstrate compliance with SR 26-2 specific requirements. The exam closes with MRAs requiring per-decision evidence infrastructure.

**With SAID:** The compliance team produces the envelope vault export for the 800 sample alerts. The examiner replays alerts on examiner hardware; the per-decision evidence demonstrates model lineage (specific model artifact → specific decision) and decision provenance (input features → output reasoning). The exam closes on schedule with no SR 26-2-related MRAs.

**The Impact:** SR 26-2 compliance moves from "build out new infrastructure" to "we already produce the artifact you're asking for." The first-mover examination capital compounds.

### Scenario 3: The False-Positive Reduction Initiative

**The Situation:** The fraud-disposition team is processing 18,000 false-positive alerts per week, a 60% increase year-over-year. The CFO is asking why fraud-disposition costs are accelerating faster than transaction volume.

**Before SAID:** The team analyzes aggregate patterns. Some segments are clearly over-flagged but the granular cause is unclear without per-decision reasoning. The team adjusts model thresholds; the change reduces volume but also increases false-negatives.

**With SAID:** The team queries the envelope vault for over-flagged segments. Population-level analysis identifies a specific rationale code that the AI invokes inconsistently — sometimes flagging similar transactions, sometimes not. The pattern points to a model training data gap. The team works with the AI vendor to address the gap; the new model deploys; envelope evidence in the new period shows the inconsistency is resolved; false-positive volume in the affected segment drops 35% without affecting true-positive rate.

**The Impact:** Per-decision evidence enables targeted false-positive reduction. Disposition costs decline; alert quality improves; the AI's value proposition strengthens.

## Key Metrics & KPIs: Measuring What Matters

### Reproducibility Metrics

- **Envelope Coverage:** Percentage of AI-driven transaction monitoring decisions producing a signed envelope.
  - **Target:** 100%.
  - **Impact:** Every decision is per-transaction evidentiable.

- **Replay Match Rate:** Percentage of envelope replays producing byte-identical output.
  - **Target:** 100% on supported hardware.
  - **Impact:** Examiner-grade reproducibility is structural.

- **Replay Latency:** Median time from envelope to verified replay.
  - **Target:** ≤ 30 seconds for typical transaction-monitoring envelopes.
  - **Impact:** Examinations and investigations operate at workflow speed.

### Regulatory Posture Metrics

- **SR 26-2 Examination Closure Rate:** Percentage of SR 26-2-relevant examinations closing without an MRA.
  - **Target:** ≥ 90%.
  - **Impact:** Model risk capital compounds.

- **Sanctions Enforcement Investigation Resolution:** Median time and exposure reduction in OFAC, FinCEN, or state-level investigations.
  - **Target:** Per-decision evidence reduces resolution time by 60-80%.
  - **Impact:** Penalty exposure narrows.

- **OFAC and BSA Reporting Quality:** Percentage of regulatory reports backed by per-transaction envelope evidence.
  - **Target:** 100%.
  - **Impact:** Reporting integrity is structural.

### Operational Metrics

- **False-Positive Disposition Consistency:** Variance in disposition action for similar transaction patterns.
  - **Target:** Coefficient of variation < 0.05 across dispositioner teams.
  - **Impact:** False-positive cost declines; alert quality improves.

- **Investigation Cycle Time:** Median time from case opening to evidence-complete case closure.
  - **Target:** ≥ 40% reduction post-SAID deployment.
  - **Impact:** Investigator capacity stretches.

- **Cross-Engine Investigation Efficiency:** Time required to assemble per-decision evidence across fraud, sanctions, AML, and customer-risk engines.
  - **Target:** ≤ 1 hour for typical multi-engine investigations.
  - **Impact:** Investigations complete without engine-by-engine forensic work.

## Integration Points: Fitting Into Your Workflow

### Transaction-Monitoring Platforms

- **FICO Falcon, NICE Actimize, SAS AML, Featurespace, Quantexa, Verafin:** SAID integrates as the deterministic inference layer behind the platform's AI components.
- **In-house transaction-monitoring systems:** SAID via OpenAI-compatible API.

### Sanctions and Watchlist

- **LexisNexis Bridger, Refinitiv World-Check, Dow Jones Risk & Compliance:** AI-enhanced screening layers wrap through SAID; hard rules continue running natively.
- **In-house sanctions logic:** SAID wraps the AI-enhanced disambiguation and entity resolution components.

### Model Risk and Compliance

- **Model risk platforms (Yields.io, ValidMind, Datatron):** Envelope vault as the evidence substrate for ongoing validation.
- **Compliance management (NICE Compliance, Wolters Kluwer):** Envelope evidence into compliance workflows.
- **Regulatory reporting (FinCEN, OFAC, BSA, EU AMLD):** Per-decision evidence in reporting templates.

### Investigation and Case Management

- **Case management (SAS Visual Investigator, NICE Actimize Investigation, Quantexa):** Envelope evidence in case files.
- **eDiscovery for AML/sanctions matters:** Vault exports to legal hold and discovery platforms.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of non-deterministic AI in transaction monitoring is the regulatory exposure of every alert disposition the bank has issued under AI assistance, the next sanctions enforcement action that names the bank, and the SR 26-2 examination cycle that finds the AI evidence inadequate. Banks operating without per-decision evidence in 2026 are operating in a regulatory environment that has moved past the architecture they ship.

### The Value of Having This

SAID turns AI transaction monitoring from a regulatory liability into queryable per-decision infrastructure. The vendor models the bank already licenses continue to run; the SR 26-2 evidentiary requirements are satisfied per decision; the dispositioner team's consistency improves through envelope-based feedback loops.

### The Competitive Advantage

The banks that produce per-transaction evidence at scale operate in a different regulatory and operational environment than those that don't. The differentiation compounds: fewer MRAs, lower model risk capital, faster examinations, lower false-positive costs, faster investigations, stronger sanctions enforcement posture. The cumulative effect is material to ROE.

## Learn More

- **SAID Overview:** [Deterministic Inference README](https://github.com/SmartHausGroup/.github/blob/main/products/said/README.md)
- **Other SAID Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/said/use-cases/README.md)
- **The Six Failures:** [Why Bank Examiners Now Demand Per-Decision Evidence](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **SMARTHAUS Vision:** [The Full End-to-End View](https://github.com/SmartHausGroup/.github/blob/main/vision/README.md)

---

**SAID transforms AI transaction monitoring from a regulatory liability into per-transaction infrastructure — every alert, every disposition, every screening decision producing a signed envelope that satisfies SR 26-2 model lineage and decision provenance requirements by construction, with byte-identical replay on examiner hardware whenever the question is asked.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
