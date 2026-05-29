# CAIO — Orchestrator

**Latin: Coordinatio Auctus Imperium Ordo · Status: Active development · Integrated into TAI Y1 H2 milestone**

---

## What CAIO is

CAIO is the **orchestration layer** of the SMARTHAUS substrate. It coordinates service invocation across Components — routing requests, controlling access, sequencing dependencies, and ensuring that no Component executes without its preconditions satisfied.

Where UCP is the policy gate (does the action satisfy our rules?), CAIO is the execution coordinator (in what order, with what data flow, with what fallback if something fails?). CAIO is what makes the Component set composable into integrated experiences rather than a loose collection of independent services.

## What CAIO does

- **Service routing against formal contracts.** When TAI receives a request that needs governance from UCP, inference from SAID, and proven logic from MAE, CAIO routes the request through each Component in the right sequence with the right data — based on a formal routing contract, not orchestration code.
- **Access control across Components.** CAIO enforces which Components can call which other Components, with what authority, under what conditions. The Component-to-Component invocation graph is governed, not free-form.
- **Precondition enforcement.** No Component executes unless CAIO has verified that all preconditions for the call are satisfied — input shape, authority chain, dependency availability, rate limits, policy admission.
- **Fallback and degradation handling.** When a downstream Component is unavailable or returns an error, CAIO handles the degradation gracefully — surfacing a clear partial result rather than a cascading failure.

## How CAIO fits with the other Components

CAIO is the conductor of the SMARTHAUS Component orchestra:

- **[TAI](../../PALI/TAI/README.md)** delegates Component orchestration to CAIO. The user's intent reaches TAI; CAIO routes the work through the appropriate Components; TAI assembles the response.
- **[UCP](../UCP/README.md)** participates in the orchestration as the admission gate. CAIO routes potential actions through UCP before they execute.
- **[SAID](../SAID/README.md)** is called by CAIO when inference is needed; the inference envelope flows back through CAIO to the next Component in the routing graph.
- **[MAE](../MAE/README.md)** generated code participates in routing via the same contracts as other Components.
- **[MAIA](../MAIA/README.md)** intent records are input to CAIO's routing decisions.

## Status

CAIO is in **active development**. The orchestration core is in build; the routing-contract specification is matured; productization is integrated into the TAI Y1 H2 pilot milestone — CAIO is what makes TAI's Component orchestration mathematically governed rather than imperatively coded.

Repo: `caio-core`.

---

**[Other Components](../README.md)** · **[Substrate](../../Substrate/README.md)** · **[PALI](../../PALI/README.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
