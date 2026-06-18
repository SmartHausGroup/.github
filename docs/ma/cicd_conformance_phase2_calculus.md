# SmartHausGroup.github Repo CI/CD Conformance - Phase 2 Calculus

## Predicates

```text
ManifestValid_R(m) =
  m.schema_version = 0.1.0
  and m.repository.name = SmartHausGroup.github
  and m.profile.primary = docs-site
```

```text
BranchRulesProtected_R(b) =
  protected branch set includes main and the standard branch names
  and pull_request required
  and direct_push blocked
  and force_push blocked
  and deletion blocked
```

```text
RequiredChecksGreen_R(q, c) =
  q.repo-cicd-conformance.sha = c
  and q.repo-cicd-conformance.status = success
  and q.evidence-pack.sha = c
  and q.evidence-pack.status = success
```

```text
MAEvidenceTraceable_R(e) =
  intent, formula, calculus, lemmas, invariants, notebook, and scorecard exist
```

```text
ScorecardGreen_R(s) =
  s.status = GREEN
  and s.determinism.seed_locked = true
  and s.score.passed = s.score.total
```

## Boundary Conditions

- Missing conformance manifest denies.
- Missing ruleset denies.
- Missing notebook or scorecard denies.
- Missing required workflow job denies.
- Required check soft failure denies.
