# SmartHausGroup/.github

This is the public GitHub front door for `SmartHausGroup`.

It exists for public-safe organization profile copy, default contribution
templates, security reporting guidance, and lightweight health checks for this
public repository.

## What Belongs Here

| Area | Path | Purpose |
|---|---|---|
| Organization profile | `profile/README.md` | Public copy shown on the SmartHausGroup GitHub organization page. |
| Public product index | `products/README.md` | Concise product map with evidence-bounded status language. |
| Community defaults | `.github/` | Default issue templates, pull request template, security policy, and ownership hints. |
| Public-repo checks | `.github/workflows/`, `scripts/ci/` | Checks that this public repo remains safe, current, and free of obvious secrets. |

## What Does Not Belong Here

This repository is not the place for internal operating manuals, private
roadmaps, enterprise settings runbooks, agent workforce instructions, detailed
security implementation notes, internal collaboration-system detail, or product
release machinery.

Detailed source of truth lives in the owning product repositories and internal
systems. This public repository should point people in the right direction
without exposing internal process.

## Public Copy Rules

- Keep the content external-safe.
- Do not publish secrets, customer data, private logs, unreleased plans, or
  internal operating instructions.
- Do not make product maturity, release, compliance, certification, or security
  claims unless the owning product repository has current evidence.
- Prefer plain product descriptions over architecture internals.
- Use transitional aliases carefully when names are still being reconciled.

## Local Checks

```bash
make validate
make github-settings-audit
make github-settings-audit-live
```

GitHub-native Secret Protection requires enterprise approval. Until that is
approved, this public repo uses required CI scanners for secret scanning.
