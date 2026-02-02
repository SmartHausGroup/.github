# AEF — AIVA Execution Fabric

**Physics layer of AIVA: particle-based execution engine**

Part of the **AIVA** archetype. [← Back to AIVA](../README.md)

## Role

AEF (AIVA Execution Fabric) is the **Physics layer** of the triadic AIVA system. It receives compiled DAGs from AQL, turns them into particle instructions, and **runs** them: scheduling, resource allocation, and telemetry are all within AEF. AIOS decides what to do; AQL proves the structure is correct; AEF **executes** that structure. Particles are **stateless** (A2) and **deterministic** (A1), so execution is reproducible and auditable. The physics layer exists because **running** is a different job from **deciding** and **proving**: splitting execution from structure gives scale (particles run in parallel, across nodes, without the brain or chemistry in the loop), resource safety (AEF enforces concurrency and time budgets; admission control rejects overload per A9), and observability (every run produces canonical execution state and metrics, fed back to AIOS via the ANS for monitoring and fail-close). AEF is **bounded, observable execution** that the rest of the pipeline can trust and audit.

## Architecture

AEF organizes work into **particle types**, each with a well-defined role and contract. **Quarks** perform core computation (e.g. LOAD_QUARK, EXEC_QUARK, STORE_QUARK). **Leptons** handle I/O (READ_LEPTON, WRITE_LEPTON, STREAM_LEPTON). **Bosons** handle communication and messaging (EMIT_BOSON, RECV_BOSON, BROADCAST_BOSON). **Gluons** handle binding and synchronization (BIND_GLUON, RELEASE_GLUON, BARRIER_GLUON). **Neutrinos** handle silent monitoring and tracing (TRACE_NEUTRINO, MONITOR_NEUTRINO, LOG_NEUTRINO). The scheduler respects DAG dependencies and resource budgets so that particles run in the correct order without overloading the system. Execution is quantum-inspired on classical hardware—superposition and entanglement are simulated where useful—with energy-based resource management and built-in telemetry so that every run is observable and, where required, reproducible.

## Key features

AEF provides **quantum-like computation** on classical hardware (superposition and entanglement simulation where it aids parallelism or reasoning), **energy-based resource management** so that CPU, memory, and time are bounded (A9), and **built-in telemetry and observability** so that execution state and metrics are canonical and feed back into AIOS. **A/B testing and optimization** can be run over particle execution so that tuning is data-driven and consistent with the same mathematical guarantees that govern the rest of the pipeline.

## Integration

**AQL** feeds AEF with compiled DAGs. AEF turns those DAGs into particle instructions, schedules them, and runs them. No structure verification happens in AEF; AQL guarantees correctness before execution begins.

**AIOS** receives execution telemetry from AEF via the SNS and ANS. Telemetry (latency, errors, resource use) is used for monitoring, fail-close (A3), and learning—policy tuning, Basal Ganglia gates, and Amygdala sensitivity all consume AEF’s output so that the next intent can be gated or routed differently.

**RFS** can store execution state and telemetry when persistence or audit is required, so that runs are traceable and reproducible alongside the rest of the system’s memory and state.
