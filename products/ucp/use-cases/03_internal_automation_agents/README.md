# Use Case 3: Internal Automation Agents in M365, Salesforce, and SAP

**Gating cross-system actions before the agent breaks segregation of duties**

## The Real Problem: When the Agent Has Every Credential at Once

It's Wednesday morning at a mid-size insurance carrier. A finance director, drowning in invoice approvals, deploys an internal automation agent to "process backlog invoices from approved vendors." The agent has connections to Outlook (to read vendor emails), SharePoint (to retrieve invoice PDFs), SAP (to enter the invoice into the AP module), Workday (to verify the requestor still works there), and DocuSign (to dispatch the payment authorization). The agent has every credential the director has, because the agent runs as the director.

In its first hour the agent processes 73 invoices. One of them is from a vendor terminated for fraud six months ago — the termination record is in the vendor master, but the agent did not check that table; the invoice came from an email address that matched a previously approved vendor. The payment is dispatched. Within ten days $148,000 has been wired to a controlled account. By the time the next reconciliation catches the anomaly, the funds are gone.

**The current reality:** This pattern is not hypothetical, and it is not limited to fraud. Every enterprise running Microsoft Power Automate, Salesforce Agentforce, SAP Joule, ServiceNow's agentic flows, or open-source RPA augmented with LLMs is exposing themselves to cross-system mistakes the underlying SaaS platforms were never designed to prevent. Each platform enforces its own native controls; none enforces controls across platforms. The agent that has credentials in all of them inherits the union of permissions and is bounded by none of them.

**The hidden cost:** The cross-system class of failure is the most expensive AI category most enterprises have not yet priced. The Workday case (Mobley v. Workday, May 2025) demonstrated that even a single-platform agent operating across resume parsing, qualification scoring, and recommendation ranking creates legal exposure that individual-step monitoring cannot resolve. Multi-platform agents amplify this. A SOX violation, a GDPR violation, a HIPAA violation, or a segregation-of-duties violation routinely involves an action sequence that no single SaaS platform's controls were designed to catch.

## Why Traditional Systems Fail

### Native SaaS Controls Are Single-System

Salesforce has profiles and permission sets. SAP has authorization objects. M365 has Conditional Access. Each is sophisticated within its own perimeter. None of them sees what is happening in the others. When an agent reads a confidential email in Outlook, looks up a customer record in Salesforce, updates a contract in DocuSign, and posts a Slack notification — each individual action passes each native control. The composite action is the violation. There is no native place to check the composite.

**The mathematical reality:** SaaS access controls evaluate predicates over the local system state. They have no syntax for predicates over composite cross-system actions. The agent's value comes from operating across systems; the controls cannot govern across systems.

### Identity Federation Compounds the Problem

The standard recommendation is to use a unified identity provider — Okta, Entra ID, Ping — to centralize access control. This makes identity management cleaner. It does not make cross-system policy enforcement cleaner. The federated identity grants the agent the union of permissions across every connected SaaS. The gap between "the agent should be allowed to do these things in Salesforce *and* these things in SAP, but never both within the same transaction" is exactly the gap UCP fills.

### iPaaS and RPA Auditing Is Post-Hoc

Integration platforms (Workato, Tray.io, MuleSoft) and RPA platforms (UiPath, Automation Anywhere, Blue Prism) provide audit trails of automation runs. These trails are post-hoc reconstructions — they show what happened after it happened. When a cross-system policy violation occurs at 9:47 AM, the audit report surfaces it at 9:54 AM, by which time the wire is already in flight, the contract is already signed, the email is already sent.

**The organizational cost:** Compliance teams operate in detection-and-response mode for AI-driven cross-system actions. They cannot operate in prevention mode, because the platforms do not provide prevention primitives that span systems.

### "AI Governance" Tools Are Mostly Model Governance

The current vendor category labeled "AI governance" — Credo AI, Holistic AI, Fairly AI, Robust Intelligence — primarily addresses *model* concerns: bias evaluation, model card management, drift monitoring, explainability scoring. These are useful for model-risk teams; they are not architectural controls over what the agent does at the action layer.

## Current Solutions: iPaaS, RPA Auditing, and "Agentic" Vendor Promises

### How the Market Currently Handles This

Four approaches dominate today:

1. **iPaaS workflow constraints** — Build the cross-system policy into the workflow definition itself (Workato, Boomi, Mulesoft, Power Automate).
2. **RPA audit and observability** — Post-hoc reconstruction of what RPA bots did (UiPath Process Mining, Automation Anywhere Discovery).
3. **Native SaaS guardrails** — Vendor-provided controls inside Agentforce, Joule, Copilot, and similar agentic surfaces.
4. **DLP and CASB layers** — Data-loss-prevention tools sitting at the network edge between systems (Netskope, Zscaler, Microsoft Purview).

