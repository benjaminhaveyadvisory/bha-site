#!/usr/bin/env python3
"""
Ben Havey field-report hero generator — 1200x630 WebP, benjaminhavey.com house style.

Renders the standard article hero: gold-on-navy, corner ticks, "A BEN HAVEY FIELD
REPORT" eyebrow, DejaVu Serif Bold title, mono subtitle, byline, site footer, and a
gold line-art motif in the top-right.

Layout constants below were reverse-measured from the existing heroes
(unmoved-movers, augmentation-question, final-pixel) and verified to land within
1px of the originals. Do not change them casually — that is what keeps the set
looking like a set.

Usage
-----
Edit the HEROES dict at the bottom (or import `build`) and run:

    python3 scripts/make_hero.py                 # render everything in HEROES
    python3 scripts/make_hero.py codegen-wars    # render one

Notes
-----
- Fonts are the system DejaVu faces. Do NOT swap in Fraunces/Inter here — the
  existing heroes were all rendered with DejaVu and would no longer match.
- Do NOT use ImageMagick to render SVG text (broken letter spacing). Pillow only.
- Rendered at 2x and downsampled with LANCZOS for clean antialiasing.
"""
from PIL import Image, ImageDraw, ImageFont
import math
import os
import sys

# ---------------------------------------------------------------- canvas / palette
W, H = 1200, 630
S = 2  # supersample factor

BG      = (12, 19, 33)     # #0d1320 dark navy
GOLD    = (201, 168, 106)  # #c9a86a
GOLD_LT = (224, 196, 136)  # #e0c488
TEXT    = (238, 242, 249)  # #eef2f9 primary
SOFT    = (200, 208, 224)  # subtitle
DIM     = (107, 119, 148)  # #6b7794 labels / footer
HAIR    = (32, 42, 62)     # footer hairline

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
serif_b = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSerif-Bold.ttf", int(s * S))
mono    = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSansMono.ttf", int(s * S))

# ---------------------------------------------------------------- layout constants
L               = 90     # left margin for every text block
TICK_INSET      = 30     # corner tick offset from edge
TICK_LEN        = 28
EYEBROW_Y       = 118
EYEBROW_SIZE    = 14
EYEBROW_TRACK   = 3.6
EYEBROW_RULE_Y  = 150
EYEBROW_RULE_X1 = 210
TITLE_Y         = 191    # top of first title line
TITLE_SIZE      = 84
TITLE_LEAD      = 91     # baseline-to-baseline
TITLE_RULE_Y    = 386    # gold gradient rule under the title
TITLE_RULE_X1   = 404
SUB_Y           = 427
SUB_SIZE        = 24
SUB_LEAD        = 36
KICKER_SIZE     = 19     # optional dim third line
DASH_Y          = 530
DASH_X1         = 150
BYLINE_Y        = 546
BYLINE_SIZE     = 13
BYLINE_TRACK    = 2.2
HAIRLINE_Y      = 574
FOOTER_Y        = 587
FOOTER_SIZE     = 14
FOOTER_TEXT     = "benjaminhavey.com"
EYEBROW_TEXT    = "A BEN HAVEY FIELD REPORT"


def _tracked(d, xy, text, font, fill, ls=0.0):
    """Draw text with manual letter-spacing (`ls` in unscaled px)."""
    x, y = xy[0] * S, xy[1] * S
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + ls * S


# ---------------------------------------------------------------- motifs
# Each motif is a function taking the ImageDraw and rendering gold line art in the
# top-right quadrant, centred near (1074, 100). Keep them geometric and sparse.

