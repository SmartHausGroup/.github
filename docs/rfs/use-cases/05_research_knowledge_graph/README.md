# Use Case 5: Research Knowledge Graph

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10

## Problem Statement

### Current Pain Points

Researchers face critical challenges when searching academic papers:

1. **Keyword Search Limitations**: Misses semantic relationships
   - "quantum entanglement" doesn't find "quantum correlation"
   - "neural networks" doesn't find "deep learning"
   - No discovery of related research

2. **No Relationship Discovery**: Can't see how papers connect
   - Related papers aren't linked
   - Research communities aren't visible
   - Evolution of concepts isn't tracked

3. **No Temporal Analysis**: Can't track how concepts evolved
   - Can't see how research evolved over time
   - No timeline of concept development
   - Missing historical context

4. **No Community Detection**: Research groups aren't visible
   - Can't identify research communities
   - Collaboration patterns aren't visible
   - Hard to find related researchers

### Business Impact

- **Slower Research**: Researchers spend too long finding related papers
- **Missed Connections**: Related research isn't discovered
- **Knowledge Loss**: Research relationships aren't captured
- **Inefficient Collaboration**: Research communities aren't visible

## RFS Solution Overview

### How RFS Solves This

**1. Semantic Paper Search: Find by Meaning, Not Keywords**
```
Query: "quantum entanglement"
    ↓
Query field resonates with paper field
    ↓
Finds papers by MEANING, not just keywords:
- Direct matches: "quantum entanglement" papers
- Related: "quantum correlation" papers (constructive interference)
- Related: "Bell inequality" papers (constructive interference)
- Evolution: Papers showing concept development over time
```

**2. Temporal Analysis: Track Concept Evolution**
```
All papers → encode → superpose in field
    ↓
Temporal dimension (t) tracks time
    ↓
Can see how concepts evolved over time
    ↓
Timeline of research development
```

**3. Entanglement Graph: Visualize Research Communities**
```
Field interference patterns → entanglement graph
    ↓
Shows:
- Paper clusters (research communities)
- Related papers (connections)
- Research groups (communities)
```

**4. Relationship Discovery: Understand Research Connections**
```
Interference patterns reveal:
- Constructive: Related papers (reinforce each other)
- Destructive: Contradictory papers (cancel each other)
- Temporal: How concepts evolved
```

## MVP Scope

### Phase 1: Basic Paper Search + Temporal Analysis (MVP Demo)

**Features:**
- Ingest research papers (abstracts, titles, metadata)
- Query papers by natural language
- Return ranked papers with explanations
- Show temporal evolution (how concepts changed over time)
- Basic relationship visualization

**Demo Flow:**
1. Load paper dataset (100-1000 papers)
2. Ingest into RFS field (with temporal dimension)
3. Query: "quantum entanglement"
4. Show results:
   - Ranked paper IDs
   - Resonance scores (Q_dB)
   - Temporal evolution (papers over time)
   - Relationship explanations
5. Show entanglement graph (basic)

**Success Criteria:**
- Papers found by meaning (not just keywords)
- Temporal evolution visible
- Relationships discovered
- Explanations generated

### Phase 2: Entanglement Graph (Post-MVP)

**Features:**
- Full entanglement graph construction
- Research community detection
- Collaboration pattern analysis
- Graph visualization

### Phase 3: Production Features (Future)

**Features:**
- Real-time paper indexing
- Integration with academic databases
- Advanced temporal analysis
- Research trend prediction

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────┐
│                    Research Papers                       │
│  (Abstracts, titles, metadata, dates)                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              RFS Field-Native Encoder                    │
│  • Encode papers into 4D field (with temporal)        │
│  • Temporal dimension (t) encodes publication date     │
│  • Superpose all papers in field                       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              User Query                                  │
│  "quantum entanglement"                                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              RFS Resonance Search                        │
│  • Query field resonates with paper field              │
│  • Returns papers with temporal context                │
│  • Shows relationships and evolution                   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Entanglement Graph                          │
│  • Build graph from interference patterns              │
│  • Detect research communities                         │
│  • Visualize relationships                             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Results + Temporal + Graph                  │
│  • Ranked papers                                       │
│  • Temporal evolution                                  │
│  • Research communities                                │
│  • Relationship explanations                           │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Ingest**: Research papers → RFS field (with temporal dimension)
2. **Superpose**: All papers combined in one field
3. **Query**: Natural language query → query field
4. **Resonate**: Query field resonates with paper field
5. **Temporal**: Track evolution over time (temporal dimension)
6. **Graph**: Build entanglement graph (research communities)

## Demo Walkthrough

### Step 1: Prepare Paper Dataset

**Paper Format:**
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
    "keywords": ["quantum", "entanglement", "many-body"]
  }
}
```

**Dataset:**
- 100-1000 research papers
- Mix of topics (quantum, ML, physics, etc.)
- Various publication dates (temporal spread)
- Some related/contradictory papers

### Step 2: Ingest into RFS

```python
from src.rfs.retrieval import FieldRetriever, FieldRetrieverConfig

# Load papers
papers = load_papers("papers.jsonl")

# Extract text (title + abstract)
paper_texts = [f"{p['title']} {p['abstract']}" for p in papers]
paper_ids = [p['paper_id'] for p in papers]
paper_dates = [p['publication_date'] for p in papers]

# Encode to vectors
vectors = encode_papers(paper_texts)

