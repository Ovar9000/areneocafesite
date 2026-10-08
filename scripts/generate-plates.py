"""Generate the procedural license-plate wall used as the site's background.

    python -I scripts/generate-plates.py

Writes static/images/plates-page.svg, a seamless tile with the colours faded most of the way
into the canvas (app.css adds a veil behind the content column on top). For a full-colour
version, call build(0, WOOD).

Each plate gets a colourway, a design (bands, a Mayon sunset, stripes...), embossed lettering,
bolts, a registration sticker and random wear: rust, scratches, sun fade, grime, dents, chipped
paint, creases and the odd bent corner. Lettering is Bebas Neue (SIL OFL, already the site's
display face) converted to outlines, so the plates look the same on every device without
loading a font. Change SEED for a different wall. Requires fontTools.
"""

import random
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / 'node_modules' / '@fontsource' / 'bebas-neue' / 'files' / 'bebas-neue-latin-400-normal.woff'
OUT = ROOT / 'static' / 'images'

SEED = 7
COLS, ROWS = 6, 4
PW, PH = 220, 110  # plate size (2:1, like a real plate)
PITCH_X, PITCH_Y = 240, 130
W, H = COLS * PITCH_X, ROWS * PITCH_Y  # 1440 x 520 tile

CANVAS = '#f2f2f7'  # --bg-base
WOOD = '#2b211b'

# Plate colourways: (face, second face for gradients or None, ink, accent)
LIGHT = [
	('#f4f2ec', None, '#1f3466', '#c0392b'),
	('#efe6cf', None, '#7a1f1f', '#2d6cb5'),
	('#d7e6f4', '#f6f1e4', '#1f3466', '#e07b39'),
	('#f3e3a3', None, '#1b1b1f', '#2d6cb5'),
	('#d5eadb', '#f4f2ec', '#1e5a3a', '#c0392b'),
	('#f6d7c3', '#f7efe2', '#7a1f1f', '#1e5a3a'),
	('#f4f2ec', '#f5d78e', '#00388a', '#e07b39'),
]
DARK = [
	('#00388a', None, '#f3ecd8', '#f2c94c'),
	('#1e1e22', None, '#f2c94c', '#f3ecd8'),
	('#2f5d46', None, '#f4f2ec', '#f2c94c'),
	('#7a2e2e', None, '#f3ecd8', '#f2c94c'),
]
STICKERS = ['#e74c3c', '#f1c40f', '#2ecc71', '#3498db', '#e67e22', '#9b59b6']
TOP_TEXT = ['NAGA CITY', 'CAMARINES SUR', 'BICOL', 'PHILIPPINES', 'LOT 7 CAFE', 'NEIGHBORHOOD']
BOTTOM_TEXT = ['JUST A LITTLE BETTER', 'YOUR NEIGHBORHOOD', 'EST 2026', 'SPECIALTY COFFEE',
	'RESIDENT VINYL', 'ISLAS DE LUZON', '']
# Consonants only, so random serials can never spell a word
LETTERS = 'BCDFGHJKLMNPRSTVWXZ'
MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


def mix(hex_color: str, toward: str, amount: float) -> str:
	a = [int(hex_color[i : i + 2], 16) for i in (1, 3, 5)]
	b = [int(toward[i : i + 2], 16) for i in (1, 3, 5)]
	return '#' + ''.join(f'{round(x + (y - x) * amount):02x}' for x, y in zip(a, b))


