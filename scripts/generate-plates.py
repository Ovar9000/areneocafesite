"""Generate the procedural license-plate wall used as the site's background.

    python -I scripts/generate-plates.py

Writes:

  static/images/plates-page.svg        60 unique plates, colours faded most of the way into the
                                       canvas. app.css lays it on a fixed layer with a slow
                                       parallax drift and a veil behind the content column.
  src/lib/assets/brand/plate-lot7.svg  the wall's LOT 7 plate on its own, full colour; inlined
                                       into the hero intro so it never waits on the network

For a full-colour wall, call build(0, WOOD).

Each plate gets a colourway, a design (bands, a Mayon sunset, stripes...), embossed lettering,
bolts, a registration sticker and wear modelled on real plates: rust blooming from the bolt
holes with ragged edges and short bleeds, scuffed metal, chipped paint, worn edges, dirt that
settles at the bottom, sun fade, dents and warped metal. All of it is plain shapes and
gradients (no SVG filters), so the wall stays cheap to rasterise on phones.

Lettering is Bebas Neue (SIL OFL, already the site's display face) converted to outlines, so
the plates look the same on every device without loading a font. Change SEED for a different
wall. Requires fontTools.
"""

import math
import random
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / 'node_modules' / '@fontsource' / 'bebas-neue' / 'files' / 'bebas-neue-latin-400-normal.woff'
OUT = ROOT / 'static' / 'images'
BRAND = ROOT / 'src' / 'lib' / 'assets' / 'brand'

SEED = 7
COLS, ROWS = 10, 6  # 60 unique plates: about two screens of wall before anything repeats
PW, PH = 220, 110  # plate size (2:1, like a real plate)
PITCH_X, PITCH_Y = 240, 130
W, H = COLS * PITCH_X, ROWS * PITCH_Y  # 2400 x 780 tile

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
	('#e9e4f2', '#f7f4ec', '#3b2a6b', '#d9962a'),
	('#f0ebe0', None, '#2a2a2e', '#2f8f6b'),
]
DARK = [
	('#00388a', None, '#f3ecd8', '#f2c94c'),
	('#1e1e22', None, '#f2c94c', '#f3ecd8'),
	('#2f5d46', None, '#f4f2ec', '#f2c94c'),
	('#7a2e2e', None, '#f3ecd8', '#f2c94c'),
	('#23415f', None, '#f4f2ec', '#e07b39'),
]
STICKERS = ['#e74c3c', '#f1c40f', '#2ecc71', '#3498db', '#e67e22', '#9b59b6']
TOP_TEXT = ['NAGA CITY', 'CAMARINES SUR', 'BICOL', 'PHILIPPINES', 'LOT 7 CAFE', 'NEIGHBORHOOD',
	'PENAFRANCIA', 'MAGSAYSAY AVE', 'BICOL REGION']
BOTTOM_TEXT = ['JUST A LITTLE BETTER', 'YOUR NEIGHBORHOOD', 'EST 2026', 'SPECIALTY COFFEE',
	'RESIDENT VINYL', 'ISLAS DE LUZON', 'HEART OF BICOL', '', '']
# Consonants only, so random serials can never spell a word
LETTERS = 'BCDFGHJKLMNPRSTVWXZ'
MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

RUST_DARK, RUST_MID, RUST_LIGHT = '#4f220e', '#8e4317', '#c47a3c'
METAL = '#c3c4c9'


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
		self.design = forced.get('design') or rng.choice(['plain', 'plain', 'band', 'mayon', 'stripe', 'sun', 'split'])
		self.top = forced.get('top') or rng.choice(TOP_TEXT)
		self.bottom = forced['bottom'] if 'bottom' in forced else rng.choice(BOTTOM_TEXT)
		self.serial = forced.get('serial') or (
			''.join(rng.choice(LETTERS) for _ in range(3)) + ' ' + ''.join(rng.choice('0123456789') for _ in range(rng.choice([3, 4])))
		)
		self.sticker = rng.random() < 0.6 and (rng.choice(STICKERS), rng.choice(MONTHS), rng.choice(['24', '25', '26']), rng.choice(['left', 'right']))
		self.four_bolts = rng.random() < 0.25
		# How weathered this plate is overall: most are lightly used, a few are rough
		self.age = forced.get('age', rng.choice([0.15, 0.3, 0.3, 0.5, 0.5, 0.7, 0.9]))
		self.rng_state = rng.random()  # per-plate seed for wear, so every variant matches

	@property
	def bolts(self) -> list[tuple[int, int]]:
		return [(36, 14), (184, 14)] + ([(36, 96), (184, 96)] if self.four_bolts else [])


