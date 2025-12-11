# Use Case 3: Code Intelligence — Execution Plan

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10  
**Source of Truth:** This document

## Overview

This execution plan outlines the MVP implementation for Code Intelligence. The MVP demonstrates RFS capabilities: semantic code search, analogy discovery, contradiction detection, and pattern recognition.

## MVP Phases

### Phase 1: Code Extraction & Infrastructure (Week 1)

**Goal:** Set up code extraction and RFS infrastructure

**Tasks:**
- [ ] Create code extraction tool (functions, classes)
- [ ] Define code snippet schema (JSON format)
- [ ] Create code ingestion script
- [ ] Set up RFS field configuration
- [ ] Test field-native encoder with code

**Deliverables:**
- Code extraction tool (`src/use_cases/03_code_intelligence/extractor.py`)
- Sample code dataset (`artifacts/use_cases/03_code_intelligence/code_snippets.jsonl`)
- Ingestion script (`scripts/use_cases/03_code_intelligence/ingest_code.py`)
- Field configuration (`configs/use_cases/03_code_intelligence/field_config.json`)

**Success Criteria:**
- 100+ code snippets extracted successfully
- Field created with all code superposed
- No errors in extraction/ingestion pipeline

---

### Phase 2: Code Search Implementation (Week 2)

**Goal:** Implement semantic code search with RFS

**Tasks:**
- [ ] Implement query encoding (text → vector → field)
- [ ] Implement resonance search (query field vs code field)
- [ ] Implement result ranking (by resonance score)
- [ ] Add code snippet retrieval
- [ ] Create search API endpoint

**Deliverables:**
- Search implementation (`src/use_cases/03_code_intelligence/search.py`)
- Search API (`src/use_cases/03_code_intelligence/api.py`)
- Basic tests (`tests/use_cases/03_code_intelligence/test_search.py`)

**Success Criteria:**
- Code found by meaning (not just keywords)
- Results ranked by resonance
- Query latency P95 ≤ 50ms

---

### Phase 3: Analogy & Contradiction Detection (Week 3)

**Goal:** Add analogy discovery and contradiction detection

**Tasks:**
- [ ] Implement analogy detection (constructive interference)
- [ ] Implement contradiction detection (destructive interference)
- [ ] Generate explanations for results
- [ ] Add analogy grouping
- [ ] Add contradiction alerts

**Deliverables:**
- Analogy detection (`src/use_cases/03_code_intelligence/analogies.py`)
- Contradiction detection (`src/use_cases/03_code_intelligence/contradictions.py`)
- Updated API with analogies/contradictions

**Success Criteria:**
- Analogies discovered automatically
- Contradictions detected
- Explanations generated

---

### Phase 4: Demo & Visualization (Week 4)

**Goal:** Create demo-ready MVP with visualization

**Tasks:**
- [ ] Create demo script with sample queries
- [ ] Build result visualization (code snippets + explanations)
- [ ] Add analogy visualization
- [ ] Add contradiction visualization
- [ ] Create demo documentation

**Deliverables:**
- Demo script (`scripts/use_cases/03_code_intelligence/demo.py`)
- Visualization tool (`scripts/use_cases/03_code_intelligence/visualize.py`)
- Demo documentation (`docs/use_cases/03_code_intelligence/DEMO.md`)

**Success Criteria:**
- Demo runs end-to-end
- Visualization shows results clearly
- Demo is presentable

---

## Implementation Details

### Code Snippet Schema

**Code JSON Format:**
```json
{
  "code_id": "CODE-001",
  "file_path": "src/auth/middleware.py",
  "snippet": "def authenticate(request):\n    ...",
  "language": "python",
  "type": "function",
  "start_line": 42,
  "end_line": 67,
  "metadata": {
    "author": "alice",
    "commit": "abc123",
    "date": "2025-12-01"
  }
}
```

### Field Configuration

```python
FieldRetrieverConfig(
    field_shape=(32, 32, 32, 4),
    n_symbols=1024,
    n_channels=4,
    seed=42,
    use_metal=True,
    shortlist_size=32,
    refine_top=200,
)
```

### API Endpoints

**Code Search Endpoint:**
```
GET /api/v1/code/search?q={query}&top_k={k}
Response: {
  "results": [
    {
      "code_id": "CODE-001",
      "file_path": "src/auth/middleware.py",
      "score": 0.94,
      "q_dB": 23.1,
      "is_analogy": false,
      "is_contradiction": false,
      "explanation": {
        "reason": "Direct match on 'authentication middleware'",
        "constructive": 0.91,
        "destructive": 0.05
      }
    },
    ...
  ],
  "analogies": [
    {
      "pattern": "Authentication/Authorization",
      "codes": ["CODE-001", "CODE-042", ...]
    }
  ],
  "contradictions": [
    {
      "code1": "CODE-001",
      "code2": "CODE-156",
      "reason": "One requires auth, other disables it"
    }
  ]
}
```

