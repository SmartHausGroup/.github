# Use Case 2: Customer-Facing Support Agents

**Stopping fabrication before the customer sees it**

## The Real Problem: When the Bot Invents Company Policy

It's a Tuesday afternoon. A developer using a popular AI coding tool gets logged out switching between her laptop and her desktop. She emails support. Within minutes she receives a polite, professional reply from "Sam" explaining that the company's product is "designed to work with one device per subscription as a core security feature." She is annoyed but accepts it. She tweets her frustration. Other developers reply: *they were told different things by the same support bot*. Some were told the policy existed; others were told it didn't. Within 48 hours the company's product is trending on Reddit, the cofounder is apologizing publicly, and customers are canceling subscriptions.

Sam is not a person. Sam is an AI support bot that fabricated a company policy that did not exist. The company has no way to reproduce which users got which fabricated answers. The conversations cannot be replayed because the bot is probabilistic by design.

**The current reality:** This is the Cursor AI support bot incident, April 2025. The cofounder Michael Truell acknowledged on Reddit that the bot had hallucinated. The trust damage in the developer community persisted for months. Every customer-facing AI deployment in production today has the same vulnerability — the bot can say anything to anyone, at any time, with no record an outside party can verify and no mechanism that prevents the fabrication before the customer reads it.

**The hidden cost:** Customer-facing fabrication is not a one-off incident. It is a *category* of incident every AI-supported company is now exposed to. The cost compounds: each fabrication erodes brand trust, each contradiction between customers erodes consistency, each escalation to a human agent eats the cost savings the bot was deployed to capture. Companies running customer-facing bots today are absorbing this cost silently because most fabrications are small enough that the affected customer does not tweet about them.

## Why Traditional Systems Fail

### The "We Trained the Model" Defense

The standard answer to "how do you stop the bot from making things up" is "we trained it on our actual policies and documentation." This sounds reassuring. It is also wrong.

Training a language model on company documentation makes the model more likely to produce policy-consistent answers in average conditions. It does not bind the model to those policies. The same model that produces correct answers 99% of the time produces fabricated answers 1% of the time, and the 1% looks identical to the 99% from the outside. The customer cannot tell when they got the fabricated one. The company cannot tell either, until the customer complains publicly.

**The mathematical reality:** Probabilistic generation cannot guarantee adherence to a non-probabilistic constraint. "The bot will probably cite real policy" is not a control. It is a hope.

### Output Filters Are Behind the Failure

The standard architectural answer is to add output filtering — a classifier that examines the bot's response before it reaches the customer. This pattern fails for three structural reasons:

1. **The filter is also AI.** The classifier that decides whether the bot's response is "policy-compliant" is itself a language model. It has its own false-negative rate. Fabricated policy that *sounds* plausible gets through the filter because plausible-sounding policy is exactly what the filter is trying to recognize.
2. **The filter does not know the policy.** Output filters check for obvious problems (profanity, PII, hate speech). They do not check whether the policy citation in the response actually matches the company's real policy library. To check that, the filter would need to be deterministic — at which point it stops being a filter and starts being UCP.
3. **The filter sees only the response.** It does not see the customer's history, the account state, the entitlements, the prior conversations — all the context that would let it know whether the action the bot is proposing is even allowed for this specific customer.

### Human-in-the-Loop Is a Volume Bottleneck

The fallback answer is "we have human review for anything sensitive." In practice this fails on three axes:

1. **Volume.** A bot handling 100,000 inquiries per month cannot have human review on every response. Companies that try collapse the bot into a triage layer and absorb the cost they were trying to avoid.
2. **Latency.** Customers expect sub-30-second responses. Human review takes minutes. The customer churns before review completes.
3. **The reviewer is reviewing AI output.** The reviewer has the same problem the customer does — fabricated policy looks plausible. The reviewer rubber-stamps the bot's response because the bot's response *reads correctly*.

### Logs Are Not Evidence

After an incident, the company turns to its logs. The logs show what the bot said. They do not show why the bot said it, whether the bot was authorized to say it, or what policy the bot was operating under at the time. When the regulator (or plaintiff, or angry customer) asks the company to *prove* the bot's response was not fabricated, the logs cannot answer the question. They show the output. They do not show the authority chain.

## Current Solutions: RAG, Constitutional AI, and Guardrails

### How the Market Currently Handles This

Three approaches dominate today:

