# VEE — Voluntas Engine

**Intent classification and quantum-inspired math**

Part of the **TAI** archetype. [← Back to TAI](../README.md)

## Role

VEE (Voluntas Engine) is TAI’s intent-classification and routing layer. It consumes user input (voice or text), interprets what the user is trying to achieve, and produces a structured representation of intent that downstream services use to choose models, actions, and memory queries. VEE does not execute actions or run inference itself; it answers “what does the user want?” so that MAIA can focus attention, VFE can select a model, and NME can decide what to recall. The engine uses quantum-inspired mathematics—superposition of candidate intents, interference for disambiguation, and a “measurement” step for commitment—so that ambiguity is explicit and auditable rather than collapsed inside a single black-box label.

Intent drives everything downstream: which model, which action, which memory query. VEE classifies intent in a way that can represent **ambiguity** (multiple plausible intents) and **commitment** (one chosen path). Keeping multiple readings alive until context or policy forces a choice, then routing cleanly to MAIA, VFE, or NME, keeps TAI’s behavior interpretable and auditable—intent is explicit, not buried inside an opaque classifier.

## Integration

**TAI** uses VEE as the primary source of classified intent for the personal assistant. Every user turn that requires routing—to a tool, a model, or memory—flows through VEE’s classification so that the rest of the pipeline has a consistent, structured view of user goals.

**MAIA** consumes VEE’s intent to drive attention and intent decomposition. Once intent is classified (or left in superposition), MAIA decides where to look in context and how to break the goal into steps, using VEE’s output as the anchor for focus and decomposition.

**VFE** uses intent to select which model or inference path to use. VEE’s classification (or committed reading) informs model choice and parameterization so that inference aligns with what the user asked for.

**NME** can use intent and context from VEE when structuring or recalling memory. Trait extraction and episode organization can be conditioned on the current intent so that stored and recalled content stays relevant to the conversation.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; intent classification in VEE is a natural candidate for alignment with COE regions such as the Prefrontal Cortex.
