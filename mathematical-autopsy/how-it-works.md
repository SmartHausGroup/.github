# Mathematical Autopsy: How to Build Deterministic Systems with Probabilistic AI

Every AI system in production today has the same dirty secret: the AI that writes the code is guessing. Not "approximating." Not "estimating." Guessing. Large language models are probabilistic token generators — they sample from probability distributions over sequences, conditioned on prompts and prior context. Run the same prompt twice and you get different code. Different module boundaries, different naming, different error handling, different architecture. The code works. It just isn't the *same* code.

For exploratory work, this is fine. For production systems that must be audited, reproduced, and defended — in finance, healthcare, security, and regulated infrastructure — this is structural risk. And it compounds. 90% accuracy per step sounds good until you realize that over five steps, you're at 59%. Over ten steps, you're at 35%. The system works until it doesn't, and when it doesn't, no one can tell you why — because the architecture itself was generated probabilistically.

Mathematical Autopsy (MA) was built to solve this. Not by making AI deterministic — that's impossible. By building a deterministic scaffold *around* AI that makes correctness external, explicit, executable, and enforced.

**AI proposes. Proof disposes.**

The result is a development framework where probabilistic AI is used to its full creative potential — exploring solution spaces, proposing architectures, generating implementations — but nothing ships until it survives deterministic verification. The AI is the hypothesis generator. The framework is the falsification engine. What survives is proven. What doesn't is refined until it is.

This document traces the arc of how MA works — from the first articulation of intent to the extraction of proven runtime code. Every step builds on the one before it. Skip a step and the chain breaks.

Every formal AI development lifecycle standard — NIST AI RMF 1.0, ISO/IEC 5338, ISO/IEC 42001 — defines the same stages: Plan and Design, Data and Input, Model Build, Testing and Evaluation, Deployment, Operation and Monitoring. Cross-cutting governance functions (Govern, Map, Measure, Manage) and continuous Test, Evaluation, Verification, and Validation (TEVV) run alongside. MA covers every one of them. But it inverts the sequence and changes what each stage actually means.

In the standard AI lifecycle, you plan, then build, then test, then deploy, then monitor. Testing is downstream of building. Monitoring is the last thing you think about. Governance is a cross-cutting concern that everyone acknowledges and nobody enforces mechanically.

MA flips this entirely. The monitoring contracts (invariants with rollback criteria) are built in Phase 3 — before a single line of implementation code exists. The testing infrastructure (notebooks, artifacts, scorecards) constitutes the majority of the process, not an afterthought bolted on at the end. Governance is not cross-cutting — it is the skeleton that every phase hangs from. And code is the last artifact produced, not the first.

But MA does not merely rearrange the standard. It exposes how shallow the standard actually is. The NIST lifecycle asks "did you plan?" MA asks "can a machine verify your plan?" The standard asks "did you test?" MA asks "is your test deterministic, seeded, and does it produce replayable evidence?" The standard asks "do you monitor?" MA asks "did you define the monitoring contract before the code existed, and does it fail-closed?" Every stage the standard defines, MA covers — and then goes further than any standard has gone, because the standards were written for a world where humans write code and other humans review it. MA was built for a world where AI writes code and machines must verify it. That requires a fundamentally higher bar.

The eight phases that follow map to every stage and function in the formal AI SDLC. The order is different. The depth is different. The enforcement is different. That is the point.

---

# Act I — Define Before You Build

*Every system that failed in production had code that "worked." What it didn't have was a clear definition of what "worked" means.*

The most dangerous failure mode in AI-assisted development is not wrong code. It's correct code for the wrong system. A language model can produce flawless implementations of things you never asked for — and if you don't define what you actually need before the model starts generating, you'll discover the mismatch in production, not in development.

MA inverts the traditional sequence. Instead of Code → Test → Debug → Refactor, MA enforces Intent → Math → Invariants → Proof → Code. Code is the *last* thing that happens, not the first. This is the foundational inversion that makes everything else possible.

---

## 1. Intent Articulation

Before a single equation is written, before a single line of code is generated, someone must answer these questions in plain language:

- **What problem are we solving?** Not "build feature X." What behavior must the system exhibit? What must never change?
- **What does success look like?** Measurable outcomes. Numbers. Thresholds. Not "it should be fast" — how fast, measured how, under what conditions?
- **What are the constraints?** What is explicitly out of scope? What are the non-goals?
- **What does failure look like?** When something goes wrong, what happens? Does the system stop? Degrade? Retry? The answer cannot be "undefined."

