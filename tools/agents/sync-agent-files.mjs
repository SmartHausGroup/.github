#!/usr/bin/env node
// sync-agent-files.mjs — one canonical AGENTS.md, N verified+safe binds.
// Default mode: regenerate every bound file from AGENTS.md and write .agents/manifest.json.
// --check mode (CI gate): recompute each bind FROM canonical, fail on drift, run the
//   injection content-safety lint, and assert no higher-precedence shadow file exists.
// No symlinks are used (a Windows symlink checks out as a plaintext file whose body is the
//   literal string "AGENTS.md", which the agent then ingests as its entire instruction set).
import { readFileSync, writeFileSync, existsSync, readdirSync, statSync, mkdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { dirname, join, relative } from 'node:path';

const ROOT = process.cwd();
const CANON = 'AGENTS.md';
const CHECK = process.argv.includes('--check');

const sha256 = (s) => createHash('sha256').update(s).digest('hex');
const banner = (h) => `<!-- GENERATED FROM AGENTS.md @ ${h} — DO NOT EDIT. Edit AGENTS.md then run \`make agents-sync\`. -->\n\n`;

if (!existsSync(CANON)) { console.error('FATAL: canonical AGENTS.md missing'); process.exit(2); }
const canonical = readFileSync(CANON, 'utf8');
const HASH = sha256(canonical);

// REAL generated copies (cannot import / degrade unsafely under symlink).
const COPIES = [
  'GEMINI.md',
  '.github/copilot-instructions.md',
  '.junie/guidelines.md',
  '.amazonq/rules/agents.md',
  '.continue/rules/00-agents.md',
];
// Import-stub binds: file must reference canonical, never duplicate it.
const STUBS = [{ path: 'CLAUDE.md', mustContain: '@AGENTS.md' }];

const errors = [];
const writes = [];

function ensure(path, content) {
  const abs = join(ROOT, path);
  mkdirSync(dirname(abs), { recursive: true });
  const want = banner(HASH) + canonical;
  if (CHECK) {
    if (!existsSync(abs) || readFileSync(abs, 'utf8') !== want) errors.push(`drift: ${path} (run \`make agents-sync\`)`);
  } else {
    writeFileSync(abs, want);
    writes.push(path);
  }
}

// 1. Generated copies
for (const p of COPIES) ensure(p, canonical);

// 2. Import stubs — verify only (never overwrite a human-authored addendum)
for (const s of STUBS) {
  if (!existsSync(s.path) || !readFileSync(s.path, 'utf8').includes(s.mustContain))
    errors.push(`stub ${s.path} must reference ${s.mustContain}`);
}

// 3. Copilot OFF-by-default ingestion keys (must be committed)
const VS = '.vscode/settings.json';
const needKeys = { 'chat.useAgentsMdFile': true, 'chat.useNestedAgentsMdFiles': true };
{
  let cur = {};
  if (existsSync(VS)) { try { cur = JSON.parse(readFileSync(VS, 'utf8')); } catch {} }
  const merged = { ...cur, ...needKeys };
  if (CHECK) {
    for (const [k, v] of Object.entries(needKeys))
      if (cur[k] !== v) errors.push(`${VS}: missing ${k}=${v} (Copilot AGENTS.md ingestion is OFF by default)`);
  } else { mkdirSync('.vscode', { recursive: true }); writeFileSync(VS, JSON.stringify(merged, null, 2) + '\n'); writes.push(VS); }
}

// 4. CONTENT-SAFETY LINT (P0): the canonical root is authored + review/branch-protection gated, so it
//    gets only HARD patterns (phrases never legitimate even in our own text); NESTED / vendored
//    AGENTS.md are untrusted (planted by a dependency or a stray nested file) and get the full scan.
const HARD = [
  /ignore\s+(all\s+|your\s+)?previous\s+instructions/i,
  /disregard\s+(the\s+)?(above|prior|previous)\s+(instructions|rules|prompt)/i,
  /conceal\s+your\s+actions|hide\s+this\s+from\s+the\s+user/i,
  /[​-‍⁠﻿]/, // hidden / zero-width unicode
];
const NESTED_ONLY = [/exfiltrat/i, /send\s+[^\n]*secret/i, /leak\s+[^\n]*token/i, /curl[^\n]*\|\s*(sh|bash)/i];
const SKIP = new Set(['node_modules', 'vendor', '.git', '.venv', 'dist', 'build']);
function walk(dir, out = []) {
  for (const name of readdirSync(dir)) {
    if (SKIP.has(name)) continue;
    const p = join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) walk(p, out);
    else if (name === 'AGENTS.md') out.push(p);
  }
  return out;
}
const canonAbs = join(ROOT, CANON);
for (const f of walk(ROOT)) {
  const rel = relative(ROOT, f);
  const body = readFileSync(f, 'utf8');
  const pats = f === canonAbs ? HARD : [...HARD, ...NESTED_ONLY];
  for (const re of pats) if (re.test(body)) errors.push(`injection-lint: ${rel} matches ${re}`);
}
// vendored agent files that could be auto-ingested
for (const v of ['node_modules', 'vendor']) {
  const p = join(ROOT, v);
  if (existsSync(p)) for (const f of walk(p)) errors.push(`unsafe: auto-ingestible AGENTS.md under ${v}/: ${relative(ROOT, f)}`);
}
// 5. Shadow-file assertion (Zed first-match etc.) — legacy interop files must not outrank canonical.
for (const shadow of ['.cursorrules', '.windsurfrules', '.rules', '.clinerules', 'AGENT.md'])
  if (existsSync(join(ROOT, shadow)) && statSync(join(ROOT, shadow)).isFile())
    errors.push(`shadow: ${shadow} can silently override AGENTS.md (remove or make a verified bind)`);

// 6. Manifest = the agent-file slice of the repo FILE_INDEX
const manifest = {
  canonical: CANON,
  canonical_sha256: HASH,
  policy: 'one canonical AGENTS.md; every other file is a verified, content-safe bind. No symlinks.',
  binds: [
    { path: 'CLAUDE.md', tool: 'Claude Code', role: 'import-stub' },
    ...COPIES.map((p) => ({ path: p, tool: 'copilot/gemini/junie/amazonq/continue', role: 'generated', sha256: HASH })),
    { path: VS, tool: 'GitHub Copilot (VS Code)', role: 'config' },
    { path: '.aider.conf.yml', tool: 'Aider', role: 'config-directive' },
  ],
  caveat: 'User-global layers (~/.config/zed/AGENTS.md, ~/.agents/AGENTS.md, personal tool settings) outrank the repo and are NOT visible to this gate.',
};
if (!CHECK) { mkdirSync('.agents', { recursive: true }); writeFileSync('.agents/manifest.json', JSON.stringify(manifest, null, 2) + '\n'); }

if (errors.length) { console.error('AGENT-FILE GATE FAILED:\n' + errors.map((e) => '  - ' + e).join('\n')); process.exit(1); }
console.log(CHECK ? `OK: ${COPIES.length + STUBS.length} binds verified, no injection, no shadow (canonical ${HASH.slice(0, 12)})`
                  : `synced ${writes.length} files from AGENTS.md @ ${HASH.slice(0, 12)}`);
