.DEFAULT_GOAL := help

include Makefile.ai

.PHONY: help validate agents-sync agents-check github-settings-audit github-settings-audit-live

help:
	@echo "SMARTHAUS .github governance targets"
	@echo "  validate              Run the full repo CI/CD conformance gate"
	@echo "  repo-cicd-conformance Verify repo CI/CD controls"
	@echo "  github-settings-audit Run local GitHub governance audit"
	@echo "  github-settings-audit-live Run local + live GitHub governance audit"
	@echo "  ai-evidence-pack      Build deterministic evidence pack"
	@echo "  ai-pack-verify        Verify deterministic evidence pack"

validate: ai-validate-full

agents-sync:
	@node tools/agents/sync-agent-files.mjs

agents-check:
	@node tools/agents/sync-agent-files.mjs --check

github-settings-audit:
	@$(CICD_PY) scripts/ci/audit_org_profile_repo.py --local

github-settings-audit-live:
	@GH_TOKEN="$${GH_TOKEN:-$$(gh auth token)}" $(CICD_PY) scripts/ci/audit_org_profile_repo.py --local --live --require-live --repo SmartHausGroup/.github
