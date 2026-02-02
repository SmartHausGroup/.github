# CAIO

**Service routing and access control**

Part of the **TAI** archetype. [← Back to TAI](../README.md)

## Role

CAIO provides service routing and access control. It enables TAI and external systems (e.g. AIVA) to integrate via a single protocol: CAIO-mediated, protocol-based integration over HTTP/gRPC.

## Integration

- **TAI** — Routes and secures service calls within the personal assistant
- **AIVA** — External systems (e.g. TAI) integrate with AIVA via CAIO; no direct code dependencies
- **MGE** — Can work with governance for compliance and audit

CAIO replaced the former AIUCP (AI Unified Control Plane) for integration.