def motif_loop(d):
    """Human-in-the-loop: an open orbit closed by an arrowhead, node at centre."""
    cx, cy, r = 1074, 100, 46
    a0, a1 = -55, 248
    d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
          start=a0, end=a1, fill=GOLD, width=2 * S)
    th = math.radians(a1)
    ax, ay = cx + r * math.cos(th), cy + r * math.sin(th)
    tx, ty = -math.sin(th), math.cos(th)  # tangent / direction of travel
    for sgn in (1, -1):
        ca, sa = math.cos(math.radians(148 * sgn)), math.sin(math.radians(148 * sgn))
        bx, by = tx * ca - ty * sa, tx * sa + ty * ca
        d.line([(ax * S, ay * S), ((ax + bx * 12) * S, (ay + by * 12) * S)],
               fill=GOLD, width=2 * S)
    ir = 22
    d.arc([(cx - ir) * S, (cy - ir) * S, (cx + ir) * S, (cy + ir) * S],
          start=0, end=360, fill=(150, 126, 82), width=2 * S)
    d.ellipse([(cx - 5) * S, (cy - 5) * S, (cx + 5) * S, (cy + 5) * S], fill=GOLD_LT)
    for ang, rr, sz in ((202, r, 4.5), (34, ir, 3.5), (118, r, 3)):
        nx, ny = cx + rr * math.cos(math.radians(ang)), cy + rr * math.sin(math.radians(ang))
        d.ellipse([(nx - sz) * S, (ny - sz) * S, (nx + sz) * S, (ny + sz) * S], fill=GOLD_LT)


def motif_orbit(d):
    """Concentric rings with orbiting nodes (as used on The Unmoved Movers)."""
    cx, cy = 1044, 105
    for r, col in ((66, (90, 78, 54)), (44, (150, 126, 82)), (22, GOLD)):
        d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
              start=0, end=360, fill=col, width=2 * S)
    d.ellipse([(cx - 5) * S, (cy - 5) * S, (cx + 5) * S, (cy + 5) * S], fill=GOLD_LT)
    for ang, rr, sz in ((188, 44, 4), (12, 44, 3.5), (72, 66, 4.5)):
        nx, ny = cx + rr * math.cos(math.radians(ang)), cy + rr * math.sin(math.radians(ang))
        d.ellipse([(nx - sz) * S, (ny - sz) * S, (nx + sz) * S, (ny + sz) * S], fill=GOLD_LT)


def motif_arc(d):
    """Dashed trajectory between two ringed nodes (as used on The Augmentation Question)."""
    p0, p1 = (938, 137), (1108, 92)
    for i in range(28):
        if i % 2:
            continue
        t0, t1 = i / 28, (i + 1) / 28
        def pt(t):
            x = p0[0] + (p1[0] - p0[0]) * t
            y = p0[1] + (p1[1] - p0[1]) * t - 34 * math.sin(math.pi * t)
            return x * S, y * S
        d.line([pt(t0), pt(t1)], fill=(150, 126, 82), width=2 * S)
    for (nx, ny), r in ((p0, 15), (p1, 15)):
        d.arc([(nx - r) * S, (ny - r) * S, (nx + r) * S, (ny + r) * S],
              start=0, end=360, fill=GOLD, width=2 * S)
        d.ellipse([(nx - 4) * S, (ny - 4) * S, (nx + 4) * S, (ny + 4) * S], fill=GOLD_LT)


def motif_triad(d):
    """Three ringed nodes converging on one point — three titans, one prize."""
    cx, cy, r = 1070, 100, 44
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
           for a in (-90, 30, 150)]
    for x, y in pts:
        d.line([(x * S, y * S), (cx * S, cy * S)], fill=(150, 126, 82), width=2 * S)
        d.arc([(x - 11) * S, (y - 11) * S, (x + 11) * S, (y + 11) * S],
              start=0, end=360, fill=GOLD, width=2 * S)
        d.ellipse([(x - 3.5) * S, (y - 3.5) * S, (x + 3.5) * S, (y + 3.5) * S], fill=GOLD_LT)
    d.ellipse([(cx - 6) * S, (cy - 6) * S, (cx + 6) * S, (cy + 6) * S], fill=GOLD_LT)


