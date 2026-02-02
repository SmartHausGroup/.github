# CAIO

**Service routing and access control**

Part of the **TAI** archetype. [← Back to TAI](../README.md)

## Role

CAIO is the single integration boundary for service routing and access control across SmartHaus archetypes. It exposes a protocol (HTTP/gRPC) by which TAI, AIVA, and other systems call each other without sharing codebases or build pipelines. Every cross-system request is routed, authenticated, and optionally audited through CAIO, so that integration is contract-based and observable rather than hidden inside direct imports.

Keeping TAI and AIVA (and other systems) **decoupled** is deliberate: shared repos and shared releases would create brittle coupling and slow down independent evolution. CAIO centralizes routing, auth, and audit in one layer so that TAI can talk to AIVA over a **contract**, not by importing each other’s code. That enables independent release cadences, a single place for governance (e.g. MGE) to apply to all traffic, and full auditability of cross-system calls. CAIO is the protocol and control plane that keeps archetypes composable and provably integrated.

## Integration

**TAI** uses CAIO to route and secure all outbound service calls from the personal assistant. Internal services (NME, VFE, VEE, MAIA, RFS) and external systems (e.g. AIVA) are reached via CAIO so that policy and audit apply consistently.

**AIVA** (and other external systems) integrate with TAI only through CAIO. There are no direct code dependencies between TAI and AIVA; all interaction is protocol-based and CAIO-mediated. That allows each side to evolve and deploy independently while still cooperating.

**MGE** can sit at or behind CAIO to enforce governance and compliance on every cross-system call. Policy checks, access control, and audit logging can be applied in one place for all CAIO-mediated traffic.

CAIO replaced the former AIUCP (AI Unified Control Plane) as the canonical integration layer.