**What this provides:**
- iPaaS workflows are deterministic for fixed flows.
- RPA auditing is comprehensive for traditional script-driven bots.
- Native SaaS guardrails work within their own platform.
- DLP catches obvious data exfiltration at the network layer.

### Why These Solutions Fall Short

**1. iPaaS Workflows Don't Match Agent Behavior**
An iPaaS workflow is a fixed graph of nodes and edges. An AI agent operates dynamically — it decides, in flight, which tools to call based on what it discovers. The whole productivity case for agents over RPA is that the agent figures out the workflow at runtime. Constraining the agent to a fixed iPaaS workflow defeats this purpose. Most agent deployments coexist with iPaaS rather than replacing it.

**2. RPA Audit Misses Dynamic Decisions**
RPA auditing was built for deterministic bots. The audit trail says "the bot read this field, copied it to that field, clicked this button." For an AI agent, the question is "why did the agent decide to read that field at all" — and the audit trail does not answer it.

**3. Native SaaS Guardrails Are Sandbox-Limited**
Salesforce Agentforce's Einstein Trust Layer protects the actions Agentforce takes within Salesforce. It does not protect what the agent does when it leaves Salesforce to call an external API or read an external system. Microsoft Copilot's guardrails are scoped to M365. SAP Joule's are scoped to S/4HANA. Each vendor's guardrails stop at the vendor's perimeter.

**4. DLP Is Pattern-Based, Not Policy-Based**
DLP catches recognizable patterns (credit card numbers, SSNs, classified document markings). It does not catch "this customer's data should not have moved from System A to System B because customer C is in jurisdiction D." That kind of policy requires structured knowledge of the customer's regulatory state, which DLP does not have.

**5. None Provide Signed, Replayable Receipts**
When the auditor asks "show me, for this specific automation run on this specific day, that the agent did not violate segregation of duties between PR creation and PR approval" — the iPaaS logs, the RPA traces, the native SaaS audits, and the DLP alerts collectively cannot answer the question. They are descriptive artifacts about what the systems each saw. They are not a proof object about what the policy decided to allow.

## How UCP Is Different

**1. The Gate Sits Above All the SaaS Systems**
UCP is not inside Salesforce, SAP, or M365. It sits between the agent and every connected system. The composite action is evaluated against composite policy before any individual SaaS call happens.

**2. Policies Span Systems by Design**
A UCP rule that says "no single agent session may both create a purchase order in SAP and approve the same purchase order" fires correctly because UCP sees both actions in the same session. The native SaaS controls cannot see this composite; UCP can.

**3. Data Classification Is Policy Input**
Customer data, employee data, regulated data — UCP receives data classification metadata alongside each action and applies policy that depends on it. "This action would move classified data from environment A to environment B; environment B does not have a Data Processing Agreement covering this customer's jurisdiction; deny."

**4. The Same Gate Serves SOX, HIPAA, GDPR, SOC 2, and PCI**
Different compliance frameworks have different requirements, but they share a common architecture: prevent specific composite actions from occurring. UCP's policy engine is general; the compliance team writes policies for each framework using the same primitives.

**5. Cross-Platform Actions Carry Composite Receipts**
Every composite action — every sequence the agent strings together across systems — produces a single signed receipt naming the full chain. The receipt is the cross-system evidence artifact compliance teams have been trying to construct from disjoint logs for years.

**6. The Platform Layer Stays Pluggable**
The customer's M365, Salesforce, SAP, and other platforms are not modified. The agent stays connected through whatever native APIs and connectors already exist. UCP intercepts at the agent's action-emission layer.

## The UCP Solution: Cross-System Admission for Cross-System Action

### What If "Across Systems" Meant Across One Policy Set?

Imagine an architecture where the agent's session — every action it takes across every connected SaaS — is governed by a single policy set. The agent reads from Outlook, looks up in Salesforce, writes to SAP, posts to Slack; UCP sees the entire composite, evaluates it against the organization's actual SOX, GDPR, HIPAA, and SOD policies, admits the actions that comply and denies the actions that don't. There is no gap between systems for the agent to slip through.

This is UCP's cross-system mode. The customer's existing SaaS controls remain in place; UCP adds the composite layer on top.

### The Action-Stream Interception

