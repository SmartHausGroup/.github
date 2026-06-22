# SmartHausGroup/.github - North Star

> Source of truth for scope, metrics, and guardrails. Everything in this repo must align to this document.
> Governed: changes to architecture / invariants / `unified-calculus/` require a matching update here (enforced by the doc-drift gate).

## Vision
The organization profile repository presents SMARTHAUS public GitHub context while obeying the same deterministic governance floor as product repositories.

## Scope
- **In scope:** organization profile content, repository governance controls, CI/CD conformance, agent instruction bindings, and supply-chain policy gates.
- **Out of scope:** product runtime code, package publication, deployment automation, and AICP/UCP runtime promotion.

## Metrics (must stay true)
| Metric | Target | Gate |
|---|---|---|
| Traceability | 100% — every shipped function traces to a lemma/plan | conformance |
| Determinism | seeded artifacts, no NaN/Inf | determinism gate |
| Receipt of truth | every governed action emits a decision + receipt | action log + scorecard |
| Org profile safety | no unvetted secrets or mutable workflow bypasses | security + supply-chain |

## Guardrails
- Fail-closed: unknown / stale / unproven → reject, never silently degrade.
- Notebook-first for math/algorithm work; extract to code only after a green scorecard.
- Hard enforcement lives in hooks / CI / rulesets, never in advisory text.

## Foundational calculus
This repo consumes the shared SMARTHAUS repository CI/CD conformance standard through `configs/ucp/repo_cicd.yaml`; it does not define a product runtime calculus.
