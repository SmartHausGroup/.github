# TAI: Tutelarius Auxilium Intellectus

**Guardian of Intelligent Assistance**

[![Repository](https://img.shields.io/badge/Repository-TAI-blue)](#)
[![Status](https://img.shields.io/badge/Status-Foundation%20Complete-brightgreen)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

A service-oriented personal assistant platform with endless memory, contextual intelligence, continuous user learning, and an AI agent marketplace.

## Overview

**TAI (Tutelarius Auxilium Intellectus)** is a voice-first personal assistant platform with endless memory, contextual intelligence, continuous user learning, and an AI agent marketplace. TAI is designed so that the primary interaction is **voice**—hands-free, natural, always available—with text as secondary. Core capabilities (memory, inference, intent, attention, routing) are provided by **standalone services** (RFS, NME, VFE, VEE, MAIA, CAIO) that integrate over HTTP/gRPC via CAIO; TAI does not embed those services in its codebase. That enables hot-swapping, independent evolution, and a marketplace where developers can add or replace modules without forking the assistant. Memory is backed by **RFS (Resonant Field Storage)**—the same mathematical substrate used in AIVA—so that recall is exact-byte or semantic, with explainability and determinism. All operations are governed by the **Mathematical Autopsy (MA)** process: invariants, proofs, and CI enforcement so that behavior is provable, not only tested.

**Full name:** Tutelarius Auxilium Intellectus—**Tutelarius** (guardian, protector: guards intelligence with mathematical guarantees), **Auxilium** (aid, help: provides assistance through orchestration), **Intellectus** (intelligence, understanding: enables intelligent behavior through composition).

## Why voice-first and why RFS for memory

We design TAI **voice-first** because the primary use case is a personal assistant you talk to—hands-free, natural, always available. Text is secondary; voice drives the interaction model, so STT/TTS, latency, and context are first-class. We use **RFS (Resonant Field Storage)** as the memory substrate because we want **endless memory with provable guarantees**: not “approximate recall” or “best-effort similarity,” but **exact-byte recall** when needed and **semantic retrieval** with explainability (interference patterns, not black-box distance). RFS is the same mathematical substrate used in AIVA (AIOS Hippocampus); so TAI and AIVA share the same memory *math*—determinism, energy conservation, invariants—even when they serve different users and workloads. The “why” is: we want a personal assistant that **never forgets** and that we can **audit and prove correct**, not one that “usually” remembers and “hopefully” behaves. Voice-first + RFS + MA is how we get there.

## Core Capabilities

### 🎤 Voice-First Interface

Primary interaction mode is **voice** (STT/TTS), with text as secondary. The assistant is optimized for natural conversation over voice—latency, context window, and turn-taking are tuned for spoken interaction so that the experience is hands-free and always available. Voice drives the interaction model; text is supported but not the default.

### 🧠 Endless Memory

Memory is backed by **RFS (Resonant Field Storage)**—TAI’s mathematical memory substrate. RFS uses a 4D field architecture for episodic memory: documents and episodes are superposed as waveforms, and retrieval is resonance-based (exact-byte or semantic) with explainability (interference patterns) and determinism. **NME (Nota Memoria Engine)** structures memory and extracts persona traits (preferences, personality, communication style) *before* data is stored in RFS, so that what enters the field is consistent, typed, and queryable. The result is endless, auditable memory—never forgets, with exact-byte recall when needed and semantic retrieval with mathematical guarantees.

### 🔄 Any Model

Inference is provided by **VFE (Verbum Field Engine)**—a GPU-first LLM inference engine with an **expandable model registry**. TAI is not locked to a single provider or model; VFE maintains a registry so that models can be swapped or added without rewriting the assistant. That supports a **marketplace** of alternatives: developers can offer new models or tools, and TAI can route to them via CAIO and VEE/MAIA. Model-agnostic design keeps the assistant flexible and audit-ready (inference can be bounded, logged, and where possible reproduced).

### 🛡️ Mathematical Guarantees

All operations are mathematically verified via the **Mathematical Autopsy (MA)** process. Determinism (same inputs → same outputs), formal proofs (invariants and lemmas), and CI enforcement ensure that behavior is **provably correct**, not only tested. MA order is strict: math → invariants → code (never code → math). That aligns TAI with the same guarantees used in RFS, AIVA, and MGE.

### 🎯 Continuous Learning

TAI learns from every interaction. A **user learning module** (and NME-backed trait extraction) supports personalization: preferences, communication style, and episodic memory grow with use. Learning is structured and stored via NME and RFS so that adaptation is auditable and consistent with the same mathematical substrate used for recall.

## Architecture

TAI is a **service-oriented architecture**. The TAI core handles frontend/UX/UI (web interface, enterprise dashboard, CLI), orchestration (service coordination and routing), the user learning module (continuous learning and personalization), and the marketplace (AI tools and services). All **capability services**—memory, inference, intent, attention, routing—are **standalone packages** that communicate via HTTP APIs. Services are **not embedded** in the TAI codebase: TAI uses HTTP clients to call them, so that services can be hot-swapped, versioned independently, and replaced by marketplace alternatives without changing TAI’s core code.

### TAI Core

The core provides **frontend/UX/UI** (web, dashboard, CLI), an **orchestration layer** that coordinates service calls and routes user turns to the right services (VEE, MAIA, VFE, NME, RFS), a **user learning module** that feeds interaction data into NME and RFS for personalization, and a **marketplace** surface so that developers can register and distribute AI tools and services. Orchestration is CAIO-aware: cross-system calls (e.g. to AIVA) go through CAIO; internal service calls use the same protocol discipline where applicable.

### Standalone Service Packages

Each capability is a separate service with its own API and (where applicable) port. **RFS** (Resonant Field Storage) is the 4D wave-based memory substrate (e.g. Port 8002). **NME** (Nota Memoria Engine) structures memory and extracts traits before RFS → [NME](nme/README.md). **VFE** (Verbum Field Engine) is the GPU-first LLM inference engine (e.g. Port 8081) → [VFE](vfe/README.md). **VEE** (Voluntas Engine) handles intent classification and quantum-inspired math (e.g. Port 8001) → [VEE](vee/README.md). **CAIO** provides service routing and access control → [CAIO](caio/README.md). **MAIA** provides attention mechanisms and intent processing → [MAIA](maia/README.md). An orchestrator/gateway (e.g. Port 8000) coordinates discovery and routing. **Key principle:** TAI uses these packages via HTTP clients; services are not embedded, enabling hot-swapping and modularity.

## Service Architecture

All services implement a **TAIService**-style interface protocol so that TAI can discover, call, and (where needed) replace them consistently. **Hot-swapping** is supported: a service can be upgraded or replaced with zero downtime because TAI talks to it over HTTP, not by importing it. **Service discovery** allows automatic registration and discovery so that new services (e.g. from the marketplace) can be added without hardcoding endpoints. **Mathematical guarantees** are enforced per service: invariants and contracts are verified via CI (MA process) so that each service’s behavior is provable. The **marketplace** can plug in new services with compliance verification (e.g. via MGE or CAIO) so that extensions are both flexible and governed.

## Key Features

### Service-Oriented Design
- **HTTP-based Communication**: All services communicate via HTTP APIs
- **No Direct Imports**: Services are NOT embedded in TAI codebase
- **Service Clients**: TAI uses HTTP clients to communicate with services
- **Hot-swappable**: Services can be replaced without code changes

### Memory & Traits
- **4D Field Architecture**: RFS provides episodic memory
- **Persona Traits Store**: Preferences, personality, communication style
- **Semantic Relationships**: Waveform superposition for semantic relationships
- **Exact-Byte Recall**: AEAD-backed byte channel for perfect reconstruction

### Model & Tool Agnostic
- **Expandable Model Registry**: VFE maintains registry of any model
- **Marketplace Support**: Developers can build and distribute modules
- **Flexible Integration**: Not locked to any single AI provider
- **Compliance Verification**: Marketplace services verified for compliance

### Mathematical Guarantees
- **Deterministic Operations**: All operations are mathematically guaranteed
- **Formal Proofs**: Every component has invariants, lemmas, and verification
- **MA Process**: Rigorous Mathematical Autopsy process ensures correctness
- **CI Enforcement**: Automated validation enforces invariants

## Mathematical Autopsy (MA) Process

TAI follows a rigorous **MA Doc-First** approach:

1. **Docs**: North Star and math appendices define guarantees
2. **Math**: Formal operators and definitions
3. **Invariants**: Mathematical guarantees encoded in YAML
4. **Notebooks**: Verification notebooks produce artifacts
5. **Code**: Implementation matches documented math
6. **CI Gates**: Automated validation enforces invariants

**Critical Order**: Math → Invariants → Code (NEVER Code → Math)

## Implementation Status

### ✅ Foundation Complete
- Service architecture and orchestration
- RFS integration
- MA infrastructure in place
- Hot-swapping enabled
- Service discovery and routing
- Mathematical guarantees framework

### 🚧 In Development
- Voice-first interface (in development)
- User learning module (in development)
- Marketplace UI (in development)
- Service extraction to standalone repos

### 🔬 Research
- Advanced personalization
- Multi-modal integration
- Enhanced memory capabilities

## TAI parts (on this site)

TAI integrates with the following standalone services. Each has a page on this site:

- **[RFS](../../resonant-field-storage/README.md)** — Memory substrate (Resonant Field Storage)
- **[NME](nme/README.md)** — Nota Memoria Engine (memory structuring / trait extraction)
- **[VFE](vfe/README.md)** — Verbum Field Engine (GPU-first LLM inference)
- **[VEE](vee/README.md)** — Voluntas Engine (intent classification)
- **[CAIO](caio/README.md)** — Service routing and access control
- **[MAIA](maia/README.md)** — Attention mechanisms and intent processing

## Documentation

- **North Star**: Strategic vision and architecture
- **MA Process**: Mathematical Autopsy methodology
- **Service Docs**: Service architecture overview
- **API Documentation**: Service API references

## Learn More

- **SMARTHAUS Vision**: [SMARTHAUS Vision Document](../../SMARTHAUS_VISION.md)
- **RFS**: [Resonant Field Storage](../../resonant-field-storage/README.md)
- **On this site**: [NME](nme/README.md) · [VFE](vfe/README.md) · [VEE](vee/README.md) · [CAIO](caio/README.md) · [MAIA](maia/README.md)
- **Website**: [smarthaus.ai](https://smarthaus.ai)

## License

**PROPRIETARY SOFTWARE** — All content in this repository is proprietary and confidential property of SmartHaus Group. All rights reserved. Unauthorized copying, modification, distribution, or use is strictly prohibited.

For licensing inquiries, please contact: **Philip Siniscalchi** at phil@smarthausgroup.com

See [LICENSE](../../LICENSE) file for full terms.

---

**TAI — Your personal AI assistant that remembers everything and knows you deeply.**

*Tutelarius Auxilium Intellectus - Guardian of Intelligent Assistance*
