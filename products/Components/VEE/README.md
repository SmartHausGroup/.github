# VEE — Math, Privacy, and Reinforcement-Learning Kernel

**Latin: Voluntas Engine · Status: Active development**

---

## What VEE is

VEE is the **math kernel** that other Components depend on. It provides the mathematical primitives — Lyapunov stability utilities, quantum-inspired compute, differential-privacy primitives, and a reinforcement-learning substrate — that other Components import rather than re-implement.

VEE is not customer-facing. It is the shared math layer that lets MAIA, UCP, SAID, MAE, and the broader substrate stand on a common, optimized foundation rather than each Component carrying its own math implementations.

**Note on naming:** Despite the Latin name *Voluntas* (will/intent), VEE is **not** the intent engine. The intent engine is [MAIA](../MAIA/README.md). An earlier naming asserted VEE as the intent engine; that framing is retired. VEE provides math primitives that MAIA (and other Components) consume.

## What VEE provides

- **Lyapunov stability utilities.** Mathematical tools for analyzing the stability of dynamic systems — used by Components that need to reason about whether a control loop or feedback system will converge or drift.
- **Quantum-inspired compute primitives.** Native C++ via pybind11 over Eigen. The `aiucp_quantum_core` package provides high-performance tensor operations used in the SMARTHAUS substrate's field encoding and retrieval.
- **Differential privacy primitives.** Composable building blocks for differentially-private operations (Laplace mechanism, Gaussian mechanism, privacy budget accounting). Used by Components that need to compute over user data with formal privacy guarantees.
- **Reinforcement-learning substrate.** Common RL primitives (policy representations, value functions, reward shaping) that MAIA's intent refinement and other Components' learning loops build on.

## How VEE fits with the other Components

VEE is the math infrastructure underneath the SMARTHAUS Component stack:

- **[MAIA](../MAIA/README.md)** uses VEE's RL substrate for intent refinement.
- **[UCP](../UCP/README.md)** uses VEE's privacy primitives where admission decisions involve user-data computations.
- **[SAID](../SAID/README.md)** uses VEE's quantum-inspired compute for substrate-related inference operations.
- **The [RFS substrate](../../Substrate/RFS/README.md)** uses VEE's Eigen-backed tensor primitives in its field operations.
- **Any Component** that needs Lyapunov stability analysis or differential privacy can import VEE rather than re-deriving the math.

## Status

VEE is in **active development**. The core math primitives are built and in use by other Components (UCP, SAID, RFS). The standalone FastAPI surface (`/health`, `/quantum/*`) is optional for Components that need network-mediated access. Productization is internal-facing; VEE is not sold as a standalone customer product.

Repo: `VoluntasEngine`.

---

**[Other Components](../README.md)** · **[Substrate](../../Substrate/README.md)** · **[PALI](../../PALI/README.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
