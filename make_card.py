#!/usr/bin/env python3
"""Samloryx social card generator.

Navy card, white headline, teal accent, white logo lockup. Matches the 22 Jul card.
Usage: make_card.py "<headline>" "<subline or empty>" <out.png> [size]
  size: wide (1200x628, LinkedIn/Facebook) or square (1080x1080)
"""
import sys
from PIL import Image, ImageDraw, ImageFont

NAVY = (2, 31, 63)
NAVY_DEEP = (1, 22, 46)
TEAL = (26, 188, 176)
BLUE = (46, 155, 240)
WHITE = (255, 255, 255)
MUTED = (183, 196, 214)

BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
LOCKUP = "/home/samloryx/Desktop/Samloryx Consultancy/samloryx-consultancy-platform/src/main/resources/static/assets/logo-lockup-white.png"
URL = "samloryxconsultancy.co.za"


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build(headline, subline, out, size="wide"):
    W, H = (1200, 628) if size == "wide" else (1080, 1080)
    pad = int(W * 0.065)
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Subtle diagonal depth panel on the right, echoing the existing card.
    panel = Image.new("RGB", (W, H), NAVY)
    pd = ImageDraw.Draw(panel)
    pd.polygon([(W * 0.62, 0), (W, 0), (W, H), (W * 0.80, H)], fill=NAVY_DEEP)
    pd.polygon([(W * 0.86, 0), (W, 0), (W, H * 0.42)], fill=(9, 46, 66))
    img = Image.blend(img, panel, 0.9)
    d = ImageDraw.Draw(img)

    # Teal accent stroke, top right.
    d.polygon([(W * 0.935, H * 0.10), (W * 0.975, H * 0.10),
               (W * 0.855, H * 0.52), (W * 0.815, H * 0.52)], fill=TEAL)

    # Bottom block first (logo, rule, url), so the text above can never collide with it.
    lock = Image.open(LOCKUP).convert("RGBA")
    a = lock.getchannel("A").point(lambda v: 255 if v > 110 else 0)
    lock.putalpha(a)
    lock = lock.crop(lock.getbbox())
    lw = int(W * 0.24)
    lock = lock.resize((lw, int(lock.height * lw / lock.width)), Image.LANCZOS)

    fu = ImageFont.truetype(REG, int(H * 0.032))
    url_h = int(H * 0.045)
    rule_gap = int(H * 0.028)
    block_h = lock.height + rule_gap + url_h
    block_top = H - pad - block_h

    img.paste(lock, (pad, block_top), lock)
    ry = block_top + lock.height + rule_gap
    d.line([(pad, ry), (pad + int(W * 0.36), ry)], fill=(120, 140, 165), width=2)
    d.text((pad, ry + int(H * 0.018)), URL, font=fu, fill=WHITE)

    # Text column: fits between the top padding and the bottom block.
    max_w = int(W * 0.62) if size == "wide" else int(W * 0.84)
    top = pad + int(H * 0.03)
    avail = block_top - int(H * 0.06) - top
    fs = ImageFont.truetype(REG, int(H * 0.044))
    sub_lines = wrap(d, subline, fs, int(W * 0.55))[:3] if subline else []
    sub_h = (len(sub_lines) * int(fs.size * 1.36) + int(H * 0.075)) if sub_lines else 0

    for pt in range(int(H * 0.115), 22, -2):
        f = ImageFont.truetype(BOLD, pt)
        lines = wrap(d, headline, f, max_w)
        if len(lines) <= 4 and len(lines) * int(pt * 1.14) + sub_h <= avail:
            break

    y = top
    for ln in lines:
        d.text((pad, y), ln, font=f, fill=WHITE)
        y += int(pt * 1.14)

    if sub_lines:
        y += int(H * 0.032)
        d.line([(pad, y), (pad + int(W * 0.40), y)], fill=(120, 140, 165), width=2)
        y += int(H * 0.038)
        for ln in sub_lines:
            d.text((pad, y), ln, font=fs, fill=MUTED)
            y += int(fs.size * 1.36)

    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({W}x{H}) headline lines={len(lines)} pt={pt}")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3],
          sys.argv[4] if len(sys.argv) > 4 else "wide")
