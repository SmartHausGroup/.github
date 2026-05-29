# SMARTHAUS Components

**The seven mathematical-governance products that compose into [PALI](../PALI/README.md) — and that deploy standalone in enterprise contexts.**

---

## What Components are

Components are the SMARTHAUS products that customers deploy directly. Each Component is a mathematical operator on AI behavior — a contract the action has to satisfy, a verdict, and a signed record anyone can verify later. Each Component is built under [Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md) discipline. Each Component ships independently and composes with the others into the [PALI](../PALI/README.md) experience delivered by [TAI](../PALI/TAI/README.md).

Seven Components are in active development. Three are pilot-ready today.

## Pilot-ready Components

### [UCP — Universal Control Plane](./UCP/README.md)
**Current release: v0.6.3 · Signed for distribution · Pilot-ready**

Runtime governance for AI systems. Nothing executes that hasn't been admitted by policy. Every action carries a cryptographically signed authority chain.

Closes the **PROVE** and **PREVENT** [Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md).

Four canonical deployments documented in depth: [coding agents in regulated codebases](./UCP/use-cases/01_coding_agents_regulated_codebases/README.md) · [customer support agents](./UCP/use-cases/02_customer_support_agents/README.md) · [internal automation across M365/Salesforce/SAP](./UCP/use-cases/03_internal_automation_agents/README.md) · [bounded autonomous workflows](./UCP/use-cases/04_bounded_autonomous_workflows/README.md).

### [SAID — Deterministic Inference Engine](./SAID/README.md)
**Current release: v0.2.5 · Signed for distribution · Pilot-ready**

GPU-first deterministic inference. Same input, same fixed context, same output. Every time. Every model. Frontier models become interchangeable underneath your application logic.

Closes the **REPLAY** failure.

Four canonical deployments: [credit decisioning under fair lending](./SAID/use-cases/01_credit_decisioning_fair_lending/README.md) · [insurance underwriting and pricing](./SAID/use-cases/02_insurance_underwriting_pricing/README.md) · [clinical decision support](./SAID/use-cases/03_clinical_decision_support/README.md) · [fraud, sanctions, and AML adjudication](./SAID/use-cases/04_fraud_sanctions_aml/README.md).

### [MAE — Mathematical Autopsy Engine](./MAE/README.md)
**Status: Foundation in place; deployment build under construction**

The build authority underneath every SMARTHAUS product. The engine that enforces Mathematical Autopsy — defines, validates, proves, and embeds verified properties inside customer software. Customer owns the result.

Closes the **BIND** and **SPECIFY** failures.

Four canonical deployments: [medical-necessity logic in payer adjudication](./MAE/use-cases/01_medical_necessity_logic/README.md) · [eligibility and benefits determination](./MAE/use-cases/02_eligibility_benefits/README.md) · [regulatory disclosure and submission generation](./MAE/use-cases/03_disclosure_submission/README.md) · [capital, KYC, and AML calculations](./MAE/use-cases/04_capital_kyc_aml_calculations/README.md).

## In active development

### [MAIA — Intent Engine](./MAIA/README.md)
**Latin: Mens Animus Intentio Anima**

Figures out what the user actually wants. Classifies intent and refines it through reinforcement learning. The reasoning layer that turns raw user input into structured intent records the rest of the substrate can act on.

Y1 H2 pilot target.

### [MGE — Mathematical Governance Engine](./MGE/README.md)

Governance running as a sidecar inside the customer's application. The runtime that enforces the proven properties MAE generates. Where UCP gates *external* AI actions, MGE gates *internal* application behavior — bringing the same mathematical governance discipline inside the customer's own software.

Active development; Y2 pilot target.

### [CAIO — Orchestrator](./CAIO/README.md)
**Latin: Coordinatio Auctus Imperium Ordo**

Orchestrates services and controls access across the SMARTHAUS substrate. Routes requests against formal contracts; nothing executes unless preconditions are met. The execution-coordination layer that lets TAI orchestrate Components and substrate primitives without bespoke wiring.

Active development; integrated into the TAI Y1 H2 milestone.

### [VEE — Math, Privacy, and Reinforcement-Learning Kernel](./VEE/README.md)
**Latin: Voluntas Engine**

Lyapunov stability utilities, quantum-inspired compute (native C++ pybind11 over Eigen), differential-privacy primitives, and an RL substrate. Consumed by MAIA, UCP, SAID, and other Components via native import or an optional FastAPI surface.

Active development; powers the math kernel that several other Components depend on.

---

## How Components compose

The Components are designed to deploy independently *and* to compose into integrated experiences. Three composition patterns matter:

**Standalone enterprise deployment.** A customer deploys UCP for runtime governance of AI agents. Or SAID for deterministic inference. Or MAE through the Applied-MA engagement. Each Component delivers its own value without requiring the others.

**Cross-Component reinforcement.** When multiple Components deploy at the same customer, they reinforce each other. SAID's deterministic envelopes flow into UCP's signed admission records. MAE's proven code embeds policies that UCP's runtime enforces. Each additional Component compounds the value of the others.

**PALI integration through TAI.** The full Component set integrates into the PALI experience delivered by TAI. The user's personal AI inherits governance from UCP, inference determinism from SAID, proven properties from MAE, intent classification from MAIA, orchestration from CAIO, math primitives from VEE, and governance-inside-app from MGE — without the user needing to know any of those Components exist.

---

## How to engage

Pilots on UCP, SAID, and MAE are open in regulated industries — financial services, insurance, healthcare, life sciences, defense. Reach out via **[smarthaus.ai](https://smarthaus.ai)** with your deployment context.

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