This is not documentation for documentation's sake. This is the control surface that prevents the AI from solving the wrong problem. If intent is precise, AI can do most of the symbolic exploration. If intent is vague, AI will formalize the wrong system — and the proofs may still pass, because the wrong thing was proven correctly.

The gate to proceed: intent must be explicit enough that two engineers reading it would implement the *same* semantics. If they wouldn't, Phase 1 isn't done.

In formal AI lifecycle terms, this is the Plan and Design stage — but MA demands more than the standard's "objectives, context, and requirements." Intent in MA must be precise enough to survive mathematical formalization, invariant encoding, and deterministic verification downstream. The standard asks you to document what you want. MA asks you to document it well enough that a machine can check whether you got it. No standard, methodology, or framework in existence has ever made intent precision a formal gate — a gate where downstream machinery rejects your work if the intent was not specific enough to verify. This is new. And it matters because every system that shipped the wrong behavior had a requirements document that said the right thing in language too vague to enforce.

---

## 2. Mathematical Foundation

Once intent is precise, MA formalizes it. This is where "the system should be reliable" becomes equations, operators, state spaces, and boundary conditions.

MA treats every system as transformations over state spaces. Define a state space capturing the system's relevant internal state. Define the operators — the allowed transformations. Define what must remain true across those transformations. Define what happens at the boundaries.

This isn't academic math for its own sake. It's the difference between "rules" and "governance." Rules are advisory — probabilistic systems may ignore them. Operators and invariants define the *valid solution space* and create a basis for deterministic validation. A system prompt says "always handle errors gracefully." A mathematical foundation says "the transition function δ(s,e) is total and single-valued — every state-event pair has exactly one deterministic outcome, including failure."

The formalization produces: notation, equations, named thresholds, assumptions, and explicit boundary conditions. Every threshold is named — no magic numbers. Every boundary is specified — no undefined behavior. Every assumption is stated — because unstated assumptions are where systems break.

The gate to proceed: every threshold is named, every boundary is specified, and failure semantics are explicit.

Phases 1 and 2 together satisfy what the NIST AI lifecycle calls Plan and Design and Data and Input — the formalization of what a system accepts, transforms, and produces. But where the standard focuses on data collection, cleaning, and metadata documentation, MA focuses on defining the valid state space itself. Input governance in MA is not "clean your dataset." It is "define mathematically what a valid input is, what transformations are allowed, and what happens at every boundary." You cannot govern data you have not formally defined.

This is what formal verification has done for chip design for decades — Intel does not fabricate a processor without proving its arithmetic logic mathematically. MA brings that level of rigor to AI-assisted software development for the first time. No software development methodology — Agile, DevOps, SAFe, CMMI, none of them — has ever required mathematical formalization of system behavior as a precondition for writing code. They all assume you can test your way to correctness after the fact. MA assumes you cannot, and the empirical evidence from every major software failure in history supports that assumption.

---

# Act II — Create the Guarantees

*Mathematics describes what should be true. Invariants and lemmas make it enforceable.*

The mathematical foundation tells you what the system should do. But a specification sitting in a markdown file doesn't prevent anything. It needs to become machine-readable contracts that can be executed, checked, and enforced — automatically, on every build, with no human in the loop at the enforcement boundary.

---

## 3. Invariants

An invariant is a property that must always hold. In MA, invariants are not documentation. They are machine-readable, executable contracts tied to verification artifacts.

Each invariant is a YAML file with a stable ID, a human-readable summary, mathematical equations, named thresholds, acceptance assertions (artifact path + comparator + value), producer references (which notebook generates the evidence), and rollback guidance (what to do when it fails).

The critical design: acceptance assertions are not prose. They are executable. "The drift must be less than tolerance" becomes `max_drift_complex64 <= 1e-6`, checked against a specific field in a specific JSON artifact produced by a specific notebook. The machine can run this check without understanding what drift means. It just reads the number and compares.

Invariants come in tiers. Tier 1 (non-negotiable): safety, determinism boundaries, contract enforcement — always fail-closed. Tier 2 (release-critical): correctness bounds and performance constraints — fail-closed for production. Tier 3 (optimization): informative metrics, research targets — informational. Tiering prevents the common failure of formal systems: either everything is strict (velocity collapse) or nothing is strict (theater).