1. **RAG (Retrieval-Augmented Generation)** — Provide the bot with documents at inference time and instruct it to cite from those documents. Pinecone, Weaviate, and similar vector databases ride this pattern.
2. **Constitutional AI / Self-Critique** — Have the bot evaluate its own response against a constitution before releasing it. Anthropic's published patterns and Inflection's earlier work explore this.
3. **Guardrails frameworks** — NeMo Guardrails, Guardrails AI, and proprietary classifier stacks layered on top of the bot's output.

**What this provides:**
- RAG reduces fabrication frequency by giving the bot a grounded source.
- Constitutional approaches catch some categories of obvious violation.
- Guardrails frameworks block well-known bad patterns.

### Why These Solutions Fall Short

**1. RAG Reduces Fabrication; It Does Not Eliminate It**
A bot with RAG access to real policy docs still fabricates. The retrieval step is itself probabilistic — the bot may retrieve the wrong document, retrieve a partial document, or ignore the retrieval entirely if its base model "knows" a different answer with high confidence. The Cursor support bot likely had access to real Cursor documentation. It fabricated anyway.

**2. Self-Critique Asks the Liar to Audit Themselves**
The same model that produces the response evaluates the response. The failure modes correlate. Models that are over-confident about fabricated content are over-confident about their self-evaluations of that content. The technique is useful in some contexts; it is not a guarantee.

**3. Guardrails Catch Categories, Not Specifics**
A guardrail can catch "don't curse at customers" or "don't share other customers' data." It cannot catch "don't claim a refund policy exists when it doesn't" — because that requires knowing the actual refund policy, which a regex pattern cannot encode.

**4. None Produce Court-Defensible Receipts**
When the customer or regulator demands proof that the bot was operating within authorized parameters at the time of the incident, none of the market solutions produce a cryptographically signed, replayable receipt of what the bot was permitted to say and what it was denied from saying. They produce probabilistic logs, which are not evidence.

## How UCP Is Different

**1. The Gate Is Pre-Response, Not Post-Hoc**
UCP intercepts the bot's intended response *before* it leaves the application. The customer never sees a response that the policy gate did not admit.

**2. Policy Maps to Real Authority, Not Plausible-Sounding Text**
A UCP rule that says "any refund > $50 requires named-authority approval" matches the *effect* of the bot's intended action — issue a refund — not the text the bot used to describe it. The bot cannot phrase its way past the rule.

**3. Every Customer Touch Carries a Signed Receipt**
Every response the bot ships to a customer is accompanied by a cryptographic receipt naming the policy that admitted it, the authority chain, and the rule set version in force. The bot's conversation is, by construction, replayable.

**4. Fabrication Is Architecturally Bounded**
Responses that cite policies must be grounded in the company's actual policy library — UCP's policy-citation rule requires the cited policy to exist as a verifiable artifact. The bot cannot cite a policy that is not in the library, because the policy gate will not admit such a response.

**5. The Same Receipts Serve Customer, Regulator, and Auditor**
When the customer asks "show me the policy you cited," when the regulator asks "prove the bot was authorized to make that statement," and when the auditor asks "show me your controls over customer-facing AI" — the answer is the same artifact, queried different ways.

**6. Cross-Channel Coverage**
The same policy surface applies whether the bot is responding in email, chat, voice, or in-product messaging. The policy fires on the action, not on the channel.

## The UCP Solution: Admission Before the Customer Sees Anything

### What If Every Bot Response Was Pre-Authorized?

Imagine a customer-facing bot architecture where every response — every policy citation, every refund offer, every account modification, every escalation — passes through a policy gate before the customer receives it. The bot proposes the response; the policy disposes; the customer sees the response only if the policy admits it. Responses that violate policy never ship. The bot, the customer, and the auditor all operate from the same authority chain.

This is UCP applied to the customer-facing surface. The architecture is the same as the coding-agent case; the policies are different.

### The Response Admission Hook

UCP integrates with the bot's response pipeline at the moment the bot has decided what to say but before the response transits to the customer. The intended response is converted into a structured action object: response type (informational, refund, policy-citation, account-change, escalation), target customer, claimed policies cited, monetary value at stake, downstream effects. The action object is submitted to the UCP policy engine.

A typical policy fragment for a financial-services support bot:

```
rule refund_authority_required:
  when action.type == "response_with_refund"
    and action.refund_amount > 50.00
  then deny with reason="Refunds exceeding $50 require human
    review per policy REF-2024-03. Escalate to queue 'finance_review'."

rule policy_citation_grounded:
  when action.type == "response_with_policy_citation"
    and action.cited_policy_id not in policy_library.active_policies
  then deny with reason="Cited policy does not exist in the authoritative
    policy library. Rephrase using only policies from policy_library or
    escalate to a human agent."
```

