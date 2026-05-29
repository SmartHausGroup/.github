# NME — Nota Memoria Engine

**The meaning-extraction encoder that feeds the [RFS](../RFS/README.md) substrate · Latin: Noted Memory Engine · Status: Early active research**

---

## What NME is

NME is the **encoder layer** that turns raw text into the structured complex-valued waveforms that the [RFS field substrate](../RFS/README.md) stores. Where RFS is the storage layer (the 4D Fourier field that holds wave-encoded patterns), NME is the meaning-extraction layer (the encoder that decides what to store).

The two are complementary: without RFS, NME has nowhere to put its output; without NME, RFS would be physics on noise — wave-encoding random embeddings without any structured meaning behind the waves.

## What NME does

NME decomposes input text into the **10 components of meaning** the [SMARTHAUS Mathematical Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md) identifies, and produces FHRR-encoded waveforms that capture each component faithfully.

**Per-utterance components** (extracted from each chunk of input):
1. **Structure** — who did what to whom (the syntactic/semantic role frame).
2. **Content** — what the words refer to (entities, denotations).
3. **Modality** — certainty, possibility, obligation (epistemic status).
4. **Affect** — emotional coloring (sentiment, judgment).

**Between-utterance components** (connecting chunks):
5. **Relationships** — causal, temporal, contrastive links between events.
6. **Reference** — co-reference tracking (who "he/she/it" points to).
7. **Intent** — why something was said (speech acts: assert, request, promise).

**Over-time components** (accumulated in the field):
8. **Context** — surrounding discourse, situation, prior conversation.
9. **World knowledge** — background assumptions, common sense.
10. **Ambiguity resolution** — collapsing superposition via context and world knowledge.

The output is a **FHRR (Fourier Holographic Reduced Representation)** complex-valued waveform per semantic frame — phase encodes structure, magnitude encodes content. Multiple frames superpose in the RFS field, preserving both their individual identities (via phase orthogonality) and their relational structure (via interference patterns).

## How NME fits with RFS

NME and RFS communicate through a well-defined interface specified in the SMARTHAUS thesis: the encoder produces FHRR complex vectors at structured anchor positions in the field; the field stores them as superposed wave patterns; retrieval uses matched-filter projections that recover the encoded structure.

This separation matters architecturally: NME can be retrained, swapped, or specialized for new domains without changing the RFS substrate. RFS can be tuned (field dimension, dynamics parameters, decay rates) without changing the NME encoder. The interface is the contract; the two sides evolve independently.

## Status

NME is in **early active research**. The encoder architecture is implemented; the multi-task training across the 10 meaning components is in progress; the FHRR upgrade from scalar-phase to full FHRR is in design. The Princeton research collaboration uses an early NME variant to encode meaning structure into the RFS field for the spectral-pattern-discovery work in non-language domains.

Productization is on the Y2 H2 timeline alongside the RFS standalone offering.

Repo: `NotaMemoriaEngine`.

---

**[RFS — the storage substrate](../RFS/README.md)** · **[Substrate overview](../README.md)** · **[Mathematical Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)**

---

**[The Six Failures](https://github.com/SmartHausGroup/.github/blob/main/six-failures/README.md)** · **[Products](https://github.com/SmartHausGroup/.github/blob/main/products/README.md)** · **[PALI](https://github.com/SmartHausGroup/.github/blob/main/products/PALI/README.md)** · **[Mathematical Autopsy](https://github.com/SmartHausGroup/.github/blob/main/mathematical-autopsy/README.md)** · **[Princeton Research](https://github.com/SmartHausGroup/.github/blob/main/research/princeton.md)** · **[Patents](https://github.com/SmartHausGroup/.github/blob/main/research/patents.md)** · **[Math Thesis](https://github.com/SmartHausGroup/.github/blob/main/thesis/README.md)** · **[smarthaus.ai](https://smarthaus.ai)**