UCP integrates with the agent's tool-call layer — for MCP-based agents, through the MCP broker; for Salesforce Agentforce, through Agent Action Framework hooks; for Microsoft Copilot, through the Copilot Studio governance integration; for custom in-house agents, through the language-runtime SDKs.

Every tool call the agent makes is converted into a structured action object and submitted to UCP before execution. UCP maintains session state — the agent's prior actions in the current session inform the evaluation of subsequent actions. A composite policy fires when the composite action pattern is detected.

### Cross-System Policy Semantics

A typical UCP cross-system policy:

```
rule sod_pr_create_approve:
  when action.target.system == "sap"
    and action.type == "approve_purchase_order"
    and session.has_prior_action(
      target_system="sap",
      action_type="create_purchase_order",
      target_object_id=action.target.object_id
    )
  then deny with reason="Segregation of duties violation: same session
    cannot both create and approve PR. (SOX control SOD-001)"

rule customer_data_jurisdiction:
  when action.type == "data_movement"
    and action.data_classification == "customer_pii"
    and action.target.region != action.source.data_subject.jurisdiction
    and not session.context.has_dpa_for(
      jurisdiction=action.source.data_subject.jurisdiction,
      destination_region=action.target.region
    )
  then deny with reason="GDPR Article 44: cross-border transfer
    requires Data Processing Agreement. None on file for
    {jurisdiction} → {destination_region}."
```

The first rule binds segregation-of-duties to the actual object identity — same PR cannot be both created and approved by the same session. The second rule binds data movement to jurisdictional policy, applying the actual DPA registry as context.

### Composite Receipts

Cross-system actions produce composite receipts:

```
{
  "session_id": "uuid",
  "composite_action_chain": [
    {"action_id": "...", "target": "outlook.read", "decision": "admit"},
    {"action_id": "...", "target": "salesforce.lookup", "decision": "admit"},
    {"action_id": "...", "target": "sap.update_vendor", "decision": "deny",
     "rule_fired": "vendor_status_must_be_active"}
  ],
  "policy_set_hash": "sha256:...",
  "receipt_signature": "ed25519:..."
}
```

The compliance team queries against composite receipts the same way they would query against single-action receipts. The cross-system evidence becomes a queryable artifact rather than a forensic reconstruction.

### Data Classification Integration

UCP integrates with the customer's existing data classification systems — Microsoft Purview Information Protection, Salesforce Shield, SAP Information Lifecycle Management, native CDM tags — to receive classification metadata alongside each action. Policies that depend on classification (GDPR, HIPAA, CCPA, PCI) fire correctly because they have the input they need.

## Real-World Impact: The Numbers That Matter

### For Compliance and Risk

**Cross-System Violation Detection:** Organizations report 5–15x increase in cross-system policy violations detected and prevented, because the violations were occurring before UCP and going undetected. The detection-to-prevention shift is the structural value.

**Audit Cycle Time:** Time to deliver evidence for cross-system controls drops from weeks (reconstruction) to hours (query against receipt vault).

**Examination Posture:** Regulators examining AI-driven automation are now asking specifically for cross-system control evidence. UCP receipts answer this question directly.

### For Operations

**Agent Deployment Velocity:** Organizations can deploy automation agents into production with months less compliance review, because the policy surface is the same regardless of which systems the agent will touch.

**Incident Cost Reduction:** Cross-system incidents — the most expensive class — drop to near-zero. The agent cannot execute the composite action that constitutes the incident.

**Audit-Driven Re-Architecture Avoided:** Without UCP, an audit finding on cross-system controls typically forces re-architecting the automation. With UCP, audit findings close against existing receipt evidence; no re-architecture required.

### For the Organization

**Insurance Posture:** Cyber and E&O underwriters writing policies for organizations with significant AI automation footprints recognize UCP-class composite controls as compensating evidence.

**M&A Diligence:** Acquirers performing technical diligence on targets with substantial AI automation can be shown UCP receipt evidence as part of the data room — a structural improvement over the typical "we have logs but cannot prove what they mean" posture.

**Regulatory Engagement:** Organizations operating in heavily regulated industries (financial services, healthcare, defense) can proactively share UCP architecture and sample receipts with regulators during pre-examination engagements — moving from defensive posture to constructive posture.

## The Architecture: How It Works

### The Universal Connector Layer

UCP ships connectors for the major enterprise SaaS platforms — M365 (via Graph + Purview), Salesforce (via REST + Agentforce hooks), SAP (via OData + RFC), Workday (via Reports-as-a-Service + SOAP), ServiceNow (via REST), Slack (via Web API), DocuSign (via REST), Box, Google Workspace, and others. Connectors intercept agent actions at the SaaS API boundary.

