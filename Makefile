.DEFAULT_GOAL := help

PY ?= python3

.PHONY: help validate github-settings-audit github-settings-audit-live

help:
	@echo "SMARTHAUS public .github targets"
	@echo "  validate              Run local public-profile governance audit"
	@echo "  github-settings-audit Run local GitHub governance audit"
	@echo "  github-settings-audit-live Run local + live GitHub governance audit"

validate: github-settings-audit

github-settings-audit:
	@$(PY) scripts/ci/audit_org_profile_repo.py --local

github-settings-audit-live:
	@echo "Use SMARTHAUS Automation App reads for live repository settings; no personal GitHub auth."
	@exit 2
