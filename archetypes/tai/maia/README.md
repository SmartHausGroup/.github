# MAIA

**Attention mechanisms and intent processing**

Part of the **TAI** archetype. [← Back to TAI](../README.md)

## Role

MAIA is TAI’s attention and intent-decomposition layer. It receives classified intent (e.g. from VEE) and the current context—conversation history, retrieved memory, persona traits, available tools—and decides **what to attend to** and **how to break the goal into steps**. It does not run inference or store memory itself; it produces a focused view and a decomposition that VFE, RFS, and downstream actions consume. By making attention explicit and tunable, MAIA lets us bound what goes into inference, log what was attended to, and keep behavior auditable.

Context is large, but only a subset matters for the current intent. Without a dedicated attention layer we would either pass the entire context every time (expensive and noisy) or rely on ad-hoc selection. MAIA fills that gap: it focuses retrieval and decomposition so that VEE’s “what the user wants” is combined with “where to look” and “how to break it down,” in a way that complements NME (structured memory) and VFE (inference).

## Integration

**TAI** uses MAIA as the core component for attention and intent decomposition in the personal assistant. Every turn that requires reasoning over context or breaking a goal into steps flows through MAIA so that inference and memory access are focused and efficient.

**VFE** receives from MAIA the focused context and decomposition needed for model selection and inference. MAIA’s output determines which parts of context are passed to the model and how the task is framed.

**VEE** feeds MAIA with classified intent. MAIA uses that intent to drive attention (what to retrieve, what to weight) and to decompose the goal into concrete steps that other services can execute.

**RFS** is queried under MAIA’s direction for context and memory. Attention over the field—what to recall, how much, and in what order—is decided by MAIA so that retrieval stays aligned with the current intent.

Some TAI components may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA’s biology layer; attention and decomposition in MAIA are natural candidates for alignment with COE regions such as the Prefrontal Cortex and Basal Ganglia.
