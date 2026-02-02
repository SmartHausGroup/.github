# SMARTHAUS Docs site (Docusaurus)

This directory contains the **docs site** for [docs.smarthaus.ai](https://docs.smarthaus.ai). It is built from the markdown in this repo (READMEs, thesis, RFS, MA, archetypes).

## Build

- **Copy:** `node scripts/copy-docs.js` copies markdown from the repo root into `docs/`.
- **Build:** `npm run build` runs the copy step then `docusaurus build`. Output is in `build/`.

## Deploy (Vercel)

1. In Vercel, add a project for **SmartHausGroup/SmartHausGroup.github**.
2. Set **Root Directory** to `website`.
3. Build command: `npm run build`. Output: `build`.
4. Add custom domain **docs.smarthaus.ai**.

See [DEPLOYMENT.md](../DEPLOYMENT.md) in the repo root for full steps.

## Local dev

```bash
npm install
npm run build   # copy + build
npm start       # dev server at http://localhost:3000
```

Note: Changing markdown in the repo root does not hot-reload; re-run `node scripts/copy-docs.js` then refresh.
