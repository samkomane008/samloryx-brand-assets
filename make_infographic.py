#!/usr/bin/env python3
"""Samloryx infographic card generator.

Portrait 1080x1350 (4:5), the size that takes the most feed height on both LinkedIn and
Facebook. Brand navy with the same constellation texture the website footer and the portal
login page use, so a post, the site and the portal all read as one brand.

Four layouts, all built from advice rather than statistics, because inventing a number is
not an option (global rule 4):
  steps     numbered rows, label plus one supporting line
  checklist ticked rows
  compare   two columns, three points each
  flow      vertical stages with connectors

Usage: build(spec, out_path) where spec is a dict. See CARDS in batch_infographics.py.
"""
import math
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1350

NAVY_TOP = (28, 34, 85)
NAVY_MID = (23, 28, 66)
NAVY_LOW = (18, 21, 44)
WHITE = (255, 255, 255)
LAVENDER = (200, 203, 228)
MUTED = (150, 157, 190)
BLUE = (46, 155, 240)
TEAL = (26, 188, 176)

BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"
LOCKUP = ("/home/samloryx/Desktop/Samloryx Consultancy/samloryx-consultancy-platform"
          "/src/main/resources/static/assets/logo-lockup-white.png")
URL = "samloryxconsultancy.co.za"

PAD = 78


def _font(path, size):
    return ImageFont.truetype(path, size)


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def _background(seed):
    """Navy gradient, constellation, glow. Same construction as the site texture."""
    img = Image.new("RGB", (W, H), NAVY_MID)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        if t < 0.5:
            k = t / 0.5
            c = tuple(int(NAVY_TOP[i] + (NAVY_MID[i] - NAVY_TOP[i]) * k) for i in range(3))
        else:
            k = (t - 0.5) / 0.5
            c = tuple(int(NAVY_MID[i] + (NAVY_LOW[i] - NAVY_MID[i]) * k) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)

    glow = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.35, -H * 0.22, W * 1.45, H * 0.48], fill=(24, 82, 130))
    gd.ellipse([-W * 0.45, H * 0.62, W * 0.62, H * 1.30], fill=(30, 38, 108))
    # Blurred hard, otherwise the ellipse edge reads as a drawn circle rather than light.
    glow = glow.filter(ImageFilter.GaussianBlur(150))
    img = Image.blend(img, glow, 0.20)

    d = ImageDraw.Draw(img, "RGBA")
    for y in range(0, H, 42):
        for x in range(0, W, 42):
            d.ellipse([x, y, x + 2.4, y + 2.4], fill=(200, 203, 228, 14))

    rnd = random.Random(seed)
    pts = []
    for row in range(6):
        for col in range(5):
            pts.append(((col + 0.5) * W / 5 + rnd.uniform(-44, 44),
                        (row + 0.5) * H / 6 + rnd.uniform(-40, 40)))
    edges = set()
    for i, p in enumerate(pts):
        near = sorted(((math.dist(p, q), j) for j, q in enumerate(pts) if j != i))
        for _, j in near[:2]:
            edges.add((min(i, j), max(i, j)))
    for a, b in edges:
        d.line([pts[a], pts[b]], fill=(143, 184, 232, 34), width=1)
    for i, (x, y) in enumerate(pts):
        if i % 7 == 0:
            d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(46, 155, 240, 150))
        else:
            d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(200, 203, 228, 70))
    return img


