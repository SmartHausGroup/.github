# SmartHausGroup/.github Repo CI/CD Conformance - Phase 2 Calculus

## Predicates

```text
ManifestValid_R(m) =
  m.schema_version = 0.1.0
  and m.repository.name = .github
  and m.profile.primary = org-profile-governance
```

```text
BranchRulesProtected_R(b) =
  protected branch set includes main and the standard branch names
  and direct mutation blocked by strict required status checks
  and force_push blocked
  and deletion blocked
  and signed commits required
  and linear history required
  and bypass_actors = []
```

```text
NoHumanDeadlock_R(b) =
  pull_request rule absent
  and required_approvals = 0 in repo manifest
  and requires_codeowners = false in repo manifest
  and requires_conversation_resolution = false in repo manifest
```

```text
RequiredChecksGreen_R(q, c) =
  q.repo-cicd-conformance.sha = c
  and q.repo-cicd-conformance.status = success
  and q.evidence-pack.sha = c
  and q.evidence-pack.status = success
  and q.verify.status = success
  and q.validate.status = success
  and q.secret-scan.status = success
  and q.zizmor.status = success
  and q.supply-chain-policy.status = success
  and q.sbom-vulnerability-budget.status = success
  and q.trufflehog.status = success
  and q.semgrep.status = success
  and q.ossf-scorecard.status = success
  and q.org-governance-audit.status = success
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
- Reintroduced human-review quorum, CODEOWNERS, or last-push approval denies.