For custom in-house systems, UCP provides SDKs (Python, Node.js, Java, .NET) for embedding admission in any application that an agent might invoke.

### The Session-Scoped Policy Engine

Cross-system policies require session awareness — the engine has to know what the agent did earlier in the session to evaluate what the agent is doing now. UCP's session-scoped engine maintains structured state for each agent session and exposes session predicates to policies (`session.has_prior_action(...)`, `session.context.has_dpa_for(...)`, etc.).

Sessions are scoped per-agent-instance and per-business-context. The compliance team controls the session boundary rules.

### The Composite Receipt Vault

Composite receipts are written to UCP's vault inside the customer environment. The vault is structured (queryable as a database), cryptographically signed, append-only, and portable.

Compliance teams query the vault for cross-system evidence; SIEM platforms stream events from the vault for security analytics; legal teams export from the vault under examination or discovery requests.

### The Classification Integration Surface

UCP receives data classification metadata through pluggable adapters. Each adapter normalizes classification from the source system (Purview labels, Salesforce field-level security, SAP information classes) into UCP's policy input schema. Policies depend on the normalized classification, not on source-specific labels.

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The Fraudulent Vendor

**The Situation:** The invoice-processing agent from our opening scenario attempts to enter a $148K invoice from a vendor terminated for fraud six months ago.

**Before UCP:** The agent enters the invoice. The payment dispatches. The funds are gone within ten days.

**With UCP:** The agent attempts to create the invoice in SAP. UCP intercepts. The `vendor_status_must_be_active` rule queries the vendor master, sees the vendor's status is "TERMINATED-FRAUD," and denies. The agent receives a denial and an escalation instruction. The finance director receives a notification: *"Agent attempted to enter invoice from vendor with status TERMINATED-FRAUD. Action denied. See receipt rec-2026-05-29-001."* The director investigates, discovers the spoofed vendor email, alerts security. The attempted fraud generates a detection, not a loss.

**The Impact:** The agent's autonomous productivity is preserved for the 72 legitimate invoices; the single attempted fraud is caught architecturally rather than reconciliation-archaeologically.

### Scenario 2: The GDPR Cross-Border Transfer

**The Situation:** A customer service agent in a US office uses an AI agent to retrieve order history for a European customer. The agent's natural flow involves pulling the data from a European CRM, processing it through a US-based summarization step, and writing notes back to the European CRM.

**Before UCP:** The data flow happens routinely, with no system flagging that data subject to European jurisdiction has crossed to a US processor without a documented transfer mechanism. The violation goes undetected until a DPIA audit six months later flags it as systemic.

**With UCP:** The agent attempts the data movement. The `customer_data_jurisdiction` rule fires. The DPA registry shows no current Data Processing Agreement covering this specific transfer pattern. UCP denies the action and proposes an alternative: keep the data in the European processing environment and return only the summarization output (which has no PII). The agent adapts. The customer service representative gets the answer they need. The cross-border transfer never happens.

**The Impact:** A would-be GDPR violation — and the consequent regulatory fine and DPIA remediation — becomes an architectural non-event. The agent operates productively within the jurisdictional bounds.

### Scenario 3: The Segregation-of-Duties Audit

**The Situation:** Internal audit examines the AP automation function for SOX compliance, specifically the segregation between PR creation and PR approval. The audit team requests evidence that no single automation agent session has both created and approved the same PR over the past 18 months.

**Before UCP:** The audit team pulls SAP authorization logs, RPA execution traces, agent chat logs. Reconstructs each automation run. Cannot definitively prove the negative — there may be violations the reconstruction missed. The audit issues a finding requiring remediation, which forces re-architecting the automation to add manual approval steps. The productivity benefit of the automation is partially clawed back.

**With UCP:** The compliance team runs a query against the receipt vault: *"All sessions, last 18 months, target_system=sap, action_pattern=create_pr → approve_pr same object_id."* The result is zero composite actions matching the pattern — UCP's `sod_pr_create_approve` rule has been firing on every attempt. The receipts demonstrate the negative directly. The audit closes without finding. The automation continues operating at full velocity.

**The Impact:** SOX compliance moves from "trust the reconstruction" to "verify the evidence." The audit team gets a faster, more rigorous answer; the operations team avoids forced re-architecture; the organization gets to keep the productivity.

## Key Metrics & KPIs: Measuring What Matters

### Cross-System Coverage Metrics

