# Use Case 1: Incident Memory for On-Call Teams

**Status:** MVP Planning  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10

## Problem Statement

### Current Pain Points

On-call engineers face critical challenges when responding to incidents:

1. **Slow Incident Discovery**: Finding related incidents takes too long
   - Keyword search misses semantic relationships
   - Engineers manually connect incidents based on experience
   - No automatic pattern detection

2. **Missed Relationships**: Related incidents aren't discovered
   - "Database connection timeout" vs "Connection pool exhaustion" aren't linked
   - Similar root causes across different symptoms aren't connected
   - Historical context is lost

3. **Contradictory Information**: Conflicting reports aren't surfaced
   - Some incidents say "database is fine" while others report failures
   - No automatic contradiction detection
   - Engineers waste time reconciling conflicts

4. **No Explainability**: Can't explain why incidents are related
   - Black-box search results
   - No way to prove relationships
   - Hard to build trust in recommendations

### Business Impact

- **Increased MTTR** (Mean Time To Resolution): Engineers spend too long finding context
- **Knowledge Loss**: Incident relationships aren't captured or retained
- **Repeated Issues**: Same problems recur because patterns aren't detected
- **Low Trust**: Engineers don't trust search results without explanations

## RFS Solution Overview

### How RFS Solves This

**1. Superposition: All Incidents in One Field**
```
All incident reports → encode → superpose in field
    ↓
One superposed field with ALL incidents combined
    ↓
Incidents interact and create interference patterns
```

**2. Resonance Search: Find by Meaning, Not Keywords**
```
Query: "database connection timeout"
    ↓
Query field resonates with superposed field
    ↓
Finds incidents by MEANING, not just keywords:
- Direct matches: "database timeout" incidents
- Related: "connection pool exhaustion" (constructive interference)
- Related: "network latency" (constructive interference)
- Contradictory: "database is fine" (destructive interference)
```

**3. Interference Patterns: Reveal Relationships**
- **Constructive Interference**: Similar incidents amplify → shows relationships
- **Destructive Interference**: Contradictory incidents cancel → shows conflicts
- **Explainable**: Can show WHY incidents are related via interference patterns

**4. Entanglement Graph: Visualize Relationships**
- Builds graph of incident relationships
- Shows incident clusters (communities)
- Tracks how incidents are connected

## MVP Scope

### Phase 1: Basic Incident Search (MVP Demo)

**Features:**
- Ingest incident reports (JSON format)
- Encode incidents into RFS field
- Query incidents by natural language
- Return ranked results with explanations
- Show interference patterns (constructive/destructive)

**Demo Flow:**
1. Load sample incident dataset (100-500 incidents)
2. Ingest into RFS field
3. Query: "database connection timeout"
4. Show results with:
   - Ranked incident IDs
   - Resonance scores (Q_dB)
   - Interference patterns (why they match)
   - Relationship indicators (constructive/destructive)

**Success Criteria:**
- Query returns relevant incidents (not just keyword matches)
- Finds related incidents automatically
- Explains why incidents match
- Detects contradictions

### Phase 2: Relationship Discovery (Post-MVP)

**Features:**
- Entanglement graph visualization
- Incident clustering
- Pattern detection
- Temporal analysis (how incidents evolved)

### Phase 3: Production Features (Future)

**Features:**
- Real-time incident ingestion
- Integration with incident management systems (PagerDuty, Opsgenie)
- Alerting on pattern detection
- Incident correlation dashboards

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────┐
│                    Incident Reports                      │
│  (JSON: title, description, timestamp, metadata)        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              RFS Field-Native Encoder                    │
│  • ThetaTextEncoder: text → vector                      │
│  • ResonantFieldEncoder: vector → 4D field              │
│  • AssociativeProjector: filter frequencies             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Superposed Field (All Incidents)            │
│  • One 4D field with all incidents combined             │
│  • Interference patterns emerge automatically           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Query & Resonance Search                    │
│  • Query field resonates with superposed field          │
│  • Finds incidents by meaning (not keywords)            │
│  • Returns interference patterns (explanations)         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Results + Explanations                      │
│  • Ranked incident IDs                                  │
│  • Resonance scores (Q_dB)                              │
│  • Interference patterns (why they match)               │
│  • Relationship indicators                              │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Ingest**: Incident reports → RFS field
2. **Superpose**: All incidents combined in one field
3. **Query**: Natural language query → query field
4. **Resonate**: Query field resonates with superposed field
5. **Explain**: Return results with interference patterns

## Demo Walkthrough

### Step 1: Prepare Sample Data

**Sample Incident Format:**
```json
{
  "incident_id": "INC-001",
  "title": "Database connection timeout",
  "description": "Users reporting slow queries. Database connection pool exhausted. Root cause: connection leak in service X.",
  "timestamp": "2025-12-10T10:30:00Z",
  "severity": "high",
  "status": "resolved"
}
```

**Dataset:**
- 100-500 sample incidents
- Mix of related and unrelated incidents
- Some contradictory reports
- Various severities and statuses

### Step 2: Ingest into RFS