class Glyphs:
	"""Bebas Neue outlines, emitted once as <defs> and placed with <use>."""

	def __init__(self) -> None:
		font = TTFont(FONT)
		self.glyph_set = font.getGlyphSet()
		self.cmap = font.getBestCmap()
		self.hmtx = font['hmtx']
		self.cap = font['OS/2'].sCapHeight
		self.used: set[str] = set()

	def advance(self, ch: str) -> int:
		return self.hmtx[self.cmap[ord(ch)]][0]

	def defs(self) -> str:
		out = []
		for ch in sorted(self.used):
			pen = SVGPathPen(self.glyph_set)
			self.glyph_set[self.cmap[ord(ch)]].draw(pen)
			out.append(f'<path id="g{ord(ch)}" d="{pen.getCommands()}"/>')
		return ''.join(out)

	def text(self, s: str, cx: float, baseline: float, cap_px: float, spacing: float, fill: str,
		max_width: float | None = None, opacity: float = 1) -> str:
		scale = cap_px / self.cap
		width = sum(self.advance(c) for c in s) * scale + spacing * (len(s) - 1)
		if max_width and width > max_width:  # squeeze long words to fit, like a real stamping die
			squeeze = max_width / width
		else:
			squeeze = 1
		x = cx - width * squeeze / 2
		uses = []
		for ch in s:
			if ch != ' ':
				self.used.add(ch)
				uses.append(f'<use href="#g{ord(ch)}" transform="translate({x:.1f} {baseline:.1f}) scale({scale * squeeze:.4f} {-scale:.4f})"/>')
			x += (self.advance(ch) * scale + spacing) * squeeze
		op = f' opacity="{opacity}"' if opacity < 1 else ''
		return f'<g fill="{fill}"{op}>{"".join(uses)}</g>'


class Plate:
	def __init__(self, rng: random.Random, forced: dict | None = None) -> None:
		forced = forced or {}
		dark = rng.random() < 0.3
		self.face, self.face2, self.ink, self.accent = forced.get('colors') or rng.choice(DARK if dark else LIGHT)
		self.dark = self.face in [d[0] for d in DARK]
		self.design = forced.get('design') or rng.choice(['plain', 'plain', 'band', 'mayon', 'stripe', 'sun'])
		self.top = forced.get('top') or rng.choice(TOP_TEXT)
		self.bottom = forced['bottom'] if 'bottom' in forced else rng.choice(BOTTOM_TEXT)
		self.serial = forced.get('serial') or (
			''.join(rng.choice(LETTERS) for _ in range(3)) + ' ' + ''.join(rng.choice('0123456789') for _ in range(rng.choice([3, 4])))
		)
		self.sticker = rng.random() < 0.6 and (rng.choice(STICKERS), rng.choice(MONTHS), rng.choice(['24', '25', '26']), rng.choice(['left', 'right']))
		self.four_bolts = rng.random() < 0.25
		self.rng_state = rng.random()  # per-plate seed for wear, so both variants match
		self.bent = forced.get('bent', rng.random() < 0.12) and rng.choice(['tl', 'tr', 'br', 'bl'])


