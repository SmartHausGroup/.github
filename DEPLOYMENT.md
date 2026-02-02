# Deploying the docs site (docs.smarthaus.ai)

The docs site is built with **Docusaurus** from this repo and is intended to be hosted on **Vercel** at **docs.smarthaus.ai**.

## How it works

- **Source:** This repo (SmartHausGroup/.github). Markdown lives in the repo root (READMEs, thesis, RFS, MA, archetypes).
- **Build:** Docusaurus app is at repo root. Before each build, `scripts/copy-docs.js` copies that markdown into `docs/`. Docusaurus then builds a static site.
- **Host:** Vercel. Connect this repo, leave **Root Directory** as `./` (default), and add the custom domain `docs.smarthaus.ai`.

## Vercel setup (one-time)

1. **Connect the repo**
   - In [Vercel](https://vercel.com), add a new project.
   - Import **SmartHausGroup/.github**.

2. **Configure the project**
   - **Root Directory:** leave as `./` (repo root).
   - **Framework Preset:** Other (or leave auto; we use a custom build).
   - **Build Command:** `npm run build` (default; runs copy script + Docusaurus build).
   - **Output Directory:** `build` (default for Docusaurus).
   - **Install Command:** `npm ci` (recommended).

3. **Custom domain**
   - **Via CLI** (from repo root, after linking):
     ```bash
     vercel link -p github -S smarthausgroup -y   # if not already linked
     vercel domains add docs.smarthaus.ai
     ```
   - **Via dashboard:** Project → Settings → Domains → Add **docs.smarthaus.ai**.
   - If the apex **smarthaus.ai** is not on Vercel DNS, add the CNAME (or A record) Vercel shows for **docs** at your DNS provider. (If you use Vercel DNS for smarthaus.ai, the subdomain is configured automatically.)

4. **Deploy**
   - Push to the branch Vercel is watching (e.g. `main`). Each push deploys. Each PR gets a preview URL.

## Local development

```bash
npm install
npm run build   # copies docs then builds (no watch)
npm start       # dev server; re-run copy-docs.js manually if you change repo-root markdown
```

To refresh copied docs during dev: `node scripts/copy-docs.js` from repo root.

## Linking from the main website

Point "Documentation", "Read the docs", and any "dive deeper" links from [smarthaus.ai](https://www.smarthaus.ai) to **https://docs.smarthaus.ai**.
