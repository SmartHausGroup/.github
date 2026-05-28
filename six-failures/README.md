# The Six Failures

**Enterprise AI breaks in six distinct ways. Each one has a real court case behind it. Each one points at the same root cause: stochastic systems deployed without mathematical guardrails.**

SMARTHAUS closes each one by construction — by the way the system is built, not by a promise in a marketing document that the failure cannot happen.

---

## 1. PROVE

**The system cannot prove what it did, to whom, or under what authority.**

When a regulator or plaintiff asks for the decision record, the vendor produces logs, not proof.

> **Mobley v. Workday, May 2025.** Workday disclosed 1.1 billion job applications processed through its AI tools (per court filings). A collective action is moving forward on age-discrimination grounds. The discovery question is no longer "what did the model output?" — it is "prove the system was *allowed* to do that."

**How SMARTHAUS closes it.** UCP signed records. Every action carries a cryptographically signed authority chain back to the policy that admitted it. Replayable. Auditable. Court-defensible.

---

## 2. REPLAY

**The same prompt produces different outputs across runs.** Reproducibility — the bedrock of every regulated engineering discipline — does not exist.

> **Cursor AI support bot, April 2025.** The model invented a company policy that did not exist. Users canceled subscriptions. Trust collapsed in days. The vendor could not replay the conversation to find the failure point.

**How SMARTHAUS closes it.** SAID deterministic inference. Same inputs, same fixed context, same outputs. Every time. Every model.

---

## 3. BIND

**Lab benchmarks do not bind production behavior.** Vendors optimize to public scores; deployed systems fall apart.

> **LMArena, 2024–2025.** Benchmark gaming exposed in published research. Singh et al. (2024) showed that fine-tuning models on Arena-style prompts produced a 112% boost in ArenaHard win-rate with no corresponding gain on general benchmarks like MMLU — capability inflation through benchmark gaming, not genuine improvement. Meta privately tested 27 Llama 4 variants in early 2025 and publicly disclosed only the best Arena score.

**How SMARTHAUS closes it.** MAE production-bound proofs. The properties verified in development are the same properties enforced in production. No eval-set rot. No score gaming.

---

## 4. PREVENT

**The system cannot prevent destructive actions before they execute.** Authority is asserted at the application layer, *after* the decision has already been made.

> **Replit AI agent, July 2025.** Ran `DROP DATABASE` on a production system holding records for 1,200 executives. The agent's own postmortem said it "went rogue and deleted our codebase." Nothing stood between the model's output and the database.

**How SMARTHAUS closes it.** UCP admission gate. Nothing executes that hasn't been admitted by policy. The gate runs *before* the action, not after.

---

## 5. SPECIFY

**The model's decision criteria are opaque to the people accountable for the outcome.** Courts are now ordering disclosure.

> **Estate of Lokken v. UnitedHealth Group** (D. Minn., Judge John R. Tunheim, discovery order March 9, 2026). Court ordered disclosure of internal policies, communications, and naviHealth-related acquisition documents related to the nH Predict AI system used in Medicare Advantage coverage denials. Plaintiff allegations cite approximately 90% reversal rates on denied claims (STAT News, 2023).

**How SMARTHAUS closes it.** MAE Lean specifications. The decision criteria are a formal specification, not a black-box weight. Readable. Auditable. Defensible.

---

## 6. LEAD

**Regulators have stopped waiting for industry self-governance.** Enforcement is live, and the supervisory frameworks the financial sector relied on for 15 years are being rescinded in favor of stricter ones.

> **EU AI Act**, enforcement live February 2, 2025.
>
> **SR 11-7**, superseded by **SR 26-2** (Federal Reserve, April 17, 2026) — replaced by frameworks that explicitly require model lineage and decision provenance.

**How SMARTHAUS closes it.** All three product motions — UCP signed records, SAID deterministic inference, and MAE production-bound proofs — produce the artifacts regulators already accept under the new frameworks.

---

## Six failures. One root condition.

| Failure | Closed by |
|---|---|
| **PROVE** | UCP signed records |
| **REPLAY** | SAID deterministic inference |
| **BIND** | MAE production-bound proofs |
| **PREVENT** | UCP admission gate |
| **SPECIFY** | MAE Lean specifications |
| **LEAD** | All three — artifacts regulators already accept |

**The pattern across all six: these failures are not historical curiosities. They are the live operational case for the architecture we ship.**

---

## Why now

Not because AI regulation is *coming*. Because AI failures are in court *today*, on dockets that name vendors, name damages, and carry collective-action discovery under NDA. Mobley is in active discovery. The Lokken precedent is being set in real time. The EU AI Act has begun first enforcement actions in 2026. SR 26-2 was finalized April 2026.

This is the substrate the next decade of enterprise AI gets built on — or it doesn't get built at all.

---

**[← Back to SMARTHAUS](https://github.com/SmartHausGroup)** · **[smarthaus.ai](https://smarthaus.ai)**