### Code Structure

```
src/use_cases/03_code_intelligence/
├── __init__.py
├── extractor.py        # Code extraction
├── ingest.py          # Code ingestion
├── search.py          # Code search
├── analogies.py       # Analogy detection
├── contradictions.py  # Contradiction detection
└── api.py            # REST API endpoints

scripts/use_cases/03_code_intelligence/
├── extract_code.py    # Extract code from repo
├── ingest_code.py     # Ingest code into RFS
├── demo.py           # Demo script
└── visualize.py      # Visualization tool

tests/use_cases/03_code_intelligence/
├── test_extractor.py
├── test_search.py
└── test_analogies.py

artifacts/use_cases/03_code_intelligence/
├── code_snippets.jsonl
└── field_data/
```

## Testing Strategy

### Unit Tests

- **Extraction Tests**: Verify code extraction
- **Search Tests**: Verify code search by meaning
- **Analogy Tests**: Verify analogy detection
- **Contradiction Tests**: Verify contradiction detection

### Integration Tests

- **End-to-End Tests**: Full pipeline from extraction to search
- **API Tests**: REST API endpoint testing
- **Performance Tests**: Latency and throughput validation

### Validation Tests

- **Quality Tests**: Verify code found is relevant
- **Analogy Tests**: Verify analogies are correct
- **Contradiction Tests**: Verify contradictions are detected

## Demo Milestones

### Milestone 1: Code Search (End of Week 2)
- ✅ Code found by meaning
- ✅ Results ranked by resonance
- ✅ Query latency meets target

### Milestone 2: Analogies & Contradictions (End of Week 3)
- ✅ Analogies discovered
- ✅ Contradictions detected
- ✅ Explanations generated

### Milestone 3: Demo Ready (End of Week 4)
- ✅ Full demo script works
- ✅ Visualization functional
- ✅ Demo is presentable

## Dependencies

### RFS Core Features
- ✅ FieldNativeEncoder (available)
- ✅ FieldRetriever (available)
- ✅ Interference analysis (available)

### External Dependencies
- Code parsing library (tree-sitter, etc.)
- Sample codebase (to be created)
- Visualization library (optional)

## Risks & Mitigations

### Risk 1: Code Extraction Complexity
- **Risk**: Code extraction is complex (multi-language)
- **Mitigation**: Start with single language, use existing parsers

### Risk 2: Code Encoding Quality
- **Risk**: Code doesn't encode well (syntax vs semantics)
- **Mitigation**: Test encoding quality, iterate on approach

### Risk 3: Analogy Detection Accuracy
- **Risk**: Analogies not accurate
- **Mitigation**: Tune interference thresholds, validate with users

## Timeline

| Phase | Duration | Start | End | Status |
|-------|----------|-------|-----|--------|
| Phase 1: Extraction | 1 week | TBD | TBD | ⏳ Planned |
| Phase 2: Search | 1 week | TBD | TBD | ⏳ Planned |
| Phase 3: Analogies | 1 week | TBD | TBD | ⏳ Planned |
| Phase 4: Demo | 1 week | TBD | TBD | ⏳ Planned |
| **Total MVP** | **4 weeks** | | | **⏳ Planned** |

## Success Metrics

### Technical Metrics
- Query latency P95 ≤ 50ms ✅
- Resonance quality Q_dB ≥ 20 ✅
- Analogy detection accuracy ≥ 80% ✅
- Contradiction detection accuracy ≥ 80% ✅

### Business Metrics
- Demo completion: 100% ✅
- Stakeholder approval: Positive feedback ✅
- MVP readiness: Demo-ready ✅

## Next Steps

1. **Approve Plan**: Review and approve execution plan
2. **Allocate Resources**: Assign engineers to MVP
3. **Start Phase 1**: Begin code extraction
4. **Weekly Reviews**: Track progress against milestones
5. **Demo Prep**: Prepare demo for stakeholders

## Related Documentation

- **README:** `README.md` (problem, solution, demo)
- **North Star:** `NORTH_STAR.md` (vision, success criteria)
- **RFS Execution Plan:** `../../operations/execution_plan.md`
- **RFS North Star:** `../../RFS_NORTH_STAR_V4.md`
