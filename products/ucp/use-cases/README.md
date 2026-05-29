# UCP Use Cases — Where Runtime Governance Lives

**Status:** Public Documentation
**Last Updated:** 2026-05

## Overview

This directory contains four in-depth use cases for the **Universal Control Plane (UCP)** — the runtime governance product that gates AI agent actions before they execute. Each use case is a white paper covering the operational problem, why existing market solutions fall short, how UCP closes the gap by construction, and the measurable outcomes for the organization adopting it.

UCP applies wherever AI agents are doing things — writing code, talking to customers, moving data, making decisions, executing commands — and where the cost of an unauthorized or hallucinated action is more than a refund.

## Use Cases

### 1. Coding Agents in Regulated Codebases
**Directory:** `01_coding_agents_regulated_codebases/`
**Problem:** Cursor, Claude Code, Codex, Devin, and Cline are operating inside financial-services, healthcare, and government engineering organizations — running shell commands, writing files, pushing branches, executing tests. Without an admission gate, a single hallucinated command can wipe a production database or push unreviewed code to a regulated repo.
**UCP Solution:** Every action the agent attempts passes through a policy gate before execution. Blocked actions never fire. Allowed actions carry a signed authority chain.
**Key Value:** The "Replit DROP DATABASE" pattern (July 2025, 1,200 executive records wiped) is structurally unavailable. SR 26-2 and EU AI Act artifact requirements are produced automatically.

### 2. Customer-Facing Support Agents
**Directory:** `02_customer_support_agents/`
**Problem:** Support bots invent policies that do not exist, issue unauthorized refunds, cite contradictory information across users, and erode trust in days. Cursor's April 2025 support-bot incident is the canonical case — fabricated company policy, mass subscription cancellations, no replay capability.
**UCP Solution:** Every customer-facing action (policy citation, refund, account change, plan modification, identity verification, escalation) passes through admission against the customer's actual policy library before the agent sends a single word.
**Key Value:** Customers receive consistent, policy-grounded answers. The vendor can replay any conversation under examiner or plaintiff scrutiny. Brand damage from fabrication is eliminated structurally.

### 3. Internal Automation Agents in M365, Salesforce, and SAP
**Directory:** `03_internal_automation_agents/`
**Problem:** RPA-style agents are increasingly running across enterprise SaaS — reading Outlook, writing to Salesforce, updating SAP records, posting Slack messages, scheduling meetings, transferring files. The blast radius of a misbehaving agent in this layer spans every system the agent has credentials for. There is no native cross-system gate.
**UCP Solution:** UCP sits between the agent and every connected enterprise system. Every cross-system action is gated against the organization's data-classification, access-control, and segregation-of-duties policies before it executes.
**Key Value:** The agent operates with full access but cannot violate the organization's existing controls. SOX, HIPAA, GDPR, and SOC 2 obligations are enforced at the action layer, not at the audit layer.

### 4. Bounded Autonomous Workflows
**Directory:** `04_bounded_autonomous_workflows/`
**Problem:** Treasury operations, automated trading, claims adjudication, fraud disposition, healthcare prior-auth — workflows where the business wants the agent to operate autonomously but where a single mistake is catastrophic. Most organizations either disallow autonomy entirely (and lose the productivity) or allow it and absorb the tail risk.
**UCP Solution:** UCP enables **hard-lockdown workspaces** — mathematically bounded sandboxes where an agent is allowed to operate without per-action human approval but where the mathematical contract guarantees the agent cannot exceed the bounds of the workspace. Position limits, dollar limits, counterparty restrictions, time windows — all enforced before any action executes.
**Key Value:** Productivity of autonomous operation with the bounded risk of a hard-gated workflow. The board and the regulator both get the same answer: *the agent cannot do what it is not allowed to do, and we can prove it.*

## Quick Comparison

| Use Case | Primary UCP Feature | Key Differentiator | Enterprise Value |
|---|---|---|---|
| Coding Agents | Pre-execution command admission | Stops destructive operations at the syscall layer | Eliminates Replit-class incidents, SR 26-2 artifacts |
| Support Agents | Pre-response content admission | Blocks fabrication before customer sees it | Brand protection, replayable conversations |
| Internal Automation | Cross-system action admission | Single gate spanning M365 + Salesforce + SAP + Slack | SOX/HIPAA/GDPR/SOC 2 enforced at action layer |
| Bounded Autonomous | Hard-lockdown workspace | Autonomy with mathematically proven bounds | Productivity + bounded risk for high-stakes workflows |

## Common UCP Capabilities Used

Every UCP use case shares the same underlying capabilities:

- **Pre-execution admission gate** — the policy check happens *before* the action, not after.
- **Signed authority chain** — every admitted action carries cryptographic evidence of which policy allowed it, who requested it, and what was decided.
- **Append-only receipt log** — actions cannot be edited or deleted after the fact; the record is permanent.
- **Replayable evidence** — any historical action can be re-verified by an external auditor or regulator on open-source toolchain, without trusting SMARTHAUS or the customer.
- **Hard-fail enforcement** — when policy denies, the action does not happen. There is no application-layer override.
- **Mathematical Autopsy build discipline** — every UCP rule is mathematically defined and proven before it ships into a customer environment.

## How to Engage

UCP is pilot-ready and currently deployed in design-partner engagements at financial-services, healthcare, and software organizations. Pilots run 60–90 days with three engagement tiers based on environment scope. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with the use case that best matches your deployment context.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/ucp/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