The first rule binds refund authority to the monetary effect of the action, not the bot's claim about authorization. The second rule binds policy citations to a verifiable source of truth — the company's actual policy library, exposed to UCP as a structured artifact.

### Cryptographic Receipts for Every Customer Touch

Every customer-facing message — whether the bot generated it or a human agent did — carries a signed receipt. The receipt is portable: the customer can request it, the regulator can demand it, the auditor can sample it. The receipt names the policy that admitted the response, the authority chain, and the rule set version in force at the time.

When the customer asks "where does it say that?", the answer is in the receipt. When the regulator asks "prove the bot was not operating outside its authority on Tuesday afternoon," the answer is the receipt log, replayable on examiner hardware.

### Grounded Policy Citation

UCP's policy library is a structured artifact — every refund rule, every coverage policy, every entitlement table — exposed to the policy engine as queryable, versioned data. When the bot intends to cite a policy, the policy citation must reference an entry in this library. If the policy does not exist, the gate denies the response. The bot cannot fabricate a policy citation, because the gate verifies the citation against ground truth before admitting it.

This eliminates the Cursor incident pattern structurally. A bot operating inside UCP cannot tell a customer that a non-existent device-restriction policy is "a core security feature" — there is no such policy in the policy library, the policy_citation_grounded rule fires, and the response never ships.

### Channel-Agnostic Enforcement

The same UCP policy set applies whether the bot is responding in:
- Email (intercepted at the response queue)
- Chat / chatbot (intercepted at the conversation API)
- Voice (intercepted at the response generation, before TTS)
- In-product messaging (intercepted at the message delivery layer)

This means the customer experiences consistent policy enforcement across channels, and the company has a single policy surface to maintain.

## Real-World Impact: The Numbers That Matter

### For Customers

**Before UCP:**
- Responses to identical questions vary across customers and across days.
- Cited policies cannot be verified — the customer must trust the bot.
- When the customer challenges the answer, the company cannot replay the conversation to investigate.

**After UCP:**
- Responses to identical questions are consistent because policy is deterministic.
- Every cited policy resolves to a real, verifiable artifact in the policy library.
- When the customer challenges the answer, the receipt provides the authority chain that admitted the response.

### For the Support Operation

**Escalation Quality:** Escalations from the bot to human agents arrive with structured context — the action the bot proposed, the rule that denied it, the customer history. Human agents spend their time solving problems, not reconstructing what the bot was trying to do.

**Volume Bot-Handled:** Organizations report 20–40% increase in volume the bot can safely handle, because the policy gate provides the safety floor that human review previously provided.

**Brand Risk:** The Cursor-class incident — bot fabrication going viral on social media — moves from "category of risk we manage with apologies" to "architecturally unavailable." This is not a marketing claim; it is a structural consequence of grounded citation.

### For the Organization

**Customer Trust Metrics:** Net Promoter Scores measured against bot-handled conversations align with NPS for human-handled conversations, rather than collapsing two-to-five-points below. Trust converges because consistency converges.

**Regulatory Posture:** For sectors with consumer-protection regulators (CFPB, FTC, state attorneys general, EU consumer authorities), UCP receipts are the artifact format that increasingly demonstrates compliance with disclosure, fair-dealing, and accurate-representation obligations.

**Litigation Risk:** When a customer disputes what the bot told them — and increasingly takes that dispute to court — the company can produce the signed receipt and the corresponding policy. The plaintiff's bar shifts from "the company won't share what really happened" to "the company has produced verifiable evidence."

## The Architecture: How It Works

### The Response Interception Point

UCP integrates with the bot's response delivery path through a thin SDK in the customer's response pipeline. For most architectures this is a single function call: `ucp.admit_response(intended_response, customer_context) → verdict`. The function returns admit, deny (with replacement instruction), or escalate.

For voice channels, the integration sits between response-generation and TTS — the same policy gate fires before any audio reaches the customer.

### The Policy Library

UCP maintains a structured policy library inside the customer's environment — every refund policy, every coverage rule, every entitlement, every disclaimer requirement. The library is the source of truth that grounded-citation rules reference. Updates to the policy library go through the same Mathematical Autopsy build discipline as UCP rules themselves: define, validate, prove, ship.

### The Customer Context Surface

