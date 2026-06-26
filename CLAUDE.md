# benjaminhavey.com — Claude Code Context

## Stack & deploy
- **Astro v6** static site, dark-navy + gold design system, Fraunces + Inter fonts
- **GitHub repo:** `bha-site` → **Cloudflare Pages** auto-builds on push
- **Build command:** `npm run build` · **Output dir:** `dist`
- **Dev server:** `npm run dev` → http://localhost:4321
- **Deploy flow:** edit files → `git add -A` → `git commit` → `git push` → Cloudflare rebuilds in ~1 min

## File structure
```
src/
  layouts/Base.astro          # Shared shell: nav, footer, fonts, JSON-LD Person schema, scroll-reveal
  pages/
    index.astro               # Homepage
    articles/
      index.astro             # Article listing
      [slug].astro            # Article template — hero image + series prev/next nav + Article schema
  content/
    articles/*.md             # One Markdown file per article
  content.config.ts           # Frontmatter schema
  styles/global.css           # All styles
public/
  images/*.webp               # Article hero + landscape graphics
  robots.txt                  # Open crawler policy
  llms.txt                    # AI crawler guidance
```

## Homepage sections (in order)
1. Hero — `bg`
2. Latest Articles — `bg-2` (auto-pulls 3 newest non-draft articles)
3. Areas of Focus — `bg`
4. Current Portfolio — `bg-2`
5. Services — `bg`
6. Corporate Heritage — `bg-2`
7. Recognition & Patents — `bg`
8. Get in Touch — `bg-2`

Sections alternate `--bg` (#0d1320) and `--bg-2` (#121a2b). Each has `border-top/bottom: 1px solid var(--line)`.

## Design tokens
```css
--bg:         #0d1320   /* dark navy — primary background */
--bg-2:       #121a2b   /* slightly lighter navy — alternating sections */
--panel:      #161f33   /* card/panel background */
--line:       #26314a   /* borders and dividers */
--ink:        #eef2f9   /* primary text */
--ink-soft:   #a3b0c7   /* secondary text */
--ink-dim:    #6b7794   /* muted/label text */
--accent:     #5b8cff   /* blue accent */
--accent-warm:#7da3ff   /* softer blue */
--gold:       #c9a86a   /* gold accent */
```
Fonts: `Fraunces` (serif display, headings, italic em) · `Inter` (body, UI)

## Article frontmatter schema
```yaml
title: ""
date: YYYY-MM-DD
summary: ""          # shown in listings and og:description
hero: "/images/filename.webp"
heroAlt: ""
series: "State of the Union in AI · Part N of 4"   # optional
seriesSlug: "state-of-the-union-in-ai"              # optional — links series articles
seriesPart: N                                        # optional — integer
draft: false
```

## Adding an article
1. Create `src/content/articles/slug.md` with frontmatter above
2. Add hero image to `public/images/` (see Image style below)
3. **Restart dev server** — new content files require `npm run dev` restart (editing existing body hot-reloads fine)
4. For series articles: set matching `seriesSlug` and incrementing `seriesPart` — prev/next nav wires up automatically

## Embedding a landscape/data graphic in article body
```html
<figure class="fig">
  <img src="/images/filename.webp" alt="..." />
  <figcaption>Caption text.</figcaption>
</figure>
```

## Image style guide
All article graphics follow this visual language:
- **Background:** `#0d1320` (dark navy)
- **Primary accents:** `#c9a86a` / `#e0c488` (gold) — corner ticks, accent bars, key labels
- **Text:** `#eef2f9` (primary), `#a3b0c7` (soft), `#6b7794` (dim/label)
- **Monospace labels**, bordered panels, corner tick marks, `benjaminhavey.com` footer
- **Hero images:** 1200×630px WebP (standard OG size)
- **Landscape/data graphics:** 1200×variable WebP

Generate images with Python + Pillow using DejaVu fonts available on the system:
- `/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf`
- `/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf`
- `/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf`
- `/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf`

Do NOT use ImageMagick to render SVG text — it produces broken letter spacing. Use Pillow directly.

## SEO / structured data
- **JSON-LD Person schema** in `Base.astro` `<head>` — covers homepage
- **JSON-LD Article schema** in `[slug].astro` — injected per article, eligible for Google rich results
- **OG image:** `public/images/og-homepage.webp` (1200×630) — wired up in `Base.astro`
- **robots.txt / llms.txt** — open policy, all crawlers welcome

## Active article series
**State of the Union in AI** (`seriesSlug: state-of-the-union-in-ai`)
- Part 1 — *The LLM Wars* (`llm-wars.md`) — published Jun 15 2026
- Part 2 — *The ImageGen Wars* (`imagegen-wars.md`) — published Jun 22 2026
- Part 3 — image generation market deep-dive — **pending**
- Part 4 — **pending**

## Open items
- **Contact form handler** — form fields are currently decorative; mailto fallback works. First serverless piece.
- **Parts 3 & 4** of the State of the Union in AI series
- **Cloudflare Scrape Shield** — if contact email shows as `[email protected]`, disable email obfuscation in Cloudflare dashboard
- **Headless CMS** — possible future: Astro + Sanity or Contentful

## Gotchas
- Restart `npm run dev` after adding new articles or editing `content.config.ts` / `astro.config.mjs`
- `astro.config.mjs` is in the repo root (not in this folder) — has site URL + sitemap config
- Verify all stats, patent numbers, and factual claims against primary sources before publishing — AI drafts have produced fabricated figures
- Cloudflare build config must be saved before the first Git deploy
- LinkedIn caches OG images aggressively — use https://www.linkedin.com/post-inspector/ to force refresh after updating `og-homepage.webp`

## Author
Ben Havey · me@benjaminhavey.com · Los Angeles
Emmy Award winner · 11 patents (AI, ML, AR) · Founded Disney StudioLAB
Current: Global studio technology leadership at Universal Pictures / NBCUniversal
