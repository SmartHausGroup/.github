# GitHub Terminology & README Master Plan

**Purpose**: Single source of truth for (1) aligning SmartHausGroup.github (public-facing site) with current naming and architecture, and (2) building substantial READMEs for each part of the TAI and AIVA archetypes.  
**Status**: In progress — Part III (site terminology) and site structure (one section per product) executed. Repo READMEs per Part VI may still be applied to individual repos.  
**Date**: 2025-02-02

**Supersedes** (combines; do not lose content from):
- `GITHUB_SITE_TERMINOLOGY_PLAN.md`
- `README_BUILD_PLAN.md`

---

# Part I — Canonical Terminology Changes

## 1.1 Chemistry layer: LQL → AQL

| Old | New | Clarity |
|-----|-----|---------|
| LQL (LATTICE Query Language) | **AQL (AIVA Query Language)** | Chemistry layer; **separate** from Biology (AIOS). Transforms intent into mathematically provable execution graphs (DAGs). |

- **Use everywhere**: "Chemistry Layer (AQL)", "AQL (AIVA Query Language)", "AQL — Chemistry layer".
- **Repository**: If the repo stays named LQL for now, site copy should still say "AQL (AIVA Query Language)" and can note "implementation: LQL repository" if desired.

## 1.2 Physics layer: LEF → AEF

| Old | New | Clarity |
|-----|-----|---------|
| LEF (Lattice Execution Fabric) | **AEF (AIVA Execution Fabric)** | Physics layer; executes AQL-compiled particle instructions. |

- **Use everywhere**: "Physics Layer (AEF)", "AEF (AIVA Execution Fabric)", "AEF — Physics layer".

## 1.3 RFS — mathematical memory substrate (both archetypes)

- **RFS** = **Resonant Field Storage** — our **mathematical memory substrate**.
- **Shared by both archetypes**:
  - **TAI**: RFS is the memory substrate (user memory, endless recall, semantic retrieval).
  - **AIVA**: RFS is the memory substrate (e.g. AIOS Hippocampus, system/episodic memory).
- **Wording**: Where we describe TAI and AIVA, explicitly state that "RFS is the memory substrate for both TAI and AIVA" (or "in both TAI and AIVA").

## 1.4 CAIO replaced AIUCP

- **AIUCP (AI Unified Control Plane)** and "AIUCP protocol" are **no longer used**. **CAIO replaced AIUCP** for integration.
- **Action**: Remove every mention of AIUCP on the GitHub site and replace with **CAIO**-based language.
- **Replace with**: External systems (e.g. TAI) integrate with AIVA **via CAIO** (service routing and access control). Use "CAIO-mediated integration", "integrates via CAIO", or "protocol-based integration through CAIO" as appropriate. Do not use "AIUCP" or "AI Unified Control Plane".

## 1.5 TAI components: NME, VFE, MAIA, VEE, CAIO (and COE)

- **Five TAI service components** (may become or align with parts of the COE):
  - **NME** — Nota Memoria Engine: memory structuring / trait extraction before RFS.
  - **VFE** — Verbum Field Engine: GPU-first LLM inference.
  - **MAIA** — Attention mechanisms and intent processing.
  - **VEE** — Voluntas Engine: intent classification and quantum-inspired math.
  - **CAIO** — Service routing and access control.
- **Action**: Ensure the GitHub site lists these five by name (NME, VFE, MAIA, VEE, CAIO) where TAI architecture is described, and add a short note that some of these may align with or become parts of the COE (Cognitive Orchestration Engine) in AIVA's biology layer.

---

# Part II — Summary of Copy Rules (Site + Repos)

1. **Chemistry layer** → Always **AQL (AIVA Query Language)**. Describe as the **separate** Chemistry layer that compiles intent to DAGs.
2. **Physics layer** → Always **AEF (AIVA Execution Fabric)**. Describe as executing AQL output (particle instructions).
3. **RFS** → Always "**mathematical memory substrate**" and "**memory substrate for both TAI and AIVA**" (or "in both TAI and AIVA").
4. **AIUCP** → Remove. **CAIO replaced AIUCP**: say "via CAIO" or "CAIO-mediated integration" for TAI ↔ AIVA / external integration.
5. **TAI components** → List **NME, VFE, MAIA, VEE, CAIO** by name; note possible COE alignment where relevant.

**Terminology to apply in all READMEs** (repos):

- **AQL** — AIVA Query Language (Chemistry layer). Not "LQL" in narrative unless referring to repo name.
- **AEF** — AIVA Execution Fabric (Physics layer). Not "LEF" in narrative unless referring to repo name.
- **RFS** — Resonant Field Storage; **memory substrate for both TAI and AIVA**.
- **CAIO** — Replaced AIUCP; use "via CAIO" or "CAIO-mediated" for TAI ↔ AIVA / external integration.
- **NME, VFE, MAIA, VEE, CAIO** — List by name in TAI; optional note that some may align with COE.

