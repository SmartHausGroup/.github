# Rule-to-Constraint Prompt Template

## Purpose

Use this template with any AI agent to convert natural-language governance rules into valid constraint YAML for the MCP constraint algebra.

## Copy/Paste Prompt

```text
You are converting natural-language governance rules into deterministic MCP constraint YAML.

Output requirements:
1. Return valid YAML only.
2. Use this file shape:
   - top-level `version: "1.0"`
   - top-level `constraints:` list
3. Every constraint entry must include:
   - id
   - name
   - description
   - severity (error|warning|info)
   - filter.action_types
   - filter.scopes
   - predicate
4. Allowed action_types:
   file_edit, commit, push, deploy, test_run, command_exec, config_change, governance_edit
5. Allowed scopes:
   code, config, docs, governance, infrastructure, math, test
6. Allowed predicate types (EXACT list):
   field_required, min_phase, scorecard_green, branch_allowed,
   tier_minimum, notebook_backing, compound_all, compound_any
7. Do not invent predicate types.
8. Keep constraints deterministic and fail-closed.

Natural-language rules to convert:
{{RULE_TEXT}}
```

## Input format

Provide one or more rules in plain English. Include:

- The action being governed (commit, push, deploy, etc.)
- The scope (code, config, docs, governance, etc.)
- The required condition
- Desired severity (`error`, `warning`, `info`)

## Output format

Return valid YAML using this structure:

```yaml
version: "1.0"
constraints:
  - id: "example-id"
    name: "Example name"
    description: "What this enforces"
    severity: "error"
    filter:
      action_types: [commit]
      scopes: [code]
    predicate:
      type: "field_required"
      field: "plan_ref"
```

## Predicate selection decision tree

- Rule says "must include field X": use `field_required`
- Rule says "must be phase N or higher": use `min_phase`
- Rule says "must have green scorecard": use `scorecard_green`
- Rule says "only on branch set": use `branch_allowed`
- Rule says "requires tier X or higher": use `tier_minimum`
- Rule says "must have notebook evidence": use `notebook_backing`
- Rule says "all conditions must hold": use `compound_all`
- Rule says "any one condition is acceptable": use `compound_any`

## Worked examples

### Example 1

Natural-language rule:

"All commits in code scope must include a plan reference."

YAML:

```yaml
version: "1.0"
constraints:
  - id: "ex-commit-plan-ref"
    name: "Commit requires plan reference"
    description: "Commits must include a plan_ref for traceability."
    severity: "error"
    filter:
      action_types: [commit]
      scopes: [code]
    predicate:
      type: "field_required"
      field: "plan_ref"
```

### Example 2

Natural-language rule:

"Only enterprise tier can deploy infrastructure changes."

YAML:

```yaml
version: "1.0"
constraints:
  - id: "ex-deploy-enterprise-tier"
    name: "Deploy requires enterprise tier"
    description: "Infrastructure deploy actions require enterprise tier."
    severity: "error"
    filter:
      action_types: [deploy]
      scopes: [infrastructure]
    predicate:
      type: "tier_minimum"
      tier: "enterprise"
```

### Example 3

Natural-language rule:

"Push is allowed only when scorecard is green and branch is development or main."

YAML:

```yaml
version: "1.0"
constraints:
  - id: "ex-push-green-and-branch"
    name: "Push requires green scorecard and approved branch"
    description: "Push needs green scorecard plus development/main branch type."
    severity: "error"
    filter:
      action_types: [push]
      scopes: [infrastructure, code, config, docs]
    predicate:
      type: "compound_all"
      predicates:
        - type: "scorecard_green"
        - type: "branch_allowed"
          branches: [development, main]
```

## Validation checklist

- [ ] YAML parses successfully
- [ ] Top-level `version` and `constraints` are present
- [ ] Each constraint has `id`, `name`, `description`, `severity`, `filter`, `predicate`
- [ ] `severity` is one of `error`, `warning`, `info`
- [ ] `filter.action_types` values are from the allowed list
- [ ] `filter.scopes` values are from the allowed list
- [ ] `predicate.type` is one of the 8 allowed predicate types
- [ ] Predicate parameters match predicate type
- [ ] No invented fields that change predicate semantics

## Schema reference

Validate generated YAML against:

- `SMARTHAUS_MCPSERVER_core/configs/constraints/CONSTRAINT_SCHEMA.yaml`
- Runtime loader: `SMARTHAUS_MCPSERVER_core/src/smarthaus_mcp/constraints/registry.py`
