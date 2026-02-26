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
// TAI sub-services
copyFile(path.join(REPO_ROOT, 'archetypes', 'tai', 'nme', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'tai', 'nme.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'tai', 'vfe', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'tai', 'vfe.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'tai', 'vee', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'tai', 'vee.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'tai', 'caio', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'tai', 'caio.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'tai', 'maia', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'tai', 'maia.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'aiva', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'aiva.md'));
copyFile(path.join(REPO_ROOT, 'archetypes', 'mge', 'README.md'), path.join(DOCS_OUT, 'archetypes', 'mge.md'));

// Advisory
copyFile(path.join(REPO_ROOT, 'advisory', 'README.md'), path.join(DOCS_OUT, 'advisory', 'README.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'overview.md'), path.join(DOCS_OUT, 'advisory', 'overview.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'methodology.md'), path.join(DOCS_OUT, 'advisory', 'methodology.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'guarantees.md'), path.join(DOCS_OUT, 'advisory', 'guarantees.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'self-service.md'), path.join(DOCS_OUT, 'advisory', 'self-service.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'services', 'express-assessment.md'), path.join(DOCS_OUT, 'advisory', 'services', 'express-assessment.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'services', 'readiness-assessment.md'), path.join(DOCS_OUT, 'advisory', 'services', 'readiness-assessment.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'services', 'strategy-roadmap.md'), path.join(DOCS_OUT, 'advisory', 'services', 'strategy-roadmap.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'services', 'pilot-implementation.md'), path.join(DOCS_OUT, 'advisory', 'services', 'pilot-implementation.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'services', 'advisor-retainer.md'), path.join(DOCS_OUT, 'advisory', 'services', 'advisor-retainer.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'verticals', 'healthcare.md'), path.join(DOCS_OUT, 'advisory', 'verticals', 'healthcare.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'verticals', 'professional-services.md'), path.join(DOCS_OUT, 'advisory', 'verticals', 'professional-services.md'));
copyFile(path.join(REPO_ROOT, 'advisory', 'verticals', 'property-real-estate.md'), path.join(DOCS_OUT, 'advisory', 'verticals', 'property-real-estate.md'));

// About (profile README)
copyFile(
  path.join(REPO_ROOT, 'profile', 'README.md'),
  path.join(DOCS_OUT, 'about.md')
);

// Vision
copyFile(
  path.join(REPO_ROOT, 'SMARTHAUS_VISION.md'),
  path.join(DOCS_OUT, 'vision.md')
);

console.log('copy-docs.js: done.');