---

# Part III — GitHub Site Files to Update (SmartHausGroup.github)

**Status**: ✅ Done. Terminology (AQL, AEF, CAIO, RFS, NME) applied across the site; AIUCP removed.

| File | Changes | Done |
|------|--------|------|
| **README.md** | LQL→AQL, LEF→AEF; RFS as memory substrate; NME in TAI; AIUCP removed. **Plus**: one section per product; no RFS Core/SDK or mge-core/mge-sdk on site. | ✅ |
| **profile/README.md** | Same as README.md (in sync); relative links from `profile/`. | ✅ |
| **SMARTHAUS_VISION.md** | LQL→AQL, LEF→AEF; RFS wording; AIUCP removed; NME + five components + COE note. | ✅ |
| **archetypes/aiva/README.md** | AQL, AEF, CAIO; RFS as memory substrate; repo links as "AQL (LQL repo)" etc. | ✅ |
| **archetypes/tai/README.md** | NME in services; RFS as TAI memory substrate; VFE, MAIA, VEE, CAIO named. | ✅ |
| **archetypes/mge/README.md** | Scan for LQL/LEF/AIUCP; update if needed. | (no hits in scan) |
| **resonant-field-storage/README.md** | Optional: RFS memory substrate for both TAI and AIVA. | (optional) |
| **mathematical-autopsy/README.md** | Scan for LQL/LEF/AIUCP; update if needed. | (no hits in scan) |

---

# Part IIIb — Site Structure: One Section per Product (GitHub Pages–ready)

**Status**: ✅ Done. Site presents one website-style section per product; no Core/SDK sub-lists on the main site.

**Principle**: One page per product on SmartHausGroup.github. Do **not** list RFS Core, RFS SDK, mge-core, mge-sdk, or MA Application/Methodology/SDK as separate bullets on the site. Each product has a single destination (product page in this repo + primary GitHub repo).

**Product pages** (single section each, linked from root README and profile):

| Product | Page in this repo | Primary GitHub repo |
|--------|--------------------|----------------------|
| **Resonant Field Storage (RFS)** | `resonant-field-storage/README.md` | ResonantFieldStorage |
| **TAI** (Personal Assistant) | `archetypes/tai/README.md` | TAI |
| **AIVA** (Triadic AI) | `archetypes/aiva/README.md` | AIVA |
| **MGE** (Governance) | `archetypes/mge/README.md` | MGE |
| **Mathematical Autopsy (MA)** | `mathematical-autopsy/README.md` | MathematicalAutopsy |

**Root README.md** (and profile/README.md): "Product Pages" section with one short block + one link per product; "Product & Repo Index" table (one row per product, no -core/-sdk rows). Ready for GitHub Pages: root = homepage; the five paths above = product pages.

---

# Part IV — README Standard (Substantial READMEs for Each Repo)

## Standard sections for each repo README

Each substantial README should include:

1. **Title & one-line tagline** — Repo name, full name if acronym, and role in one sentence.
2. **Archetype placement** — "Part of the **TAI** archetype" or "Part of the **AIVA** archetype" and how it fits (e.g. "Chemistry layer of AIVA").
3. **Overview** — 2–4 sentences: what it does, for whom, and why it exists.
4. **Key capabilities** — Bullet list of main features/capabilities.
5. **Architecture** — High-level components, directory or service map if helpful.
6. **Integration** — Upstream/downstream: RFS, CAIO, VFE, AQL, AEF, etc. Use current terminology (AQL not LQL, AEF not LEF, CAIO not AIUCP, RFS as memory substrate for both TAI and AIVA).
7. **Quick start** — Prerequisites, install, minimal run/test.
8. **Documentation** — Links to North Star, API, ops, math docs.
9. **Mathematical guarantees** — If applicable: MA process, invariants, determinism.
10. **License & contact** — Consistent with org.

## TAI archetype — repos and findings

| Repo | Role | Current README | Action |
|------|------|----------------|--------|
| **tai** | Personal assistant orchestration; voice-first; API & web UI | Good: voice-first, CAIO/VFE, services | Add NME, RFS as memory substrate, all five services (NME, VFE, MAIA, VEE, CAIO); "integrates via CAIO" |
| **ResonantFieldStorage** | RFS product/landing; 4-pillar narrative | Strong: math, four capabilities | Add "memory substrate for both TAI and AIVA" |
| **rfs-core** | RFS implementation | Technical, North Star, status | Add one-line archetype: "RFS is the memory substrate for TAI and AIVA" |
| **NotaMemoriaEngine (NME)** | Trait extraction & memory structuring before RFS | Short | Expand: traits, Titans patterns, integration (TAI, RFS, VEE, VFE), quick start |
| **vfe** / **vfe-core** | Verbum Field Engine — GPU-first inference | Good: calculus, backends | Add archetype placement (TAI + optional AIVA/COE) |
| **VoluntasEngine (VEE)** | Intent engine; RL + quantum-inspired | Structured, dry | Add narrative, TAI/MAIA integration, archetype placement |
| **caio** / **caio-core** | Service routing & access control; **replaced AIUCP** | Good quick start | Add "CAIO replaced AIUCP"; TAI and AIVA integration via CAIO |
| **MAIA** | Attention & intent; routes to VFE/RFS/marketplace | Good: master equation | Add archetype placement, link to VEE/CAIO |