def motif_aperture(d):
    """Nested rotating squares — prompt narrowing to pixel."""
    cx, cy = 1070, 100
    for size, rot, col in ((50, 0, (90, 78, 54)), (40, 22, (150, 126, 82)), (28, 45, GOLD)):
        pts = []
        for a in (45, 135, 225, 315):
            th = math.radians(a + rot)
            pts.append(((cx + size * math.cos(th)) * S, (cy + size * math.sin(th)) * S))
        d.line(pts + [pts[0]], fill=col, width=2 * S, joint="curve")
    d.rectangle([(cx - 5) * S, (cy - 5) * S, (cx + 5) * S, (cy + 5) * S], fill=GOLD_LT)


def motif_frames(d):
    """Three film frames in sequence with a sprocket rail — who owns the final frame."""
    x0, cy = 1006, 100
    for i in range(3):
        x = x0 + i * 44
        last = i == 2
        col = GOLD if last else (110, 94, 62)
        d.rectangle([x * S, (cy - 22) * S, (x + 34) * S, (cy + 22) * S],
                    outline=col, width=2 * S)
        for sy in (cy - 15, cy + 15):
            d.rectangle([(x + 6) * S, (sy - 2) * S, (x + 12) * S, (sy + 2) * S], fill=col)
            d.rectangle([(x + 22) * S, (sy - 2) * S, (x + 28) * S, (sy + 2) * S], fill=col)
        if last:  # the final frame, claimed
            d.rectangle([(x + 9) * S, (cy - 6) * S, (x + 25) * S, (cy + 6) * S], fill=GOLD_LT)


def motif_donut(d):
    """A ring with most of its mass gone — the click collapse."""
    cx, cy, r = 1070, 100, 46
    d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
          start=-64, end=64, fill=GOLD, width=7 * S)
    d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
          start=64, end=296, fill=(50, 44, 34), width=7 * S)
    ir = 24
    d.arc([(cx - ir) * S, (cy - ir) * S, (cx + ir) * S, (cy + ir) * S],
          start=0, end=360, fill=(90, 78, 54), width=2 * S)
    d.ellipse([(cx - 4) * S, (cy - 4) * S, (cx + 4) * S, (cy + 4) * S], fill=GOLD_LT)


def motif_fanout(d):
    """One node fanning out to three — the agent doing the hunting."""
    sx, cy = 1016, 100
    d.arc([(sx - 12) * S, (cy - 12) * S, (sx + 12) * S, (cy + 12) * S],
          start=0, end=360, fill=GOLD, width=2 * S)
    d.ellipse([(sx - 4) * S, (cy - 4) * S, (sx + 4) * S, (cy + 4) * S], fill=GOLD_LT)
    for dy in (-38, 0, 38):
        ex, ey = sx + 96, cy + dy
        mid = sx + 52
        d.line([((sx + 14) * S, cy * S), (mid * S, cy * S), (mid * S, ey * S),
                ((ex - 9) * S, ey * S)], fill=(150, 126, 82), width=2 * S, joint="curve")
        d.ellipse([(ex - 5) * S, (ey - 5) * S, (ex + 5) * S, (ey + 5) * S], fill=GOLD_LT)


def motif_cycle(d):
    """Four stations on a closed square loop — the self-improving research pipeline."""
    cx, cy, h = 1070, 100, 40
    corners = [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)]
    for i in range(4):
        a, b = corners[i], corners[(i + 1) % 4]
        d.line([(a[0] * S, a[1] * S), (b[0] * S, b[1] * S)],
               fill=(150, 126, 82), width=2 * S)
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        dx, dy = (b[0] - a[0]) / (2 * h), (b[1] - a[1]) / (2 * h)
        for sgn in (1, -1):
            ca, sa = math.cos(math.radians(145 * sgn)), math.sin(math.radians(145 * sgn))
            d.line([(mx * S, my * S),
                    ((mx + (dx * ca - dy * sa) * 9) * S, (my + (dx * sa + dy * ca) * 9) * S)],
                   fill=GOLD, width=2 * S)
    for x, y in corners:
        d.ellipse([(x - 5) * S, (y - 5) * S, (x + 5) * S, (y + 5) * S], fill=GOLD_LT)