def wear(rng: random.Random, p: Plate, c) -> list[str]:
	"""Random wear and damage, in plate coordinates. `c` fades a colour for the current variant."""
	out = []
	bolts = [(36, 14), (184, 14)] + ([(36, 96), (184, 96)] if p.four_bolts else [])
	# Sun fade: a bleached patch
	if rng.random() < 0.45:
		x, y, r = rng.uniform(20, 200), rng.uniform(10, 100), rng.uniform(40, 90)
		out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="url(#fade)" opacity="{rng.uniform(0.25, 0.55):.2f}"/>')
	# Grime around the edges
	if rng.random() < 0.5:
		out.append(f'<rect width="{PW}" height="{PH}" fill="url(#grime)" opacity="{rng.uniform(0.25, 0.6):.2f}"/>')
	# Rust blooming from the bolt holes, with the odd streak running down
	if rng.random() < 0.5:
		for bx, by in rng.sample(bolts, rng.randint(1, len(bolts))):
			for _ in range(rng.randint(3, 7)):
				out.append(
					f'<circle cx="{bx + rng.uniform(-9, 9):.1f}" cy="{by + rng.uniform(-6, 9):.1f}" r="{rng.uniform(1.5, 6):.1f}" '
					f'fill="{c(rng.choice(["#8b4513", "#a0522d", "#b5651d"]))}" opacity="{rng.uniform(0.15, 0.45):.2f}"/>'
				)
			if rng.random() < 0.5:
				length = rng.uniform(20, 55)
				out.append(
					f'<path d="M{bx - 2.5:.1f} {by + 3} L{bx + 2.5:.1f} {by + 3} L{bx + 0.6:.1f} {by + length:.1f} L{bx - 0.6:.1f} {by + length:.1f} Z" '
					f'fill="url(#streak)" opacity="{rng.uniform(0.4, 0.8):.2f}"/>'
				)
	# Scratches
	for _ in range(rng.choice([0, 1, 2, 3, 4, 6])):
		x, y = rng.uniform(5, 215), rng.uniform(5, 105)
		length, angle = rng.uniform(8, 45), rng.uniform(-0.6, 0.6)
		x2, y2 = x + length, y + length * angle
		light = rng.random() < 0.65
		out.append(
			f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{"#ffffff" if light else c("#2a2a2a")}" '
			f'stroke-width="{rng.uniform(0.5, 1.2):.1f}" stroke-linecap="round" opacity="{rng.uniform(0.25, 0.6):.2f}"/>'
		)
	# Chipped paint showing bare metal, mostly near the edges
	for _ in range(rng.choice([0, 0, 1, 2, 3])):
		edge = rng.choice(['x', 'y'])
		x = rng.choice([rng.uniform(2, 14), rng.uniform(206, 218)]) if edge == 'x' else rng.uniform(10, 210)
		y = rng.uniform(10, 100) if edge == 'x' else rng.choice([rng.uniform(2, 10), rng.uniform(100, 108)])
		pts = ' '.join(
			f'{x + rng.uniform(-5, 5):.1f},{y + rng.uniform(-4, 4):.1f}' for _ in range(rng.randint(4, 6))
		)
		out.append(f'<polygon points="{pts}" fill="{c("#c9c9cc")}"/>')
	# A dent: shadow and highlight side by side
	if rng.random() < 0.2:
		x, y = rng.uniform(40, 180), rng.uniform(30, 80)
		out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="18" ry="10" fill="url(#dent)" opacity="0.5"/>')
	# A crease across the plate
	if rng.random() < 0.1:
		y1, y2 = rng.uniform(10, 100), rng.uniform(10, 100)
		out.append(f'<line x1="0" y1="{y1:.0f}" x2="{PW}" y2="{y2:.0f}" stroke="#ffffff" stroke-width="1.2" opacity="0.6"/>')
		out.append(f'<line x1="0" y1="{y1 + 1.5:.0f}" x2="{PW}" y2="{y2 + 1.5:.0f}" stroke="{c("#000000")}" stroke-width="1" opacity="0.18"/>')
	return out


