# VFE — Verbum Field Engine

**GPU-first LLM inference engine**

Part of the **TAI** archetype. [← Back to TAI](../README.md)

## Role

VFE (Verbum Field Engine) is TAI’s primary inference engine for language and reasoning. It runs LLM inference on GPU-backed infrastructure, maintains an expandable model registry so TAI is not locked to a single provider, and exposes a consistent interface so that the rest of the assistant can request completions, embeddings, or other model outputs without depending on a specific vendor or model. VFE does not classify intent or structure memory; it executes inference on the context and prompts it receives from MAIA, VEE, and NME.

TAI needs **inference** that is fast, scalable, and—where possible—**deterministic** (seeded, logged, replayable). VFE is GPU-first so that latency and throughput scale with hardware, and it maintains a **model registry** so we can swap or add models without rewriting the assistant. That yields flexibility, performance for voice and context, and auditability: when determinism is required, we isolate inference and log context so we can replay. VFE fits the same **mathematical guarantees** story as the rest of the stack—inference that can be bounded, logged, and (where possible) reproduced, not a black-box LLM.

## Integration

**TAI** uses VFE as the primary inference engine for the personal assistant. All LLM calls—completions, embeddings, tool use—go through VFE so that model selection, latency, and logging are centralized and auditable.

**RFS** can supply context and memory to VFE when inference needs retrieved content. MAIA and NME decide what to recall; that content is passed to VFE as part of the prompt or context so that inference is grounded in the user’s stored history and traits.

**MAIA and VEE** feed VFE with focused context and intent. MAIA’s attention output and VEE’s classified intent determine what context is sent to the model and how the request is framed, so that inference stays aligned with user goals and current focus.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; inference orchestration in VFE could align with execution and policy layers in the COE.
