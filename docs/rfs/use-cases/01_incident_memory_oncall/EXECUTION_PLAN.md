# Use Case 1: Incident Memory for On-Call Teams — Execution Plan

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10  
**Source of Truth:** This document

## Overview

This execution plan outlines the MVP implementation for Incident Memory for On-Call Teams. The MVP demonstrates RFS capabilities: superposition, resonance search, interference patterns, and explainability.

## MVP Phases

### Phase 1: Data Preparation & Infrastructure (Week 1)

**Goal:** Set up data pipeline and RFS infrastructure

**Tasks:**
- [ ] Create sample incident dataset (100-500 incidents)
- [ ] Define incident data schema (JSON format)
- [ ] Create data ingestion script
- [ ] Set up RFS field configuration
- [ ] Test field-native encoder with incident data

**Deliverables:**
- Sample incident dataset (`artifacts/use_cases/01_incident_memory/sample_incidents.jsonl`)
- Data ingestion script (`scripts/use_cases/01_incident_memory/ingest_incidents.py`)
- Field configuration (`configs/use_cases/01_incident_memory/field_config.json`)

**Success Criteria:**
- 100+ incidents ingested successfully
- Field created with all incidents superposed
- No errors in ingestion pipeline

---

### Phase 2: Basic Search Implementation (Week 2)

**Goal:** Implement basic incident search with RFS

**Tasks:**
- [ ] Implement query encoding (text → vector → field)
- [ ] Implement resonance search (query field vs superposed field)
- [ ] Implement result ranking (by resonance score)
- [ ] Add basic result formatting
- [ ] Create query API endpoint

**Deliverables:**
- Search implementation (`src/use_cases/01_incident_memory/search.py`)
- Query API (`src/use_cases/01_incident_memory/api.py`)
- Basic tests (`tests/use_cases/01_incident_memory/test_search.py`)

**Success Criteria:**
- Query returns ranked incident results
- Results are relevant (not just keyword matches)
- Query latency P95 ≤ 50ms

---

### Phase 3: Interference Pattern Analysis (Week 3)

**Goal:** Add explainability via interference patterns

**Tasks:**
- [ ] Implement interference pattern computation (Λ_ij)
- [ ] Detect constructive interference (relationships)
- [ ] Detect destructive interference (contradictions)
- [ ] Generate explanations for results
- [ ] Add explanation to API response

**Deliverables:**
- Interference analysis (`src/use_cases/01_incident_memory/interference.py`)
- Explanation generator (`src/use_cases/01_incident_memory/explanations.py`)
- Updated API with explanations

**Success Criteria:**
- Explanations generated for all results
- Constructive/destructive interference detected
- Explanations are human-readable

---

### Phase 4: Demo & Visualization (Week 4)

**Goal:** Create demo-ready MVP with visualization

**Tasks:**
- [ ] Create demo script with sample queries
- [ ] Build result visualization (CLI or web)
- [ ] Add relationship graph visualization (basic)
- [ ] Create demo walkthrough documentation
- [ ] Record demo video

**Deliverables:**
- Demo script (`scripts/use_cases/01_incident_memory/demo.py`)
- Visualization tool (`scripts/use_cases/01_incident_memory/visualize.py`)
- Demo documentation (`docs/use_cases/01_incident_memory/DEMO.md`)
- Demo video (optional)

**Success Criteria:**
- Demo runs end-to-end without errors
- Visualization shows results clearly
- Demo is presentable to stakeholders

---

## Implementation Details

### Data Schema

**Incident JSON Format:**
```json
{
  "incident_id": "INC-001",
  "title": "Database connection timeout",
  "description": "Users reporting slow queries. Database connection pool exhausted.",
  "timestamp": "2025-12-10T10:30:00Z",
  "severity": "high",
  "status": "resolved",
  "metadata": {
    "service": "api-service",
    "environment": "production",
    "team": "backend"
  }
}
```

### Field Configuration

```python
FieldRetrieverConfig(
    field_shape=(32, 32, 32, 4),  # Smaller for MVP
    n_symbols=1024,
    n_channels=4,
    seed=42,
    use_metal=True,  # Use Metal acceleration
    shortlist_size=32,
    refine_top=200,
)
```

### API Endpoints

**Search Endpoint:**
```
GET /api/v1/incidents/search?q={query}&top_k={k}
Response: {
  "results": [
    {
      "incident_id": "INC-001",
      "score": 0.95,
      "q_dB": 24.3,
      "explanation": {
        "constructive": 0.89,
        "destructive": 0.05,
        "reason": "Direct match on 'database timeout'"
      }
    },
    ...
  ]
}
```

