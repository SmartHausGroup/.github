# UCP — Universal Control Plane

**Current release: [UCP Studio v0.6.3](https://github.com/SmartHausGroup/UCP/releases/tag/ucp-studio-v0.6.3) · Signed for distribution · Pilot-ready**

---

## What it is

UCP is the runtime governance layer for AI systems. **Nothing executes that hasn't been admitted by policy.**

Most enterprise AI ships with governance written into PowerPoint slides and prayers. UCP makes governance an executable contract: every action — model call, tool invocation, agent step, data access — passes through a policy gate before it runs. The gate produces a cryptographically signed record of *what* was attempted, *who* attempted it, *under what authority*, and *what was decided.* The record is portable, replayable, and admissible.

If policy says no, the action does not happen. There is no application-layer override.

## The failures it closes

UCP is the answer to two of the [Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md):

- **PROVE** — When a regulator or plaintiff demands the decision record, UCP produces a signed authority chain. Not logs. Proof.
- **PREVENT** — The admission gate runs *before* the action executes. The Replit "rogue agent" pattern (model output → destructive command → no intermediary → production database deleted) is structurally impossible inside UCP.

It also contributes to **LEAD** — UCP signed records are the artifact format regulators already accept under SR 26-2 and the EU AI Act.

## Who buys it

- **CISO or Chief AI Officer** in regulated industries — financial services, insurance, healthcare, life sciences, defense.
- **Budget origin:** security or governance, not "AI experimentation."
- **Typical trigger:** an AI deployment is blocked or constrained because the governance gap is too big to close with documentation alone.

## What ships today

- Universal Control Plane Studio — Tauri desktop application, macOS, signed.
- Loge tier (free) and Forge tier (premium) — license-determined feature gating.
- Local MCP broker — AI clients connect, policy gates fire inline.
- Reference packs in repo: `ma_guard`, `policy_pack`, `rate_guard_pack`, `siem_bridge_pack`, `artifact_vault_pack`, `agent_comm`, `ide_bridge`, `template_guard_pack`, `marketplace`, and others.
- Operation Center node-registration + heartbeat schemas published.
- Release signing in CI is forbidden by policy; release authority stays with controlled keys.

## Use cases

UCP applies wherever AI agents are taking actions in production. Four canonical deployments are documented in depth:

1. **[Coding Agents in Regulated Codebases](./use-cases/01_coding_agents_regulated_codebases/README.md)** — Cursor, Claude Code, Codex, and Devin operating inside financial-services or healthcare engineering organizations. UCP gates every file write, every git push, every command exec. The "Replit DROP DATABASE" pattern is structurally unavailable.
2. **[Customer-Facing Support Agents](./use-cases/02_customer_support_agents/README.md)** — Cursor-style fabrication and unauthorized concessions. Every refund, account change, and policy-cite passes admission. No silent invention.
3. **[Internal Automation Agents in M365 / Salesforce / SAP](./use-cases/03_internal_automation_agents/README.md)** — RPA-style agents acting across enterprise SaaS. Every cross-system write gated; every action carries a signed authority chain.
4. **[Bounded Autonomous Workflows](./use-cases/04_bounded_autonomous_workflows/README.md)** — Treasury, trading desks, claims automation. Hard-lockdown workspaces where an agent is allowed to operate, but only inside a mathematically bounded sandbox.

**[See all UCP use cases →](./use-cases/README.md)**

## How to engage

We are taking on a small number of design partners in regulated industries for the next phase. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with your AI deployment context and governance constraint.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