- **Composite Policy Coverage:** Percentage of cross-system action patterns governed by at least one active policy.
  - **Target:** ≥ 95% within 90 days of deployment for SOX, GDPR, HIPAA, and SOC 2 domains.
  - **Impact:** Cross-system gaps closed before incidents.

- **Connector Breadth:** Number of unique SaaS platforms gated by UCP per customer.
  - **Target:** ≥ 5 platforms within 60 days; ≥ 10 within 180 days.
  - **Impact:** The composite policy surface scales with the customer's SaaS estate.

- **Data Classification Integration Rate:** Percentage of actions involving classified data that arrive at UCP with normalized classification metadata.
  - **Target:** ≥ 90%.
  - **Impact:** Classification-dependent policies fire correctly.

### Risk Reduction Metrics

- **Cross-System Violations Prevented:** Count of composite-action denials per quarter that prevented a SOX, GDPR, HIPAA, SOC 2, or PCI violation.
  - **Target:** Track-only metric; informs policy tuning.
  - **Impact:** Quantifies the structural value of the composite gate.

- **Audit Findings Closed via UCP Evidence:** Percentage of internal and external audit findings on cross-system controls that close on UCP receipt evidence alone.
  - **Target:** ≥ 85%.
  - **Impact:** Compliance becomes a queryable function.

- **Regulatory Examination Duration:** Median exam cycle duration for engagements involving cross-system AI automation.
  - **Target:** ≥ 40% reduction vs. pre-UCP baseline.
  - **Impact:** Examiner cycles shorten; compliance team bandwidth expands.

## Integration Points: Fitting Into Your Workflow

### Enterprise SaaS Platforms

- **Microsoft 365 (Outlook, SharePoint, Teams, Purview):** Native connector via Graph API + Purview classification integration.
- **Salesforce (Sales Cloud, Service Cloud, Agentforce):** Native Apex action hooks + Einstein Trust Layer integration.
- **SAP (S/4HANA, SuccessFactors, Ariba, Concur):** OData and RFC connector + Information Lifecycle Management integration.
- **Workday, ServiceNow, Slack, DocuSign, Box, Google Workspace:** Native connectors via published APIs.

### Agent Platforms

- **Microsoft Copilot (Studio + agents):** Copilot Studio governance hook integration.
- **Salesforce Agentforce:** Agent Action Framework gating.
- **SAP Joule:** S/4HANA agent action integration.
- **In-house agents:** UCP SDKs (Python, Node.js, Java, .NET).

### Compliance and GRC

- **GRC platforms (ServiceNow GRC, Archer, OneTrust, MetricStream):** UCP findings flow into existing compliance workflows.
- **Audit platforms (AuditBoard, Workiva, Galvanize):** Receipt evidence exported into audit workpapers.
- **Privacy management (OneTrust, BigID, Privitar):** DPA registry integration; jurisdiction-aware policy enforcement.

### SIEM and Identity

- **SIEM platforms (Splunk, Datadog, Sumo, Microsoft Sentinel):** Receipt stream via OpenTelemetry.
- **Identity (Okta, Entra ID, Ping, ForgeRock):** Session identity federation; agent identity binding.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

Cross-system AI automation is being deployed at scale today. The compliance and security teams know there is a gap. The legal teams know there is exposure. The platform vendors are not solving it — they cannot, because the gap exists exactly between their platforms. Organizations are absorbing the cost as detection-and-response overhead, occasional incidents, and quiet re-architecting after audit findings. The aggregate cost is high and growing.

### The Value of Having This

UCP turns cross-system AI automation from a category of exposure into a category of governed productivity. The agent gets to operate across every system that gives it productivity leverage; the organization gets to operate every cross-system policy that gives it compliance assurance. Both are true at once, and both produce the same artifact: a queryable, signed, replayable receipt log.

### The Competitive Advantage

The organizations that solve cross-system AI governance first will compound deployment velocity, audit posture, and operational productivity faster than the organizations still managing the gap with detection-and-response. The advantage is not theoretical — it shows up as faster audit cycles, lower insurance premiums, and a workforce that trusts the automation enough to actually use it.

## Learn More

- **UCP Overview:** [Universal Control Plane README](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/README.md)
- **Other UCP Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/use-cases/README.md)
- **The Six Failures:** [The Workday Pattern in Context](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **SMARTHAUS Vision:** [The Full End-to-End View](https://github.com/SmartHausGroup/.github/blob/main/vision/README.md)

---

**UCP transforms cross-system AI automation from the most expensive class of governance gap into infrastructure that enforces SOX, GDPR, HIPAA, SOC 2, and PCI policies at the action layer — across every SaaS the agent touches, with composite receipts that close audit cycles in hours.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
