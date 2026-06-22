.DEFAULT_GOAL := help

include Makefile.ai

.PHONY: help validate agents-sync agents-check

help:
	@echo "SMARTHAUS .github governance targets"
	@echo "  validate              Run the full repo CI/CD conformance gate"
	@echo "  repo-cicd-conformance Verify repo CI/CD controls"
	@echo "  ai-evidence-pack      Build deterministic evidence pack"
	@echo "  ai-pack-verify        Verify deterministic evidence pack"

validate: ai-validate-full

agents-sync:
	@node tools/agents/sync-agent-files.mjs

agents-check:
	@node tools/agents/sync-agent-files.mjs --check
