# Use Case 2: RAG with Proofs (Retrieval-Augmented Generation)

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10

## Problem Statement

### Current Pain Points

Retrieval-Augmented Generation (RAG) systems face critical challenges:

1. **Black-Box Document Selection**: Can't explain why documents were selected
   - LLMs get context, but no proof of why
   - Users can't verify document relevance
   - Compliance requires explainability

2. **Poor Context Quality**: Documents selected by similarity, not meaning
   - Vector similarity misses semantic relationships
   - No understanding of document interactions
   - Contradictory documents included together

3. **No Relationship Awareness**: Documents treated as isolated
   - Can't leverage document relationships
   - Missing context from related documents
   - No contradiction detection

4. **Compliance Gaps**: Can't prove document selection
   - No audit trail of why documents were chosen
   - Can't explain to regulators
   - Hard to debug incorrect answers

### Business Impact

- **Low Trust**: Users don't trust AI answers without explanations
- **Compliance Risk**: Can't prove document selection for regulations
- **Poor Quality**: Wrong documents selected → wrong answers
- **Debugging Difficulty**: Hard to understand why answers are wrong

## RFS Solution Overview

### How RFS Solves This

**1. Resonance-Based Selection: Documents Selected by Meaning**
```
Query: "What are security best practices?"
    ↓
Query field resonates with document field
    ↓
Documents selected by RESONANCE (meaning), not just similarity
    ↓
High Q_dB = high quality match
```

**2. Interference Patterns: Explain Why Documents Were Selected**
```
For each selected document:
    ↓
Compute interference pattern with query
    ↓
Show:
- Constructive interference: Why document matches
- Destructive interference: Contradictions detected
- Resonance quality: Q_dB score
    ↓
Explainable proof of selection
```

**3. Relationship Awareness: Leverage Document Relationships**
```
Selected documents interact in field
    ↓
Constructive interference: Documents reinforce each other
    ↓
Better context: Related documents provide richer context
```

**4. Contradiction Detection: Avoid Conflicting Information**
```
Destructive interference detected
    ↓
Contradictory documents flagged
    ↓
LLM can handle contradictions explicitly
```

## MVP Scope

### Phase 1: Basic RAG with Explanations (MVP Demo)

**Features:**
- Ingest documents (knowledge base)
- Query documents via RFS
- Return top-K documents with explanations
- Generate LLM response with citations
- Show interference patterns (proofs)

**Demo Flow:**
1. Load knowledge base (100-1000 documents)
2. Ingest into RFS field
3. Query: "What are security best practices?"
4. RFS returns:
   - Top-K documents
   - Resonance scores (Q_dB)
   - Interference patterns (why selected)
   - Contradiction flags
5. LLM generates answer with citations
6. Show proofs: Why each document was selected

**Success Criteria:**
- Documents selected by meaning (not just similarity)
- Explanations generated for all selections
- Contradictions detected and flagged
- LLM answers are accurate and cited

### Phase 2: Advanced RAG Features (Post-MVP)

**Features:**
- Multi-document relationship analysis
- Contextual document ranking
- Automatic contradiction resolution
- Relationship-aware context building

### Phase 3: Production Features (Future)

**Features:**
- Real-time document updates
- Multi-query batching
- Relationship graph visualization
- Compliance reporting

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────┐
│                    Knowledge Base                        │
│  (Documents: articles, docs, FAQs, etc.)                │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              RFS Field-Native Encoder                    │
│  • Encode documents into 4D field                       │
│  • Superpose all documents                              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              User Query                                  │
│  "What are security best practices?"                    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              RFS Resonance Search                        │
│  • Query field resonates with superposed field          │
│  • Returns top-K documents with explanations            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Document Selection + Proofs                 │
│  • Selected documents                                   │
│  • Interference patterns (why selected)                 │
│  • Contradiction flags                                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              LLM Generation                              │
│  • Context: Selected documents                          │
│  • Citations: Document IDs + proofs                     │
│  • Answer: Generated with citations                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Response with Proofs                        │
│  • Answer text                                          │
│  • Citations with explanations                          │
│  • Interference patterns (proofs)                       │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Ingest**: Knowledge base documents → RFS field
2. **Superpose**: All documents combined in one field
3. **Query**: User question → query field
4. **Resonate**: Query field resonates with superposed field
5. **Select**: Top-K documents with explanations
6. **Generate**: LLM generates answer with citations
7. **Prove**: Return answer + proofs (interference patterns)

## Demo Walkthrough

### Step 1: Prepare Knowledge Base

**Sample Document Format:**
```json
{
  "doc_id": "DOC-001",
  "title": "Security Best Practices",
  "content": "Use strong passwords, enable 2FA, keep software updated...",
  "category": "security",
  "metadata": {
    "author": "Security Team",
    "last_updated": "2025-12-01"
  }
}
```

**Dataset:**
- 100-1000 documents
- Mix of topics (security, operations, development)
- Some overlapping/contradictory content
- Various formats (articles, FAQs, docs)

### Step 2: Ingest into RFS

```python
from src.rfs.retrieval import FieldRetriever, FieldRetrieverConfig

# Load documents
docs = load_documents("knowledge_base.jsonl")

# Extract text (title + content)
doc_texts = [f"{doc['title']} {doc['content']}" for doc in docs]
doc_ids = [doc['doc_id'] for doc in docs]

# Encode to vectors
vectors = encode_documents(doc_texts)

# Build RFS retriever
config = FieldRetrieverConfig(
    field_shape=(32, 32, 32, 4),
    n_symbols=1024,
    use_metal=True,
)
retriever = FieldRetriever(vectors, doc_ids, config=config)
```