## AIVA archetype — repos and findings

| Repo | Role | Current README | Action |
|------|------|----------------|--------|
| **AIVA** | Architecture & specs only; triadic system | Long; uses LATTICE, AIUCP, LQL, LEF | Terminology pass: AQL, AEF, CAIO not AIUCP; "implementation in AIOS, AQL, AEF" |
| **AIOS** | Biology layer = CNS (COE + SNS + ANS); RFS as memory | Root README is **LQL Enterprise** (wrong) | **Replace** with full AIOS README: CNS, COE, SNS, ANS, RFS, orchestration, link to AQL/AEF |
| **LQL** | Chemistry layer → **AQL (AIVA Query Language)** | Root README is planning index | Add or promote **AQL** README: Chemistry layer, DAGs, molecules, link to AIOS/LEF |
| **LEF** | Physics layer → **AEF (AIVA Execution Fabric)** | Good: particles, compiler, runtime | Terminology: AEF, "executes AQL output"; keep LEF in repo name if unchanged |

---

# Part V — File Locations for README Updates (Repos)

- TAI: `tai/README.md`
- RFS: `ResonantFieldStorage/README.md`, `rfs-core/README.md`
- NME: `NotaMemoriaEngine/README.md`
- VFE: `vfe/README.md`, `vfe-core/README.md`
- VEE: `VoluntasEngine/README.md`
- CAIO: `caio/README.md`, `caio-core/README.md`
- MAIA: `MAIA/README.md`
- AIVA: `AIVA/README.md`
- AIOS: `AIOS/README.md`
- LQL: `LQL/README.md` (consider `README.enterprise.md` or new root README for AQL)
- LEF: `LEF/README.md`

---

# Part VI — Execution Order

**GitHub site** (SmartHausGroup.github): After you confirm or adjust open points (§VIII), apply terminology edits file-by-file (Part III), then run a final grep for any remaining LQL/LEF/AIUCP on the site.

**Repo READMEs** (suggested order):

1. **AIOS** — Replace root README (currently LQL) with full AIOS CNS README.
2. **AIVA** — Terminology pass (AQL, AEF, CAIO).
3. **LQL** — New root README for AQL (Chemistry layer).
4. **LEF** — Terminology pass (AEF).
5. **TAI** — Add NME, RFS wording, five components.
6. **ResonantFieldStorage** / **rfs-core** — Add "memory substrate for both TAI and AIVA".
7. **NotaMemoriaEngine** — Substantial README.
8. **VoluntasEngine** — Narrative + archetype.
9. **caio** / **caio-core** — CAIO replaced AIUCP, integration wording.
10. **MAIA** — Archetype placement.
11. **vfe** / **vfe-core** — Archetype placement.

---

# Part VII — Open Points for You

1. ~~**AIUCP replacement**~~ **Resolved**: CAIO replaced AIUCP; use "via CAIO" / "CAIO-mediated integration".
2. **Repo names vs product names**: If repos stay **LQL** and **LEF**, should the site say "AQL (implementation: LQL repository)" and "AEF (implementation: LEF repository)", or only "AQL" / "AEF" with links to the same repos?
3. **NME on .github**: Confirm NME = Nota Memoria Engine and that it should be listed alongside VFE, MAIA, VEE, CAIO in TAI and in the COE-alignment note.
4. **COE alignment**: Preferred wording: "Some TAI components (NME, VFE, MAIA, VEE, CAIO) may align with or become parts of the COE" or something stronger (e.g. "are candidates for COE integration")?

---

# Part VIII — Next Step

**Done**:
1. ✅ **GitHub site** (Part III): Terminology and one-section-per-product structure applied; final grep leaves only intentional LQL/LEF in repo links and paths.
2. ✅ **Site structure** (Part IIIb): One section per product; Product & Repo Index; no Core/SDK on site.

**Optional / when needed**:
3. Apply the **repo README** updates (Part VI) in each respective repo (AIOS, AIVA, LQL, LEF, TAI, ResonantFieldStorage, NotaMemoriaEngine, VoluntasEngine, caio, MAIA, vfe) as those repos are edited.
4. Confirm or adjust **Part VII open points** (repo names vs product names, NME wording, COE alignment phrasing) and update site copy if desired.
5. **GitHub Pages**: When ready, enable Pages on this repo; root README = homepage, product paths above = product pages (optionally add Jekyll theme or static generator later).
