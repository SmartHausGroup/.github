# NME — Nota Memoria Engine

**Memory structuring and trait extraction before RFS**

Part of the **TAI** archetype. [← Back to TAI](../README.md)

## Role

NME (Nota Memoria Engine) is the memory-structuring and trait-extraction layer that sits **upstream** of RFS. It consumes raw user content—conversations, preferences, events, feedback—and turns it into structured episodes and persona traits (preferences, personality, communication style) that RFS can store and that TAI can recall with the same mathematical guarantees (exact-byte or semantic). NME does not run the 4D field or execute inference; it prepares and types the data so that what enters the field is consistent, queryable, and suitable for endless recall and personalization.

RFS stores **waveforms**—superposed, interference-rich, deterministic. Raw user content is not yet in that form. Without NME we would either dump raw data into the field (noisy, hard to recall by trait) or leave structuring undefined. NME is the layer that turns user interactions into **structured memory** and **persona traits** so that RFS and TAI get endless, auditable memory instead of a pile of unstructured data.

## Integration

**RFS** receives from NME the structured memory and traits that are encoded into the 4D field. NME’s output—typed episodes, trait vectors, and metadata—is what gets superposed and queried; NME ensures that format and schema are consistent so that retrieval and interference behave as specified.

**TAI** uses NME for all learning and personalization that feeds into memory. Every user interaction that should be remembered or used to update persona traits flows through NME before being written to RFS, so that the assistant’s “endless memory” is both rich and auditable.

**VEE and VFE** can integrate with NME when intent or inference depend on memory and traits. NME’s structured output can inform intent classification (VEE) and context selection for inference (VFE) so that recall and reasoning stay aligned.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; memory structuring and trait extraction in NME are natural candidates for alignment with COE regions such as the Hippocampus.
