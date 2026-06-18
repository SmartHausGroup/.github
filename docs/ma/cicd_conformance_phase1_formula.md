# SmartHausGroup.github Repo CI/CD Conformance - Phase 1 Formula

Let:

- `R` be `SmartHausGroup.github`.
- `c` be the commit under evaluation.
- `t` be the git tree hash.
- `m` be `configs/ucp/repo_cicd.yaml`.
- `b` be `.github/rulesets/protected-branches.json`.
- `q` be required CI check results.
- `e` be the CI/CD MA evidence set.
- `s` be `artifacts/scorecards/cicd_conformance.json`.

```text
RepoAdmissible_R(c) =
  ManifestValid_R(m)
  and BranchRulesProtected_R(b)
  and RequiredChecksGreen_R(q, c)
  and MAEvidenceTraceable_R(e)
  and ScorecardGreen_R(s)
```

Any unknown, missing, stale, or non-green predicate denies admission.