An invariant without a failure plan is incomplete. For every invariant, the question "what happens when this fails?" must have a deterministic answer — not "we'll figure it out" but "the system blocks promotion and reports exactly what violated what."

This is where MA does something no existing framework, standard, or methodology has done: it collapses three separate NIST functions into a single executable artifact. An invariant simultaneously serves as governance policy (the GOVERN function — what must be true and who owns it), risk identification with tiered severity (the MAP function — what can go wrong and how bad is it), and runtime monitoring contract (the Operation and Monitoring lifecycle stage — what to watch and when to rollback). In the standard AI lifecycle, these are separate concerns handled by separate teams at separate times — and the gaps between those teams are where production failures live. In MA, they are unified in one YAML file because they must be: a monitoring contract that does not match the governance policy is theater, and a risk register disconnected from runtime enforcement is a filing cabinet. Every organization that has suffered a production incident where "the policy said X but the monitoring checked Y" understands why this unification matters. MA makes it structurally impossible for governance, risk, and monitoring to disagree — because they are the same artifact.

---

## 4. Lemmas

Lemmas are the bridge between human understanding and machine enforcement. An invariant says *what* must hold. A lemma explains *why* it holds.

Each lemma is a formal claim: "under assumptions A, operator O preserves invariant I." It states the assumptions explicitly, references the thresholds (with provenance — which invariant is the source of truth), maps to a supporting notebook, and explains what would falsify it.

Lemmas make the system auditable. When a production system makes a consequential decision, an auditor can trace the chain: which invariant governs this? → which lemma justifies the invariant? → which notebook produced the evidence? → which artifacts prove it? This chain is what makes systems defendable in audits and post-incident investigations.

The practical rule: keep lemmas small and compositional. A lemma tied to one operator with explicit assumptions survives refactors. A mega-lemma that tries to justify an entire subsystem becomes dead governance weight that nobody reads.

In NIST terms, lemmas provide the formal risk documentation that the MAP function requires — but with teeth. A standard risk register says "this could go wrong." A lemma says "under these explicit assumptions, this operator preserves this invariant — and here is exactly what would falsify it." The difference is the difference between acknowledging risk and governing it. Every assumption is a testable claim. Every falsification condition is a notebook waiting to be written.

This is Karl Popper's falsification principle — the foundation of the scientific method — made operational in software engineering. Science does not prove theories true; it proves them not-yet-falsified. MA applies the same logic: a lemma is not proven correct by passing tests. It is proven not-yet-falsified by surviving every attempt to break it. No software development methodology has ever operationalized falsification as a first-class engineering practice. Risk registers document what might happen. Lemmas dare you to prove them wrong — and give you the exact conditions under which you could.

---

# Act III — Execute the Proof

*An invariant that isn't tested is a slogan. A lemma that isn't executed is a wish. The proof happens in notebooks — running code that generates evidence.*

---

## 5. Verification Notebooks

This is where MA departs from every other development methodology. The proof is not documentation. It is not a comment in the code. It is not a test that runs in CI. The proof is a Jupyter notebook that executes the mathematics, asserts the invariant conditions, and exports a JSON artifact that gates can check.

Notebooks in MA are not exploratory scratchpads. They are structured verification harnesses with a strict contract:

- **Seeded execution.** Every notebook runs with a controlled seed. No unapproved entropy sources. The same notebook, same seed, same environment produces the same artifact every time.
- **Implementation code lives here first.** Code is written directly in notebook cells — not imported from the codebase. The notebook is the source of truth. The codebase is the deployment target. This is the notebook-first principle that prevents untested code from entering production.
- **Atomic cells with assertions.** Each behavior is implemented in a cell, explained in a preceding markdown cell, and immediately followed by deterministic assertions. If the assertion fails, the notebook fails. If the notebook fails, the gate fails. If the gate fails, nothing ships.
- **Artifact export.** The notebook writes its results to a JSON file with a stable schema. This artifact is what the invariant's acceptance assertions check against. The artifact is replayable evidence — anyone can re-run the notebook and compare.

