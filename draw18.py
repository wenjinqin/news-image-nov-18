#!/usr/bin/env python3
"""Entry image for make.fun's news-image-20261118 contest: the world news
of Wednesday 18 November 2026 on one drawn front page.

Flat-shape illustrations only — no photos and no borrowed artwork. Each
panel pairs a small scene with a headline and a one-line summary so a
reader who missed the day can reconstruct it from the page alone.
Running this file writes entry.png (1024 x 1024) next to it.
"""

import math

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
PAPER = (246, 241, 231)
INK = (24, 24, 24)
RED = (179, 49, 42)
GREY = (92, 92, 92)
BLUE = (46, 109, 164)
SKY = (214, 230, 242)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(d, text, fnt, width):
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def para(d, x, y, text, fnt, fill, width, centered=False, leading=1.12):
    for line in wrap_lines(d, text, fnt, width):
        lx = x + (width - d.textlength(line, font=fnt)) / 2 if centered else x
        d.text((lx, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def story(d, x, y, w, kicker, headline, caption, hs=25, cs=18):
    d.text((x, y), kicker, font=F(BOLD, 19), fill=RED)
    y = para(d, x, y + 26, headline, F(BOLD, hs), INK, w)
    para(d, x, y + 4, caption, F(REG, cs), GREY, w)


# ---------------------------------------------------------------- scenes
def scene_quad(d, x, y, w, h):
    """Four Quad flags over a harbour sun."""
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.rectangle([x, y + h - 26, x + w, y + h], fill=BLUE)
    d.ellipse([x + w - 50, y + 6, x + w - 10, y + 46], fill=(240, 170, 60))
    flags = ["us", "in", "jp", "au"]
    for i, kind in enumerate(flags):
        px = x + 26 + i * ((w - 40) // 4)
        d.line([px, y + 16, px, y + h - 24], fill=INK, width=4)
        fw, fh = 56, 36
        top = y + 16
        if kind == "us":
            d.rectangle([px, top, px + fw, top + fh], fill=(240, 240, 240))
            for s in range(4):
                d.rectangle([px, top + s * 9, px + fw, top + 4 + s * 9], fill=(178, 34, 52))
            d.rectangle([px, top, px + 25, top + 18], fill=(60, 59, 110))
        elif kind == "in":
            d.rectangle([px, top, px + fw, top + 12], fill=(240, 140, 50))
            d.rectangle([px, top + 12, px + fw, top + 24], fill=(245, 245, 245))
            d.rectangle([px, top + 24, px + fw, top + fh], fill=(40, 140, 70))
            d.ellipse([px + 23, top + 14, px + 33, top + 24], outline=(40, 60, 160), width=2)
        elif kind == "jp":
            d.rectangle([px, top, px + fw, top + fh], fill=(248, 248, 248), outline=(180, 180, 180))
            d.ellipse([px + 19, top + 9, px + 37, top + 27], fill=(200, 40, 50))
        else:
            d.rectangle([px, top, px + fw, top + fh], fill=(30, 50, 140))
            for sx, sy in ((10, 8), (26, 20), (42, 10), (16, 28), (38, 28)):
                d.ellipse([px + sx - 2, top + sy - 2, px + sx + 2, top + sy + 2], fill=(255, 255, 255))


def scene_crash(d, x, y, w, h):
    """A transport plane goes down toward snowy Siberian peaks."""
    d.rectangle([x, y, x + w, y + h], fill=(206, 220, 234))
    for bx, bw in ((0, 130), (95, 150), (205, 140)):
        peak = [(x + bx, y + h), (x + bx + bw / 2, y + h - 74), (x + bx + bw, y + h)]
        d.polygon(peak, fill=(110, 124, 142))
        tip = [(x + bx + bw / 2 - 13, y + h - 56), (x + bx + bw / 2, y + h - 74),
               (x + bx + bw / 2 + 13, y + h - 56), (x + bx + bw / 2, y + h - 64)]
        d.polygon(tip, fill=(255, 255, 255))
    px, py = x + w * 0.20, y + 14  # nose-down plane
    body = [(px, py + 26), (px + 26, py + 6), (px + 88, py), (px + 104, py + 8),
            (px + 40, py + 22), (px + 12, py + 34)]
    d.polygon(body, fill=(70, 76, 84))
    d.polygon([(px + 40, py + 10), (px + 58, py - 10), (px + 70, py + 8)], fill=(70, 76, 84))
    d.polygon([(px + 6, py + 24), (px - 8, py + 8), (px + 14, py + 14)], fill=(70, 76, 84))
    for t in range(5):  # dashed descent path
        sx = px + 108 + t * 22
        sy = py + 16 + t * 13
        d.line([sx, sy, sx + 10, sy + 7], fill=RED, width=4)


def scene_chip(d, x, y, w, h):
    """A microchip with a barred arrow — earnings up, founder stays out."""
    d.rectangle([x, y, x + w, y + h], fill=(30, 34, 44))
    cx, cy, s = x + w * 0.44, y + h * 0.52, 74
    for i in range(5):  # pins
        off = -s / 2 + 10 + i * 14
        d.line([cx + off, cy - s / 2 - 10, cx + off, cy - s / 2], fill=(190, 198, 210), width=4)
        d.line([cx + off, cy + s / 2, cx + off, cy + s / 2 + 10], fill=(190, 198, 210), width=4)
        d.line([cx - s / 2 - 10, cy + off, cx - s / 2, cy + off], fill=(190, 198, 210), width=4)
        d.line([cx + s / 2, cy + off, cx + s / 2 + 10, cy + off], fill=(190, 198, 210), width=4)
    d.rectangle([cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2], fill=(52, 120, 90))
    d.rectangle([cx - 20, cy - 20, cx + 20, cy + 20], outline=(220, 240, 225), width=3)
    d.line([cx - 12, cy + 8, cx - 2, cy - 4], fill=(255, 255, 255), width=4)  # rising tick
    d.line([cx - 2, cy - 4, cx + 12, cy - 12], fill=(255, 255, 255), width=4)
    bx, by = x + w * 0.80, y + h * 0.30  # no-return sign
    d.ellipse([bx - 17, by - 17, bx + 17, by + 17], outline=RED, width=5)
    d.line([bx - 12, by + 12, bx + 12, by - 12], fill=RED, width=5)


def scene_virus(d, x, y, w, h):
    """A virus particle — the measles story."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 214))
    cx, cy, r = x + w * 0.5, y + h * 0.54, 30
    for i in range(10):
        a = 2 * math.pi * i / 10
        ex, ey = cx + (r + 13) * math.cos(a), cy + (r + 13) * math.sin(a)
        d.line([cx + r * math.cos(a) * 0.9, cy + r * math.sin(a) * 0.9, ex, ey], fill=INK, width=4)
        d.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill=RED)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(196, 120, 90))
    for dx, dy in ((-12, -8), (10, 4), (-2, 14)):
        d.ellipse([cx + dx - 4, cy + dy - 4, cx + dx + 4, cy + dy + 4], fill=(150, 70, 55))


def scene_knesset(d, x, y, w, h):
    """A parliament portico: pediment, columns, steps."""
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    cx = x + w / 2
    top = y + 12
    d.polygon([(cx - 66, top + 22), (cx + 66, top + 22), (cx, top)], fill=(120, 110, 96))
    d.rectangle([cx - 66, top + 26, cx + 66, top + 32], fill=(120, 110, 96))
    for i in range(5):
        px = cx - 52 + i * 26
        d.rectangle([px, top + 36, px + 9, top + 78], fill=(150, 140, 122))
    d.rectangle([cx - 68, top + 82, cx + 68, top + 88], fill=(120, 110, 96))
    d.rectangle([cx - 76, top + 92, cx + 76, top + 98], fill=(120, 110, 96))


def scene_dna(d, x, y, w, h):
    """A DNA double helix with one broken rung."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 234, 226))
    cx = x + w * 0.5
    top, bot = y + 10, y + h - 10
    steps = 26
    prev_a = prev_b = None
    for i in range(steps + 1):
        t = i / steps
        yy = top + (bot - top) * t
        off = 26 * math.sin(t * 4.4 * math.pi)
        a = (cx + off, yy)
        b = (cx - off, yy)
        if prev_a:
            d.line([prev_a, a], fill=BLUE, width=4)
            d.line([prev_b, b], fill=RED, width=4)
        if i % 4 == 0:
            broken = i == 12
            if broken:
                d.line([a, (cx + off * 0.35, yy)], fill=INK, width=3)
                d.line([b, (cx - off * 0.35, yy)], fill=INK, width=3)
            else:
                d.line([a, b], fill=(120, 120, 120), width=3)
        prev_a, prev_b = a, b


# ------------------------------------------------------------------ page
def main():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    d = ImageDraw.Draw(img)
    M = 36

    d.text((SIZE / 2, 20), "T H E   W O R L D   I N   O N E   I M A G E",
           font=F(BOLD, 26), fill=INK, anchor="ma")
    date_f = F(BOLD, 66)
    while d.textlength("WEDNESDAY 18 NOVEMBER 2026", font=date_f) > SIZE - 2 * M:
        date_f = F(BOLD, date_f.size - 2)
    d.text((SIZE / 2, 54), "WEDNESDAY 18 NOVEMBER 2026", font=date_f, fill=INK, anchor="ma")
    d.line([M, 140, SIZE - M, 140], fill=INK, width=5)
    d.line([M, 148, SIZE - M, 148], fill=INK, width=2)

    # lead: the Quad summit in Manila
    d.rectangle([M, 164, SIZE - M, 444], outline=INK, width=3)
    scene_quad(d, M + 10, 174, 452, 260)
    lx = M + 486
    d.text((lx, 182), "ASIA \u00b7 DIPLOMACY", font=F(BOLD, 22), fill=RED)
    y = para(d, lx, 214, "TRUMP, MODI LEAD QUAD SUMMIT IN MANILA", F(BOLD, 40), INK, SIZE - M - lx - 8)
    para(d, lx, y + 8,
         "Quad leaders open their Manila summit and unveil new maritime, "
         "AI and cyber initiatives.",
         F(REG, 22), GREY, SIZE - M - lx - 8)

    # row of three
    y0, y1 = 458, 718
    cw = (SIZE - 2 * M - 24) // 3
    cells = [
        (scene_crash, "RUSSIA", "MILITARY PLANE CRASH KILLS 19 IN SIBERIA",
         "A Russian transport plane comes down; 19 aboard die."),
        (scene_chip, "TECH \u00b7 BUSINESS", "NVIDIA BEATS FORECASTS, BARS HUANG RETURN",
         "Strong earnings; founder's return barred."),
        (scene_virus, "HEALTH", "US LOSES ITS MEASLES-FREE STATUS",
         "Elimination status withdrawn as cases keep climbing."),
    ]
    for i, (scene, kick, head, cap) in enumerate(cells):
        x0 = M + i * (cw + 12)
        d.rectangle([x0, y0, x0 + cw, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, cw - 16, 84)
        story(d, x0 + 12, y0 + 102, cw - 24, kick, head, cap)

    # row of two
    y0, y1 = 732, 952
    cw2 = (SIZE - 2 * M - 12) // 2
    cells2 = [
        (scene_knesset, "ISRAEL", "NETANYAHU BLOW AS KNESSET ELECTS SPEAKER",
         "Parliament picks an ally of rival Eisenkot as speaker — "
         "a defeat for him."),
        (scene_dna, "CHINA", "SCIENTIST SACKED AFTER GENE-TRIAL DEATH",
         "Sacked after a six-year-old dies in the trial."),
    ]
    for i, (scene, kick, head, cap) in enumerate(cells2):
        x0 = M + i * (cw2 + 12)
        d.rectangle([x0, y0, x0 + cw2, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, 168, y1 - y0 - 16)
        story(d, x0 + 188, y0 + 12, cw2 - 200, kick, head, cap, hs=26)

    d.line([M, 960, SIZE - M, 960], fill=INK, width=3)
    para(d, M, 968,
         "ALSO TODAY \u00b7 Ebola cases double in DR Congo \u00b7 Dhoni retires from the IPL \u00b7 US jails "
         "man 27 years over Iran-backed Trump plot \u00b7 Mongolia's president resigns",
         F(BOLD, 18), INK, SIZE - 2 * M, centered=True)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
