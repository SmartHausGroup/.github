# Use Case 2: RAG with Proofs — Execution Plan

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10  
**Source of Truth:** This document

## Overview

This execution plan outlines the MVP implementation for RAG with Proofs. The MVP demonstrates RFS capabilities: resonance-based document selection, interference pattern explanations, contradiction detection, and provable document selection for LLM context.

## MVP Phases

### Phase 1: Knowledge Base & RFS Setup (Week 1)

**Goal:** Set up knowledge base and RFS infrastructure

**Tasks:**
- [ ] Create sample knowledge base (100-1000 documents)
- [ ] Define document schema (JSON format)
- [ ] Create document ingestion script
- [ ] Set up RFS field configuration
- [ ] Test field-native encoder with documents

**Deliverables:**
- Sample knowledge base (`artifacts/use_cases/02_rag_with_proofs/knowledge_base.jsonl`)
- Ingestion script (`scripts/use_cases/02_rag_with_proofs/ingest_documents.py`)
- Field configuration (`configs/use_cases/02_rag_with_proofs/field_config.json`)

**Success Criteria:**
- 100+ documents ingested successfully
- Field created with all documents superposed
- No errors in ingestion pipeline

---

### Phase 2: Document Selection with RFS (Week 2)

**Goal:** Implement RFS-based document selection

**Tasks:**
- [ ] Implement query encoding (text → vector → field)
- [ ] Implement resonance search (query field vs superposed field)
- [ ] Implement result ranking (by resonance score)
- [ ] Add Q_dB computation (resonance quality)
- [ ] Create document selection API

**Deliverables:**
- Document selection (`src/use_cases/02_rag_with_proofs/selection.py`)
- Search API (`src/use_cases/02_rag_with_proofs/api.py`)
- Basic tests (`tests/use_cases/02_rag_with_proofs/test_selection.py`)

**Success Criteria:**
- Documents selected by resonance (not just similarity)
- Results ranked by Q_dB (resonance quality)
- Query latency P95 ≤ 50ms

---

### Phase 3: Proof Generation (Week 3)

**Goal:** Generate explanations and proofs for document selection

**Tasks:**
- [ ] Implement interference pattern computation (Λ_ij)
- [ ] Detect constructive interference (why document matches)
- [ ] Detect destructive interference (contradictions)
- [ ] Generate human-readable explanations
- [ ] Format proofs (JSON/markdown)
- [ ] Add proofs to API response

**Deliverables:**
- Proof generation (`src/use_cases/02_rag_with_proofs/proofs.py`)
- Explanation formatter (`src/use_cases/02_rag_with_proofs/explanations.py`)
- Updated API with proofs

**Success Criteria:**
- Explanations generated for all selected documents
- Constructive/destructive interference detected
- Proofs are human-readable
- Proofs are machine-readable (JSON)

---

### Phase 4: LLM Integration & Demo (Week 4)

**Goal:** Integrate with LLM and create demo

**Tasks:**
- [ ] Integrate with LLM API (OpenAI/Anthropic)
- [ ] Build context with documents + proofs
- [ ] Generate answers with citations
- [ ] Format response (answer + citations + proofs)
- [ ] Create demo script
- [ ] Create demo documentation

**Deliverables:**
- LLM integration (`src/use_cases/02_rag_with_proofs/llm_integration.py`)
- Demo script (`scripts/use_cases/02_rag_with_proofs/demo.py`)
- Demo documentation (`docs/use_cases/02_rag_with_proofs/DEMO.md`)

**Success Criteria:**
- LLM generates answers with citations
- Citations include proofs
- Demo runs end-to-end
- Demo is presentable to stakeholders

---

## Implementation Details

### Document Schema

**Document JSON Format:**
```json
{
  "doc_id": "DOC-001",
  "title": "Security Best Practices",
  "content": "Use strong passwords, enable 2FA, keep software updated...",
  "category": "security",
  "metadata": {
    "author": "Security Team",
    "last_updated": "2025-12-01",
    "source": "internal-wiki"
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

**RAG Query Endpoint:**
```
POST /api/v1/rag/query
Body: {
  "query": "What are security best practices?",
  "top_k": 5,
  "llm_provider": "openai",
  "include_proofs": true
}
Response: {
  "answer": "Security best practices include...",
  "citations": [
    {
      "doc_id": "DOC-001",
      "score": 0.94,
      "q_dB": 23.5,
      "proof": {
        "constructive": 0.91,
        "destructive": 0.05,
        "reason": "Direct match on 'security best practices'"
      },
      "interference_pattern": {...}
    },
    ...
  ]
}
```

### Code Structure

```
src/use_cases/02_rag_with_proofs/
├── __init__.py
├── ingest.py          # Document ingestion
├── selection.py       # Document selection
├── proofs.py          # Proof generation
├── explanations.py    # Explanation formatting
├── llm_integration.py # LLM integration
└── api.py            # REST API endpoints