This is the machinery that makes "AI proposes, proof disposes" real. The AI can generate the implementation. The notebook executes it under controlled conditions. The assertions verify the invariants. The artifact records the evidence. If the AI got it wrong, the notebook catches it — deterministically, reproducibly, every time.

The falsification principle: notebooks are not demonstrations. They are counterexample generators. Adversarial inputs that violate assumptions. Boundary vectors that stress tolerances. Regression cases that reproduce prior failures. The highest-leverage notebook is the one that tries hardest to break the system — and fails.

This is where MA departs most dramatically from the standard AI lifecycle — and from every software development methodology that has ever existed. In NIST terms, verification notebooks simultaneously serve as the AI Model Build stage (implementation code is written here first — notebook-first development), the Testing and Evaluation stage (deterministic assertions verify every behavior against invariant thresholds), and the continuous TEVV function (verification and validation happen in every cell, not in a separate phase after deployment). The standard lifecycle separates these into sequential stages handled by different teams. MA fuses them into a single environment because separating "build" from "test" is precisely how untested code enters production.

In MA, there is no gap between writing code and proving it works. They are the same action, in the same cell, in the same environment. This eliminates an entire category of defects that every other methodology accepts as inevitable — the defects that live in the handoff between "the team that builds" and "the team that tests." In traditional development, those handoff gaps are where assumptions go undocumented, edge cases go untested, and integration failures go undetected until production. MA does not have handoff gaps because there is no handoff. The person who writes the code proves it in the same notebook, in the same session, before it can be extracted to the codebase. No methodology — not Agile, not DevOps, not TDD, not formal methods as traditionally practiced — has achieved this level of build-test fusion.

---

## 6. Artifact Generation

Notebooks produce artifacts — JSON files containing the metrics, measurements, and pass/fail results that gates need to make promotion decisions.

Artifacts are not secondary output. They are **the evidence surface**. The entire MA pipeline converges on this: can the gate read the artifact, check it against the invariant thresholds, and make a deterministic pass/fail decision?

