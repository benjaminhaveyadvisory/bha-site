#!/usr/bin/env python3
"""
Ben Havey field-report comparison table — 1200xN WebP, benjaminhavey.com house style.

Renders a three-column platform comparison (header cards + labelled rows + an
italic-serif "strategy" row) in gold-on-navy with corner ticks, mono labels, and
the site footer. Companion to make_hero.py; shares its palette and fonts.

Usage
-----
    python3 scripts/make_table.py                      # render everything in TABLES
    python3 scripts/make_table.py reversibility-consumer

Notes
-----
- DejaVu fonts only (see make_hero.py). Pillow only — no ImageMagick.
- Rendered at 2x and downsampled with LANCZOS.
"""
from PIL import Image, ImageDraw, ImageFont
import os
import sys

W = 1200
S = 2

BG      = (12, 19, 33)     # #0d1320
PANEL   = (22, 31, 51)     # #161f33
LINE    = (38, 49, 74)     # #26314a
GOLD    = (201, 168, 106)  # #c9a86a
GOLD_LT = (224, 196, 136)  # #e0c488
GOLD_DK = (110, 94, 62)
TEXT    = (238, 242, 249)  # #eef2f9
SOFT    = (163, 176, 199)  # #a3b0c7
DIM     = (107, 119, 148)  # #6b7794
HAIR    = (32, 42, 62)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
def F(name, s): return ImageFont.truetype(FONT_DIR + name, int(s * S))
serif_b = lambda s: F("DejaVuSerif-Bold.ttf", s)
serif_i = lambda s: F("DejaVuSerif-Italic.ttf", s)
sans    = lambda s: F("DejaVuSans.ttf", s)
mono    = lambda s: F("DejaVuSansMono.ttf", s)
mono_b  = lambda s: F("DejaVuSansMono-Bold.ttf", s)

L = 60                 # outer margin
TICK_INSET, TICK_LEN = 30, 28
LABEL_W = 170          # width of the row-label column
GAP = 18               # gap between platform columns


def tracked(d, xy, text, font, fill, ls=0.0):
    x, y = xy[0] * S, xy[1] * S
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + ls * S


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w * S:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


def draw_block(d, x, y, text, font, fill, max_w, lead):
    lines = wrap(d, text, font, max_w)
    for ln in lines:
        d.text((x * S, y * S), ln, font=font, fill=fill)
        y += lead
    return y


def measure_block(d, text, font, max_w, lead):
    return len(wrap(d, text, font, max_w)) * lead