UCP receives customer context — account state, entitlements, prior interaction history, regulatory classification — alongside each admission request. Policies can fire on context-dependent conditions: "this customer is in a state with stricter consumer-protection rules," "this customer has an open dispute and cannot be offered settlement," "this customer's account is past-due and cannot be issued credit." The context surface is provided by the customer's existing CRM and entitlement systems.

### The Receipt Distribution

Receipts are written to UCP's append-only vault inside the customer environment and made available through:
- Customer-facing receipt URLs (if the customer wishes to share evidence with their customer)
- Internal compliance dashboards
- Regulatory examination exports
- SIEM and observability stacks via OpenTelemetry

## Use Case Scenarios: Real Situations, Real Impact

### Scenario 1: The Refund That Wasn't Approved

**The Situation:** A customer contacts a SaaS support bot demanding a $400 refund for a service issue. The bot, trying to resolve quickly, offers the full refund.

**Before UCP:** The refund issues. The customer is satisfied. Three weeks later, finance discovers that the customer's contract terms explicitly disallow refunds above $50 without director approval. The bot has bypassed a control nobody knew it had to enforce. The finance team has to claw back the refund, which generates a complaint, which escalates to a small-claims filing.

**With UCP:** The bot proposes the $400 refund. The `refund_authority_required` rule fires (refund > $50). The bot receives a denial and an escalation instruction. The bot responds: *"I'd like to help resolve this. Because the amount you've requested exceeds my authority, I'm transferring you to a senior agent who can review your case."* The escalation lands with full context. The senior agent reviews, approves a $300 settlement consistent with the contract terms. The customer accepts. No claw-back. No complaint. No filing.

**The Impact:** A would-be operational and reputational mess becomes a routine escalation. The policy that the bot did not know about — and could not have known about, because it was buried in the contract — fired automatically.

### Scenario 2: The Class-Action Question

**The Situation:** Three months after a service outage, a class of customers files a complaint alleging that the company's support bot consistently misrepresented their refund eligibility during the outage period. The plaintiffs request, in discovery, evidence of what the bot was authorized to say.

**Before UCP:** The company produces chat logs. The plaintiffs argue the logs are incomplete — they show what the bot said, not what the bot was authorized to say. The judge orders production of training data, system prompts, retrieval indices, and source documentation. The discovery period extends six months. Legal fees escalate. The case settles for an inflated amount because the defense posture is "trust our logs."

**With UCP:** The company produces the receipt log, the policy set in force during the outage period, the cryptographic signatures, and the open-source verification tooling. The plaintiffs and their expert witnesses re-verify the receipts independently. The evidence shows that the bot was operating under tightened post-outage policies, that every refund offer above the standard threshold was correctly escalated, and that the bot did not represent ineligible customers as eligible. The case proceeds on its actual merits, which are narrower than originally alleged. The settlement aligns with the actual exposure.

**The Impact:** The litigation posture shifts from "the company's word against the plaintiff's" to "verifiable evidence either confirms or refutes the specific allegation." This is the structural change UCP enables, and it materially changes settlement economics.

### Scenario 3: The Multi-Channel Customer

**The Situation:** A high-value customer interacts with the company through three channels in a single week: email (to support), in-app chat (about an entitlement question), and voice (during a renewal call). Each channel uses a different AI assistant. The customer notices that the three assistants give them three different answers about what their plan includes.

**Before UCP:** The contradictions are real. Each AI assistant operates from its own retrieval index, its own training, its own context. The customer escalates angrily, citing the inconsistency. Customer success spends a week reconstructing what each assistant said and why. The customer churns.

**With UCP:** All three assistants run admission against the same UCP policy set and the same entitlement-resolution rules. The answers are consistent across channels because the underlying authority is the same. The customer's question — "what does my plan include" — returns the same structured answer whether they ask in email, chat, or voice. The customer renews.

**The Impact:** UCP's single policy surface across channels converts "AI-amplified inconsistency" into "AI-amplified consistency." This is the moat against the customer experience problem that multi-channel AI creates in companies without a unified gate.

## Key Metrics & KPIs: Measuring What Matters

### Response Quality Metrics

- **Grounded Citation Rate:** Percentage of bot responses citing policies that resolve to verifiable policy library entries.
  - **Target:** 100% (mathematically enforced by `policy_citation_grounded`).
  - **Impact:** Cursor-class fabrication structurally unavailable.

- **Cross-Channel Consistency:** Percentage of identical-question responses that produce equivalent answers across channels.
  - **Target:** ≥ 98% (variation only on context-dependent rules).
  - **Impact:** Customers experience the company as coherent.