**Explain Endpoint:**
```
GET /api/v1/incidents/{id}/explain?query={query}
Response: {
  "incident_id": "INC-001",
  "interference_pattern": {...},
  "relationships": [...],
  "contradictions": [...]
}
```

### Code Structure

```
src/use_cases/01_incident_memory/
├── __init__.py
├── ingest.py          # Incident ingestion
├── search.py          # Search implementation
├── interference.py    # Interference analysis
├── explanations.py    # Explanation generation
└── api.py            # REST API endpoints

scripts/use_cases/01_incident_memory/
├── prepare_sample_data.py  # Generate sample incidents
├── ingest_incidents.py     # Ingest incidents into RFS
├── demo.py                 # Demo script
└── visualize.py            # Visualization tool

tests/use_cases/01_incident_memory/
├── test_ingest.py
├── test_search.py
└── test_interference.py

artifacts/use_cases/01_incident_memory/
├── sample_incidents.jsonl
└── field_data/
```

## Testing Strategy

### Unit Tests

- **Ingest Tests**: Verify incident ingestion works correctly
- **Search Tests**: Verify search returns relevant results
- **Interference Tests**: Verify interference pattern computation
- **Explanation Tests**: Verify explanations are generated correctly

### Integration Tests

- **End-to-End Tests**: Full pipeline from ingest to search
- **API Tests**: REST API endpoint testing
- **Performance Tests**: Latency and throughput validation

### Validation Tests

- **Quality Tests**: Recall@10, nDCG@10 validation
- **Resonance Tests**: Q_dB validation (≥20)
- **Relationship Tests**: Verify relationships are discovered

## Demo Milestones

### Milestone 1: Basic Search (End of Week 2)
- ✅ Ingest 100+ incidents
- ✅ Query returns results
- ✅ Results are ranked

### Milestone 2: Explainable Search (End of Week 3)
- ✅ Explanations generated
- ✅ Interference patterns computed
- ✅ Constructive/destructive detected

### Milestone 3: Demo Ready (End of Week 4)
- ✅ Full demo script works
- ✅ Visualization functional
- ✅ Documentation complete

## Dependencies

### RFS Core Features
- ✅ FieldNativeEncoder (available)
- ✅ FieldRetriever (available)
- ✅ Interference analysis (available)
- ⏳ Entanglement graph (Phase 2)

### External Dependencies
- Sample incident dataset (to be created)
- Visualization library (matplotlib/plotly)
- API framework (FastAPI or Flask)

## Risks & Mitigations

### Risk 1: Sample Data Quality
- **Risk**: Sample incidents don't show relationships well
- **Mitigation**: Curate high-quality sample dataset with known relationships

### Risk 2: Performance
- **Risk**: Query latency too high for demo
- **Mitigation**: Use smaller field shape, optimize query path, use Metal acceleration

### Risk 3: Explanation Quality
- **Risk**: Explanations not human-readable
- **Mitigation**: Iterate on explanation format, add examples, test with users

## Timeline

| Phase | Duration | Start | End | Status |
|-------|----------|-------|-----|--------|
| Phase 1: Data Prep | 1 week | TBD | TBD | ⏳ Planned |
| Phase 2: Basic Search | 1 week | TBD | TBD | ⏳ Planned |
| Phase 3: Interference | 1 week | TBD | TBD | ⏳ Planned |
| Phase 4: Demo | 1 week | TBD | TBD | ⏳ Planned |
| **Total MVP** | **4 weeks** | | | **⏳ Planned** |

## Success Metrics

### Technical Metrics
- Query latency P95 ≤ 50ms ✅
- Resonance quality Q_dB ≥ 20 ✅
- Recall@10 ≥ 0.80 ✅
- Ingest throughput ≥ 100 incidents/sec ✅

### Business Metrics
- Demo completion: 100% ✅
- Stakeholder approval: Positive feedback ✅
- MVP readiness: Demo-ready ✅

## Next Steps

1. **Approve Plan**: Review and approve execution plan
2. **Allocate Resources**: Assign engineers to MVP
3. **Start Phase 1**: Begin data preparation
4. **Weekly Reviews**: Track progress against milestones
5. **Demo Prep**: Prepare demo for stakeholders

## Related Documentation

- **README:** `README.md` (problem, solution, demo walkthrough)
- **North Star:** `NORTH_STAR.md` (vision, success criteria)
- **RFS Execution Plan:** `../../operations/execution_plan.md`
- **RFS North Star:** `../../RFS_NORTH_STAR_V4.md`
