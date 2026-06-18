#!/usr/bin/env python3
"""Build deterministic repo CI/CD evidence for UCP admission."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'artifacts/cicd/repo_cicd_evidence.json'


def sha(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main() -> int:
    tree = subprocess.run(['git', 'write-tree'], cwd=ROOT, text=True, stdout=subprocess.PIPE, check=True).stdout.strip()
    manifest_text = (ROOT / 'configs/ucp/repo_cicd.yaml').read_text(encoding='utf-8')
    repo_name = 'unknown'
    for line in manifest_text.splitlines():
        if line.strip().startswith('name:'):
            repo_name = line.split(':', 1)[1].strip()
            break
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        'schema_version': '0.1.0',
        'standard': 'repo-cicd-conformance',
        'repo': repo_name,
        'tree': tree,
        'manifest_sha256': sha('configs/ucp/repo_cicd.yaml'),
        'notebook_sha256': sha('notebooks/ma/cicd_conformance.ipynb'),
        'scorecard_sha256': sha('artifacts/scorecards/cicd_conformance.json'),
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'wrote {OUT.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