def build(out, eyebrow, title_lines, subtitle, columns, rows, strategy, sources,
          byline="BEN HAVEY ON LINKEDIN"):
    body_f, body_lead = sans(17), 25
    strat_f, strat_lead = serif_i(21), 29
    label_f = mono_b(11)
    col_w = (W - 2 * L - LABEL_W - 2 * GAP) / 3
    col_x = [L + LABEL_W + i * (col_w + GAP) for i in range(3)]
    cell_w = col_w - 20

    # --- pass 1: measure height
    scratch = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    y = 70
    y += 34                                  # eyebrow + rule
    y += 48 * len(title_lines) + 10          # title
    y += 34                                  # subtitle
    y += 20 + 92 + 20                        # header cards
    row_heights = []
    for label, cells in rows:
        h = max(measure_block(scratch, c, body_f, cell_w, body_lead) for c in cells)
        h = max(h, 2 * body_lead)
        row_heights.append(h + 36)
        y += h + 36
    sh = max(measure_block(scratch, c, strat_f, cell_w, strat_lead) for c in strategy)
    strat_h = sh + 44
    y += 16 + strat_h + 24
    y += 30                                  # sources
    y += 50                                  # footer
    H = int(y)

    img = Image.new("RGB", (W * S, H * S), BG)
    d = ImageDraw.Draw(img)

    # corner ticks
    for cx, cy, sx, sy in ((TICK_INSET, TICK_INSET, 1, 1), (W - TICK_INSET, TICK_INSET, -1, 1),
                           (TICK_INSET, H - TICK_INSET, 1, -1), (W - TICK_INSET, H - TICK_INSET, -1, -1)):
        d.line([(cx * S, (cy + sy * TICK_LEN) * S), (cx * S, cy * S), ((cx + sx * TICK_LEN) * S, cy * S)],
               fill=GOLD, width=2 * S)

    # --- pass 2: draw
    y = 70
    tracked(d, (L, y), eyebrow, mono(13), GOLD, ls=3.2)
    d.rectangle([L * S, (y + 24) * S, (L + 120) * S, (y + 24) * S + 3], fill=GOLD)
    y += 34
    tf = serif_b(40)
    for ln in title_lines:
        d.text((L * S, y * S), ln, font=tf, fill=TEXT); y += 48
    y += 10
    d.text((L * S, y * S), subtitle, font=sans(19), fill=SOFT)
    y += 34

    # header cards
    y += 20
    for i, (name, meta) in enumerate(columns):
        x = col_x[i]
        d.rectangle([x * S, y * S, (x + col_w) * S, (y + 92) * S], fill=PANEL, outline=LINE, width=1 * S)
        d.rectangle([x * S, y * S, (x + col_w) * S, y * S + 3 * S], fill=GOLD)
        d.text(((x + 18) * S, (y + 22) * S), name, font=serif_b(24), fill=TEXT)
        d.text(((x + 18) * S, (y + 60) * S), meta, font=mono(12), fill=DIM)
    y += 92 + 20

    # rows
    for (label, cells), rh in zip(rows, row_heights):
        d.rectangle([L * S, y * S, (W - L) * S, y * S + 1 * S], fill=LINE)
        ty = y + 18
        tracked(d, (L, ty + 4), label, label_f, GOLD, ls=1.4)
        for i, c in enumerate(cells):
            draw_block(d, col_x[i], ty, c, body_f, TEXT, cell_w, body_lead)
        y += rh

    # strategy row
    y += 16
    d.rectangle([L * S, y * S, (W - L) * S, (y + strat_h) * S], fill=PANEL, outline=LINE, width=1 * S)
    d.rectangle([L * S, y * S, L * S + 3 * S, (y + strat_h) * S], fill=GOLD)
    ty = y + 22
    for k, ln in enumerate(["REVERSIBILITY", "STRATEGY"]):
        tracked(d, (L + 16, ty + 4 + k * 15), ln, label_f, GOLD, ls=1.4)
    for i, c in enumerate(strategy):
        draw_block(d, col_x[i], ty, c, strat_f, GOLD_LT, cell_w, strat_lead)
    y += strat_h + 24

    # sources + byline
    sf = sans(12)
    draw_block(d, L, y, sources, sf, DIM, W - 2 * L - 260, 16)
    bw = d.textlength(byline, font=mono(11)) + 2.2 * S * len(byline)
    tracked(d, (W - L - bw / S, y + 2), byline, mono(11), GOLD, ls=2.2)

    # hairline + footer
    d.rectangle([40 * S, (H - 44) * S, (W - 40) * S, (H - 44) * S + 1], fill=HAIR)
    ff = mono(13)
    fw = d.textlength("benjaminhavey.com", font=ff)
    d.text(((W * S - fw) / 2, (H - 32) * S), "benjaminhavey.com", font=ff, fill=DIM)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(out, "WEBP", quality=90, method=6)
    print("wrote", out, f"{W}x{H}")


IMAGES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public", "images")