def bent_corner(corner: str, gap: str, c) -> str:
	"""The tip of one corner folded back over the face, showing what's behind the plate."""
	a, b = 34, 26
	cx, cy = (0 if corner[1] == 'l' else PW), (0 if corner[0] == 't' else PH)
	sx, sy = (1 if corner[1] == 'l' else -1), (1 if corner[0] == 't' else -1)
	p1 = (cx + sx * a, cy)
	p2 = (cx, cy + sy * b)
	# Reflect the corner across the fold line p1-p2
	dx, dy = p2[0] - p1[0], p2[1] - p1[1]
	t = ((cx - p1[0]) * dx + (cy - p1[1]) * dy) / (dx * dx + dy * dy)
	fx, fy = p1[0] + t * dx, p1[1] + t * dy
	rx, ry = 2 * fx - cx, 2 * fy - cy
	hide = f'<polygon points="{cx - sx * 2},{cy - sy * 2} {p1[0] + sx * 2},{cy - sy * 2} {p1[0]},{p1[1]} {p2[0]},{p2[1]} {cx - sx * 2},{p2[1] + sy * 2}" fill="{gap}"/>'
	shadow = f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {rx + sx * 3:.1f},{ry + sy * 3:.1f}" fill="#000" opacity="0.14"/>'
	fold = f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {rx:.1f},{ry:.1f}" fill="url(#metal)"/>'
	edge = f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="#ffffff" stroke-width="1" opacity="0.7"/>'
	return hide + shadow + fold + edge


def render_plate(g: Glyphs, p: Plate, x: float, y: float, fade: float, gap: str) -> str:
	c = (lambda col: mix(col, CANVAS, fade)) if fade else (lambda col: col)
	face, ink, accent = c(p.face), c(p.ink), c(p.accent)
	rng = random.Random(p.rng_state)
	parts = [f'<g transform="translate({x} {y})">']
	# Drop edge, then the clipped face
	parts.append(f'<rect y="2" width="{PW}" height="{PH}" rx="10" fill="{c("#000000")}" opacity="0.12"/>')
	parts.append('<g clip-path="url(#pc)">')
	if p.face2:
		gid = f'grad{x:.0f}-{y:.0f}'
		parts.append(
			f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c(p.face2)}"/>'
			f'<stop offset="1" stop-color="{face}"/></linearGradient><rect width="{PW}" height="{PH}" fill="url(#{gid})"/>'
		)
	else:
		parts.append(f'<rect width="{PW}" height="{PH}" fill="{face}"/>')
	# Design
	if p.design == 'band':
		parts.append(f'<rect width="{PW}" height="24" fill="{accent}" opacity="0.85"/>')
	elif p.design == 'stripe':
		parts.append(f'<rect y="88" width="{PW}" height="6" fill="{accent}" opacity="0.7"/><rect y="96" width="{PW}" height="2" fill="{accent}" opacity="0.7"/>')
	elif p.design == 'mayon':  # Mt Mayon, Bicol's volcano, under a low sun
		parts.append(f'<circle cx="150" cy="72" r="20" fill="{c("#f2994a")}" opacity="0.45"/>')
		parts.append(f'<path d="M30 {PH} L104 54 L112 54 L190 {PH} Z" fill="{accent}" opacity="0.28"/>')
	elif p.design == 'sun':
		for i in range(7):
			parts.append(f'<path d="M110 {PH + 30} L{-40 + i * 50} -10 L{-20 + i * 50} -10 Z" fill="{accent}" opacity="0.08"/>')
	# Pressed rim
	rim = c('#ffffff') if p.dark else c(p.ink)
	parts.append(f'<rect x="5.5" y="5.5" width="{PW - 11}" height="{PH - 11}" rx="6" fill="none" stroke="{rim}" stroke-width="1.4" opacity="0.35"/>')
	# Lettering
	top_fill = c(p.face) if p.design == 'band' else accent
	parts.append(g.text(p.top, 110, 21, 10, 2.4, top_fill, max_width=120))
	highlight = c('#ffffff') if not p.dark else c('#000000')
	parts.append(g.text(p.serial, 110.8, 79.2, 44, 3, highlight, max_width=176, opacity=0.5))
	parts.append(g.text(p.serial, 109.2, 77.6, 44, 3, c('#000000'), max_width=176, opacity=0.25))
	parts.append(g.text(p.serial, 110, 78, 44, 3, ink, max_width=176))
	if p.bottom:
		parts.append(g.text(p.bottom, 110, 98, 7.5, 2, ink if p.design != 'stripe' else accent, max_width=(70 if p.four_bolts else 110) if p.sticker else 150, opacity=0.8))
	# Registration sticker, in a bottom corner clear of the serial (inboard of any lower bolt)
	if p.sticker:
		color, month, year, side = p.sticker
		sx = 11 if side == 'left' else PW - 11 - 28
		sx += 0 if not p.four_bolts else (36 if side == 'left' else -36)
		parts.append(f'<rect x="{sx}" y="88" width="28" height="13" rx="2" fill="{c(color)}"/>')
		parts.append(g.text(f'{month} {year}', sx + 14, 97.8, 7, 0.6, c('#ffffff'), max_width=24))
	# Wear
	parts.extend(wear(rng, p, c))
	parts.append('</g>')
	# Bolts sit on top of the wear
	for bx, by in [(36, 14), (184, 14)] + ([(36, 96), (184, 96)] if p.four_bolts else []):
		if rng.random() < 0.8:
			parts.append(f'<circle cx="{bx}" cy="{by}" r="5" fill="url(#bolt)"/><line x1="{bx - 3}" y1="{by}" x2="{bx + 3}" y2="{by}" stroke="{c("#6b6b70")}" stroke-width="1" transform="rotate({rng.randint(0, 179)} {bx} {by})"/>')
		else:
			parts.append(f'<circle cx="{bx}" cy="{by}" r="3.6" fill="{c("#3a3a3e")}" opacity="0.7"/>')
	if p.bent:
		parts.append(bent_corner(p.bent, gap, c))
	parts.append('</g>')
	return ''.join(parts)


