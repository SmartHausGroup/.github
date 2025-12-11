# Use Case 4: Compliance/Legal Archive — Execution Plan

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10  
**Source of Truth:** This document

## Overview

This execution plan outlines the MVP implementation for Compliance/Legal Archive. The MVP demonstrates RFS capabilities: relationship discovery, explainable document selection, exact byte recall (AEAD-verified), and complete audit trails.

## MVP Phases

### Phase 1: Document Ingestion & Dual-Path Setup (Week 1)

**Goal:** Set up dual-path ingestion (semantic + byte)

**Tasks:**
- [ ] Create legal document dataset (100-500 documents)
- [ ] Define document schema (JSON format)
- [ ] Implement semantic path ingestion (document → field)
- [ ] Implement byte path ingestion (document → byte channel)
- [ ] Set up RFS field configuration
- [ ] Test dual-path ingestion

**Deliverables:**
- Sample document dataset (`artifacts/use_cases/04_compliance_legal_archive/documents.jsonl`)
- Ingestion script (`scripts/use_cases/04_compliance_legal_archive/ingest_documents.py`)
- Field configuration (`configs/use_cases/04_compliance_legal_archive/field_config.json`)

**Success Criteria:**
- 100+ documents ingested (semantic + byte paths)
- Field created with all documents superposed
- Byte channel stores exact bytes (AEAD-encrypted)
- No errors in ingestion pipeline

---

### Phase 2: Document Search & Relationship Discovery (Week 2)

**Goal:** Implement document search with relationship discovery

**Tasks:**
- [ ] Implement query encoding (text → vector → field)
- [ ] Implement resonance search (query field vs semantic field)
- [ ] Implement result ranking (by resonance score)
- [ ] Implement relationship detection (interference patterns)
- [ ] Generate relationship explanations
- [ ] Create search API endpoint

**Deliverables:**
- Search implementation (`src/use_cases/04_compliance_legal_archive/search.py`)
- Relationship analysis (`src/use_cases/04_compliance_legal_archive/relationships.py`)
- Search API (`src/use_cases/04_compliance_legal_archive/api.py`)

**Success Criteria:**
- Documents found by meaning (not just keywords)
- Relationships discovered automatically
- Explanations generated
- Query latency P95 ≤ 50ms

---

### Phase 3: Exact Recall & Audit Trail (Week 3)

**Goal:** Implement exact recall and audit trail

**Tasks:**
- [ ] Implement exact recall (byte channel lookup)
- [ ] Implement AEAD verification
- [ ] Implement audit trail logging
- [ ] Add audit trail export
- [ ] Test exact recall integrity

**Deliverables:**
- Exact recall (`src/use_cases/04_compliance_legal_archive/recall.py`)
- Audit trail (`src/use_cases/04_compliance_legal_archive/audit.py`)
- Updated API with exact recall

**Success Criteria:**
- Exact recall works (100% success rate)
- AEAD verification works (100% integrity)
- Audit trail complete
- Exact recall latency P95 ≤ 200ms

---

### Phase 4: Demo & Compliance Reporting (Week 4)

**Goal:** Create demo-ready MVP with compliance features

**Tasks:**
- [ ] Create demo script with sample queries
- [ ] Build result visualization (documents + relationships + proofs)
- [ ] Add exact recall demonstration
- [ ] Add audit trail visualization
- [ ] Create compliance report format
- [ ] Create demo documentation

**Deliverables:**
- Demo script (`scripts/use_cases/04_compliance_legal_archive/demo.py`)
- Visualization tool (`scripts/use_cases/04_compliance_legal_archive/visualize.py`)
- Compliance report (`scripts/use_cases/04_compliance_legal_archive/report.py`)
- Demo documentation (`docs/use_cases/04_compliance_legal_archive/DEMO.md`)

**Success Criteria:**
- Demo runs end-to-end
- Exact recall demonstrated
- Audit trail shown
- Compliance report generated
- Demo is presentable

---

## Implementation Details

### Document Schema

**Document JSON Format:**
```json
{
  "doc_id": "DOC-001",
  "title": "Data Breach Incident Report",
  "content": "On 2025-12-01, unauthorized access detected...",
  "type": "incident_report",
  "date": "2025-12-01",
  "metadata": {
    "author": "Security Team",
    "classification": "confidential",
    "related_docs": ["DOC-042", "DOC-089"]
  }
}
```

### Dual-Path Configuration

**Semantic Path:**
```python
FieldRetrieverConfig(
    field_shape=(32, 32, 32, 4),
    n_symbols=1024,
    use_metal=True,
)
```

**Byte Path:**
```python
ResonantFieldStorage(
    field_shape=(64, 64, 64, 8),
    aead_material=load_aead_material(),
)
```

### API Endpoints

**Document Search Endpoint:**
```
GET /api/v1/legal/search?q={query}&top_k={k}
Response: {
  "results": [
    {
      "doc_id": "DOC-001",
      "score": 0.95,
      "q_dB": 24.2,
      "relationship": "direct_match",
      "proof": {
        "interference_pattern": {...},
        "reason": "Direct match on 'data breach incident'"
      }
    },
    ...
  ]
}
```

