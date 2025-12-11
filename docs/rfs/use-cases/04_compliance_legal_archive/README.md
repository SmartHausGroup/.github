# Use Case 4: Compliance/Legal Archive

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10

## Problem Statement

### Current Pain Points

Legal and compliance teams face critical challenges:

1. **Slow Document Discovery**: Finding related documents takes too long
   - Keyword search misses semantic relationships
   - Manual document correlation is time-consuming
   - No automatic relationship discovery

2. **No Relationship Mapping**: Can't see how documents connect
   - Contracts, policies, incident reports aren't linked
   - Relationships between documents aren't visible
   - Hard to understand document connections

3. **No Explainability**: Can't prove why documents are related
   - Black-box search results
   - No way to explain relationships to regulators
   - Hard to build audit trails

4. **Exact Recall Required**: Need original bytes for evidence
   - Current systems only return IDs/vectors
   - Need exact document bytes for legal evidence
   - Must prove document integrity (AEAD)

### Business Impact

- **Slow Legal Research**: Lawyers spend too long finding documents
- **Compliance Risk**: Can't prove document relationships
- **Audit Failures**: No audit trail of document selection
- **Evidence Issues**: Can't retrieve exact document bytes

## RFS Solution Overview

### How RFS Solves This

**1. Relationship Discovery: Automatic Document Connection**
```
All legal documents → encode → superpose in field
    ↓
Interference patterns reveal relationships
    ↓
Documents automatically connected by meaning
    ↓
Entanglement graph shows document relationships
```

**2. Explainable Relationships: Prove Why Documents Connect**
```
Query: "data breach incident"
    ↓
Resonance finds related documents
    ↓
Shows interference patterns (why they're related)
    ↓
Mathematical proofs of relationships
```

**3. Exact Recall: Get Original Bytes (AEAD-Verified)**
```
Document ID → byte channel lookup
    ↓
Extract bytes from field
    ↓
AEAD decryption + verification
    ↓
Return exact original bytes (proven integrity)
```

**4. Audit Trail: Complete Provenance**
```
Every query logged with:
- Documents selected
- Interference patterns (proofs)
- Exact recall operations
- Timestamps and metadata
```

## MVP Scope

### Phase 1: Basic Document Search + Exact Recall (MVP Demo)

**Features:**
- Ingest legal documents (contracts, policies, reports)
- Query documents via RFS
- Return ranked documents with relationship explanations
- Exact byte recall (AEAD-verified)
- Show interference patterns (proofs)

**Demo Flow:**
1. Load legal document dataset (100-500 documents)
2. Ingest into RFS field
3. Query: "data breach incident"
4. Show results:
   - Ranked document IDs
   - Resonance scores (Q_dB)
   - Relationship explanations
   - Interference patterns (proofs)
5. Exact recall: Get original bytes for selected document
6. Show audit trail: Query + results + proofs

**Success Criteria:**
- Documents found by meaning (not just keywords)
- Relationships discovered automatically
- Explanations generated (proofs)
- Exact recall works (AEAD-verified)
- Audit trail complete

### Phase 2: Relationship Graph (Post-MVP)

**Features:**
- Entanglement graph visualization
- Document relationship mapping
- Timeline analysis
- Relationship export

### Phase 3: Production Features (Future)

**Features:**
- Real-time document ingestion
- Integration with legal systems
- Compliance reporting
- Advanced relationship analysis

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────┐
│                    Legal Documents                       │
│  (Contracts, policies, reports, emails)                │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              RFS Dual-Path Encoding                      │
│  • Semantic path: document → field (for search)        │
│  • Byte path: document → byte channel (for exact recall)│
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Superposed Field + Byte Channel            │
│  • Semantic field: all documents combined              │
│  • Byte channel: exact bytes (AEAD-encrypted)          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Query & Resonance Search                    │
│  • Query field resonates with semantic field           │
│  • Returns documents with relationship explanations    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Exact Recall (AEAD-Verified)                │
│  • Document ID → byte channel lookup                   │
│  • Extract bytes → AEAD decrypt + verify               │
│  • Return exact original bytes                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Results + Proofs + Exact Bytes              │
│  • Ranked documents                                    │
│  • Relationship explanations (proofs)                  │
│  • Exact document bytes (AEAD-verified)                │
│  • Audit trail                                         │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Ingest**: Legal documents → RFS (semantic + byte paths)
2. **Superpose**: All documents in semantic field
3. **Query**: Natural language query → query field
4. **Resonate**: Query field resonates with semantic field
5. **Explain**: Return documents + relationship proofs
6. **Recall**: Get exact bytes (AEAD-verified) for evidence

## Demo Walkthrough

### Step 1: Prepare Legal Documents

**Document Format:**
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
    "related_contracts": ["CONTRACT-042"]
  }
}
```

**Dataset:**
- 100-500 legal documents
- Mix of types (contracts, policies, reports, emails)
- Some related/contradictory documents
- Various dates and classifications

### Step 2: Ingest into RFS

```python
from src.rfs.recall import ResonantFieldStorage
from src.rfs.retrieval import FieldRetriever