# Build RFS retriever (with temporal dimension)
config = FieldRetrieverConfig(
    field_shape=(32, 32, 32, 16),  # Larger t dimension for temporal
    n_symbols=1024,
    use_metal=True,
)
retriever = FieldRetriever(vectors, paper_ids, config=config)

# Store temporal metadata
retriever.store_temporal_metadata(paper_ids, paper_dates)
```

### Step 3: Query Papers

```python
# Query: "quantum entanglement"
query_text = "quantum entanglement"
query_vector = encode_query(query_text)

# Search
results = retriever.query(query_vector, top_k=10)

# Results with temporal context
for paper_id, score in results:
    paper = get_paper(paper_id)
    explanation = get_explanation(query_field, paper_field)
    temporal_info = get_temporal_info(paper_id)
    
    print(f"{paper['title']} ({paper['publication_date']})")
    print(f"  Score: {score}, Q_dB: {explanation['q_dB']}")
    print(f"  Temporal Position: {temporal_info['t_slice']}")
    print(f"  Why: {explanation['reason']}")
```

### Step 4: Show Temporal Evolution

```python
# Get temporal evolution
evolution = get_temporal_evolution(results, time_slices=16)

print("Temporal Evolution:")
for time_slice, papers in evolution.items():
    print(f"\nTime Slice {time_slice}:")
    for paper_id in papers:
        paper = get_paper(paper_id)
        print(f"  - {paper['title']} ({paper['publication_date']})")
```

### Step 5: Show Entanglement Graph

```python
# Build entanglement graph
from src.rfs.semantic.entanglement import build_entanglement_graph

graph = build_entanglement_graph(doc_coeffs, config)

# Visualize research communities
communities = detect_communities(graph)

print("Research Communities:")
for community_id, papers in communities.items():
    print(f"\nCommunity {community_id}:")
    for paper_id in papers:
        paper = get_paper(paper_id)
        print(f"  - {paper['title']}")
```

## Quick Start Guide

### Prerequisites

- RFS installed and configured
- Research paper dataset
- Python 3.12+
- Metal/GPU available

### Setup

```bash
# 1. Navigate to project root
cd /path/to/ResonantFieldStorage

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Prepare paper dataset
python scripts/use_cases/05_research_knowledge_graph/prepare_papers.py
```

### Run MVP Demo

```bash
# Run demo script
python scripts/use_cases/05_research_knowledge_graph/demo.py \
    --data artifacts/use_cases/05_research_knowledge_graph/papers.jsonl \
    --query "quantum entanglement" \
    --top-k 10 \
    --show-temporal \
    --show-graph
```

### Expected Output

```
Query: "quantum entanglement"

Results:
1. PAPER-001: "Quantum Entanglement in Many-Body Systems" (2020-01-15)
   Score: 0.95, Q_dB: 24.1
   Temporal: Slice 8 (2020)
   Why: Direct match on "quantum entanglement"

2. PAPER-042: "Quantum Correlation in Spin Chains" (2019-06-20)
   Score: 0.88, Q_dB: 21.5
   Temporal: Slice 6 (2019)
   Why: Related concept "quantum correlation", constructive interference

3. PAPER-089: "Bell Inequality Violations" (2021-03-10)
   Score: 0.83, Q_dB: 20.2
   Temporal: Slice 10 (2021)
   Why: Related concept "Bell inequality", constructive interference

Temporal Evolution:
Slice 6 (2019): 5 papers (early work on quantum correlation)
Slice 8 (2020): 12 papers (peak: quantum entanglement)
Slice 10 (2021): 8 papers (later: Bell inequality)

Research Communities:
Community 0: Quantum Entanglement (15 papers)
  - PAPER-001, PAPER-042, PAPER-089, ...
Community 1: Many-Body Systems (8 papers)
  - PAPER-023, PAPER-067, ...
```

## Key Metrics & KPIs

### Search Quality

- **Recall@10**: % of relevant papers found
- **Temporal Accuracy**: % of papers in correct time slices
- **Community Detection**: % of papers in correct communities
- **Q_dB**: Resonance quality (target: ≥20)

### Research Value

- **Relationship Discovery**: % of relationships discovered
- **Temporal Coverage**: % of time period covered
- **Community Coverage**: % of papers in communities

### Performance

- **Query Latency**: P95 ≤ 50ms
- **Graph Construction**: Time to build entanglement graph
- **Temporal Analysis**: Time for temporal evolution

## Integration Points

### Paper Sources

- **Academic Databases**: arXiv, PubMed, etc.
- **Local Repositories**: PDF collections
- **Citation Networks**: Citation data import

### Output Formats

- **REST API**: Query endpoint for paper search
- **Graph Export**: Entanglement graph (JSON/GraphML)
- **Temporal Export**: Timeline data (JSON/CSV)
- **Visualization**: Graph and temporal visualizations

## Next Steps

1. **Review NORTH_STAR.md**: Understand vision and success criteria
2. **Review EXECUTION_PLAN.md**: See MVP implementation roadmap
3. **Prepare Papers**: Create sample paper dataset
4. **Implement MVP**: Follow execution plan phases
5. **Demo**: Show MVP to stakeholders

## Related Documentation

- **North Star:** `NORTH_STAR.md`
- **Execution Plan:** `EXECUTION_PLAN.md`
- **RFS Architecture:** `../../RFS_NORTH_STAR_V4.md`
- **Entanglement:** `../../src/rfs/semantic/entanglement.py`
