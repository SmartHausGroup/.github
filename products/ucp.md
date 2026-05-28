# UCP — Universal Control Plane

**Current release: [UCP Studio v0.6.3](https://github.com/SmartHausGroup/UCP/releases/tag/ucp-studio-v0.6.3) · Signed for distribution · Pilot-ready**

---

## What it is

UCP is the runtime governance layer for AI systems. **Nothing executes that hasn't been admitted by policy.**

Most enterprise AI ships with governance written into PowerPoint slides and prayers. UCP makes governance an executable contract: every action — model call, tool invocation, agent step, data access — passes through a policy gate before it runs. The gate produces a cryptographically signed record of *what* was attempted, *who* attempted it, *under what authority*, and *what was decided.* The record is portable, replayable, and admissible.

If policy says no, the action does not happen. There is no application-layer override.

## The failures it closes

UCP is the answer to two of the [Six Failures](../six-failures/):

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

## How to engage

We are taking on a small number of design partners in regulated industries for the next phase. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with your AI deployment context and governance constraint.

---

**[← Back to SMARTHAUS](https://github.com/SmartHausGroup)** · **[The Six Failures](../six-failures/)** · **[SAID →](./said.md)**
