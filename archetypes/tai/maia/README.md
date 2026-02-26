# MAIA

**Attention mechanisms and intent processing**

[![Repository](https://img.shields.io/badge/Repository-MAIA-blue)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](#)

Part of the **TAI** archetype. [← Back to TAI](/archetypes/tai)

## Overview

**MAIA** is TAI's attention and intent-processing service. It translates classified user intent into focused context windows and actionable decomposition plans, ensuring downstream inference receives only the most relevant context. By design, MAIA is a standalone service so attention policy remains explicit, tunable, and auditable.

MAIA is in development with foundational interfaces in place. Focus operators, decomposition contracts, and integration boundaries are defined, while adaptive weighting, longer-horizon planning, and cross-service coordination are still under active MA-driven iteration.

## Role

MAIA is TAI’s attention and intent-decomposition layer. It receives classified intent (e.g. from VEE) and the current context—conversation history, retrieved memory, persona traits, available tools—and decides **what to attend to** and **how to break the goal into steps**. It does not run inference or store memory itself; it produces a focused view and a decomposition that VFE, RFS, and downstream actions consume. By making attention explicit and tunable, MAIA lets us bound what goes into inference, log what was attended to, and keep behavior auditable.

Context is large, but only a subset matters for the current intent. Without a dedicated attention layer we would either pass the entire context every time (expensive and noisy) or rely on ad-hoc selection. MAIA fills that gap: it focuses retrieval and decomposition so that VEE’s “what the user wants” is combined with “where to look” and “how to break it down,” in a way that complements NME (structured memory) and VFE (inference).

## Why MAIA Exists

As context volume grows, unrestricted prompt construction becomes costly and unstable. MAIA exists to make context selection an explicit, governed process instead of a side effect of prompt templates. It chooses what matters now and excludes what does not.

Separating attention from inference also improves transparency. VFE can focus on execution while MAIA provides documented rationale for context inclusion, ordering, and decomposition choices.

## Core Capabilities

### 🎯 Attention-Driven Context Focusing

MAIA identifies relevant context slices from active conversation state, memory retrieval, and trait profiles, then prioritizes them for downstream reasoning.

### 🧩 Intent Decomposition

Given classified intent, MAIA breaks high-level goals into ordered sub-steps that downstream services can execute or infer against.

### 🪟 Context Window Management

MAIA enforces bounded context windows so inference costs and signal-to-noise ratios remain controlled for voice-first interactions.

### ⚖️ Priority Weighting and Focus Controls

MAIA applies tunable weighting parameters to balance recency, relevance, user preference, and task urgency.

## Architecture

MAIA sits between intent classification and inference execution in the TAI service chain. It consumes intent artifacts from VEE, retrieves supporting context from RFS and NME-informed channels, and emits focused context packages plus step plans for VFE and orchestration controllers.

Core components include attention selectors, decomposition planners, context weighting modules, and envelope builders. MAIA avoids owning memory persistence or model execution; its contract is to provide a deterministic focus layer.

This separation enables independent tuning of attention policy without changing model adapters or storage internals. As MAIA evolves, interface stability is preserved through contract versioning.

## Key Features

### Attention and Planning Functions

- **Focused context selection**: Chooses high-relevance context for each user turn.
- **Goal decomposition pipeline**: Converts broad goals into ordered executable steps.
- **Window budget enforcement**: Keeps context payloads within bounded limits.
- **Priority weighting controls**: Tunes relevance scoring across multiple signals.

### Integration and Observability

- **Intent-consistent focus**: Uses VEE outputs as the primary attention anchor.
- **Memory-directed retrieval hints**: Guides RFS queries with explicit focus metadata.
- **Inference-ready envelopes**: Produces structured payloads for VFE execution.
- **Traceable focus decisions**: Preserves attention lineage for governance review.

## Mathematical Autopsy (MA) Process

MAIA development follows MA order: define attention operators and decomposition constraints first, encode invariants second, then implement and validate behavior through CI-gated verification. This keeps focus decisions bounded and contract-compliant.

Key MA concerns for MAIA include deterministic context ranking rules, decomposition stability under equivalent inputs, and fail-closed handling when context contracts are incomplete or invalid.

## Implementation Status

### ✅ Foundation Complete

- Attention service boundary and decomposition contract are defined.
- Core integration interfaces with VEE, VFE, and RFS are specified.
- MA-aligned verification approach for focus contracts is documented.

### 🚧 In Development

- Context windowing implementation and weighting controls are underway.
- Multi-step planner refinement for complex user tasks is in progress.
- Observability and trace payload enrichment are being integrated.

### 🔬 Research

- Advanced attention operators for long-horizon conversational continuity.
- Cross-service coordination strategies for distributed focus decisions.
- Adaptive focus tuning under evolving user preference patterns.

## Integration

**TAI** uses MAIA as the core component for attention and intent decomposition in the personal assistant. Every turn that requires reasoning over context or breaking a goal into steps flows through MAIA so that inference and memory access are focused and efficient.

**VFE** receives from MAIA the focused context and decomposition needed for model selection and inference. MAIA’s output determines which parts of context are passed to the model and how the task is framed.

**VEE** feeds MAIA with classified intent. MAIA uses that intent to drive attention (what to retrieve, what to weight) and to decompose the goal into concrete steps that other services can execute.

**RFS** is queried under MAIA’s direction for context and memory. Attention over the field—what to recall, how much, and in what order—is decided by MAIA so that retrieval stays aligned with the current intent.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; attention and decomposition in MAIA are natural candidates for alignment with COE regions such as the Prefrontal Cortex and Basal Ganglia.

MAIA and VEE exchange both initial and refined intent representations so focus can update when user direction shifts mid-session. This supports controlled intent transitions without collapsing context state unpredictably.

MAIA-to-VFE delivery uses focused context envelopes with explicit ordering and rationale tags, while MAIA-to-RFS retrieval directives specify target memory zones and priority bands.

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
