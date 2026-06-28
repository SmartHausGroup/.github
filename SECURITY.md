# Security Policy

Security reports must not be filed as public GitHub issues.

## Reporting A Vulnerability

Use the most private channel available:

1. GitHub private vulnerability reporting, if it is enabled on the affected
   repository.
2. Email `phil@smarthausgroup.com` with `SECURITY` in the subject line.

Do not include exploit code, credentials, customer data, private logs, or secret
values in public issues, pull requests, discussions, or comments.

## What To Include

When reporting privately, include:

- affected repository and component;
- affected version, branch, tag, or commit if known;
- reproduction steps;
- expected and observed behavior;
- impact assessment;
- whether any secret, token, customer data, or private system was exposed;
- suggested mitigation, if known.

## Response Model

SMARTHAUS will triage security reports using the affected repository's current
maintainer and owner path. Public acknowledgements, advisories, patch timelines,
and researcher credit are handled case by case.

No public repository copy should promise a certification, response SLA, bug
bounty, compliance status, cryptographic property, or production guarantee unless
that claim is backed by current approved evidence.

## Security Expectations For SMARTHAUS Repositories

SMARTHAUS repositories should use the narrowest practical credential scope and
fail closed when required security evidence is missing.

Baseline expectations:

- no committed secrets;
- no broad personal access tokens for routine automation;
- pinned or approved GitHub Actions;
- read-only default workflow token where practical;
- secret scanning through GitHub features or fallback scanners;
- protected branches and protected release tags for production-bound artifacts;
- environment-scoped production secrets with approval where available;
- signed release evidence where a repository ships artifacts.

Product-specific security requirements live with the owning product repository
and approved internal standards.

## Public Issue Policy

If a public issue appears to contain a vulnerability, exploit, token, key, or
private data, maintainers should remove the sensitive material from public view
where GitHub allows it and move the report to a private channel.
