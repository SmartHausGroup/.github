# NME — Nota Memoria Engine

**Memory structuring and trait extraction before RFS**

[![Repository](https://img.shields.io/badge/Repository-NME-blue)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](#)

Part of the **TAI** archetype. [← Back to TAI](/archetypes/tai)

## Overview

**NME (Nota Memoria Engine)** is the memory-structuring and trait-extraction service in the TAI architecture. "Nota" means mark or sign, "Memoria" is memory, and "Engine" defines execution: NME marks raw interactions with a deterministic structure before they enter long-term storage. It is designed as a standalone service so memory preparation can evolve independently from assistant orchestration and inference.

NME is intentionally framed as in development. The service boundaries, contracts, and schema model are defined, while extraction depth, scoring behavior, and multi-modal pathways are still being iterated under Mathematical Autopsy (MA) controls. The target outcome is deterministic memory preparation that is explainable, replayable, and safe to integrate with RFS.

## Role

NME (Nota Memoria Engine) is the memory-structuring and trait-extraction layer that sits **upstream** of RFS. It consumes raw user content—conversations, preferences, events, feedback—and turns it into structured episodes and persona traits (preferences, personality, communication style) that RFS can store and that TAI can recall with the same mathematical guarantees (exact-byte or semantic). NME does not run the 4D field or execute inference; it prepares and types the data so that what enters the field is consistent, queryable, and suitable for endless recall and personalization.

RFS stores **waveforms**—superposed, interference-rich, deterministic. Raw user content is not yet in that form. Without NME we would either dump raw data into the field (noisy, hard to recall by trait) or leave structuring undefined. NME is the layer that turns user interactions into **structured memory** and **persona traits** so that RFS and TAI get endless, auditable memory instead of a pile of unstructured data.

## Why NME Exists

Raw interaction streams are not directly usable as deterministic memory. Voice turns, short messages, edits, and action confirmations all carry different semantic weight, and those differences must be encoded before storage. NME exists to transform unstructured content into typed episodes that preserve intent and context without introducing schema drift.

Keeping NME standalone protects field integrity. RFS is optimized for storage and retrieval behavior, not pre-ingest normalization policy. By isolating structuring logic in NME, SmartHaus can improve extraction and typing rules without destabilizing field operators, while TAI and adjacent services consume a stable output contract.

## Core Capabilities

### 🧱 Memory Structuring

NME converts raw interaction events into canonical episode objects with deterministic field names, timestamps, and provenance metadata. This prevents downstream ambiguity and makes replay across environments possible.

### 🧬 Persona Trait Extraction

NME extracts user-level trait signals such as communication preferences, style tendencies, and recurring priorities. Trait vectors are generated with explicit confidence and lineage metadata so updates remain auditable.

### 🗂 Episode Typing

NME assigns episode classes (intent, preference, task, correction, feedback, and similar categories) using rules that keep semantic boundaries explicit. Typed episodes allow selective recall instead of broad, noisy retrieval.

### ✅ Schema Enforcement

NME validates outbound payloads against schema contracts before handoff. Invalid payloads fail closed and are rejected from ingest so RFS receives only structurally valid memory units.

## Architecture

NME operates as a stateless transform service in the TAI service mesh. Inputs arrive through TAI orchestration as raw interaction payloads; NME parses, normalizes, and enriches those payloads; outputs are structured episodes, trait vectors, and metadata envelopes destined for RFS and other consumers.

The API surface is contract-driven (HTTP/gRPC boundary depending on deployment profile). Core components include ingest adapters, deterministic transform operators, schema validators, and trait aggregation units. Stateful history is not held in NME; durable memory remains in RFS.

This separation supports independent scaling and versioning. NME can evolve extraction quality and schema revisions while preserving strict backward compatibility at the service contract layer used by TAI, VEE, and VFE.

## Key Features

### Memory Preparation Pipeline

- **Deterministic normalization**: Converts heterogeneous user content to canonical records.
- **Trait extraction primitives**: Captures preferences, communication style, and behavior markers.
- **Episode segmentation**: Splits long exchanges into queryable memory episodes.
- **Metadata enrichment**: Adds provenance, timestamps, confidence, and source channels.

### Contract and Quality Controls

- **Schema validation**: Enforces required fields and allowed value domains.
- **Fail-closed ingest**: Rejects malformed or ambiguous payloads before storage.
- **Replay-friendly output**: Produces stable output objects for deterministic verification.
- **Audit visibility**: Keeps extraction lineage available for governance reviews.

## Mathematical Autopsy (MA) Process

NME follows the same MA lifecycle as other SmartHaus services: governing formula and operator definitions are specified first, invariants are encoded next, and implementation conforms to those contracts after verification artifacts pass. This preserves the deterministic order of operations: math, then invariants, then code.

For NME, MA focuses on schema invariants, trait-consistency lemmas, and deterministic transform behavior. CI gates enforce these invariants so ingest pathways fail closed when contracts are violated.

## Implementation Status

### ✅ Foundation Complete

- Service role and architectural boundary in the TAI mesh are defined.
- Episode schema model and trait vector contract are specified.
- MA-aligned contract and validation framework is documented.

### 🚧 In Development

- Production-grade extraction pipeline implementation is ongoing.
- Trait scoring refinement and calibration rules are being integrated.
- Expanded event adapters for additional TAI interaction types are in progress.

### 🔬 Research

- Multi-modal trait extraction from voice prosody and behavior traces.
- Long-horizon personalization stability and drift-control operators.
- Cross-service trait harmonization with MAIA and VEE context models.

## Integration

**RFS** receives from NME the structured memory and traits that are encoded into the 4D field. NME’s output—typed episodes, trait vectors, and metadata—is what gets superposed and queried; NME ensures that format and schema are consistent so that retrieval and interference behave as specified.

**TAI** uses NME for all learning and personalization that feeds into memory. Every user interaction that should be remembered or used to update persona traits flows through NME before being written to RFS, so that the assistant’s “endless memory” is both rich and auditable.

**VEE and VFE** can integrate with NME when intent or inference depend on memory and traits. NME’s structured output can inform intent classification (VEE) and context selection for inference (VFE) so that recall and reasoning stay aligned.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; memory structuring and trait extraction in NME are natural candidates for alignment with COE regions such as the Hippocampus.

NME-to-RFS handoff is contract-based: NME emits typed episode envelopes and trait payloads, and RFS performs field encoding on validated structures rather than raw text blocks. This boundary keeps storage operators stable while allowing extraction behavior to improve.

NME also connects to TAI learning loops through explicit update channels. Trait revisions, correction events, and preference confirmations are versioned so personalization can be traced from interaction input to memory artifact without hidden state transitions.

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
