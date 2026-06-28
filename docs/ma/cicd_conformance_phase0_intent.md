# SmartHausGroup/.github Repo CI/CD Conformance - Phase 0 Intent

Status: approved adoption
Date: 2026-06-22

## What are we building?

A repo-local adoption of the SMARTHAUS Repo CI/CD Conformance Standard for `SmartHausGroup/.github`.

## Why are we building it?

Every SMARTHAUS repository needs the same CI/CD control plane: branch protection, fail-closed required checks, UCP-readable manifests, deterministic toolchain locks, MA evidence, notebooks, and scorecards.

## Problem

Repository CI/CD surfaces were inconsistent. Some repos had no workflows, some had workflow-only checks without UCP manifests, and this org profile repo was active but not yet tagged into the conformant ruleset.

## Boundaries

In scope: repository CI/CD governance, branch protection evidence, UCP source and toolchain locks, standard Make targets, MA conformance evidence, and scorecard admission.

Out of scope: product feature behavior, cloud deployment, and new application runtime features.

## Required Guarantees

- Required CI runs on PRs and protected branch pushes.
- Protected branches block direct mutation through signed commits, linear history, no deletion, no force push, strict required mechanical contexts, and zero bypass actors.
- Human-review quorum, CODEOWNERS review, and last-push approval are not required for this solo-operator conformance mode.
- Required gates fail closed.
- CI/CD evidence binds to standards commit `d76daeb86432b00826fa7b02613dedae0ab24ad3`.
- UCP can read one deterministic manifest and scorecard for this repository.

## Success Criteria

- `make repo-cicd-conformance` passes.
- `make ai-pack-verify` passes.
- `.github/workflows/repo-cicd-conformance.yml` exposes `repo-cicd-conformance` and `evidence-pack` jobs.
- Branch ruleset required status contexts include `verify`, `validate`, `secret-scan`, `zizmor`, `supply-chain-policy`, `sbom-vulnerability-budget`, `trufflehog`, `semgrep`, `ossf-scorecard`, and `org-governance-audit`.
- `artifacts/scorecards/cicd_conformance.json` is green.

## Determinism Definition

The same checked-in tree, standard commit, lock files, branch ruleset, MA evidence paths, and scorecard produce the same conformance decision.