def _footer(img, d):
    lock = Image.open(LOCKUP).convert("RGBA")
    alpha = lock.getchannel("A").point(lambda v: 255 if v > 110 else 0)
    lock.putalpha(alpha)
    lock = lock.crop(lock.getbbox())
    lw = 240
    lock = lock.resize((lw, int(lock.height * lw / lock.width)), Image.LANCZOS)

    baseline = H - PAD
    img.paste(lock, (PAD, baseline - lock.height), lock)
    fu = _font(MONO, 25)
    d.text((W - PAD, baseline - lock.height + lock.height // 2 - 14), URL,
           font=fu, fill=MUTED, anchor="ra")
    rule_y = baseline - lock.height - 34
    d.line([(PAD, rule_y), (W - PAD, rule_y)], fill=(70, 80, 125), width=2)
    return rule_y - 44


def _header(img, d, spec):
    y = PAD
    fe = _font(MONO, 25)
    d.text((PAD, y), spec["eyebrow"].upper(), font=fe, fill=BLUE)
    y += 52
    for size in range(62, 34, -2):
        ft = _font(BOLD, size)
        lines = _wrap(d, spec["title"], ft, W - PAD * 2)
        if len(lines) <= 3:
            break
    for line in lines:
        d.text((PAD, y), line, font=ft, fill=WHITE)
        y += int(size * 1.16)
    if spec.get("standfirst"):
        y += 14
        fs = _font(REG, 30)
        for line in _wrap(d, spec["standfirst"], fs, W - PAD * 2)[:2]:
            d.text((PAD, y), line, font=fs, fill=LAVENDER)
            y += 40
    return y + 34


def _rows_block(d, spec, top, bottom, mode):
    items = spec["items"]
    gap = min((bottom - top) / len(items), 132)
    fl = _font(BOLD, 34)
    fd = _font(REG, 27)
    fn = _font(MONO, 27)
    top += max(0, (bottom - top - gap * len(items)) / 2)
    for i, item in enumerate(items):
        y = top + gap * i + 6
        if mode == "steps":
            d.ellipse([PAD, y, PAD + 46, y + 46], outline=BLUE, width=2)
            d.text((PAD + 23, y + 23), str(i + 1), font=fn, fill=BLUE, anchor="mm")
        else:
            d.line([(PAD + 6, y + 24), (PAD + 18, y + 36)], fill=TEAL, width=4)
            d.line([(PAD + 18, y + 36), (PAD + 42, y + 10)], fill=TEAL, width=4)
        tx = PAD + 72
        d.text((tx, y + 2), item["label"], font=fl, fill=WHITE)
        if item.get("detail"):
            yy = y + 44
            for line in _wrap(d, item["detail"], fd, W - tx - PAD)[:2]:
                d.text((tx, yy), line, font=fd, fill=MUTED)
                yy += 34


def _compare_block(d, spec, top, bottom):
    left, right = spec["left"], spec["right"]
    colw = (W - PAD * 2 - 34) // 2
    fh = _font(BOLD, 33)
    fb = _font(REG, 28)

    def measure(col):
        h = 52 + len(_wrap(d, col["heading"], fh, colw - 52)[:2]) * 40 + 16
        for point in col["points"]:
            h += len(_wrap(d, point, fb, colw - 68)[:3]) * 36 + 14
        return h + 30

    # Box height follows the taller column, then the pair is centred in the space left over,
    # so a short comparison does not leave a tall empty panel under it.
    box_h = min(max(measure(left), measure(right)), bottom - top)
    box_top = top + max(0, (bottom - top - box_h) / 2)

    for idx, (col, accent) in enumerate(((left, MUTED), (right, BLUE))):
        x = PAD + idx * (colw + 34)
        d.rounded_rectangle([x, box_top, x + colw, box_top + box_h], radius=22,
                            fill=(255, 255, 255, 10) if idx else None,
                            outline=(70, 80, 125), width=2)
        d.line([(x + 26, box_top + 26), (x + 26 + 44, box_top + 26)], fill=accent, width=4)
        yy = box_top + 52
        for line in _wrap(d, col["heading"], fh, colw - 52)[:2]:
            d.text((x + 26, yy), line, font=fh, fill=WHITE if idx else LAVENDER)
            yy += 40
        yy += 16
        for point in col["points"]:
            for k, line in enumerate(_wrap(d, point, fb, colw - 68)[:3]):
                if k == 0:
                    d.ellipse([x + 28, yy + 12, x + 36, yy + 20], fill=accent)
                d.text((x + 50, yy), line, font=fb, fill=LAVENDER)
                yy += 36
            yy += 14


def _flow_block(d, spec, top, bottom):
    items = spec["items"]
    gap = min((bottom - top) / len(items), 190)
    top += max(0, (bottom - top - gap * len(items)) / 2)
    fl = _font(BOLD, 34)
    fd = _font(REG, 27)
    fn = _font(MONO, 24)
    for i, item in enumerate(items):
        y = top + gap * i
        box_h = gap - 30
        d.rounded_rectangle([PAD, y, W - PAD, y + box_h], radius=20,
                            outline=(70, 80, 125), width=2)
        d.text((PAD + 28, y + 22), f"0{i + 1}", font=fn, fill=BLUE)
        d.text((PAD + 84, y + 18), item["label"], font=fl, fill=WHITE)
        if item.get("detail"):
            yy = y + 62
            for line in _wrap(d, item["detail"], fd, W - PAD * 2 - 112)[:2]:
                d.text((PAD + 84, yy), line, font=fd, fill=MUTED)
                yy += 34
        if i < len(items) - 1:
            cx = W // 2
            ay = y + box_h + 6
            d.line([(cx, ay), (cx, ay + 16)], fill=BLUE, width=3)
            d.polygon([(cx - 7, ay + 14), (cx + 7, ay + 14), (cx, ay + 24)], fill=BLUE)


def build(spec, out):
    img = _background(spec.get("seed", 7))
    d = ImageDraw.Draw(img, "RGBA")
    body_bottom = _footer(img, d)
    body_top = _header(img, d, spec)

    layout = spec["layout"]
    if layout in ("steps", "checklist"):
        _rows_block(d, spec, body_top, body_bottom, layout)
    elif layout == "compare":
        _compare_block(d, spec, body_top, body_bottom)
    elif layout == "flow":
        _flow_block(d, spec, body_top, body_bottom)
    else:
        raise ValueError(f"unknown layout {layout}")

    img.save(out, "PNG", optimize=True)
    return out