```python
from src.rfs.retrieval import FieldRetriever, FieldRetrieverConfig

# Load incidents
incidents = load_incidents("sample_incidents.jsonl")

# Extract text (title + description)
incident_texts = [f"{inc['title']} {inc['description']}" for inc in incidents]
incident_ids = [inc['incident_id'] for inc in incidents]

# Encode to vectors (using sentence transformer or field-native)
vectors = encode_incidents(incident_texts)

# Build RFS retriever
config = FieldRetrieverConfig(
    field_shape=(32, 32, 32, 4),
    n_symbols=1024,
    use_metal=True,
)
retriever = FieldRetriever(vectors, incident_ids, config=config)
```

### Step 3: Query Incidents

```python
# Query: "database connection timeout"
query_text = "database connection timeout"
query_vector = encode_query(query_text)

# Search
results = retriever.query(query_vector, top_k=10)

# Results: [(incident_id, score), ...]
# Example:
# [
#   ("INC-001", 0.95),  # Direct match
#   ("INC-042", 0.87),  # Related: "connection pool exhaustion"
#   ("INC-089", 0.82),  # Related: "network latency"
#   ("INC-156", 0.15),  # Contradictory: "database is fine"
#   ...
# ]
```

### Step 4: Show Explanations

```python
# Get interference patterns (explanations)
for incident_id, score in results:
    explanation = get_interference_pattern(query_field, incident_field)
    print(f"{incident_id}: {score}")
    print(f"  Constructive: {explanation['constructive']}")
    print(f"  Destructive: {explanation['destructive']}")
    print(f"  Why: {explanation['reason']}")
```

### Step 5: Visualize Relationships

```python
# Build entanglement graph
from src.rfs.semantic.entanglement import build_entanglement_graph

graph = build_entanglement_graph(doc_coeffs, config)
# Returns: DataFrame with (src_id, dst_id, weight, community)

# Visualize
visualize_incident_graph(graph, incidents)
```

## Quick Start Guide

### Prerequisites

- RFS installed and configured
- Sample incident dataset
- Python 3.12+
- Metal/GPU available (for field-native path)

### Setup

```bash
# 1. Navigate to project root
cd /path/to/ResonantFieldStorage

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Install dependencies (if needed)
pip install -r requirements/dev.txt

# 4. Prepare sample data
python scripts/use_cases/01_incident_memory/prepare_sample_data.py
```

### Run MVP Demo

```bash
# Run demo script
python scripts/use_cases/01_incident_memory/demo.py \
    --data artifacts/use_cases/01_incident_memory/sample_incidents.jsonl \
    --query "database connection timeout" \
    --top-k 10 \
    --show-explanations
```

### Expected Output

```
Query: "database connection timeout"

Results:
1. INC-001: score=0.95, Q_dB=24.3
   Constructive: High (0.89) - Direct match on "database timeout"
   Why: Query field strongly resonates with incident field

2. INC-042: score=0.87, Q_dB=21.7
   Constructive: High (0.76) - Related concept "connection pool"
   Why: Both involve connection management, constructive interference

3. INC-089: score=0.82, Q_dB=20.1
   Constructive: Medium (0.65) - Related concept "network latency"
   Why: Network issues can cause connection timeouts

4. INC-156: score=0.15, Q_dB=8.2
   Destructive: High (0.72) - Contradictory "database is fine"
   Why: Contradicts query intent, destructive interference

...
```

## Key Metrics & KPIs

### Search Quality

- **Recall@10**: % of relevant incidents found in top 10
- **nDCG@10**: Normalized discounted cumulative gain
- **Q_dB**: Resonance quality (target: ≥20 dB)

### Relationship Discovery

- **Relationship Coverage**: % of incidents with discovered relationships
- **Contradiction Detection**: % of contradictions automatically detected
- **Pattern Detection**: Number of recurring patterns discovered

### Performance

- **Query Latency**: P95 ≤ 50ms (target)
- **Ingest Throughput**: Incidents/second
- **Field Size**: Memory usage per incident

### Business Impact

- **MTTR Reduction**: % reduction in mean time to resolution
- **Incident Correlation**: % of incidents with discovered relationships
- **Engineer Satisfaction**: Trust in search results

## Integration Points

### Incident Management Systems

- **PagerDuty**: Webhook integration for real-time ingestion
- **Opsgenie**: API integration for incident sync
- **Jira Service Management**: Ticket ingestion
- **Custom Systems**: REST API for incident ingestion

### Output Formats

- **REST API**: Query endpoint for incident search
- **GraphQL**: Relationship queries
- **Webhooks**: Real-time relationship updates
- **Dashboards**: Visualization of incident relationships

## Next Steps

1. **Review NORTH_STAR.md**: Understand vision and success criteria
2. **Review EXECUTION_PLAN.md**: See MVP implementation roadmap
3. **Prepare Sample Data**: Create incident dataset for demo
4. **Implement MVP**: Follow execution plan phases
5. **Demo**: Show MVP to stakeholders

## Related Documentation

- **North Star:** `NORTH_STAR.md`
- **Execution Plan:** `EXECUTION_PLAN.md`
- **RFS Architecture:** `../../RFS_NORTH_STAR_V4.md`
- **Field Retriever:** `../../src/rfs/retrieval/field_retriever.py`