scripts/use_cases/02_rag_with_proofs/
├── prepare_kb.py         # Generate sample knowledge base
├── ingest_documents.py   # Ingest documents into RFS
└── demo.py               # Demo script

tests/use_cases/02_rag_with_proofs/
├── test_ingest.py
├── test_selection.py
├── test_proofs.py
└── test_llm_integration.py

artifacts/use_cases/02_rag_with_proofs/
├── knowledge_base.jsonl
└── field_data/
```

## Testing Strategy

### Unit Tests

- **Ingest Tests**: Verify document ingestion
- **Selection Tests**: Verify document selection by resonance
- **Proof Tests**: Verify proof generation
- **Explanation Tests**: Verify explanation formatting
- **LLM Integration Tests**: Verify LLM integration

### Integration Tests

- **End-to-End Tests**: Full pipeline from ingest to answer
- **API Tests**: REST API endpoint testing
- **Performance Tests**: Latency and throughput validation

### Validation Tests

- **Quality Tests**: Answer accuracy validation
- **Proof Tests**: Verify proofs are correct
- **Contradiction Tests**: Verify contradiction detection

## Demo Milestones

### Milestone 1: Document Selection (End of Week 2)
- ✅ Documents selected by resonance
- ✅ Results ranked by Q_dB
- ✅ Query latency meets target

### Milestone 2: Proofs Generated (End of Week 3)
- ✅ Explanations generated
- ✅ Interference patterns computed
- ✅ Contradictions detected

### Milestone 3: Demo Ready (End of Week 4)
- ✅ LLM integration works
- ✅ Answers generated with citations
- ✅ Proofs included in response
- ✅ Demo script functional

## Dependencies

### RFS Core Features
- ✅ FieldNativeEncoder (available)
- ✅ FieldRetriever (available)
- ✅ Interference analysis (available)

### External Dependencies
- LLM API access (OpenAI/Anthropic)
- Sample knowledge base (to be created)
- LLM client library (openai, anthropic)

## Risks & Mitigations

### Risk 1: LLM Integration Complexity
- **Risk**: LLM integration adds complexity
- **Mitigation**: Use simple API wrapper, test with multiple providers

### Risk 2: Proof Quality
- **Risk**: Proofs not human-readable
- **Mitigation**: Iterate on explanation format, test with users

### Risk 3: Answer Quality
- **Risk**: Answers not better than baseline RAG
- **Mitigation**: Tune document selection, test with multiple queries

## Timeline

| Phase | Duration | Start | End | Status |
|-------|----------|-------|-----|--------|
| Phase 1: KB Setup | 1 week | TBD | TBD | ⏳ Planned |
| Phase 2: Selection | 1 week | TBD | TBD | ⏳ Planned |
| Phase 3: Proofs | 1 week | TBD | TBD | ⏳ Planned |
| Phase 4: LLM & Demo | 1 week | TBD | TBD | ⏳ Planned |
| **Total MVP** | **4 weeks** | | | **⏳ Planned** |

## Success Metrics

### Technical Metrics
- Query latency P95 ≤ 50ms ✅
- Resonance quality Q_dB ≥ 20 ✅
- Proof generation < 10ms per document ✅
- Answer accuracy ≥ baseline RAG ✅

### Business Metrics
- Demo completion: 100% ✅
- Stakeholder approval: Positive feedback ✅
- MVP readiness: Demo-ready ✅

## Next Steps

1. **Approve Plan**: Review and approve execution plan
2. **Allocate Resources**: Assign engineers to MVP
3. **Start Phase 1**: Begin knowledge base preparation
4. **Weekly Reviews**: Track progress against milestones
5. **Demo Prep**: Prepare demo for stakeholders

## Related Documentation

- **README:** `README.md` (problem, solution, demo walkthrough)
- **North Star:** `NORTH_STAR.md` (vision, success criteria)
- **RFS Execution Plan:** `../../operations/execution_plan.md`
- **RFS North Star:** `../../RFS_NORTH_STAR_V4.md`
