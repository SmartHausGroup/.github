# Deploying the docs site (docs.smarthaus.ai)

The docs site is built with **Docusaurus** from this repo and is intended to be hosted on **Vercel** at **docs.smarthaus.ai**.

## How it works

- **Source:** This repo (SmartHausGroup.github). Markdown lives in the repo root (READMEs, thesis, RFS, MA, archetypes).
- **Build:** The `website/` directory contains a Docusaurus app. Before each build, `scripts/copy-docs.js` copies that markdown into `website/docs/`. Docusaurus then builds a static site.
- **Host:** Vercel. Connect this repo, set the root to `website/`, and add the custom domain `docs.smarthaus.ai`.

## Vercel setup (one-time)

1. **Connect the repo**
   - In [Vercel](https://vercel.com), add a new project.
   - Import **SmartHausGroup/SmartHausGroup.github** (same GitHub org as the main site).

2. **Configure the project**
   - **Root Directory:** `website`  
     (so Vercel runs `npm ci` and `npm run build` inside `website/`).
   - **Framework Preset:** Other (or leave auto; we use a custom build).
   - **Build Command:** `npm run build` (default; runs copy script + Docusaurus build).
   - **Output Directory:** `build` (default for Docusaurus).
   - **Install Command:** `npm ci` (recommended).

3. **Custom domain**
   - In the project → Settings → Domains, add **docs.smarthaus.ai**.
   - Add the CNAME (or A record) Vercel shows in your DNS (e.g. at your registrar or Cloudflare).

4. **Deploy**
   - Push to the branch Vercel is watching (e.g. `main`). Each push deploys. Each PR gets a preview URL.

## Local development

```bash
cd website
npm install
npm run build   # copies docs then builds (no watch)
npm start       # dev server; re-run copy-docs.js manually if you change repo-root markdown
```

To refresh copied docs during dev: `node scripts/copy-docs.js` from `website/`.

## Linking from the main website

Point “Documentation”, “Read the docs”, and any “dive deeper” links from [smarthaus.ai](https://www.smarthaus.ai) to **https://docs.smarthaus.ai**.