**Exact Recall Endpoint:**
```
GET /api/v1/legal/recall/{doc_id}
Response: {
  "doc_id": "DOC-001",
  "bytes": "...",
  "aead_verified": true,
  "integrity": "verified",
  "timestamp": "2025-12-10T10:30:00Z"
}
```

**Audit Trail Endpoint:**
```
GET /api/v1/legal/audit?query_id={id}
Response: {
  "query_id": "...",
  "query": "...",
  "timestamp": "...",
  "results": [...],
  "proofs": [...],
  "exact_recalls": [...]
}
```

### Code Structure

```
src/use_cases/04_compliance_legal_archive/
├── __init__.py
├── ingest.py          # Dual-path ingestion
├── search.py          # Document search
├── relationships.py   # Relationship discovery
├── recall.py         # Exact recall
├── audit.py          # Audit trail
└── api.py           # REST API endpoints

scripts/use_cases/04_compliance_legal_archive/
├── prepare_documents.py  # Generate sample documents
├── ingest_documents.py   # Ingest documents
├── demo.py              # Demo script
├── visualize.py         # Visualization tool
└── report.py           # Compliance report

tests/use_cases/04_compliance_legal_archive/
├── test_ingest.py
├── test_search.py
├── test_recall.py
└── test_audit.py

artifacts/use_cases/04_compliance_legal_archive/
├── documents.jsonl
├── field_data/
└── audit_logs/
```

## Testing Strategy

### Unit Tests

- **Ingest Tests**: Verify dual-path ingestion
- **Search Tests**: Verify document search
- **Recall Tests**: Verify exact recall (AEAD)
- **Audit Tests**: Verify audit trail

### Integration Tests

- **End-to-End Tests**: Full pipeline from ingest to recall
- **API Tests**: REST API endpoint testing
- **Integrity Tests**: AEAD verification testing

### Compliance Tests

- **Audit Trail Tests**: Verify complete audit trail
- **Proof Tests**: Verify proofs are correct
- **Recall Tests**: Verify exact recall integrity

## Demo Milestones

### Milestone 1: Document Search (End of Week 2)
- ✅ Documents found by meaning
- ✅ Relationships discovered
- ✅ Explanations generated

### Milestone 2: Exact Recall (End of Week 3)
- ✅ Exact recall works
- ✅ AEAD verification works
- ✅ Audit trail complete

### Milestone 3: Demo Ready (End of Week 4)
- ✅ Full demo script works
- ✅ Exact recall demonstrated
- ✅ Audit trail shown
- ✅ Demo is presentable

## Dependencies

### RFS Core Features
- ✅ FieldNativeEncoder (available)
- ✅ FieldRetriever (available)
- ✅ ResonantFieldStorage (available)
- ✅ AEAD byte channel (available)

### External Dependencies
- Sample legal documents (to be created)
- AEAD key material (for byte channel)

## Risks & Mitigations

### Risk 1: Dual-Path Complexity
- **Risk**: Dual-path ingestion is complex
- **Mitigation**: Test each path separately, then integrate

### Risk 2: Exact Recall Performance
- **Risk**: Exact recall too slow
- **Mitigation**: Optimize byte channel lookup, use caching

### Risk 3: Audit Trail Completeness
- **Risk**: Audit trail missing information
- **Mitigation**: Comprehensive logging, test audit export

## Timeline

| Phase | Duration | Start | End | Status |
|-------|----------|-------|-----|--------|
| Phase 1: Dual-Path Setup | 1 week | TBD | TBD | ⏳ Planned |
| Phase 2: Search & Relationships | 1 week | TBD | TBD | ⏳ Planned |
| Phase 3: Exact Recall & Audit | 1 week | TBD | TBD | ⏳ Planned |
| Phase 4: Demo | 1 week | TBD | TBD | ⏳ Planned |
| **Total MVP** | **4 weeks** | | | **⏳ Planned** |

## Success Metrics

### Technical Metrics
- Query latency P95 ≤ 50ms ✅
- Exact recall latency P95 ≤ 200ms ✅
- Exact recall success: 100% ✅
- AEAD verification: 100% ✅
- Audit trail completeness: 100% ✅

### Business Metrics
- Demo completion: 100% ✅
- Stakeholder approval: Positive feedback ✅
- MVP readiness: Demo-ready ✅

## Next Steps

1. **Approve Plan**: Review and approve execution plan
2. **Allocate Resources**: Assign engineers to MVP
3. **Start Phase 1**: Begin dual-path setup
4. **Weekly Reviews**: Track progress against milestones
5. **Demo Prep**: Prepare demo for stakeholders

## Related Documentation

- **README:** `README.md` (problem, solution, demo)
- **North Star:** `NORTH_STAR.md` (vision, success criteria)
- **RFS Execution Plan:** `../../operations/execution_plan.md`
- **RFS North Star:** `../../RFS_NORTH_STAR_V4.md`
