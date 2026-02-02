#!/usr/bin/env node
/**
 * Copies markdown from repo root into docs/ so Docusaurus can serve it.
 * Run before docusaurus build. Source of truth remains in repo root.
 */

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.join(__dirname, '..');
const DOCS_OUT = path.join(__dirname, '..', 'docs');

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function copyFile(src, dest) {
  ensureDir(path.dirname(dest));
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, dest);
    console.log('  ', path.relative(REPO_ROOT, src), '->', path.relative(DOCS_OUT, dest));
  }
}

ensureDir(DOCS_OUT);

// Thesis
copyFile(
  path.join(REPO_ROOT, 'thesis', 'MATH_THESIS_v5.md'),
  path.join(DOCS_OUT, 'thesis', 'framework.md')
);

// RFS
copyFile(
  path.join(REPO_ROOT, 'resonant-field-storage', 'README.md'),
  path.join(DOCS_OUT, 'rfs', 'overview.md')
);
copyFile(
  path.join(REPO_ROOT, 'resonant-field-storage', 'RFS: From Vector Space to Field Theory—A New Mathematical Foundation for Memory.md'),
  path.join(DOCS_OUT, 'rfs', 'field-theory.md')
);
copyFile(
  path.join(REPO_ROOT, 'resonant-field-storage', 'use-cases', 'README.md'),
  path.join(DOCS_OUT, 'rfs', 'use-cases', 'overview.md')
);
copyFile(path.join(REPO_ROOT, 'resonant-field-storage', 'use-cases', '01_incident_memory_oncall', 'README.md'), path.join(DOCS_OUT, 'rfs', 'use-cases', 'incident-memory.md'));
copyFile(path.join(REPO_ROOT, 'resonant-field-storage', 'use-cases', '02_rag_with_proofs', 'README.md'), path.join(DOCS_OUT, 'rfs', 'use-cases', 'rag-proofs.md'));
copyFile(path.join(REPO_ROOT, 'resonant-field-storage', 'use-cases', '03_code_intelligence', 'README.md'), path.join(DOCS_OUT, 'rfs', 'use-cases', 'code-intelligence.md'));
copyFile(path.join(REPO_ROOT, 'resonant-field-storage', 'use-cases', '04_compliance_legal_archive', 'README.md'), path.join(DOCS_OUT, 'rfs', 'use-cases', 'compliance-legal.md'));
copyFile(path.join(REPO_ROOT, 'resonant-field-storage', 'use-cases', '05_research_knowledge_graph', 'README.md'), path.join(DOCS_OUT, 'rfs', 'use-cases', 'research-knowledge.md'));
copyFile(path.join(REPO_ROOT, 'resonant-field-storage', 'use-cases', '06_pharmaceutical_discovery', 'README.md'), path.join(DOCS_OUT, 'rfs', 'use-cases', 'pharmaceutical.md'));

// Mathematical Autopsy
copyFile(
  path.join(REPO_ROOT, 'mathematical-autopsy', 'README.md'),
  path.join(DOCS_OUT, 'mathematical-autopsy', 'overview.md')
);

// Archetypes
copyFile(path.join(REPO_ROOT, 'archetypes', 'tai', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'tai.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'aiva', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'aiva.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'mge', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'mge.md'));

// About (profile README)
copyFile(
  path.join(REPO_ROOT, 'profile', 'README.md'),
  path.join(DOCS_OUT, 'about.md')
);

console.log('copy-docs.js: done.');