def motif_compress(d):
    """A wide bar squeezed into a narrow one — zero-overhead compression."""
    cx, cy = 1070, 100
    rows = ((cy - 32, 50, (110, 94, 62)), (cy, 32, (170, 143, 92)), (cy + 32, 16, GOLD))
    for y, w, col in rows:
        d.rectangle([(cx - w) * S, (y - 8) * S, (cx + w) * S, (y + 8) * S],
                    outline=col, width=2 * S)
    for sgn in (-1, 1):  # inward chevrons squeezing the stack
        x = cx + sgn * 62
        d.line([(x * S, (cy - 12) * S), ((x - sgn * 11) * S, cy * S), (x * S, (cy + 12) * S)],
               fill=GOLD, width=2 * S, joint="curve")


def motif_none(d):
    pass


# ---------------------------------------------------------------- renderer
def build(out, title_lines, sub_lines, byline,
          kicker=None, motif=motif_none, eyebrow=EYEBROW_TEXT):
    """Render one hero. `title_lines` is 1-2 uppercase strings, `sub_lines` 1-2 strings."""
    img = Image.new("RGB", (W * S, H * S), BG)
    d = ImageDraw.Draw(img)

    # corner ticks
    for cx, cy, sx, sy in ((TICK_INSET, TICK_INSET, 1, 1),
                           (W - TICK_INSET, TICK_INSET, -1, 1),
                           (TICK_INSET, H - TICK_INSET, 1, -1),
                           (W - TICK_INSET, H - TICK_INSET, -1, -1)):
        d.line([(cx * S, (cy + sy * TICK_LEN) * S), (cx * S, cy * S),
                ((cx + sx * TICK_LEN) * S, cy * S)], fill=GOLD, width=2 * S)

    # eyebrow + short gold rule
    _tracked(d, (L, EYEBROW_Y), eyebrow, mono(EYEBROW_SIZE), GOLD, ls=EYEBROW_TRACK)
    d.rectangle([L * S, EYEBROW_RULE_Y * S, EYEBROW_RULE_X1 * S,
                 EYEBROW_RULE_Y * S + 3], fill=GOLD)

    # title
    tf = serif_b(TITLE_SIZE)
    y = TITLE_Y
    for line in title_lines:
        d.text((L * S, y * S), line, font=tf, fill=TEXT)
        y += TITLE_LEAD

    # gold gradient rule fading right
    span = (TITLE_RULE_X1 - L) * S
    for i in range(span):
        f = 1 - i / span
        col = tuple(int(BG[k] + (GOLD_LT[k] - BG[k]) * f) for k in range(3))
        d.rectangle([L * S + i, TITLE_RULE_Y * S, L * S + i + 1,
                     TITLE_RULE_Y * S + 3], fill=col)

    # subtitle (+ optional dim kicker line)
    sf = mono(SUB_SIZE)
    y = SUB_Y
    for line in sub_lines:
        d.text((L * S, y * S), line, font=sf, fill=SOFT)
        y += SUB_LEAD
    if kicker:
        d.text((L * S, y * S), kicker, font=mono(KICKER_SIZE), fill=DIM)

    # gold dash + byline
    d.rectangle([L * S, DASH_Y * S, DASH_X1 * S, DASH_Y * S + 3], fill=GOLD)
    _tracked(d, (L, BYLINE_Y), byline, mono(BYLINE_SIZE), DIM, ls=BYLINE_TRACK)

    # hairline + centred footer
    d.rectangle([40 * S, HAIRLINE_Y * S, (W - 40) * S, HAIRLINE_Y * S + 1], fill=HAIR)
    ff = mono(FOOTER_SIZE)
    fw = d.textlength(FOOTER_TEXT, font=ff)
    d.text(((W * S - fw) / 2, FOOTER_Y * S), FOOTER_TEXT, font=ff, fill=DIM)

    motif(d)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(out, "WEBP", quality=92, method=6)
    print("wrote", out)


