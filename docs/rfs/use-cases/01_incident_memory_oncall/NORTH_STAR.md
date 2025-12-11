# Use Case 1: Incident Memory for On-Call Teams — North Star

**Status:** Rev 1.0  
**Owner:** @smarthaus  
**Last Updated:** 2025-12-10  
**Source of Truth:** This document

## Vision

On-call engineers can instantly discover related incidents, understand relationships, and detect patterns—all automatically through RFS resonance search. No more manual keyword searches or missed connections. Every incident query returns not just matches, but explanations of why incidents are related, what patterns exist, and what contradictions to watch for.

## Core Value Proposition

**For On-Call Engineers:**
- **Instant Context**: Find related incidents in seconds, not minutes
- **Automatic Discovery**: Relationships discovered automatically (no manual tagging)
- **Explainable Results**: Understand why incidents are related
- **Pattern Detection**: Recurring issues surface automatically
- **Contradiction Alerts**: Conflicting reports highlighted automatically

**For Engineering Teams:**
- **Reduced MTTR**: Faster incident resolution through better context
- **Knowledge Retention**: Incident relationships persist in the field
- **Pattern Recognition**: Recurring problems identified automatically
- **Better Post-Mortems**: Rich relationship data for analysis

**For Enterprises:**
- **Operational Excellence**: Faster incident response
- **Cost Savings**: Reduced engineer time spent searching
- **Compliance**: Audit trail of incident relationships
- **Scalability**: Handles thousands of incidents efficiently

## Success Criteria

### MVP Success (Phase 1)

- ✅ Query returns relevant incidents (Recall@10 ≥ 0.80)
- ✅ Finds related incidents automatically (not just keyword matches)
- ✅ Explains why incidents match (interference patterns)
- ✅ Detects contradictions (destructive interference)
- ✅ Query latency P95 ≤ 50ms
- ✅ Resonance quality Q_dB ≥ 20

### Production Success (Phase 3)

- ✅ Real-time incident ingestion (< 1s latency)
- ✅ Handles 10,000+ incidents per shard
- ✅ Entanglement graph visualization
- ✅ Pattern detection alerts
- ✅ Integration with major incident management systems
- ✅ MTTR reduction ≥ 30%

## User Personas

### Primary: On-Call Engineer (Sarah)

**Profile:**
- 3-5 years experience
- Responds to incidents 24/7
- Needs fast access to related incidents
- Values explainable results

**Goals:**
- Find related incidents quickly
- Understand why incidents are related
- Detect patterns and recurring issues
- Trust the search results

**Pain Points:**
- Keyword search misses relationships
- Manual incident correlation is slow
- No explanation of why incidents match
- Contradictory information isn't surfaced

**How RFS Helps:**
- Resonance search finds related incidents automatically
- Interference patterns explain relationships
- Pattern detection surfaces recurring issues
- Contradiction detection highlights conflicts

### Secondary: Incident Manager (Mike)

**Profile:**
- Manages incident response process
- Analyzes incident trends
- Needs pattern detection
- Values data-driven insights

**Goals:**
- Identify recurring incident patterns
- Understand incident relationships
- Improve incident response process
- Reduce MTTR

**Pain Points:**
- Manual pattern detection is time-consuming
- Relationships between incidents aren't clear
- Hard to prove patterns exist
- No automated alerts for recurring issues

**How RFS Helps:**
- Automatic pattern detection via interference
- Entanglement graph shows relationships
- Explainable patterns (can prove why)
- Alerting on pattern detection

### Tertiary: SRE/DevOps Lead (Alex)

**Profile:**
- Owns incident response infrastructure
- Needs scalable solutions
- Values operational metrics
- Manages team efficiency

**Goals:**
- Reduce engineer time spent searching
- Improve incident response efficiency
- Scale to handle growing incident volume
- Measure impact of improvements

**Pain Points:**
- Current search doesn't scale
- Engineers waste time on manual correlation
- Hard to measure improvement
- No clear ROI on search improvements

**How RFS Helps:**
- Scalable field-native search
- Automatic relationship discovery (saves time)
- Clear metrics (MTTR, Q_dB, relationship coverage)
- Measurable ROI

## Technical Requirements

### Core RFS Features Required

1. **Field-Native Encoder**
   - ThetaTextEncoder for incident text encoding
   - ResonantFieldEncoder for field creation
   - AssociativeProjector for frequency filtering

2. **Superposition**
   - All incidents in one superposed field
   - Automatic interference pattern creation
   - Efficient field updates (incremental)

