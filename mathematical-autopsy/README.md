# Mathematical Autopsy

**The construction discipline that produces every SMARTHAUS product.**

---

## What it is

Mathematical Autopsy (MA) is the development methodology underneath everything SMARTHAUS ships. It is the answer to a deceptively simple question: **what would software look like if every claim it made had to be mechanically proven before the code could be released?**

The short answer: it looks like the SMARTHAUS codebase. Roughly 75 named mathematical lemmas. Roughly 700 machine-enforced invariants. Roughly 880 runnable notebook proofs. All wired into continuous integration. No demo path that bypasses the gates.

The longer answer is below.

---

## Why "autopsy"

In medicine, an autopsy is a post-mortem examination that finds the cause of death.

In SMARTHAUS, a Mathematical Autopsy is the *pre-mortem* examination of the math — done before any code is written, before any system is deployed, before any customer is exposed. We dissect the mathematical foundation of what we are about to build. We identify every property that must hold, every transformation that must be reversible, every invariant the system must preserve under stress. We prove those properties hold *in the math*. Only then do we write code that implements the math.

The order is never reversed. Code is not where correctness is established. Code is where mathematics is implemented.

---

## The 9-phase pipeline

Every MA-built component moves through nine governed phases. Each phase produces artifacts that are committed to the repository and verified in CI. The aggregate scorecard must be green at phase 9 or the `release` target refuses to run.

1. **Intent** — Specify what the system must always do and must never do. No code. No prose. Structured claims.
2. **Mathematical foundation** — Formalize the problem in the appropriate mathematical language (set theory, linear algebra, type theory, complex analysis, whatever the substrate demands).
3. **Lemmas** — State the proof obligations. Each lemma is a claim that must be proven before the work can advance.
4. **Invariants** — State the properties that must hold at every point in the system's lifetime. Each invariant becomes a machine-enforceable check.
5. **Notebook verification** — Build executable proofs. Each notebook either passes (the claim holds) or fails (the claim is false, and the system cannot ship).
6. **Scorecards** — Aggregate the pass/fail evidence into a single verifiable artifact, cryptographically pinned.
7. **CI binding** — The build, release, and runtime-extraction targets refuse to run unless the aggregate scorecard is green.
8. **Signed receipts** — Every output artifact carries a cryptographic chain back to the proven properties.
9. **Deployment** — Production behavior is bound to the proven properties. The properties verified in development are the properties enforced in production.

---

## What this rules out

- **"We tested it" instead of "we proved it."** Tests sample behavior. Proofs cover the space.
- **Eval-set rot.** The properties verified at training are the properties enforced at inference. There is no benchmark to game.
- **Demo path divergence.** No path through the system bypasses the gates. The system that demos is the system that ships.
- **Untraceable failure.** When a property fails in production, the failure is traceable to a specific lemma, invariant, scorecard, and signed receipt. The "we don't know why" answer is structurally unavailable.

---

## What this enables

- **[UCP](../products/ucp.md)** ships under MA — every admission decision traces to a proven authority chain.
- **[SAID](../products/said.md)** ships under MA — every inference output traces to a proven determinism contract.
- **[MAE](../products/mae.md)** is MA externalized — the engine that lets customer teams adopt the discipline themselves.
- **[The Six Failures](../six-failures/)** are closed not by promises but by construction — by the mechanical impossibility of shipping software that violates the proven properties.

---

## The current numbers

Across the SMARTHAUS active codebase:

- **~75 named lemmas** (`L1` through `L12+` series in active products)
- **~700 machine-enforced invariants** (YAML-defined, CI-verified)
- **~880 runnable notebook proofs**
- **~265 scorecards** binding the above into release gates

None of these are decorative. Every one of them either passes in CI or the corresponding release does not happen.

---

## How to engage

- **As a customer:** through **Applied-MA** — embedded engagement to bring your own systems under MA discipline. Reach out via [smarthaus.ai](https://smarthaus.ai).
- **As a partner:** through the [MAE product roadmap](../products/mae.md) once the deployment build is generally available.
- **As a researcher or reviewer:** through joint work on the substrate (see [Princeton →](../research/princeton.md)) or by reading the [formal mathematical thesis](../thesis/).

---

**[← Back to SMARTHAUS](https://github.com/SmartHausGroup)** · **[The Six Failures](../six-failures/)** · **[MAE Product →](../products/mae.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/ucp.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/pali/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/framework.md)** · **[smarthaus.ai](https://smarthaus.ai)**