### Step 3: Query Documents

```python
# User query
query_text = "What are security best practices?"
query_vector = encode_query(query_text)

# Search with RFS
results = retriever.query(query_vector, top_k=5)

# Results with explanations
for doc_id, score in results:
    explanation = get_explanation(query_field, doc_field)
    print(f"{doc_id}: score={score}, Q_dB={explanation['q_dB']}")
    print(f"  Why: {explanation['reason']}")
    print(f"  Constructive: {explanation['constructive']}")
    print(f"  Destructive: {explanation['destructive']}")
```

### Step 4: Generate LLM Response

```python
# Get selected documents
selected_docs = [get_doc(doc_id) for doc_id, _ in results]

# Build context with proofs
context = build_context_with_proofs(selected_docs, explanations)

# Generate answer with LLM
answer = llm.generate(
    query=query_text,
    context=context,
    citations=[(doc_id, explanation) for doc_id, explanation in zip(doc_ids, explanations)]
)

# Return answer + proofs
response = {
    "answer": answer,
    "citations": [
        {
            "doc_id": doc_id,
            "score": score,
            "q_dB": explanation['q_dB'],
            "proof": explanation['interference_pattern'],
            "reason": explanation['reason']
        }
        for doc_id, score, explanation in zip(doc_ids, scores, explanations)
    ]
}
```

### Step 5: Show Proofs

```python
# Display answer with proofs
print(f"Answer: {response['answer']}")
print("\nCitations with Proofs:")
for citation in response['citations']:
    print(f"\n{citation['doc_id']}:")
    print(f"  Resonance: Q_dB = {citation['q_dB']}")
    print(f"  Why Selected: {citation['reason']}")
    print(f"  Proof: {citation['proof']}")
```

## Quick Start Guide

### Prerequisites

- RFS installed and configured
- Knowledge base documents
- LLM API access (OpenAI, Anthropic, etc.)
- Python 3.12+

### Setup

```bash
# 1. Navigate to project root
cd /path/to/ResonantFieldStorage

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Prepare knowledge base
python scripts/use_cases/02_rag_with_proofs/prepare_kb.py
```

### Run MVP Demo

```bash
# Run demo script
python scripts/use_cases/02_rag_with_proofs/demo.py \
    --kb artifacts/use_cases/02_rag_with_proofs/knowledge_base.jsonl \
    --query "What are security best practices?" \
    --top-k 5 \
    --llm openai \
    --show-proofs
```

### Expected Output

```
Query: "What are security best practices?"

Selected Documents:
1. DOC-001: score=0.94, Q_dB=23.5
   Why: Direct match on "security best practices"
   Proof: High constructive interference (0.91)

2. DOC-042: score=0.87, Q_dB=21.2
   Why: Related concept "authentication methods"
   Proof: Medium constructive interference (0.76)

3. DOC-089: score=0.82, Q_dB=19.8
   Why: Related concept "access control"
   Proof: Medium constructive interference (0.68)

4. DOC-156: score=0.15, Q_dB=7.3
   Why: Contradictory "no security needed"
   Proof: High destructive interference (0.82) - FLAGGED

Generated Answer:
"Security best practices include using strong passwords, enabling 
two-factor authentication, keeping software updated, and implementing 
access controls. [Citation: DOC-001, DOC-042, DOC-089]

Note: DOC-156 contradicts the query and was excluded from context."

Proofs:
- DOC-001: Selected because query field strongly resonates (Q_dB=23.5)
- DOC-042: Selected because related authentication concepts reinforce query
- DOC-089: Selected because access control concepts match query intent
- DOC-156: Flagged as contradictory (destructive interference detected)
```

## Key Metrics & KPIs

### RAG Quality

- **Answer Accuracy**: % of correct answers (human evaluation)
- **Citation Quality**: % of citations that support the answer
- **Contradiction Detection**: % of contradictions correctly flagged
- **Explanation Quality**: Human evaluation of explanation clarity

### RFS Performance

- **Resonance Quality**: Q_dB ≥ 20 (target: 25+)
- **Recall@K**: % of relevant documents in top-K
- **Query Latency**: P95 ≤ 50ms
- **Explanation Generation**: < 10ms per document

### Business Impact

- **User Trust**: % of users who trust answers with proofs
- **Compliance**: % of queries with audit-ready proofs
- **Answer Quality**: Improvement vs baseline RAG

## Integration Points

### LLM Providers

- **OpenAI**: GPT-4, GPT-3.5
- **Anthropic**: Claude
- **Local Models**: Llama, Mistral (via Ollama)

### Knowledge Base Sources

- **Documentation**: Markdown, HTML, PDF
- **Wikis**: Confluence, Notion
- **Code Repos**: GitHub, GitLab
- **Custom**: JSON, CSV imports

### Output Formats

- **REST API**: Query endpoint with proofs
- **Streaming**: Real-time answer generation
- **Export**: Proofs in JSON format for audit

## Next Steps

1. **Review NORTH_STAR.md**: Understand vision and success criteria
2. **Review EXECUTION_PLAN.md**: See MVP implementation roadmap
3. **Prepare Knowledge Base**: Create sample document dataset
4. **Implement MVP**: Follow execution plan phases
5. **Demo**: Show MVP to stakeholders

## Related Documentation

- **North Star:** `NORTH_STAR.md`
- **Execution Plan:** `EXECUTION_PLAN.md`
- **RFS Architecture:** `../../RFS_NORTH_STAR_V4.md`
- **Field Retriever:** `../../src/rfs/retrieval/field_retriever.py`
