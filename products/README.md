# SMARTHAUS product map

SMARTHAUS is building the mathematically governed AI fabric: components for constructing rules, running them inside applications, interpreting intent, checking outputs, governing actions, coordinating work, and sharing memory.

The research thesis, *Mathematics as the Nervous System of AI*, underpins this architecture. It describes mathematics as the integrating substrate for specialized AI components. RFS is the working memory implementation described in the thesis. The broader cognitive architecture remains a research and development direction.

## What the components do

| Component | Role |
|---|---|
| **MAE — Mathematical Autopsy Engine** | Creates and verifies bounded rules, linking generated artifacts to their mathematical definitions and verification evidence. |
| **MGR — Mathematically Governed Runtime** | The embeddable harness that runs MAE-created rules inside SMARTHAUS applications or other applications, wherever rules are needed. |
| **MAIA** | Interprets user intent and identifies when clarification is needed. |
| **SAID** | Checks model-generated outputs against declared constraints before an application accepts them. |
| **UCP — Universal Control Plane** | Governs whether actions may proceed at integrated runtime gateways and managed host boundaries. |
| **CAIO** | The orchestrator: coordinates components and workflows. |
| **MGT** | Addresses governance within model computation. |
| **RFS — Resonant Field Storage** | Shared field-based memory supporting associative retrieval and integrity-checked exact recall. |
| **NME — Nota Memoria Engine** | Encodes structured meaning for the memory foundation. |
| **Operations Center** | Management surface for governed runtimes, including enrollment, policy distribution, and lifecycle controls. |
| **TAI** | The personal AI application direction bringing components together around the user. |
| **VEE — Voluntas Engine** | Mathematical kernels and research supporting stability, privacy, and reinforcement learning. |

## Current development stages

This snapshot describes the work reviewed in October 2026. It is not an installation or release catalogue. Product-specific records govern exact versions, supported environments, and availability.

| Component | Implementation and remaining work |
|---|---|
| **MAE** | A sealed runtime implements bounded rule-generation and verification paths. Supported rule families define its present scope; broader construction capabilities continue to develop. |
| **MGR** | Bounded governed rule execution exists within MAE, alongside a released contract-validation package. The independently owned, shared embeddable harness is under development. These artifacts have different scopes. |
| **MAIA** | An intent runtime and sealed artifact exist. Integration into consuming applications remains a separate milestone. |
| **SAID** | Output constraint checking and bounded retry/fallback paths exist. Guarantees depend on the declared constraints and the application's integration. |
| **UCP** | Runtime action-admission and lifecycle controls exist. Coverage depends on the gateways and host controls an application actually uses. |
| **CAIO** | Under development as the orchestrator. Coordination, dispatch boundaries, and runtime integration are active work. |
| **MGT** | Governed computation kernels, a harness, and formal proof sources exist. Product packaging and integration continue. |
| **RFS / NME** | Memory, encoding, and retrieval implementations exist. Service packaging and broader application integration continue. |
| **Operations Center** | Management APIs and runtime lifecycle machinery exist across Operations Center and UCP. Completion of the operating surface and integrated rollout acceptance remain separate work. |
| **TAI** | Engine and application foundations exist. The integrated personal AI experience remains under development. |
| **VEE** | Mathematical kernels and research implementations exist. A complete reinforcement-learning runtime is not claimed here. |

## Applications and distribution

**SIGMA** and the **Employee Command Center (ECC)** are application work that puts controlled workflows into trading and business operations. Their individual implementation and acceptance records determine what each application can do. Their existence does not establish complete fabric integration.

**Marketplace Packages** supports the distribution of governed capabilities. A package being listed, signed, or released does not mean it has been activated in an application or accepted by a customer.

## How the pieces fit

MAE creates the rules; MGR runs them where an application needs rules. CAIO coordinates work among components. Intent, output, action, model-computation, and memory components address their respective boundaries. The thesis supplies the underlying architectural direction; each integration must establish its own behavior and evidence.

A verified rule guarantees only the property proved under its stated assumptions. Application integration must preserve those assumptions. Component verification, product release, deployment, and customer acceptance each require their own evidence.

## Learn more

- [SMARTHAUS company and products](https://smarthaus.ai)
- [Investor overview and development stages](https://investor.smarthaus.ai)
- [Organization profile](../profile/README.md)
- [Private vulnerability reporting](../SECURITY.md)

Contact: [phil@smarthausgroup.com](mailto:phil@smarthausgroup.com)
