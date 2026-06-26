# benjaminhavey.com — Project Notes

V1 complete and deployed. This note captures the conventions and gotchas so any
future session has the operational detail.

## Stack & deploy
- Astro v6, dark-navy + gold design system, Fraunces + Inter fonts.
- Source on GitHub (repo: bha-site) → Cloudflare Pages auto-build on push.
- Build config in Cloudflare: build command `npm run build`, output dir `dist`.
- Deploy = replace local src/public (or edit in repo), then: git add -A,
  git commit, git push. Cloudflare rebuilds in ~1 min.

## Structure
- src/layouts/Base.astro — shared shell: nav, footer, fonts, JSON-LD Person
  schema, scroll-reveal script, global.css import. All pages wrap in this.
- src/pages/index.astro — homepage (Latest Articles module, Areas of Focus,
  Advisory, Corporate Heritage, Recognition & patents, Contact).
- src/pages/articles/ — index.astro (listing) + [slug].astro (article template
  with optional hero image + series prev/next nav).
- src/content/articles/*.md — one Markdown file per article.
- src/content.config.ts — defines article frontmatter schema.
- public/images/*.webp — article graphics (coded SVG → WebP, gold-on-navy).
- public/robots.txt, public/llms.txt — open policy, all AI crawlers welcomed.
- astro.config.mjs (project root, NOT in this zip) — has site URL + sitemap.

## Article frontmatter fields
title, date, summary, hero, heroAlt, series, seriesSlug, seriesPart, draft

To add an article: drop a .md in src/content/articles/, set frontmatter,
add any hero image to public/images/. For a series, set matching seriesSlug
and incrementing seriesPart — prev/next links wire up automatically.

## Graphics style
Coded SVG rasterized to 2x retina WebP. Dark navy (#0d1320) background, gold
accents (#c9a86a / #e0c488), monospace labels, bordered panels, corner ticks,
benjaminhavey.com footer. Keep new article graphics in this language.

## Hard-won gotchas
- RESTART `npm run dev` after adding a new article or editing content.config.ts
  or astro.config.mjs — the dev server won't pick them up otherwise. (Editing
  an existing article's body hot-reloads fine.)
- VERIFY all stats, patent numbers, and factual claims against primary sources
  before publishing. Several AI-generated drafts had fabricated/mismatched
  figures. Patent numbers from LinkedIn exports mix publication vs grant numbers
  — confirm against Google Patents / USPTO.
- Cloudflare build config must be SAVED before the first Git deploy or it
  "skips the build step" and uploads raw source.
- llms.txt is low-value right now (crawlers mostly ignore it); robots.txt is the
  file that actually works for AI crawler access.

## Open items / next phase
- Wire up the contact form handler (currently static; mailto works, form fields
  are decorative). First real dynamic/serverless piece.
- Part 2 of the "State of the Union in AI" series (image generation market).
  When added with matching seriesSlug, the LLM Wars prev/next links activate.
- Possible headless-CMS exploration (Astro + Sanity/Contentful).
- Optional: turn off Cloudflare Scrape Shield email obfuscation if the live
  contact email shows as [email protected].