def build(fade: float, gap: str | None) -> str:
	g = Glyphs()
	rng = random.Random(SEED)
	# A few house plates in every tile
	forced = {
		(0, 2): {'colors': DARK[0], 'serial': 'LOT 7', 'top': 'NAGA CITY', 'bottom': 'JUST A LITTLE BETTER', 'design': 'plain', 'bent': False},
		(2, 4): {'colors': LIGHT[2], 'serial': 'NGA 007', 'top': 'CAMARINES SUR', 'bottom': 'YOUR NEIGHBORHOOD', 'design': 'mayon'},
		(3, 1): {'colors': LIGHT[3], 'serial': 'LOT 7', 'top': 'BICOL', 'bottom': 'EST 2026', 'design': 'stripe'},
	}
	plates = {(r, col): Plate(rng, forced.get((r, col))) for r in range(ROWS) for col in range(COLS)}
	c = (lambda col: mix(col, CANVAS, fade)) if fade else (lambda col: col)
	gap_fill = gap or CANVAS

	body = []
	for r in range(ROWS):
		offset = (r % 2) * (PITCH_X // 2)
		y = r * PITCH_Y + (PITCH_Y - PH) // 2
		for col in range(-1, COLS + 1):
			x = col * PITCH_X + offset + (PITCH_X - PW) // 2
			if x + PW <= 0 or x >= W:
				continue
			body.append(render_plate(g, plates[(r, col % COLS)], x, y, fade, gap_fill))

	defs = (
		f'<clipPath id="pc"><rect width="{PW}" height="{PH}" rx="10"/></clipPath>'
		'<radialGradient id="fade"><stop offset="0" stop-color="#ffffff" stop-opacity="0.9"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>'
		f'<radialGradient id="grime" r="0.75"><stop offset="0.55" stop-color="{c("#3b2a1a")}" stop-opacity="0"/><stop offset="1" stop-color="{c("#3b2a1a")}" stop-opacity="0.35"/></radialGradient>'
		f'<linearGradient id="streak" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c("#8b4513")}" stop-opacity="0.7"/><stop offset="1" stop-color="{c("#8b4513")}" stop-opacity="0"/></linearGradient>'
		f'<radialGradient id="dent" cx="0.4" cy="0.4"><stop offset="0" stop-color="#ffffff" stop-opacity="0.7"/><stop offset="0.5" stop-color="#ffffff" stop-opacity="0"/><stop offset="0.8" stop-color="{c("#000000")}" stop-opacity="0.25"/><stop offset="1" stop-color="{c("#000000")}" stop-opacity="0"/></radialGradient>'
		f'<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c("#e4e4e8")}"/><stop offset="0.5" stop-color="{c("#b9b9bf")}"/><stop offset="1" stop-color="{c("#d6d6db")}"/></linearGradient>'
		f'<radialGradient id="bolt" cx="0.35" cy="0.35"><stop offset="0" stop-color="{c("#f4f4f6")}"/><stop offset="1" stop-color="{c("#8e8e94")}"/></radialGradient>'
	)
	background = f'<rect width="{W}" height="{H}" fill="{gap}"/>' if gap else ''
	return (
		f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
		f'<!-- Generated by scripts/generate-plates.py (seed {SEED}, fade {fade}); do not edit by hand -->'
		f'<defs>{defs}{g.defs()}</defs>{background}{"".join(body)}</svg>\n'
	)


if __name__ == '__main__':
	path = OUT / 'plates-page.svg'
	path.write_text(build(0.78, None), encoding='utf-8')
	print(f'{path.relative_to(ROOT)}  {path.stat().st_size // 1024} KB')