# ---------------------------------------------------------------- hero definitions
IMAGES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "public", "images")

HEROES = {
    # --- State of the Union in AI series -------------------------------------
    "llm-wars": dict(
        title_lines=["THE LLM", "WARS"],
        sub_lines=["Three tech titans, one prize:",
                   "the place people go to think."],
        kicker="State of the Union in AI · Part 1 of 4",
        byline="BEN HAVEY ON LINKEDIN · 6 MIN READ",
        motif=motif_triad,
    ),
    "imagegen-wars": dict(
        title_lines=["THE IMAGEGEN", "WARS"],
        sub_lines=["From prompt to pixel —",
                   "and now to courtroom."],
        kicker="State of the Union in AI · Part 2 of 4",
        byline="BEN HAVEY ON LINKEDIN · 6 MIN READ",
        motif=motif_aperture,
    ),
    "videogen-wars": dict(
        title_lines=["THE VIDEOGEN", "WARS"],
        sub_lines=["Fourteen platforms, three tiers, and one",
                   "question: who owns the final frame?"],
        kicker="State of the Union in AI · Part 3 of 4",
        byline="BEN HAVEY ON LINKEDIN · 11 MIN READ",
        motif=motif_frames,
    ),
    "codegen-wars": dict(
        title_lines=["THE CODEGEN", "WARS"],
        sub_lines=["Sixteen platforms, four tiers, one question:",
                   "how far do you sit from the keyboard?"],
        kicker="State of the Union in AI · Part 4 of 4",
        byline="BEN HAVEY ON LINKEDIN · 12 MIN READ",
        motif=motif_loop,
    ),
    # --- standalone pieces ---------------------------------------------------
    "google-zero": dict(
        out_name="google-zero.webp",
        title_lines=["THE GOOGLE", "ZERO ERA"],
        sub_lines=["Two-thirds of searches now end",
                   "without a single click."],
        byline="BEN HAVEY ON LINKEDIN · 2 MIN READ",
        motif=motif_donut,
    ),
    "agentic-discovery": dict(
        out_name="agentic-discovery.webp",
        title_lines=["AGENTIC", "DISCOVERY"],
        sub_lines=["Agents now hunt, read, and buy on our",
                   "behalf. The whole playbook changed."],
        byline="BEN HAVEY ON LINKEDIN · 2 MIN READ",
        motif=motif_fanout,
    ),
    "ai-scientist": dict(
        out_name="ai-scientist.webp",
        title_lines=["THE AI", "SCIENTIST"],
        sub_lines=["A closed research loop that runs ideation",
                   "to peer review in a matter of days."],
        byline="BEN HAVEY ON LINKEDIN · 2 MIN READ",
        motif=motif_cycle,
    ),
    "turboquant": dict(
        out_name="turboquant.webp",
        title_lines=["THE INFERENCE", "TAX DROPPED"],
        sub_lines=["Zero-overhead KV-cache compression —",
                   "and why demand goes up, not down."],
        byline="BEN HAVEY ON LINKEDIN · 2 MIN READ",
        motif=motif_compress,
    ),
}


if __name__ == "__main__":
    names = sys.argv[1:] or list(HEROES)
    for name in names:
        if name not in HEROES:
            sys.exit(f"unknown hero '{name}' — known: {', '.join(HEROES)}")
        cfg = dict(HEROES[name])
        fname = cfg.pop("out_name", None) or f"{name}-hero.webp"
        build(os.path.join(IMAGES, fname), **cfg)