# Ingest documents (semantic + byte paths)
storage = ResonantFieldStorage(...)
retriever = FieldRetriever(...)

for doc in documents:
    # Semantic path: for search
    doc_text = f"{doc['title']} {doc['content']}"
    doc_vector = encode_document(doc_text)
    
    # Byte path: for exact recall
    doc_bytes = doc['content'].encode('utf-8')
    storage.encode(doc['doc_id'], doc_bytes)
    
    # Add to retriever
    retriever.add_document(doc_vector, doc['doc_id'])
```

### Step 3: Query Documents

```python
# Query: "data breach incident"
query_text = "data breach incident"
query_vector = encode_query(query_text)

# Search
results = retriever.query(query_vector, top_k=10)

# Results with explanations
for doc_id, score in results:
    explanation = get_relationship_explanation(query_field, doc_field)
    print(f"{doc_id}: score={score}, Q_dB={explanation['q_dB']}")
    print(f"  Relationship: {explanation['relationship_type']}")
    print(f"  Why: {explanation['reason']}")
    print(f"  Proof: {explanation['interference_pattern']}")
```

### Step 4: Exact Recall

```python
# Get exact bytes for evidence
doc_id = "DOC-001"
exact_bytes = storage.recall(doc_id)

# Verify integrity (AEAD)
if exact_bytes:
    print(f"Retrieved {len(exact_bytes)} bytes")
    print(f"Integrity: AEAD-verified")
    print(f"Original document: {exact_bytes.decode('utf-8')}")
```

### Step 5: Show Audit Trail

```python
# Audit trail
audit_log = {
    "query": query_text,
    "timestamp": "2025-12-10T10:30:00Z",
    "results": [
        {
            "doc_id": doc_id,
            "score": score,
            "q_dB": explanation['q_dB'],
            "proof": explanation['interference_pattern'],
            "exact_recall": {
                "retrieved": True,
                "aead_verified": True,
                "bytes_length": len(exact_bytes)
            }
        }
        for doc_id, score, explanation in results
    ]
}
```

## Quick Start Guide

### Prerequisites

- RFS installed and configured
- Legal document dataset
- Python 3.12+
- Metal/GPU available

### Setup

```bash
# 1. Navigate to project root
cd /path/to/ResonantFieldStorage

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Prepare legal documents
python scripts/use_cases/04_compliance_legal_archive/prepare_documents.py
```

### Run MVP Demo

```bash
# Run demo script
python scripts/use_cases/04_compliance_legal_archive/demo.py \
    --data artifacts/use_cases/04_compliance_legal_archive/documents.jsonl \
    --query "data breach incident" \
    --top-k 10 \
    --exact-recall \
    --show-proofs \
    --audit-trail
```

### Expected Output

```
Query: "data breach incident"

Results:
1. DOC-001: score=0.95, Q_dB=24.2
   Relationship: Direct match
   Why: Direct match on "data breach incident"
   Proof: High constructive interference (0.92)

2. DOC-042: score=0.88, Q_dB=21.5
   Relationship: Related contract
   Why: Contract mentions "data breach" clauses
   Proof: Medium constructive interference (0.78)

3. DOC-089: score=0.83, Q_dB=20.1
   Relationship: Related policy
   Why: Policy covers "incident response"
   Proof: Medium constructive interference (0.71)

Exact Recall:
DOC-001: Retrieved 2,543 bytes (AEAD-verified)
Original: "On 2025-12-01, unauthorized access detected..."

Audit Trail:
- Query: "data breach incident"
- Timestamp: 2025-12-10T10:30:00Z
- Results: 10 documents
- Proofs: All documents have interference pattern proofs
- Exact Recall: DOC-001 retrieved and verified
```

## Key Metrics & KPIs

### Search Quality

- **Recall@10**: % of relevant documents found
- **Relationship Discovery**: % of relationships discovered
- **Q_dB**: Resonance quality (target: ≥20)

### Compliance

- **Exact Recall Success**: 100% (AEAD-verified)
- **Audit Trail Completeness**: 100%
- **Proof Generation**: 100% of results have proofs

### Performance

- **Query Latency**: P95 ≤ 50ms
- **Exact Recall Latency**: P95 ≤ 200ms
- **Ingest Throughput**: Documents/second

## Integration Points

### Legal Systems

- **Document Management**: Integration with legal DMS
- **Case Management**: Integration with case systems
- **Compliance Tools**: Integration with compliance platforms

### Output Formats

- **REST API**: Query and exact recall endpoints
- **Audit Export**: JSON/CSV export for compliance
- **Evidence Format**: Original bytes + proofs

## Next Steps

1. **Review NORTH_STAR.md**: Understand vision and success criteria
2. **Review EXECUTION_PLAN.md**: See MVP implementation roadmap
3. **Prepare Documents**: Create sample legal document dataset
4. **Implement MVP**: Follow execution plan phases
5. **Demo**: Show MVP to stakeholders

## Related Documentation

- **North Star:** `NORTH_STAR.md`
- **Execution Plan:** `EXECUTION_PLAN.md`
- **RFS Architecture:** `../../RFS_NORTH_STAR_V4.md`
- **Byte Channel:** `../../src/rfs/recall.py`
