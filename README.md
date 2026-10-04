# SMARTHAUS on GitHub

This repository is the public GitHub front door for SMARTHAUS, The SmartHaus Group. It contains the organization profile, product map, shared community templates, and security reporting guidance.

## Find your starting point

| Resource | Purpose |
|---|---|
| [Organization profile](profile/README.md) | Company and architecture introduction displayed on the [organization landing page](https://github.com/SmartHausGroup). |
| [Product map](products/README.md) | What each component does and its current development stage. |
| [Security policy](SECURITY.md) | How to report vulnerabilities privately. |
| [Community templates](.github/) | Shared issue and pull request templates and contribution expectations. |
| [SMARTHAUS website](https://smarthaus.ai) | Current company and product positioning. |
| [Investor overview](https://investor.smarthaus.ai) | Investment context and development stages. |

GitHub displays `profile/README.md` on the organization landing page. This README explains the repository itself.

## Product source and evidence

Product code, installation guidance, and release records belong to their owning repositories. Many are private. This public repository introduces the work; access to private source and diligence materials is arranged separately.

Public descriptions distinguish a component's purpose from its implementation, release, deployment, and customer acceptance. These are separate milestones. Published copy should identify the scope of a guarantee and have current evidence for any release or readiness claim.

## Contributing and reporting

Use the issue and pull request templates for public documentation feedback. Keep credentials, customer information, private logs, and internal operating details out of public submissions. Report vulnerabilities through the [security policy](SECURITY.md).

SMARTHAUS CI and the scripts in this repository check this public documentation surface. They do not establish product certification or runtime readiness.

## Maintainer checks

`make validate` runs the local public-profile governance audit. It checks required public files, stale claims, and separation from internal material. Live GitHub settings checks require the approved SMARTHAUS Automation path; local checks do not verify remote protections.

Contact: [phil@smarthausgroup.com](mailto:phil@smarthausgroup.com)

© SMARTHAUS
