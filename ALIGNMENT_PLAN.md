# Alignment Plan: smarthaus.ai ↔ SmartHausGroup.github

**Purpose:** Single narrative across the public website (smarthaus.ai) and the GitHub org (.github repo). One source of truth for technical content; clear linking between site and repos.

**Status:** In progress  
**Last updated:** 2025-02-02

---

## 1. Goals

- **Single source of truth:** SmartHausGroup.github is the canonical source for technical narrative (RFS, MA, MGE, TAI, AIVA, archetypes). The website is the front door and surfaces or links to that content.
- **Consistent terminology:** AQL (not LQL), AEF (not LEF) everywhere. MGE described as the rules engine for MA.
- **Clear linking:** smarthaus.ai links to GitHub org/.github; .github READMEs link to smarthaus.ai.
- **Use-cases and content:** RFS use-cases and platform/archetype blurbs align between .github and website (website pulls from .github where applicable).

---

## 2. Phases

### Phase 1 – Terminology and linking (DONE in this pass)

| Task | Repo | Action |
|------|------|--------|
| Terminology | SmartHausWebsite | Replace LQL→AQL, LEF→AEF in `content/` (research, docs/lattice, docs/smarthaus). Use "AIVA Query Language" / "AIVA Execution Fabric" where full names are used. |
| North Star | SmartHausWebsite | Fix "ALQ"→"AQL" in WEBSITE_NORTH_STAR.md. Add MGE to Systems Visibility as "MGE (rules engine for MA)". |
| Website → GitHub | SmartHausWebsite | Add "GitHub" or "Code" link in header/footer → https://github.com/SmartHausGroup/.github |
| GitHub → Website | SmartHausGroup.github | Add "Website: https://www.smarthaus.ai" in main README and profile README (Organization / Links section). |

### Phase 2 – RFS use-cases and github.ts

| Task | Repo | Action |
|------|------|--------|
| Use-cases | SmartHausWebsite | Remove or fix `ENTERPRISE_KNOWLEDGE` (07) in `app/lib/content/github.ts`—.github has 01–06 only. Add pharmaceutical (06) to paths and fetch if research use-case page should pull from .github. |
| fetchAllUseCases | SmartHausWebsite | Align with .github: only 01–06, or add 07 to .github if enterprise-knowledge is canonical. |

### Phase 3 – Single source and copy

| Task | Repo | Action |
|------|------|--------|
| MGE / MA copy | SmartHausWebsite | Ensure platforms/mge and mathematical-autopsy pages state "MGE is the rules engine for MA" (align with .github). |
| Pull from .github | SmartHausWebsite | Where useful, have platform/archetype or MA intro pages pull blurbs from .github (e.g. fetch README sections) so narrative stays in sync. |

### Phase 4 – Optional: doc site from .github

| Task | Repo | Action |
|------|------|--------|
| Doc site | SmartHausGroup.github | If doc set grows, add a static doc site (e.g. Docusaurus) built from .github, host on GitHub Pages or docs.smarthaus.ai, link from smarthaus.ai. |

---

## 3. Terminology reference

| Old (website legacy) | New (canonical) |
|----------------------|-----------------|
| LQL | AQL (AIVA Query Language) |
| LEF | AEF (AIVA Execution Fabric) |
| ALQ (typo in North Star) | AQL |

---

## 4. Repo roles

- **SmartHausGroup.github:** Org face, archetypes (TAI, AIVA, MGE), RFS, MA. Canonical technical content. READMEs and markdown are the source for "doc from GitHub" or future doc site.
- **SmartHausWebsite:** Next.js site at smarthaus.ai. Front door (company, vision, recruiting). Pulls RFS use-cases and can pull more from .github. Uses consistent AQL/AEF and MGE-as-rules-engine framing.

---

## 5. Completion checklist

- [x] Phase 1: Terminology (LQL/LEF→AQL/AEF) in website content
- [x] Phase 1: North Star ALQ→AQL, MGE added
- [x] Phase 1: Website links to GitHub; .github links to smarthaus.ai
- [x] Phase 2: github.ts use-cases aligned with .github (01–06; 07 removed); enterprise-knowledge page uses local content
- [x] Phase 3: MGE/MA copy on website (MGE as rules engine for MA)
