# TAI: Tutelarius Auxilium Intellectus

**Guardian of Intelligent Assistance**

[![Repository](https://img.shields.io/badge/Repository-TAI-blue)](https://github.com/SmartHausGroup/TAI)
[![Status](https://img.shields.io/badge/Status-Foundation%20Complete-brightgreen)](https://github.com/SmartHausGroup/TAI)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/SmartHausGroup/TAI)

A service-oriented personal assistant platform with endless memory, contextual intelligence, continuous user learning, and an AI agent marketplace.

## Overview

**TAI (Tutelarius Auxilium Intellectus)** is a voice-first personal assistant that becomes everyone's personal best friend and assistant. TAI provides a flexible architecture where core systems (RFS, VFE, QuantumCore) integrate seamlessly as modules, enabling a marketplace ecosystem where developers can build and distribute modules that extend TAI's capabilities.

**Full Name**: Tutelarius Auxilium Intellectus
- **Tutelarius** = Guardian, Protector (guards intelligence with mathematical guarantees)
- **Auxilium** = Aid, Help (provides assistance through orchestration)
- **Intellectus** = Intelligence, Understanding (enables intelligent behavior through composition)

## Core Capabilities

### 🎤 Voice-First Interface
Primary interaction mode is voice (STT/TTS), with text as secondary. Natural conversation optimized for voice interaction.

### 🧠 Endless Memory
- **RFS Integration**: 4D field architecture for episodic memory
- **Exact-Byte Recall**: Never forgets, with exact-byte recall and semantic retrieval
- **Persona Traits**: Separate persona traits store for preferences, personality, communication style
- **Waveform Superposition**: Semantic relationships through field superposition

### 🔄 Any Model
- **Verbum Field Engine (VFE)**: Maintains expandable model registry
- **Not Locked to Single Provider**: Supports any AI model
- **Model Agnostic**: Not tied to any single AI model or tool
- **Marketplace Support**: Supports marketplace of alternatives

### 🛡️ Mathematical Guarantees
All operations mathematically verified via Mathematical Autopsy (MA) process:
- Deterministic operations
- Formal proofs
- Invariants and lemmas
- CI enforcement

### 🎯 Continuous Learning
- **User Learning Module**: Learns from every interaction
- **Grows with You**: Through every interaction
- **Adaptive**: Personalization based on usage patterns

## Architecture

TAI is a **service-oriented architecture** that handles frontend/UX/UI and orchestrates standalone service packages via HTTP APIs.

### TAI Core

- **Frontend/UX/UI**: Web Interface, Enterprise Dashboard, CLI
- **Orchestration Layer**: Service coordination
- **User Learning Module**: Continuous user learning
- **Marketplace**: AI tools and services

### Standalone Service Packages

All services communicate via HTTP APIs. Services are **NOT embedded** in TAI codebase.

- **AICPOrchestrator**: Central API gateway and orchestration (Port 8000)
- **RFS (Resonant Field Storage)**: 4-D wave-based field storage (Port 8002)
- **VFE (Verbum Field Engine)**: GPU-first LLM inference engine (Port 8081)
- **VEE/QuantumCore**: Intent classification and quantum-inspired math (Port 8001)
- **CAIO**: Service routing and access control
- **MAIA**: Attention mechanisms and intent processing

**Key Principle**: TAI uses service packages via HTTP clients. Services are NOT embedded in TAI codebase, enabling hot-swapping and modularity.

## Service Architecture

All services implement the `TAIService` interface protocol, enabling:

- **Hot-swapping**: Zero-downtime service replacement
- **Service Discovery**: Automatic service registration and discovery
- **Mathematical Guarantees**: Invariants and contracts verified via CI
- **Marketplace**: Pluggable services with compliance verification

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

## Component Repositories

TAI integrates with the following standalone services:

- **[RFS](https://github.com/SmartHausGroup/ResonantFieldStorage)** — Memory substrate (Resonant Field Storage)
- **[VFE](https://github.com/SmartHausGroup/VerbumFieldEngine)** — GPU-first LLM inference engine
- **[VEE](https://github.com/SmartHausGroup/VoluntasEngine)** — Intent classification and quantum-inspired math
- **[CAIO](https://github.com/SmartHausGroup/CAIO)** — Service routing and access control
- **[MAIA](https://github.com/SmartHausGroup/MAIA)** — Attention mechanisms and intent processing

## Documentation

- **North Star**: Strategic vision and architecture
- **MA Process**: Mathematical Autopsy methodology
- **Service Docs**: Service architecture overview
- **API Documentation**: Service API references

## Learn More

- **Repository**: [TAI on GitHub](https://github.com/SmartHausGroup/TAI)
- **SMARTHAUS Vision**: [SMARTHAUS Vision Document](../SMARTHAUS_VISION.md)
- **RFS Documentation**: [RFS README](../rfs/README.md)
- **Organization**: [SmartHausGroup](https://github.com/SmartHausGroup)
- **Website**: [smarthaus.ai](https://smarthaus.ai)

## License

See the [TAI repository](https://github.com/SmartHausGroup/TAI) for license information.

---

**TAI — Your personal AI assistant that remembers everything and knows you deeply.**

*Tutelarius Auxilium Intellectus - Guardian of Intelligent Assistance*