def blob(rng: random.Random, cx: float, cy: float, r: float, stretch: float = 1, roughness: float = 0.35,
	points: int = 14) -> str:
	"""A closed, organic outline: a ring of jittered points joined by smooth quadratic curves."""
	pts = []
	for i in range(points):
		a = 2 * math.pi * i / points
		rr = r * (1 + rng.uniform(-roughness, roughness))
		pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr * stretch))
	mids = [((pts[i][0] + pts[(i + 1) % points][0]) / 2, (pts[i][1] + pts[(i + 1) % points][1]) / 2) for i in range(points)]
	d = f'M{mids[-1][0]:.1f} {mids[-1][1]:.1f}'
	for i in range(points):
		d += f' Q{pts[i][0]:.1f} {pts[i][1]:.1f} {mids[i][0]:.1f} {mids[i][1]:.1f}'
	return d + 'Z'


def wear(rng: random.Random, p: Plate, c) -> list[str]:
	"""Weathering in plate coordinates. `c` fades a colour for the current variant."""
	out = []
	age = p.age
	# Sun fade: a bleached patch, mostly toward the top where the sun hits
	if rng.random() < 0.3 + age * 0.4:
		x, y, r = rng.uniform(30, 190), rng.uniform(0, 60), rng.uniform(50, 110)
		out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="url(#sunfade)" opacity="{0.2 + age * 0.4:.2f}"/>')
	# Dirt that settles along the bottom edge
	if rng.random() < 0.4 + age * 0.5:
		out.append(f'<rect y="{PH * 0.55:.0f}" width="{PW}" height="{PH * 0.45:.0f}" fill="url(#dirt)" opacity="{0.3 + age * 0.6:.2f}"/>')
	# Grime gathering in the corners
	if rng.random() < 0.3 + age * 0.5:
		out.append(f'<rect width="{PW}" height="{PH}" fill="url(#grime)" opacity="{0.2 + age * 0.5:.2f}"/>')
	# Warped metal: a soft shadow-and-highlight band where the plate has been bent and flattened
	if rng.random() < 0.08 + age * 0.15:
		corner_x = rng.choice([30, PW - 30])
		angle = rng.uniform(25, 55) * (1 if corner_x < PW / 2 else -1)
		out.append(
			f'<rect x="{corner_x - 16}" y="-40" width="32" height="200" fill="url(#warp)" opacity="{0.5 + age * 0.4:.2f}" '
			f'transform="rotate({angle:.0f} {corner_x} {rng.uniform(10, 100):.0f})"/>'
		)
	# A dent: a soft crater, lit from the top left
	if rng.random() < 0.08 + age * 0.2:
		x, y, r = rng.uniform(40, 180), rng.uniform(30, 85), rng.uniform(8, 16)
		out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r * 1.4:.0f}" ry="{r:.0f}" fill="url(#dent)"/>')
	# Rust blooming from the bolt holes: ragged blotches, darkest at the hole, and short bleeds
	for bx, by in p.bolts:
		if rng.random() < age * 0.85:
			size = rng.uniform(4, 7 + age * 8)
			out.append(f'<path d="{blob(rng, bx + rng.uniform(-1.5, 1.5), by + rng.uniform(0, 2), size, rng.uniform(0.8, 1.2))}" fill="url(#rust)"/>')
			# freckles around it
			for _ in range(rng.randint(1, 4)):
				fx, fy = bx + rng.uniform(-size * 1.8, size * 1.8), by + rng.uniform(-size, size * 1.6)
				out.append(f'<path d="{blob(rng, fx, fy, rng.uniform(0.8, 2.2), 1, 0.4, 8)}" fill="{c(rng.choice([RUST_MID, RUST_LIGHT]))}" opacity="{rng.uniform(0.35, 0.7):.2f}"/>')
			# a short bleed running down, wavering as it goes
			if by < PH / 2 and rng.random() < 0.6:
				length = rng.uniform(8, 16 + age * 18)
				wobble = [rng.uniform(-1.2, 1.2) for _ in range(4)]
				w0 = rng.uniform(1.6, 2.6)
				d = (
					f'M{bx - w0:.1f} {by + 3}'
					f' C{bx - w0 + wobble[0]:.1f} {by + length * 0.35:.1f} {bx - 0.6 + wobble[1]:.1f} {by + length * 0.7:.1f} {bx + wobble[2] * 0.3:.1f} {by + length:.1f}'
					f' C{bx + 0.6 + wobble[1]:.1f} {by + length * 0.7:.1f} {bx + w0 + wobble[3]:.1f} {by + length * 0.35:.1f} {bx + w0:.1f} {by + 3}Z'
				)
				out.append(f'<path d="{d}" fill="url(#bleed)" opacity="{0.55 + age * 0.35:.2f}"/>')
	# Rust creeping in from the edges on old plates
	if rng.random() < age * 0.5:
		ex = rng.choice([rng.uniform(0, 8), rng.uniform(PW - 8, PW)])
		ey = rng.uniform(20, PH - 10)
		out.append(f'<path d="{blob(rng, ex, ey, rng.uniform(4, 9), rng.uniform(1.2, 2))}" fill="url(#rust)" opacity="0.85"/>')
	# Chipped paint: small ragged flakes of bare metal with a dark lip, near edges and bolts
	for _ in range(rng.choice([0, 0, 1, 2, 3]) + round(age * 2)):
		if rng.random() < 0.5:
			x = rng.choice([rng.uniform(3, 12), rng.uniform(PW - 12, PW - 3)])
			y = rng.uniform(8, PH - 8)
		else:
			x = rng.uniform(12, PW - 12)
			y = rng.choice([rng.uniform(3, 9), rng.uniform(PH - 9, PH - 3)])
		r = rng.uniform(1.2, 3.2)
		d = blob(rng, x, y, r, rng.uniform(0.6, 1.4), 0.5, 9)
		out.append(f'<path d="{d}" fill="{c(METAL)}" stroke="{c("#000000")}" stroke-opacity="0.25" stroke-width="0.5"/>')
	# Scuffs: a small cluster of short, slightly curved marks going the same way
	if rng.random() < 0.25 + age * 0.4:
		cx, cy = rng.uniform(30, PW - 30), rng.uniform(25, PH - 15)
		base = rng.uniform(-0.5, 0.5)
		for _ in range(rng.randint(3, 7)):
			x0, y0 = cx + rng.uniform(-14, 14), cy + rng.uniform(-8, 8)
			length = rng.uniform(3, 10)
			a = base + rng.uniform(-0.25, 0.25)
			x1, y1 = x0 + math.cos(a) * length, y0 + math.sin(a) * length
			mx, my = (x0 + x1) / 2 + rng.uniform(-1, 1), (y0 + y1) / 2 + rng.uniform(-1, 1)
			out.append(
				f'<path d="M{x0:.1f} {y0:.1f} Q{mx:.1f} {my:.1f} {x1:.1f} {y1:.1f}" fill="none" stroke="{c("#eeeef1")}" '
				f'stroke-width="{rng.uniform(0.4, 0.8):.1f}" stroke-linecap="round" opacity="{rng.uniform(0.3, 0.55):.2f}"/>'
			)
	# Worn edges: the paint rubbed thin all the way round
	if rng.random() < 0.3 + age * 0.5:
		out.append(f'<rect x="1" y="1" width="{PW - 2}" height="{PH - 2}" rx="9" fill="none" stroke="{c(METAL)}" stroke-width="{1.2 + age * 1.6:.1f}" opacity="{0.25 + age * 0.4:.2f}"/>')
	return out


def render_plate(g: Glyphs, p: Plate, x: float, y: float, fade: float) -> str:
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
	elif p.design == 'split':
		parts.append(f'<rect y="{PH / 2:.0f}" width="{PW}" height="{PH / 2:.0f}" fill="{accent}" opacity="0.12"/>')
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
	# Registration sticker, in a bottom corner clear of the serial (inboard of any lower bolt).
	# Old stickers are sun-bleached.
	if p.sticker:
		color, month, year, side = p.sticker
		sx = 11 if side == 'left' else PW - 11 - 28
		sx += 0 if not p.four_bolts else (36 if side == 'left' else -36)
		faded = 1 - p.age * 0.45
		parts.append(f'<g opacity="{faded:.2f}"><rect x="{sx}" y="88" width="28" height="13" rx="2" fill="{c(color)}"/>')
		parts.append(g.text(f'{month} {year}', sx + 14, 97.8, 7, 0.6, c('#ffffff'), max_width=24) + '</g>')
	# Wear
	parts.extend(wear(rng, p, c))
	parts.append('</g>')
	# Bolts sit on top of the wear; old ones are rusty
	for bx, by in p.bolts:
		if rng.random() < 0.85:
			head = 'url(#bolt-rust)' if rng.random() < p.age * 0.6 else 'url(#bolt)'
			parts.append(
				f'<circle cx="{bx}" cy="{by + 0.8}" r="5.2" fill="{c("#000000")}" opacity="0.2"/>'
				f'<circle cx="{bx}" cy="{by}" r="5" fill="{head}"/>'
				f'<line x1="{bx - 3}" y1="{by}" x2="{bx + 3}" y2="{by}" stroke="{c("#5b5b60")}" stroke-width="1" transform="rotate({rng.randint(0, 179)} {bx} {by})"/>'
			)
		else:
			parts.append(f'<circle cx="{bx}" cy="{by}" r="3.6" fill="{c("#2c2c30")}" opacity="0.75"/>')
	parts.append('</g>')
	return ''.join(parts)


def make_plates() -> dict[tuple[int, int], Plate]:
	"""Every plate in the tile, keyed by (row, column). Same seed, same wall."""
	rng = random.Random(SEED)
	# A few house plates in every tile
	forced = {
		(0, 2): {'colors': DARK[0], 'serial': 'LOT 7', 'top': 'NAGA CITY', 'bottom': 'JUST A LITTLE BETTER', 'design': 'plain', 'age': 0.3},
		(2, 6): {'colors': LIGHT[2], 'serial': 'NGA 007', 'top': 'CAMARINES SUR', 'bottom': 'YOUR NEIGHBORHOOD', 'design': 'mayon'},
		(4, 1): {'colors': LIGHT[3], 'serial': 'LOT 7', 'top': 'BICOL', 'bottom': 'EST 2026', 'design': 'stripe'},
		(5, 8): {'colors': DARK[1], 'serial': 'LOT 7', 'top': 'RESIDENT VINYL', 'bottom': 'SIDE A', 'design': 'sun'},
	}
	return {(r, col): Plate(rng, forced.get((r, col))) for r in range(ROWS) for col in range(COLS)}


def shared_defs(c) -> str:
	return (
		f'<clipPath id="pc"><rect width="{PW}" height="{PH}" rx="10"/></clipPath>'
		'<radialGradient id="sunfade"><stop offset="0" stop-color="#ffffff" stop-opacity="0.9"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>'
		f'<linearGradient id="dirt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c("#3b2a1a")}" stop-opacity="0"/><stop offset="1" stop-color="{c("#3b2a1a")}" stop-opacity="0.28"/></linearGradient>'
		f'<radialGradient id="grime" r="0.75"><stop offset="0.6" stop-color="{c("#3b2a1a")}" stop-opacity="0"/><stop offset="1" stop-color="{c("#3b2a1a")}" stop-opacity="0.3"/></radialGradient>'
		f'<radialGradient id="rust" cx="0.5" cy="0.45" r="0.55"><stop offset="0" stop-color="{c(RUST_DARK)}" stop-opacity="0.95"/><stop offset="0.45" stop-color="{c(RUST_MID)}" stop-opacity="0.8"/><stop offset="0.8" stop-color="{c(RUST_LIGHT)}" stop-opacity="0.45"/><stop offset="1" stop-color="{c(RUST_LIGHT)}" stop-opacity="0"/></radialGradient>'
		f'<linearGradient id="bleed" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c(RUST_MID)}" stop-opacity="0.9"/><stop offset="0.6" stop-color="{c(RUST_LIGHT)}" stop-opacity="0.5"/><stop offset="1" stop-color="{c(RUST_LIGHT)}" stop-opacity="0"/></linearGradient>'
		f'<linearGradient id="warp" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="0.4" stop-color="{c("#000000")}" stop-opacity="0.16"/><stop offset="0.55" stop-color="#ffffff" stop-opacity="0.32"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>'
		f'<radialGradient id="dent" cx="0.5" cy="0.5" fx="0.38" fy="0.35"><stop offset="0" stop-color="{c("#000000")}" stop-opacity="0.16"/><stop offset="0.65" stop-color="{c("#000000")}" stop-opacity="0.05"/><stop offset="0.85" stop-color="#ffffff" stop-opacity="0.25"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>'
		f'<radialGradient id="bolt" cx="0.35" cy="0.35"><stop offset="0" stop-color="{c("#f4f4f6")}"/><stop offset="1" stop-color="{c("#8e8e94")}"/></radialGradient>'
		f'<radialGradient id="bolt-rust" cx="0.35" cy="0.35"><stop offset="0" stop-color="{c("#d9b08a")}"/><stop offset="0.6" stop-color="{c(RUST_MID)}"/><stop offset="1" stop-color="{c(RUST_DARK)}"/></radialGradient>'
	)


def build(fade: float, gap: str | None) -> str:
	g = Glyphs()
	plates = make_plates()

	body = []
	for r in range(ROWS):
		offset = (r % 2) * (PITCH_X // 2)
		y = r * PITCH_Y + (PITCH_Y - PH) // 2
		for col in range(-1, COLS + 1):
			x = col * PITCH_X + offset + (PITCH_X - PW) // 2
			if x + PW <= 0 or x >= W:
				continue
			body.append(render_plate(g, plates[(r, col % COLS)], x, y, fade))

	c = (lambda col: mix(col, CANVAS, fade)) if fade else (lambda col: col)
	background = f'<rect width="{W}" height="{H}" fill="{gap}"/>' if gap else ''
	return (
		f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
		f'<!-- Generated by scripts/generate-plates.py (seed {SEED}, fade {fade}); do not edit by hand -->'
		f'<defs>{shared_defs(c)}{g.defs()}</defs>{background}{"".join(body)}</svg>\n'
	)


def build_hero_plate() -> str:
	"""The LOT 7 plate from the wall (row 0, column 2) on its own, full colour, for the hero intro.
	Its ids are prefixed so they can't collide with anything else once it's inlined in the page."""
	g = Glyphs()
	plate = make_plates()[(0, 2)]
	body = render_plate(g, plate, 0, 0, 0)
	svg = (
		f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PW} {PH + 2}" preserveAspectRatio="xMidYMid meet">'
		f'<defs>{shared_defs(lambda col: col)}{g.defs()}</defs>{body}</svg>\n'
	)
	for name in ['pc', 'sunfade', 'dirt', 'grime', 'rust', 'bleed', 'warp', 'dent', 'bolt-rust', 'bolt']:
		svg = svg.replace(f'id="{name}"', f'id="hp-{name}"').replace(f'url(#{name})', f'url(#hp-{name})')
	svg = svg.replace('id="g', 'id="hp-g').replace('href="#g', 'href="#hp-g')
	return svg


if __name__ == '__main__':
	for path, svg in [(OUT / 'plates-page.svg', build(0.78, None)), (BRAND / 'plate-lot7.svg', build_hero_plate())]:
		path.write_text(svg, encoding='utf-8')
		print(f'{path.relative_to(ROOT)}  {path.stat().st_size // 1024} KB')
