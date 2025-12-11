# Use Case 5: Research Knowledge Graph — Execution Plan

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10  
**Source of Truth:** This document

## Overview

This execution plan outlines the MVP implementation for Research Knowledge Graph. The MVP demonstrates RFS capabilities: semantic paper search, temporal analysis, relationship discovery, and research community detection via entanglement graphs.

## MVP Phases

### Phase 1: Paper Ingestion & Temporal Setup (Week 1)

**Goal:** Set up paper ingestion with temporal dimension

**Tasks:**
- [ ] Create sample paper dataset (100-1000 papers)
- [ ] Define paper schema (JSON format with dates)
- [ ] Create paper ingestion script
- [ ] Set up RFS field configuration (with larger t dimension)
- [ ] Implement temporal dimension mapping
- [ ] Test field-native encoder with papers

**Deliverables:**
- Sample paper dataset (`artifacts/use_cases/05_research_knowledge_graph/papers.jsonl`)
- Ingestion script (`scripts/use_cases/05_research_knowledge_graph/ingest_papers.py`)
- Field configuration (`configs/use_cases/05_research_knowledge_graph/field_config.json`)

**Success Criteria:**
- 100+ papers ingested successfully
- Field created with temporal dimension
- Temporal metadata stored correctly
- No errors in ingestion pipeline

---

### Phase 2: Paper Search & Temporal Analysis (Week 2)

**Goal:** Implement paper search with temporal analysis

**Tasks:**
- [ ] Implement query encoding (text → vector → field)
- [ ] Implement resonance search (query field vs paper field)
- [ ] Implement result ranking (by resonance score)
- [ ] Implement temporal analysis (time slice mapping)
- [ ] Add temporal evolution tracking
- [ ] Create search API endpoint

**Deliverables:**
- Search implementation (`src/use_cases/05_research_knowledge_graph/search.py`)
- Temporal analysis (`src/use_cases/05_research_knowledge_graph/temporal.py`)
- Search API (`src/use_cases/05_research_knowledge_graph/api.py`)

**Success Criteria:**
- Papers found by meaning (not just keywords)
- Temporal evolution visible
- Query latency P95 ≤ 50ms

---

### Phase 3: Entanglement Graph & Communities (Week 3)

**Goal:** Build entanglement graph and detect communities

**Tasks:**
- [ ] Implement entanglement graph construction
- [ ] Implement community detection (Leiden algorithm)
- [ ] Add relationship visualization
- [ ] Generate community reports
- [ ] Add graph export (JSON/GraphML)

**Deliverables:**
- Entanglement graph (`src/use_cases/05_research_knowledge_graph/graph.py`)
- Community detection (`src/use_cases/05_research_knowledge_graph/communities.py`)
- Graph export (`src/use_cases/05_research_knowledge_graph/export.py`)

**Success Criteria:**
- Entanglement graph built successfully
- Communities detected correctly
- Graph export works

---

### Phase 4: Demo & Visualization (Week 4)

**Goal:** Create demo-ready MVP with visualization

**Tasks:**
- [ ] Create demo script with sample queries
- [ ] Build result visualization (papers + temporal + graph)
- [ ] Add temporal evolution visualization
- [ ] Add entanglement graph visualization
- [ ] Create demo documentation

**Deliverables:**
- Demo script (`scripts/use_cases/05_research_knowledge_graph/demo.py`)
- Visualization tool (`scripts/use_cases/05_research_knowledge_graph/visualize.py`)
- Demo documentation (`docs/use_cases/05_research_knowledge_graph/DEMO.md`)

**Success Criteria:**
- Demo runs end-to-end
- Visualization shows results clearly
- Temporal evolution visible
- Entanglement graph visible
- Demo is presentable

---

## Implementation Details

### Paper Schema

**Paper JSON Format:**
```json
{
  "paper_id": "PAPER-001",
  "title": "Quantum Entanglement in Many-Body Systems",
  "abstract": "We investigate quantum entanglement...",
  "authors": ["Alice", "Bob"],
  "publication_date": "2020-01-15",
  "venue": "Physical Review",
  "metadata": {
    "citations": 150,
    "keywords": ["quantum", "entanglement"]
  }
}
```

### Field Configuration

```python
FieldRetrieverConfig(
    field_shape=(32, 32, 32, 16),  # Larger t for temporal
    n_symbols=1024,
    n_channels=4,
    seed=42,
    use_metal=True,
    shortlist_size=32,
    refine_top=200,
)
```

### Temporal Mapping

```python
# Map publication date to temporal dimension (t)
def map_date_to_t_slice(date: str, field_shape: tuple) -> int:
    # Convert date to time slice index (0 to t_max-1)
    # Example: 2019 -> slice 6, 2020 -> slice 8, 2021 -> slice 10
    ...
```

### API Endpoints