- **Policy Currency:** Median age of policies cited in admitted responses.
  - **Target:** ≤ 7 days from policy update to citation freshness.
  - **Impact:** Policy changes propagate to customer-facing answers within a week.

### Customer Experience Metrics

- **Bot CSAT vs Human CSAT Delta:** Difference in customer satisfaction scores between bot-handled and human-handled conversations.
  - **Target:** ≤ 3 points lower (vs. 5–10 point gap typical without UCP).
  - **Impact:** Bot scales without trust collapse.

- **Escalation Quality:** Percentage of bot escalations that arrive with sufficient context for one-touch human resolution.
  - **Target:** ≥ 85%.
  - **Impact:** Human agent time is spent on resolution, not investigation.

- **Customer Complaint Reproduction Rate:** Percentage of customer complaints where the company can replay the exact prior bot conversation under examiner-equivalent verification.
  - **Target:** 100%.
  - **Impact:** Disputes resolve on evidence, not on testimony.

### Compliance and Risk Metrics

- **Unauthorized Action Prevention Rate:** Count of admission denials per quarter that prevented a material adverse action (unauthorized refund, ineligible upgrade, non-permissible disclosure).
  - **Target:** Track-only; informs policy tuning.
  - **Impact:** Quantifies the value of pre-execution governance.

- **Regulatory Inquiry Response Time:** Median time from regulator inquiry to delivered evidence package for customer-facing AI conduct.
  - **Target:** ≤ 24 hours.
  - **Impact:** Inquiries close on schedule rather than escalating.

## Integration Points: Fitting Into Your Workflow

### Support and CX Platforms

- **Zendesk, Intercom, Salesforce Service Cloud, ServiceNow CSM:** Native admission hooks via webhooks and middleware SDKs.
- **Genesys, Five9, Talkdesk (voice):** Pre-TTS admission integration.
- **Custom in-product support flows:** UCP SDK in the response delivery path.

### Bot and Conversational AI Platforms

- **OpenAI Assistants API, Anthropic Claude, Google Vertex AI:** Bot output passed to `ucp.admit_response()` before delivery.
- **In-house RAG stacks (LangChain, LlamaIndex, custom):** Admission integrated at the response-emission stage.
- **No-code chatbot builders:** Webhook integration for response admission.

### Policy and Knowledge Management

- **Document repositories (Confluence, Notion, SharePoint, Google Drive):** Source-of-truth for policy library ingestion.
- **CMS and KB platforms (Zendesk Guide, HelpScout, ServiceNow KB):** Policy library entries map to KB articles for grounded citation.
- **Custom policy management:** Direct API ingestion to UCP's policy library.

### Compliance and Records

- **SIEM (Splunk, Datadog, Sumo Logic):** Receipt stream via OpenTelemetry.
- **eDiscovery and litigation hold:** Receipt vault export to standard formats (CSV, Parquet, Arrow).
- **GRC platforms:** UCP findings into the same workflow as other compliance evidence.

## Why This Matters: The Compelling Case

### The Cost of Not Having This

The cost of customer-facing AI fabrication is not the cost of a single complaint. It is the cost of every subsequent operational decision the company makes about how much to trust its bots — and the cost of the trust-discount the customer base applies to every future bot interaction once they have heard about the fabrication once. Cursor's incident did not just hurt Cursor; it hurt the entire customer-facing-AI category by educating customers to distrust bots in general.

### The Value of Having This

UCP turns customer-facing AI from a brand risk into a brand asset. A bot that demonstrably cannot fabricate, that produces receipts customers can verify, that operates consistently across channels — this is the bot that earns the trust the human-staffed channels have built. The path to that bot is mathematical governance, not better prompts.

### The Competitive Advantage

The first cohort of companies whose customer-facing bots are operating under UCP-class governance will be the first cohort whose customers stop treating "talking to a bot" as a downgrade. That shift is worth more than the cost of UCP many times over — it materially changes Customer Lifetime Value, retention, and the cost-to-serve curve.

## Learn More

- **UCP Overview:** [Universal Control Plane README](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/README.md)
- **Other UCP Use Cases:** [Use Cases Index](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/use-cases/README.md)
- **The Six Failures:** [The Cursor Incident in Context](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)
- **SMARTHAUS Vision:** [The Full End-to-End View](https://github.com/SmartHausGroup/.github/blob/main/vision/README.md)

---

**UCP transforms customer-facing AI from a brand risk that companies manage with apologies into infrastructure that produces consistent, grounded, replayable responses — with cryptographic receipts the customer, the regulator, and the auditor can all verify independently.**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
