# VFE — Verbum Field Engine

**GPU-first LLM inference engine**

[![Repository](https://img.shields.io/badge/Repository-VFE-blue)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](#)

Part of the **TAI** archetype. [← Back to TAI](/archetypes/tai)

## Overview

**VFE (Verbum Field Engine)** is the inference execution service for TAI. "Verbum" signals language and reasoning, while "Field" anchors execution in a mathematically governed runtime context. VFE centralizes model execution so the assistant can remain provider-agnostic and deterministic where bounded replay is required.

The service is in development, not production-positioned. Architectural interfaces and GPU pipeline direction are defined, while advanced routing policies, replay controls, and model composition strategies are still moving through iterative MA verification.

## Role

VFE (Verbum Field Engine) is TAI’s primary inference engine for language and reasoning. It runs LLM inference on GPU-backed infrastructure, maintains an expandable model registry so TAI is not locked to a single provider, and exposes a consistent interface so that the rest of the assistant can request completions, embeddings, or other model outputs without depending on a specific vendor or model. VFE does not classify intent or structure memory; it executes inference on the context and prompts it receives from MAIA, VEE, and NME.

TAI needs **inference** that is fast, scalable, and—where possible—**deterministic** (seeded, logged, replayable). VFE is GPU-first so that latency and throughput scale with hardware, and it maintains a **model registry** so we can swap or add models without rewriting the assistant. That yields flexibility, performance for voice and context, and auditability: when determinism is required, we isolate inference and log context so we can replay. VFE fits the same **mathematical guarantees** story as the rest of the stack—inference that can be bounded, logged, and (where possible) reproduced, not a black-box LLM.

## Why VFE Exists

If inference logic is embedded directly in the assistant layer, every model switch becomes an application rewrite and auditability becomes fragmented. VFE exists to isolate inference execution from interaction orchestration so model operations can be governed with a single contract.

A standalone inference service also protects long-term flexibility. TAI can use different model families across workloads without changing upstream interfaces, and governance controls can be applied at one boundary for logging, replay, and policy enforcement.

## Core Capabilities

### ⚡ GPU-First Inference

VFE is designed around GPU-backed execution paths optimized for conversational latency, throughput control, and predictable runtime behavior under voice-first workloads.

### 🧩 Expandable Model Registry

A provider-agnostic registry allows models to be added, swapped, versioned, and retired through contract updates rather than assistant rewrites.

### 🔁 Deterministic Replay Controls

For bounded deterministic scenarios, VFE captures seed, prompt context, and runtime metadata needed to replay inference traces under controlled conditions.

### 🧠 Multi-Model and Embeddings Support

VFE supports both generation and embedding pipelines so semantic retrieval and reasoning can share a unified execution boundary.

## Architecture

VFE exposes a stable inference API while abstracting model-specific runtimes behind adapter contracts. TAI orchestration and MAIA/VEE provide focused context and intent; VFE resolves model selection, executes inference, and returns structured outputs with trace metadata.

Core components include model registry management, GPU scheduling, request normalization, context window controllers, and telemetry emitters. The service is intentionally decoupled from memory and intent layers; it consumes prepared context but does not own classification or storage.

This architecture allows independent lifecycle control for inference operations. Model upgrades, performance tuning, and replay features can evolve within VFE without forcing changes across the broader TAI stack.

## Key Features

### Model and Runtime Management

- **Provider-agnostic registry**: Unified model identifiers across heterogeneous backends.
- **Versioned model contracts**: Explicit compatibility tracking for model updates.
- **Hot-swappable routing**: Switches model targets without changing caller code.
- **Embeddings pipeline support**: Shared execution interface for vector generation.

### Performance and Governance Controls

- **GPU scheduling hooks**: Priority-aware dispatch for interactive workloads.
- **Latency tuning profiles**: Voice-first response timing optimization.
- **Replay telemetry capture**: Records context and execution state for audit.
- **Determinism boundaries**: Explicitly documents where replay guarantees apply.

## Mathematical Autopsy (MA) Process

VFE is developed under MA sequencing: inference operators and constraints are formalized before implementation, then invariants are encoded for deterministic bounds, replay capture requirements, and contract behavior. Code paths are validated against those invariants in CI.

Because some model internals are externally probabilistic, VFE’s MA scope emphasizes bounded divergence, input/output contract determinism, and reproducible execution envelopes rather than claims of universal deterministic token generation.

## Implementation Status

### ✅ Foundation Complete

- Service boundary and inference API contract are defined.
- Model registry interface and adapter model are documented.
- GPU-first architecture and MA controls framework are specified.

### 🚧 In Development

- Multi-model routing and policy selection logic are being implemented.
- Deterministic replay capture and verification are in active build.
- Runtime optimization for voice-turn latency is in progress.

### 🔬 Research

- Cross-model validation strategies for output consistency.
- Hybrid inference compositions for specialized task pathways.
- Advanced determinism envelopes for mixed-model workflows.

## Integration

**TAI** uses VFE as the primary inference engine for the personal assistant. All LLM calls—completions, embeddings, tool use—go through VFE so that model selection, latency, and logging are centralized and auditable.

**RFS** can supply context and memory to VFE when inference needs retrieved content. MAIA and NME decide what to recall; that content is passed to VFE as part of the prompt or context so that inference is grounded in the user’s stored history and traits.

**MAIA and VEE** feed VFE with focused context and intent. MAIA’s attention output and VEE’s classified intent determine what context is sent to the model and how the request is framed, so that inference stays aligned with user goals and current focus.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; inference orchestration in VFE could align with execution and policy layers in the COE.

In practical flow terms, MAIA constructs context slices, VEE contributes intent commitments, and VFE resolves model execution strategy from registry policy before returning response payloads to TAI orchestration.

For memory-aware reasoning, RFS retrieval packets can be attached to the inference request envelope. VFE treats these packets as bounded context segments with trace IDs so replay and audit chains remain intact.

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