**Paper Search Endpoint:**
```
GET /api/v1/research/search?q={query}&top_k={k}
Response: {
  "results": [
    {
      "paper_id": "PAPER-001",
      "title": "...",
      "score": 0.95,
      "q_dB": 24.1,
      "temporal": {
        "date": "2020-01-15",
        "t_slice": 8
      },
      "explanation": {
        "reason": "Direct match on 'quantum entanglement'",
        "constructive": 0.91
      }
    },
    ...
  ],
  "temporal_evolution": {
    "slices": [
      {"slice": 6, "count": 5, "papers": [...]},
      {"slice": 8, "count": 12, "papers": [...]},
      ...
    ]
  }
}
```

**Entanglement Graph Endpoint:**
```
GET /api/v1/research/graph
Response: {
  "nodes": [...],
  "edges": [...],
  "communities": [
    {
      "community_id": 0,
      "papers": ["PAPER-001", "PAPER-042", ...],
      "name": "Quantum Entanglement"
    },
    ...
  ]
}
```

### Code Structure

```
src/use_cases/05_research_knowledge_graph/
├── __init__.py
├── ingest.py          # Paper ingestion
├── search.py          # Paper search
├── temporal.py        # Temporal analysis
├── graph.py          # Entanglement graph
├── communities.py    # Community detection
└── api.py           # REST API endpoints

scripts/use_cases/05_research_knowledge_graph/
├── prepare_papers.py    # Generate sample papers
├── ingest_papers.py     # Ingest papers into RFS
├── demo.py             # Demo script
└── visualize.py        # Visualization tool

tests/use_cases/05_research_knowledge_graph/
├── test_ingest.py
├── test_search.py
├── test_temporal.py
└── test_graph.py

artifacts/use_cases/05_research_knowledge_graph/
├── papers.jsonl
├── field_data/
└── graphs/
```

## Testing Strategy

### Unit Tests

- **Ingest Tests**: Verify paper ingestion
- **Search Tests**: Verify paper search
- **Temporal Tests**: Verify temporal analysis
- **Graph Tests**: Verify entanglement graph
- **Community Tests**: Verify community detection

### Integration Tests

- **End-to-End Tests**: Full pipeline from ingest to graph
- **API Tests**: REST API endpoint testing
- **Performance Tests**: Latency and throughput validation

### Validation Tests

- **Quality Tests**: Verify papers found are relevant
- **Temporal Tests**: Verify temporal mapping is correct
- **Graph Tests**: Verify graph structure is correct

## Demo Milestones

### Milestone 1: Paper Search (End of Week 2)
- ✅ Papers found by meaning
- ✅ Temporal evolution visible
- ✅ Query latency meets target

### Milestone 2: Entanglement Graph (End of Week 3)
- ✅ Graph built successfully
- ✅ Communities detected
- ✅ Graph export works

### Milestone 3: Demo Ready (End of Week 4)
- ✅ Full demo script works
- ✅ Visualization functional
- ✅ Temporal + graph shown
- ✅ Demo is presentable

## Dependencies

### RFS Core Features
- ✅ FieldNativeEncoder (available)
- ✅ FieldRetriever (available)
- ✅ Entanglement graph (available)
- ⏳ Temporal dimension (needs implementation)

### External Dependencies
- Sample paper dataset (to be created)
- Graph visualization library (networkx, igraph)
- Temporal visualization library (optional)

## Risks & Mitigations

### Risk 1: Temporal Dimension Implementation
- **Risk**: Temporal dimension not fully implemented
- **Mitigation**: Use existing t dimension, map dates to slices

### Risk 2: Graph Construction Performance
- **Risk**: Graph construction too slow
- **Mitigation**: Optimize graph construction, use sampling for large datasets

### Risk 3: Community Detection Accuracy
- **Risk**: Communities not accurate
- **Mitigation**: Tune community detection parameters, validate with domain experts

## Timeline

| Phase | Duration | Start | End | Status |
|-------|----------|-------|-----|--------|
| Phase 1: Ingestion | 1 week | TBD | TBD | ⏳ Planned |
| Phase 2: Search & Temporal | 1 week | TBD | TBD | ⏳ Planned |
| Phase 3: Graph & Communities | 1 week | TBD | TBD | ⏳ Planned |
| Phase 4: Demo | 1 week | TBD | TBD | ⏳ Planned |
| **Total MVP** | **4 weeks** | | | **⏳ Planned** |

## Success Metrics

### Technical Metrics
- Query latency P95 ≤ 50ms ✅
- Resonance quality Q_dB ≥ 20 ✅
- Graph construction ≤ 5 minutes for 10K papers ✅
- Temporal analysis ≤ 1 second per query ✅

### Business Metrics
- Demo completion: 100% ✅
- Stakeholder approval: Positive feedback ✅
- MVP readiness: Demo-ready ✅

## Next Steps

1. **Approve Plan**: Review and approve execution plan
2. **Allocate Resources**: Assign engineers to MVP
3. **Start Phase 1**: Begin paper ingestion
4. **Weekly Reviews**: Track progress against milestones
5. **Demo Prep**: Prepare demo for stakeholders

## Related Documentation

- **README:** `README.md` (problem, solution, demo)
- **North Star:** `NORTH_STAR.md` (vision, success criteria)
- **RFS Execution Plan:** `../../operations/execution_plan.md`
- **RFS North Star:** `../../RFS_NORTH_STAR_V4.md`