Artifacts must be schema-stable (the fields don't change between runs), deterministically generated (same inputs produce same outputs), and referenced from invariants (every acceptance assertion points to a specific artifact field). This is what makes MA auditable: the evidence is not a story someone tells. It's a file anyone can inspect.

No NaN. No Inf. No missing fields. If an artifact is malformed, the gate treats it as a failure. Fail-closed, all the way down.

Artifacts are what make the NIST MEASURE function deterministic rather than aspirational. The standard asks organizations to "quantify and evaluate AI system risks." Most organizations interpret this as periodic reviews, dashboards, and meetings where someone presents slides about risk metrics. MA produces the actual numbers — schema-stable, deterministically generated, machine-readable — and wires them directly into automated gate decisions. Measurement in MA is not a quarterly review. It is a check that runs on every build, reads from every artifact, and blocks promotion if any value is out of range.

This is the kind of continuous, automated, evidence-based assurance that regulated industries have demanded for years and that no software methodology has ever delivered. Aerospace has flight data recorders. Pharmaceuticals have batch records. Financial services have trade audit trails. Software has had — until MA — nothing comparable. Artifacts are MA's answer: a deterministic evidence record, produced on every build, replayable by anyone, tied directly to the mathematical guarantees that govern the system. When an auditor asks "show me the evidence," the answer is not a presentation. It is a JSON file they can verify themselves.

---

# Act IV — Enforce and Ship

*The proof exists. The artifacts are generated. Now the question is: does anything actually prevent bad code from shipping?*

Every methodology claims rigor. MA enforces it. The enforcement layer is what separates "we follow best practices" from "the system will not allow non-compliant code to promote." Gates are not suggestions. They are automated checks with binary outcomes — pass or fail — wired into the build pipeline so that a human cannot accidentally (or intentionally) skip them.

---

## 7. Scorecard and Gates

MA culminates in a scorecard — a single aggregated decision surface that says whether the system is allowed to promote. Green or red. Ship or don't.

The gate chain works in layers:

1. **Core math checks** — deterministic, seeded, fast. Do the fundamental mathematical properties hold?
2. **Notebook execution** — run every verification notebook, generate every artifact. Does the evidence exist?
3. **Quality gates** — check invariant health, artifact integrity (no NaN/Inf), notebook plan completeness, scorecard status. Is the evidence valid?

The validation runs as a single command: `make ma-validate`. The output is a scorecard. If the scorecard is red, promotion is blocked. Not "flagged." Not "warned." Blocked. The CI pipeline returns non-zero and the merge is rejected.

Gates come in two categories: must-pass (fail-closed, always enforced) and recommended (informational, progressively hardened). This allows organizations to adopt MA incrementally — start with a small set of strict gates and expand as notebooks, invariants, and artifact contracts mature. But the trajectory is always toward strictness: any property you claim externally should eventually be fail-closed.

The evidence pack: when MA passes, it can emit a deterministic evidence bundle — the invariant registry, the notebooks and execution logs, the generated artifacts, the scorecard and decision policy, and the ADRs since last release. Auditors get a structured bundle instead of a story.

The scorecard is where the NIST MANAGE function and the Deployment lifecycle stage converge into a single automated decision. The standard says "implement responses to identified risks" and treats deployment as a stage where the built-and-tested system moves to production. MA's response is binary and mechanical: green means the system promotes, red means it does not. There is no "accept risk and proceed" for Tier 1 invariants. There is no deployment meeting where someone decides to ship despite failing checks. The gate is the deployment decision, and the gate is automated. This is what "fail-closed" means in practice: not a policy, but a pipeline that returns non-zero.

Every other framework — every one — leaves the ship/no-ship decision to a human. A human who can be pressured by deadlines. A human who can be convinced that "it's probably fine." A human who can be wrong. MA removes the human from the enforcement boundary entirely. The human defines the invariants (Phase 3) and the thresholds (Phase 2). The human writes the proofs (Phase 5). But the human does not decide whether the proofs passed. The machine decides. And the machine cannot be talked into shipping broken code. This is not a refinement of existing deployment practices. It is the first deployment framework where the enforcement boundary is fully automated and the evidence is fully deterministic.

---

## 8. Extraction to Runtime

Only now — after intent is defined, mathematics formalized, invariants created, lemmas written, notebooks executed, artifacts validated, and the scorecard is green — does code enter the codebase.

Code in MA is a compiled artifact of verified constraints. It is extracted from notebooks using automated scripts, not written directly in Python files. The extraction script pulls the proven implementation from the notebook cells and places it into the codebase. The notebook remains the source of truth. If the codebase code needs to change, you change the notebook, re-run verification, and re-extract.

This is the "code last" principle. It doesn't mean "never write code." It means code is *downstream* of verified intent and invariants. Any change that affects guarantees must route back through the invariant → lemma → notebook → artifact chain. The chain is bidirectional: you can start from any production function, trace it to an operator, trace the operator to an invariant, trace the invariant to a lemma, and read the formal proof of why that function is correct. Or go the other direction: start from a mathematical claim and follow it all the way down to the line of code that implements it.

This is how MA prevents the most dangerous failure mode in AI-assisted development: silent semantic drift. Code changes meaning without updating the proof surface. In MA, that's impossible — because the code *is* the proof surface, compiled.

In the standard AI lifecycle, deployment is when a system that was built and tested moves to production. In MA, deployment is when code that has survived intent formalization, mathematical specification, invariant encoding, lemma justification, notebook verification, artifact generation, and scorecard validation is extracted from its proof environment into the runtime. The code does not move to production. The proof moves to production. The code is the executable form of the proof.

This is not an incremental improvement over existing deployment practices. It is a fundamentally new relationship between code and correctness — one that has never existed in software development. In every other methodology, code is the primary artifact and correctness is a property you hope it has. In MA, correctness is the primary artifact and code is its compiled output. The distinction sounds philosophical until you realize the practical consequence: in MA, it is structurally impossible to deploy code that has not been proven against its governing invariants. Not "unlikely." Not "against policy." Impossible. The extraction script will not produce a runtime artifact from a notebook that has not passed its gates. The system being deployed has already been proven correct at a level of rigor that most organizations never achieve at any stage — because most organizations do not have a stage where proof is a prerequisite for deployment. MA does. It is the only framework that does.

---

# Act V — Why This Changes Everything

*MA is not a process improvement. It is a category.*

---

## 9. The Compounding Advantage

Every invariant you prove makes the next one cheaper. Every lemma you write creates a reusable proof pattern. Every notebook you execute becomes a regression harness that catches future violations automatically. The library of proven guarantees grows with every feature, and each new feature starts from a higher baseline of proven infrastructure.

This is the invariant library effect: MA-governed organizations accumulate deterministic assets. The longer you run MA, the more you can prove, the faster you can prove it, and the harder it becomes for competitors without this discipline to match your assurance level. The moat is not the framework. The moat is the accumulated evidence.

---

## 10. Model Agnosticism

MA doesn't care which AI model generated the code. GPT-4, Claude, Gemini, open-source, fine-tuned — the enforcement layer is identical. Models are interchangeable collaborators. Use one for writing, another for symbolic manipulation, another for counterexample generation. The gate doesn't ask "which model produced this?" It asks "does the artifact satisfy the invariant?"

This is a strategic necessity. Frontier models change fast — they improve, regress, change inference behavior, evolve safety layers. MA turns model drift into a detectable regression rather than a silent architectural mutation. If a new model version breaks an invariant, the notebook fails, the gate blocks, and you know exactly what changed. Without MA, you find out in production.

---

## 11. Falsification as the Safety Mechanism

The most common objection: "What if the AI writes the wrong math?"

MA's answer is not "trust better models." MA's answer is falsification. If the math is wrong, the notebook fails. If the notebook is shallow, the invariant will be incomplete. If assumptions are missing, boundary cases expose them.

Failure in MA is not a defect of the process. It is the process. The loop is: Hypothesis → Proof attempt → Failure → Refinement → Stable invariant. Every failure makes the system stronger — because every failure becomes a counterexample encoded in a notebook, a threshold tightened in an invariant, a boundary condition added to a lemma.

The real risk isn't incorrect math. It's correct math for the wrong intent. MA mitigates this by making semantic review mandatory: invariants include human-readable summaries, lemmas state assumptions explicitly, and acceptance assertions map to Phase 1 success criteria. Math correctness is necessary. Intent alignment is the controlling variable.

---

## 12. Enterprise-Grade Assurance

Regulated industries don't want stories. They want evidence. MA produces exactly what they need:

- **Reproducibility.** Every verification notebook runs deterministically with seeded execution. Re-run it tomorrow, next year, during an audit — same result.
- **Traceability.** Every production function traces to an operator, every operator to an invariant, every invariant to a lemma, every lemma to a notebook, every notebook to an artifact. The chain is complete and bidirectional.
- **Auditability.** The evidence pack is a structured bundle: invariant registry, notebooks, artifacts, scorecard, ADRs. Not a narrative — a deterministic evidence set.
- **Defensibility.** When a regulator asks "how do you know this system is correct?", the answer is not "we tested it." The answer is "here is the invariant that governs this behavior, the lemma that proves the invariant holds, the notebook that executes the proof, and the artifact that records the evidence. Run it yourself."

---

## Summary


| Step           | What It Does                                                          | What It Produces                                                    |
| -------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 1. Intent      | Defines the problem, success criteria, constraints, failure semantics | Problem statement, measurable outcomes, non-goals                   |
| 2. Mathematics | Formalizes intent into equations, operators, state spaces, boundaries | Notation, equations, named thresholds, assumptions                  |
| 3. Invariants  | Creates machine-enforceable contracts from the math                   | YAML files with acceptance assertions, thresholds, producers        |
| 4. Lemmas      | Explains *why* invariants hold, with explicit assumptions             | Formal claims with proof sketches, notebook references              |
| 5. Notebooks   | Executes the proof and generates evidence                             | Seeded verification harnesses, deterministic artifact export        |
| 6. Artifacts   | Records the evidence in machine-readable form                         | JSON files with metrics, pass/fail results, schema-stable fields    |
| 7. Scorecard   | Aggregates evidence into a promotion decision                         | Green/red gate decision, evidence pack for audit                    |
| 8. Extraction  | Moves proven code from notebooks to runtime                           | Production code that is a compiled artifact of verified constraints |


---

**The arc in one sentence:** Define what must be true. Prove it in a notebook. Enforce it in a gate. Extract it to runtime. Ship what survived.

**The thesis:** Probabilistic systems cannot be the source of correctness. Correctness must be defined outside the model and enforced deterministically. MA makes that operational.

**The result:** A development framework where AI is used to its full creative potential, nothing ships without proof, and the proof is executable, replayable, and auditable.

---

*AI is an extraordinary exploration engine. But exploration is not the same as correctness. Mathematical Autopsy makes that distinction explicit — and then enforces it.*