TABLES = {
    "reversibility-consumer": dict(
        eyebrow="A BEN HAVEY FIELD REPORT · CONSUMER AGENTS",
        title_lines=["DOTS · MUSE · DUET"],
        subtitle="Consumer agents. Three platforms, one question: can the mistake be undone?",
        columns=[("DOTS", "OpenAI · Sep 29, 2026"),
                 ("MUSE", "Meta · Sep 8, 2026"),
                 ("DUET", "Anthropic · Oct 21, 2026")],
        rows=[
            ("MODEL", ["GPT-6 Astra", "Muse Spark 1.3", "Claude Opus 5.5"]),
            ("WHERE IT RUNS", [
                "Its own cloud computer and browser, always on, inside ChatGPT",
                "Muse Secure VM: a dedicated per-user VM with its own browser",
                "Cloud-hosted computer; watches connected apps and surfaces what needs you"]),
            ("GUARDRAIL", [
                "You set goals and boundaries; read-only mode blocks browser control when you're away",
                "Separate Sentinel agent approves all network egress; credentials vaulted, never seen by the model",
                "Approval gate before sensitive or consequential actions; checks in only when a decision is needed"]),
            ("REACH", [
                "4,000+ connected apps; Microsoft Agent 365 for enterprise",
                "Own app, WhatsApp, Mac desktop app; Link by Stripe, one-time virtual cards",
                "6,000+ Claude Marketplace connectors; Link and Shop Pay for purchases"]),
            ("ACCESS", [
                "ChatGPT Pro and Business Premium",
                "Free tier; Power $20/mo; Maximum $100/mo",
                "Research preview, waitlist; Pro and Max, US only"]),
        ],
        strategy=["Contain it: scoped goals and a read-only fallback",
                  "Sandbox it: nothing leaves the VM without a second agent's sign-off",
                  "Gate it: a human approves anything that can't be walked back"],
        sources="Sources: company announcements and launch coverage, Sep–Oct 2026. Details as published at launch; check current terms.",
    ),
    "reversibility-work": dict(
        eyebrow="A BEN HAVEY FIELD REPORT · WORK AGENTS",
        title_lines=["GEMINI · COPILOT ·", "AGENTFORCE"],
        subtitle="Work agents. Same question, different answer: who signs off before it ships?",
        columns=[("GEMINI AGENT", "Google Cloud · Oct 8, 2026"),
                 ("COPILOT", "Microsoft · Agent 365 GA May 1, 2026"),
                 ("AGENTFORCE", "Salesforce · Agentforce 360")],
        rows=[
            ("MODEL", [
                "Gemini, auto-selects the best model per task",
                "Microsoft 365 Copilot, GPT and Microsoft models",
                "Agentforce on Salesforce Atlas reasoning, model-agnostic via AIforce"]),
            ("WHERE IT RUNS", [
                "Inside Google Workspace, Docs, email and dev environments, wired to business systems",
                "Inside Microsoft 365 apps and Teams; each agent gets its own Entra identity",
                "Inside Salesforce CRM, Slack and customer channels; runs record actions and flows"]),
            ("GUARDRAIL", [
                "Enterprise admin, governance and cost controls; the enterprise sets the boundaries, not the user",
                "Agent 365 control plane: registry, per-agent identity, Purview DLP, Defender threat detection",
                "Agent inherits the user's permissions; escalates to a human when a case can't be resolved"]),
            ("REACH", [
                "Knowledge work, content, coding and Q&A from one prompt box",
                "Researcher, Analyst and custom Copilot Studio agents across the Microsoft graph",
                "Sales, Service, Field Service, Industries; MCP connectors to Claude and Slack"]),
            ("ACCESS", [
                "Google Cloud and Gemini Enterprise plans; pricing not published at launch",
                "Copilot $30/user/mo; Agent 365 $15/user/mo add-on",
                "Flex Credits $500 per 100K ($0.10 per action); per-user add-ons $125–$150; editions from $550"]),
        ],
        strategy=["Govern it: autonomy lives inside the tenant's admin controls",
                  "Identify it: every agent is a user with revocable access",
                  "Meter it: every action is priced, logged and escalatable"],
        sources="Sources: company announcements and published pricing, May–Oct 2026. Enterprise pricing varies by contract; check current terms.",
    ),
}


if __name__ == "__main__":
    names = sys.argv[1:] or list(TABLES)
    for name in names:
        if name not in TABLES:
            sys.exit(f"unknown table '{name}' — known: {', '.join(TABLES)}")
        build(os.path.join(IMAGES, f"{name}.webp"), **TABLES[name])