3. **Resonance Search**
   - Query field creation
   - Matched filter correlation
   - Peak detection and ranking

4. **Interference Analysis**
   - Constructive interference detection
   - Destructive interference detection
   - Overlap tensor computation (Λ_ij)

5. **Entanglement Graph** (Phase 2+)
   - Relationship graph construction
   - Community detection
   - Visualization support

### Performance Requirements

- **Query Latency**: P95 ≤ 50ms (target: 20ms)
- **Ingest Throughput**: ≥ 100 incidents/second
- **Field Capacity**: ≥ 10,000 incidents per shard
- **Resonance Quality**: Q_dB ≥ 20 (target: 25+)
- **Recall**: Recall@10 ≥ 0.80 (target: 0.90+)

### Integration Requirements

- **Incident Format**: JSON (title, description, metadata)
- **API**: REST endpoints for query/search
- **Webhooks**: Real-time incident ingestion
- **Export**: Relationship graph export (JSON/GraphML)

## Value Metrics

### User Value

- **Time Saved**: 5-10 minutes per incident query → 2-3 hours/week per engineer
- **Better Context**: 80%+ of related incidents found automatically
- **Trust**: Explainable results increase engineer confidence
- **Pattern Detection**: Recurring issues identified automatically

### Business Value

- **MTTR Reduction**: 30%+ reduction in mean time to resolution
- **Cost Savings**: $50k-$100k/year per team (engineer time saved)
- **Scalability**: Handles 10x incident volume without degradation
- **Compliance**: Audit trail of incident relationships

### Technical Value

- **Unified System**: One system for search + relationships (no separate graph DB)
- **Explainable**: Interference patterns provide explanations
- **Scalable**: Field-native computation scales efficiently
- **Deterministic**: Reproducible results for debugging

## Integration Points

### Input: Incident Sources

- **PagerDuty**: Webhook integration
- **Opsgenie**: API integration
- **Jira Service Management**: Ticket sync
- **Custom Systems**: REST API ingestion
- **File Import**: JSON/CSV batch import

### Output: Results & Visualizations

- **REST API**: Query endpoint (`GET /api/v1/incidents/search?q=...`)
- **GraphQL**: Relationship queries
- **Dashboards**: Incident relationship visualization
- **Alerts**: Pattern detection notifications
- **Exports**: Relationship graph (JSON/GraphML)

## Success Stories (Target)

### Story 1: Fast Incident Resolution

**Before RFS:**
- Engineer spends 15 minutes searching for related incidents
- Finds 2-3 related incidents manually
- Misses 5+ related incidents
- No explanation of relationships

**After RFS:**
- Engineer queries in 2 seconds
- Finds 10+ related incidents automatically
- Gets explanations of why they're related
- Resolves incident 30% faster

### Story 2: Pattern Detection

**Before RFS:**
- Recurring issues go unnoticed
- Manual pattern detection takes weeks
- No automated alerts

**After RFS:**
- Patterns detected automatically
- Alerts trigger on recurring issues
- Proactive problem prevention

### Story 3: Contradiction Detection

**Before RFS:**
- Conflicting reports aren't surfaced
- Engineers waste time reconciling
- No automatic contradiction alerts

**After RFS:**
- Contradictions detected automatically
- Highlighted in search results
- Engineers can investigate immediately

## Long-Term Vision

### Phase 1: MVP (Current)
- Basic incident search with relationships
- Explainable results
- Demo-ready

### Phase 2: Production (6 months)
- Real-time ingestion
- Entanglement graph visualization
- Pattern detection alerts
- Integration with incident management systems

### Phase 3: Advanced (12 months)
- Predictive incident correlation
- Automated incident grouping
- Root cause analysis assistance
- Multi-team incident sharing

## Alignment with RFS North Star

This use case aligns with RFS North Star V4:

- **§1.2 Field-Native Semantic Encoding**: Uses field-native encoder for incident encoding
- **§1.3 Resonance Query & Retrieval**: Uses resonance search for incident discovery
- **§2.6 Guardrails**: Respects Q_dB, η, capacity guardrails
- **§3.1 Performance Envelopes**: Meets latency and throughput targets
- **§4.5 Temporal Evolution**: Can track incident evolution over time (future)

## Related Documentation

- **README:** `README.md` (problem, solution, demo)
- **Execution Plan:** `EXECUTION_PLAN.md` (implementation roadmap)
- **RFS North Star:** `../../RFS_NORTH_STAR_V4.md`
- **Business Case:** `../../operations/business_case.md`
