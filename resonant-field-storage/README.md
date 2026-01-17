# Resonant Field Storage (RFS)

**A Holographic Memory Substrate for Intelligent Systems**

[![Repository](https://img.shields.io/badge/Repository-ResonantFieldStorage-blue)](https://github.com/SmartHausGroup/ResonantFieldStorage)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/SmartHausGroup/ResonantFieldStorage)
[![Invariants](https://img.shields.io/badge/Invariants-42%2B%20Validated-success)](https://github.com/SmartHausGroup/ResonantFieldStorage)
[![NVIDIA Inception](https://img.shields.io/badge/NVIDIA%20Inception-Member-76b900.svg)](https://www.nvidia.com/en-us/startups/)

## Overview

Resonant Field Storage (RFS) is a revolutionary approach to information storage and retrieval that treats memory as a mathematical field rather than a database. Instead of storing documents in tables and building indexes, RFS stores everything as superposed wave patterns in a shared 4-dimensional field and retrieves information through resonance.

**Core Innovation**: RFS implements a resonant field representation using standard digital signal processing (DSP) — Fast Fourier Transforms (FFTs) and wavelets — and controlled superposition. The value comes from the operational guardrails and mathematical guarantees layered on top.

**Mathematical Foundation**: RFS is built on field theory mathematics, not vector space mathematics. This fundamental difference enables capabilities that vector databases cannot provide: relationships as physics (interference patterns), explainability built into the mathematics, contradiction detection through destructive interference, deterministic guarantees, and temporal intelligence. For a detailed comparison of field theory vs. vector space mathematics, see [From Vector Space to Field Theory—A New Mathematical Foundation for Memory](./RFS:%20From%20Vector%20Space%20to%20Field%20Theory—A%20New%20Mathematical%20Foundation%20for%20Memory.md).

## What Makes RFS Different?

### Traditional Systems
- Documents stored separately
- Indexes built separately  
- Relationships must be explicitly defined
- Black-box search results
- No explainability
- O(N) storage complexity

### RFS Approach
- **All documents superposed in one field** — N documents stored in O(D) space, not O(N)
- **Relationships emerge automatically** through interference patterns
- **Resonance-based retrieval** — not keyword matching, but semantic resonance
- **Explainable results** with interference patterns showing why documents are related
- **Mathematical guarantees** for correctness, determinism, and energy conservation
- **Dual query paths** — fast simple search or rich field-native search on the same field

## Core Capabilities

### 1. Superposition
All documents are stored together in a single 4D field `(x, y, z, t)`. This means:
- **Space Efficiency**: N documents stored in O(D) space, not O(N)
- **Automatic Relationships**: Documents interact and create interference patterns
- **Unified Storage**: One field, not separate indexes
- **Temporal Dimension**: Track evolution over time (4th dimension)

**How It Works**: Each document is encoded as a waveform ψ_d(x, y, z, t) through a multi-stage process:
1. **Text Encoding**: Document → embedding vector (via ThetaTextEncoder or similar)
2. **Field Encoding**: Embedding → 4D waveform via ResonantFieldEncoder using FFT operations
3. **Projection**: Waveform → associative band via AssociativeProjector (band-limited projection using Π_assoc = ℱ⁻¹ · M_assoc · ℱ)
4. **Superposition**: Individual waveforms combine linearly into the total field: Ψ = Σ_d ψ_d

The superposition is mathematically precise—wave addition is linear and energy-preserving under Parseval's theorem (‖Ψ‖₂² = ‖ℱΨ‖₂²). This means relationships are not computed—they are measured through interference patterns Λ_ij = ⟨ψ_i, ψ_j⟩.

### 2. Resonance Search
Queries work by exciting resonances in the field:
- **Semantic Matching**: Finds meaning, not just keywords
- **Fast Retrieval**: Parallel FFT operations enable rapid search
- **Relationship Discovery**: Automatically finds related documents
- **Unified Query System**: Choose `query_simple()` for fast cosine similarity or `query()` for full field-native features on the same field (see [Performance Benchmarks](#unified-query-system) for detailed metrics)

### 3. Interference Patterns
Wave interference reveals information:
- **Constructive Interference**: Documents that reinforce each other (relationships, analogies)
- **Destructive Interference**: Documents that contradict (tensions, contradictions)
- **Explainability**: Interference patterns explain why results were returned
- **Quantified Metrics**: Q (resonance clarity), η (destructive energy ratio)

### 4. Exact Recall
AEAD-backed byte channel ensures:
- **Perfect Reconstruction**: Exact bytes recovered, not approximations
- **Integrity Verification**: Cryptographic guarantees for authenticity
- **Audit Trail**: Complete provenance for compliance
- **Dual Fidelity**: Associative (fast, approximate) and recall (exact, bounded-error) modes

**How Dual Fidelity Works**: The field uses spectral separation to store both semantic content and exact byte data in the same 4D field:
- **Semantic Band (𝔅_sem)**: Stores waveforms for associative retrieval via FFT operations with band-limited projection
- **Byte Band (𝔅_byte)**: Stores exact byte data as compressed bytes + FEC codes, protected by AEAD seals
- **Guard Bands**: Mathematical isolation between bands enforced by projector Π_assoc = ℱ⁻¹ · M_assoc · ℱ

The bandplan ensures Σ(M_assoc ∧ M_byte) = 0: semantic and byte bands are disjoint. This mathematical guarantee enables dual fidelity: approximate similarity and exact recall in the same field without interference.

**Exact Recall Process**: When retrieving exact bytes:
1. Extract byte carriers from field using band-limited projection
2. Use error-correcting codes (FEC) to recover exact bytes
3. Verify cryptographic seal (AEAD) to ensure integrity
4. Decompress to recover original document bytes

If any step fails (corruption, tampering, insufficient redundancy), retrieval fails closed—no silent corruption.

### 5. Mathematical Guarantees
Every operation is mathematically proven:
- **42+ Invariants**: Validated in continuous integration
- **60+ Verification Notebooks**: Executable proofs with deterministic execution
- **Deterministic**: Same inputs always produce same outputs
- **Energy Conservation**: All operations preserve mathematical properties (Parseval's theorem)
- **Formal Proofs**: Lemmas and theorems document every guarantee

**How Determinism Works**: RFS is deterministic by mathematical design:
- **Deterministic Encoding**: Same document always produces the same waveform (seeded randomness, deterministic transforms)
- **Deterministic Superposition**: Wave addition is mathematically precise (linear superposition: Ψ = Σ_d ψ_d)
- **Deterministic Interference**: Overlap tensor is mathematically exact (Λ_ij = ⟨ψ_i, ψ_j⟩)
- **Deterministic Retrieval**: Same query always produces the same results (matched filter correlation is deterministic)

**Energy Accounting**: RFS uses Parseval's theorem for precise energy accounting. Under unitary FFT scaling, energy is preserved: ‖Ψ‖₂² = ‖ℱΨ‖₂². The field tracks:
- Total field energy: E_total = ‖Ψ‖₂²
- Energy budgets: Per-document energy constraints
- Interference energy: Destructive energy from interference
- Capacity margins: Headroom for additional documents (P99 ≥ 1.3×)

This is not monitoring—it is mathematical accounting. The field theory foundation provides energy conservation through Parseval's theorem.

## Architecture

### The 4D Field Lattice

RFS maintains a **4-dimensional complex tensor**:

$$\Psi(x, y, z, t) \in \mathbb{C}$$

**Why 4D?**
- **Three spatial dimensions** `(x, y, z)`: Allow documents to occupy distinct "locations" in the field, enabling spatial multiplexing and interference patterns that encode semantic relationships
- **One temporal dimension** `(t)`: Enables recency weighting, memory consolidation, temporal context, and decay dynamics

### Architectural Stack

1. **Field Dynamics Layer** — Maintains the complex amplitude/phase field in GPU memory
   - 4D complex tensor Ψ(x, y, z, t) ∈ ℂᴰ where D = n³·S
   - FFT/IFFT operations with unitary scaling (Parseval equivalence)
   - Optional PDE evolution (feature-gated, default off) for predictive capabilities
   - Decay-first dynamics: per-document exponential decay with periodic re-projection

2. **Field-Native Semantic Encoding Layer** — Maps tokens/features into waveform primitives
   - Text → embedding via ThetaTextEncoder
   - Embedding → 4D waveform via ResonantFieldEncoder (FFT operations)
   - Band-limited projection via AssociativeProjector (Π_assoc = ℱ⁻¹ · M_assoc · ℱ)
   - Deterministic phase masks and spatial transforms

3. **Resonance Query & Retrieval Layer** — Unified field with dual query paths (`query_simple()` and `query()`)
   - `query_simple()`: Fast cosine similarity on preserved document vectors (O(N) complexity)
   - `query()`: Full field-native resonance via matched filter correlation (O(C D log D) complexity)
   - Both paths operate on the same underlying field and vectors

4. **Ops, Integrity & Governance Layer** — Metadata, persistence, snapshots, WAL, guardrails
   - Write-Ahead Log (WAL): Every operation logged with canonical parameters
   - Snapshots: Field states captured and restored exactly
   - Mathematical provenance: Every result traceable to its mathematical origin
   - Guardrails: Q_dB, η, capacity margins, recall error budgets

### Unified Query System

**One field, two query paths:**

- **`query_simple()`**: Fast cosine similarity on preserved document vectors
  - O(N) complexity
  - <1ms p95 latency
  - Simple semantic search without field-native features

- **`query()`**: Full field-native resonance search
  - O(C D log D) complexity
  - 5-50ms latency
  - Interference patterns, relationship discovery, explainability

Both paths operate on the same underlying field and vectors, ensuring consistency and eliminating duplicate storage.

#### Performance Benchmarks

**Baseline: Mac Studio M2 Ultra (76-core GPU)**
- **`query_simple()`**: ~1,000 QPS (p95 latency <1ms)
- **`query()`**: ~200-300 QPS (p95 latency 5-50ms)

*Note: All performance measurements are based on actual benchmarks run on Mac Studio M2 Ultra hardware.*

**Theoretical Cloud Deployment Performance**

*The following performance estimates are theoretical calculations based on publicly available chip specifications and architectural analysis. Actual performance will vary based on workload characteristics, system configuration, and optimization level.*

**Small Deployment: NVIDIA A100 (Single GPU)**
- **Chip Specs**: 19.5 TFLOPS FP32, 312 TFLOPS FP16 Tensor, 1.6 TB/s memory bandwidth
- **`query_simple()`**: ~1,500-2,000 QPS (memory-bound, ~1.5-2x baseline)
- **`query()`**: ~400-600 QPS (compute-bound, ~2x baseline)

**Medium Deployment: NVIDIA H100 (Single GPU)**
- **Chip Specs**: 60 TFLOPS FP32, 1,000 TFLOPS FP16 Tensor, 3 TB/s memory bandwidth
- **`query_simple()`**: ~3,000-4,000 QPS (memory-bound, ~3-4x baseline)
- **`query()`**: ~800-1,200 QPS (compute-bound, ~4x baseline)

**Large Deployment: GPU Clusters (Cerebras WSE-3 or NVIDIA MGX)**
- **Cerebras WSE-3 Cluster**: 125,000 TFLOPS FP16, 21 PB/s memory bandwidth
- **NVIDIA MGX Cluster** (8x H100): 8,000 TFLOPS FP16, 24 TB/s aggregate memory bandwidth
- **`query_simple()`**: ~10,000-50,000+ QPS (scales with cluster size and parallelism)
- **`query()`**: ~2,000-10,000+ QPS (scales with cluster size and FFT parallelism)

*Performance scaling assumptions:*
- *`query_simple()` scales primarily with memory bandwidth and parallel matrix-vector operations*
- *`query()` scales primarily with compute throughput (FFT operations) and field dimension parallelism*
- *Cluster performance assumes efficient workload distribution and minimal communication overhead*
- *Actual performance depends on field size (D), document count (N), query complexity (C), and system optimization*

## Key Benefits

### For Developers
- **Simpler Architecture**: One system instead of vector DB + blob store + indexes
- **Automatic Relationships**: No need to manually define connections
- **Explainable Results**: Understand why documents were retrieved
- **Mathematical Guarantees**: Proven correctness, not just tested
- **Flexible Querying**: Choose the right query path per request

### For Enterprises
- **Compliance Ready**: Audit trails and exact recall for legal requirements
- **Cost Efficient**: Lower storage overhead through superposition
- **Privacy Preserving**: Runs locally on edge devices
- **Scalable**: Handles large document collections efficiently
- **Deterministic**: Reproducible results for debugging and compliance

### For Researchers
- **Relationship Discovery**: Automatic pattern detection
- **Temporal Analysis**: Track evolution over time (4th dimension)
- **Interference Insights**: Understand document interactions
- **Reproducible**: Deterministic guarantees enable scientific rigor
- **Mathematical Foundation**: Formal proofs and invariants

## Technical Highlights

- **4D Field**: Spatial (x, y, z) + temporal (t) dimensions
- **Metal Acceleration**: GPU-accelerated FFT operations on Apple Silicon
- **AEAD Security**: Cryptographic integrity for exact recall
- **Mathematical Guardrails**: Q (resonance clarity), η (destructive energy), capacity margins
- **Edge Deployment**: Runs locally, preserving data privacy
- **Deterministic**: All operations are mathematically guaranteed to be deterministic
- **Notebook-First Development**: Code originates in notebooks, then extracted to codebase

### Field Theory Foundation

RFS is built on field theory mathematics, not vector space mathematics. This fundamental difference enables:

- **Relationships as Physics**: Interference patterns (Λ_ij = ⟨ψ_i, ψ_j⟩) encode relationships, not computed distances
- **Explainability Built-In**: Interference patterns, resonance quality (Q_dB), and destructive energy ratio (η) provide explanation
- **Contradiction Detection**: Destructive interference (Re(Λ_ij) < 0) automatically detects contradictions
- **Deterministic Guarantees**: Field theory enables deterministic operations validated through 42+ invariants
- **Temporal Intelligence**: Time is a native dimension of the field, not external metadata
- **Unified Storage**: One field stores semantic content, exact bytes, relationships, and temporal evolution
- **Energy Accounting**: Parseval's theorem enables precise energy tracking and capacity planning

### Spectral Separation

The field uses guard bands to mathematically isolate semantic content from exact byte data:
- **Projector**: Π_assoc = ℱ⁻¹ · M_assoc · ℱ enforces spectral separation
- **Bandplan**: Semantic frequencies (𝔅_sem) and byte carriers (𝔅_byte) are disjoint
- **Mathematical Guarantee**: Σ(M_assoc ∧ M_byte) = 0 (bands don't overlap)
- **Dual Fidelity**: Approximate similarity (semantic band) and exact recall (byte band) in the same field

### Entanglement Graphs

RFS automatically builds relationship networks from interference patterns:
- **Overlap Tensor**: Λ_ij = ⟨ψ_i, ψ_j⟩ directly encodes relationships
- **Community Detection**: Leiden algorithm on interference-based weights finds natural clusters
- **Automatic Updates**: Graph updates as field evolves, no external computation required
- **Contradiction Detection**: Destructive interference surfaces conflicts automatically

## Implementation Status

### ✅ Production Ready
- 4D field storage and retrieval
- Wave-based encoding/decoding
- Phase mask system for document separation
- Projector-based band separation (semantic vs byte channels)
- Matched-filter retrieval
- AEAD-backed exact recall
- **42 mathematical invariants** validated
- **60+ verification notebooks** with executable proofs
- **Latest Benchmark:** 44% Recall@10 in fully superposed field (Optimization in progress)
- Unified query system (dual query paths)

### 🚧 In Development
- Multi-scale FFT pyramids + ROI refinement
- Field-native encoder v1 (harmonic/Gabor bases)
- Multi-domain cortices
- Edge deployment + sync + traits
- Entanglement graph (offline relationship discovery)

### 🔬 Research
- PDE evolution (feature-gated, default off)
- Advanced attractor dynamics
- Multi-modal field integration

## Mathematical Guarantees

### Core Metrics

- **Q_dB**: Resonance clarity over local background (20·log₁₀(peak/background))
- **η**: Fraction of energy that cancels (destructive overlap)
- **Capacity Margin**: Byte-channel headroom ratio (P99 ≥ 1.3×)
- **ε_recall**: Reconstruction error budget (archival ≤ 1e⁻⁸; assistant ≤ 1e⁻⁶)

### Invariants

RFS maintains **42+ mathematical invariants** covering:
- Energy conservation (Parseval's theorem)
- Phase orthogonality
- Interference bounds
- Capacity margins
- Recall error bounds
- Performance bounds
- Field dynamics and stability

All invariants are:
- Mathematically defined
- Verified in notebooks
- Enforced in CI
- Documented in lemmas

## Use Cases

RFS excels in scenarios where relationships, explainability, and exact recall matter:

1. **Incident Memory for On-Call Teams** — Automatically discover related incidents and patterns
2. **RAG with Proofs** — Explainable document selection for LLM context
3. **Code Intelligence** — Find code analogies and patterns automatically
4. **Compliance/Legal Archive** — Audit-ready document relationships with exact recall
5. **Research Knowledge Graph** — Track concept evolution and research communities
6. **Pharmaceutical Discovery** — Discover novel drug combinations through relationship discovery and GNN prediction

See [Use Cases](./use-cases/) for detailed documentation on each scenario.

## Development Methodology

RFS follows **notebook-first development** as part of the Mathematical Autopsy (MA) process:

1. **Math & Documentation** — Define intent, mathematical foundations, lemmas, and invariants
2. **Notebook Implementation** — Write implementation code directly in notebooks
3. **Validation** — Test code against lemmas/invariants, generate artifacts
4. **Code Extraction** — Extract validated code from notebooks to codebase
5. **Verification** — Verify extracted code matches math

**Critical Order**: Math → Invariants → Code (NEVER Code → Math)

## Learn More

- **Use Cases**: [Detailed use case documentation](./use-cases/)
- **Repository**: [ResonantFieldStorage on GitHub](https://github.com/SmartHausGroup/ResonantFieldStorage)
- **SMARTHAUS Vision**: [SMARTHAUS Vision Document](../SMARTHAUS_VISION.md)
- **Organization**: [SmartHausGroup](https://github.com/SmartHausGroup)
- **Website**: [smarthaus.ai](https://smarthaus.ai)
- **Field Theory vs. Vector Space**: [From Vector Space to Field Theory—A New Mathematical Foundation for Memory](./RFS:%20From%20Vector%20Space%20to%20Field%20Theory—A%20New%20Mathematical%20Foundation%20for%20Memory.md) — Comprehensive comparison of field theory mathematics vs. vector space mathematics, explaining why RFS's mathematical foundation enables capabilities that vector databases cannot provide

## License

**PROPRIETARY SOFTWARE** — All content in this repository is proprietary and confidential property of SmartHaus Group. All rights reserved. Unauthorized copying, modification, distribution, or use is strictly prohibited.

For licensing inquiries, please contact: **Philip Siniscalchi** at phil@smarthausgroup.com

See [LICENSE](../LICENSE) file for full terms.

---

**RFS — Storage behaving like perception: associative, interrogable, and provably recoverable from the same substrate.**
