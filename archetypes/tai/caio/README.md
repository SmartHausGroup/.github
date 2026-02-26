# CAIO

**Service routing and access control**

[![Repository](https://img.shields.io/badge/Repository-CAIO-blue)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](#)

Part of the **TAI** archetype. [← Back to TAI](/archetypes/tai)

## Overview

**CAIO** is the contract boundary for service-to-service communication across SmartHaus systems. It centralizes routing, authentication, authorization, and audit pathways so archetypes can collaborate through protocol contracts instead of direct code coupling.

CAIO is in development and positioned as foundational infrastructure still being expanded. The boundary model and core protocol direction are established, while deeper governance integrations and advanced orchestration capabilities remain in active implementation.

## Role

CAIO is the single integration boundary for service routing and access control across SmartHaus archetypes. It exposes a protocol (HTTP/gRPC) by which TAI, AIVA, and other systems call each other without sharing codebases or build pipelines. Every cross-system request is routed, authenticated, and optionally audited through CAIO, so that integration is contract-based and observable rather than hidden inside direct imports.

Keeping TAI and AIVA (and other systems) **decoupled** is deliberate: shared repos and shared releases would create brittle coupling and slow down independent evolution. CAIO centralizes routing, auth, and audit in one layer so that TAI can talk to AIVA over a **contract**, not by importing each other’s code. That enables independent release cadences, a single place for governance (e.g. MGE) to apply to all traffic, and full auditability of cross-system calls. CAIO is the protocol and control plane that keeps archetypes composable and provably integrated.

## Why CAIO Exists

As SmartHaus archetypes grow, uncontrolled direct integration increases operational risk. Every new direct dependency introduces hidden coupling and weakens governance visibility. CAIO exists to enforce a single, inspectable boundary where interaction rules are explicit.

A dedicated boundary service also improves maintainability. Each system can evolve independently while preserving interoperation via contracts, which reduces release coordination overhead and avoids brittle monorepo-level dependency chains.

## Core Capabilities

### 🔀 Contract-Based Service Routing

CAIO routes requests across internal and external services through defined protocol contracts, keeping interface drift explicit and manageable.

### 🔐 Access Control and Authentication

The service enforces caller identity, authorization policy, and request entitlement at one boundary rather than distributing those concerns across every service.

### 📜 Audit Logging

CAIO emits structured audit trails for cross-system calls, supporting traceability, investigations, and governance reviews.

### 🌐 Cross-System Integration

TAI, AIVA, and adjacent systems integrate through CAIO-mediated contracts, enabling protocol-level decoupling with consistent controls.

## Architecture

CAIO sits between orchestrators and service endpoints as an integration gateway and policy plane. Requests enter through HTTP/gRPC contracts, pass through auth and policy checks, and are routed to target services based on contract registry and discovery metadata.

Core components include protocol adapters, identity and authorization handlers, route resolution, service discovery interfaces, and audit emitters. Optional governance hooks allow MGE-aligned checks to run in-line or as companion validation services.

Because CAIO is protocol-focused, it avoids embedding domain logic from TAI or AIVA. This keeps the gateway stable as surrounding systems evolve and allows incremental rollout of governance features.

## Key Features

### Boundary and Routing Controls

- **Single integration boundary**: Standard entry point for cross-system traffic.
- **Protocol adapter support**: Handles HTTP and gRPC integration contracts.
- **Dynamic route resolution**: Maps calls using service registry metadata.
- **Decoupled service evolution**: Preserves independent release cadence across systems.

### Security and Governance Controls

- **Authentication and authorization**: Enforces caller identity and policy.
- **Structured audit trails**: Captures request lineage and routing decisions.
- **MGE integration hooks**: Supports governance checks at boundary enforcement points.
- **Fail-closed policy behavior**: Rejects unauthorized or malformed requests.

## Mathematical Autopsy (MA) Process

CAIO applies MA to routing determinism, policy decision contracts, and audit completeness guarantees. Routing operators and policy evaluation criteria are defined first, then encoded as invariants before implementation paths are accepted.

Verification focuses on fail-closed behavior, contract compliance, and trace completeness. CI gates ensure integration boundaries stay deterministic at the contract level even as connected systems change.

## Implementation Status

### ✅ Foundation Complete

- CAIO boundary role and routing architecture are defined.
- Auth framework and contract-first integration model are documented.
- Initial MA and invariant enforcement plan is established.

### 🚧 In Development

- Expanded governance checks and MGE hook integration are ongoing.
- Audit payload depth and retention policy implementation are in progress.
- Advanced discovery and route policy mechanisms are being built.

### 🔬 Research

- Cross-archetype orchestration patterns for larger service ecosystems.
- Adaptive policy frameworks with deterministic override controls.
- Advanced service mesh strategies aligned to SmartHaus contracts.

## Integration

**TAI** uses CAIO to route and secure all outbound service calls from the personal assistant. Internal services (NME, VFE, VEE, MAIA, RFS) and external systems (e.g. AIVA) are reached via CAIO so that policy and audit apply consistently.

**AIVA** (and other external systems) integrate with TAI only through CAIO. There are no direct code dependencies between TAI and AIVA; all interaction is protocol-based and CAIO-mediated. That allows each side to evolve and deploy independently while still cooperating.

**MGE** can sit at or behind CAIO to enforce governance and compliance on every cross-system call. Policy checks, access control, and audit logging can be applied in one place for all CAIO-mediated traffic.

CAIO replaced the former AIUCP (AI Unified Control Plane) as the canonical integration layer.

In deployment flow, CAIO is the boundary between TAI orchestration and non-local service calls, including calls into AIVA domains. This keeps both security checks and route decisions concentrated in one governed layer.

CAIO also supports service discovery contracts so new modules can be registered without hardcoding endpoint behavior in TAI application code.

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
