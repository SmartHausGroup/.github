# VEE — Voluntas Engine

**Intent classification and quantum-inspired math**

[![Repository](https://img.shields.io/badge/Repository-VEE-blue)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](#)

Part of the **TAI** archetype. [← Back to TAI](/archetypes/tai)

## Overview

**VEE (Voluntas Engine)** is the intent-classification service for TAI. "Voluntas" means will or intent, which reflects VEE's job: convert user input into explicit intent representations that downstream services can route, reason over, and audit. It is a standalone service so intent logic remains explicit instead of being hidden inside opaque model prompts.

VEE is in development. Core math framing and intent schema are established, while richer disambiguation operators, multi-intent trajectories, and advanced fusion pathways are still under active MA-guided iteration.

## Role

VEE (Voluntas Engine) is TAI’s intent-classification and routing layer. It consumes user input (voice or text), interprets what the user is trying to achieve, and produces a structured representation of intent that downstream services use to choose models, actions, and memory queries. VEE does not execute actions or run inference itself; it answers “what does the user want?” so that MAIA can focus attention, VFE can select a model, and NME can decide what to recall. The engine uses quantum-inspired mathematics—superposition of candidate intents, interference for disambiguation, and a “measurement” step for commitment—so that ambiguity is explicit and auditable rather than collapsed inside a single black-box label.

Intent drives everything downstream: which model, which action, which memory query. VEE classifies intent in a way that can represent **ambiguity** (multiple plausible intents) and **commitment** (one chosen path). Keeping multiple readings alive until context or policy forces a choice, then routing cleanly to MAIA, VFE, or NME, keeps TAI’s behavior interpretable and auditable—intent is explicit, not buried inside an opaque classifier.

## Why VEE Exists

Without a dedicated intent layer, routing decisions would be diffused across prompts, handlers, and ad hoc heuristics. That makes behavior hard to verify and difficult to debug. VEE exists to provide a deterministic contract for intent as a first-class artifact in the orchestration graph.

A standalone VEE also enables explicit ambiguity handling. Many user turns contain overlapping meanings; preserving candidate intents until more context arrives improves reliability and keeps decision transitions inspectable.

## Core Capabilities

### 🎯 Intent Classification

VEE transforms voice or text inputs into structured intent candidates with confidence, priority, and semantic tags suitable for downstream orchestration.

### 🌊 Superposition of Candidate Intents

The engine can keep multiple plausible intents active simultaneously rather than forcing premature collapse to a single label.

### 🧭 Interference-Based Disambiguation

As additional context arrives, competing intent candidates are reweighted through quantum-inspired interference operators until a stable commitment is justified.

### 📏 Commitment and Routing Output

When decision thresholds are met, VEE emits an explicit committed intent package used by MAIA, VFE, NME, and CAIO-controlled action paths.

## Architecture

VEE is a stateless classification service at the front of TAI decision flow. It receives normalized user input and context hints, applies intent operators, and outputs structured intent artifacts through a contract-driven API.

Internal layers include intent candidate generation, superposition maintenance, disambiguation operators, and commitment logic. VEE does not own memory or inference execution; it provides high-signal intent artifacts to those services.

This architecture keeps intent semantics decoupled from model internals. Upstream input handling and downstream reasoning can evolve independently while VEE preserves stable intent contracts.

## Key Features

### Intent Representation System

- **Structured intent schema**: Standard fields for domain, action, target, and confidence.
- **Ambiguity preservation**: Maintains candidate sets until commitment is justified.
- **Priority scoring**: Orders competing intents for downstream attention.
- **Context-aware updates**: Recomputes candidate weights as new evidence arrives.

### Routing and Governance Readiness

- **Commitment checkpoints**: Clear transitions from candidate state to selected intent.
- **Traceable intent lineage**: Intent revisions remain auditable across a session.
- **Multi-modal input compatibility**: Supports voice and text signal pathways.
- **Service handoff contracts**: Outputs are consumable by MAIA, VFE, NME, and CAIO.

## Mathematical Autopsy (MA) Process

VEE applies MA by defining intent-state operators and commitment criteria before implementation. Lemmas describe how candidate states evolve under evidence updates, and invariants enforce bounded transitions, schema integrity, and fail-closed behavior on malformed inputs.

CI checks validate these invariants so intent artifacts remain deterministic at the contract level even when upstream language signals are ambiguous. This keeps downstream orchestration mathematically governed instead of heuristic-only.

## Implementation Status

### ✅ Foundation Complete

- Intent service boundary and schema contract are defined.
- Quantum-inspired operator model is documented at architecture level.
- MA verification framework for intent artifacts is established.

### 🚧 In Development

- Disambiguation pipeline implementation is underway.
- Multi-intent management and transition logic are in active build.
- Routing feedback loops for session-level refinement are being integrated.

### 🔬 Research

- Advanced operator sets for nuanced ambiguity patterns.
- Cross-modal intent fusion from voice semantics and behavior cues.
- Long-horizon intent continuity across multi-step sessions.

## Integration

**TAI** uses VEE as the primary source of classified intent for the personal assistant. Every user turn that requires routing—to a tool, a model, or memory—flows through VEE’s classification so that the rest of the pipeline has a consistent, structured view of user goals.

**MAIA** consumes VEE’s intent to drive attention and intent decomposition. Once intent is classified (or left in superposition), MAIA decides where to look in context and how to break the goal into steps, using VEE’s output as the anchor for focus and decomposition.

**VFE** uses intent to select which model or inference path to use. VEE’s classification (or committed reading) informs model choice and parameterization so that inference aligns with what the user asked for.

**NME** can use intent and context from VEE when structuring or recalling memory. Trait extraction and episode organization can be conditioned on the current intent so that stored and recalled content stays relevant to the conversation.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; intent classification in VEE is a natural candidate for alignment with COE regions such as the Prefrontal Cortex.

Integration contracts distinguish candidate-intent envelopes from committed-intent envelopes. MAIA can consume candidate distributions for planning, while VFE and action layers typically consume committed forms for deterministic execution.

VEE can also exchange memory-conditioned hints with NME so intent interpretation reflects known user preferences without embedding memory logic in the classification engine itself.

## Documentation

- **North Star**: [Strategic positioning and architecture](/vision)
- **MA Process**: [Mathematical Autopsy overview](/mathematical-autopsy/overview)
- **TAI**: [Parent archetype documentation](/archetypes/tai)

## Learn More

- **Learn More**: [TAI architecture](/archetypes/tai)
- **Learn More**: [RFS memory substrate](/rfs/overview)
- **Reach Out**: [smarthaus.ai](https://smarthaus.ai)

## License

**PROPRIETARY SOFTWARE** — All content in this repository is proprietary and confidential property of SmartHaus Group. All rights reserved. Unauthorized copying, modification, distribution, or use is strictly prohibited.

For licensing inquiries, please contact: **Philip Siniscalchi** at phil@smarthausgroup.com

See [LICENSE](https://github.com/SmartHausGroup/.github/blob/main/LICENSE) file for full terms.
