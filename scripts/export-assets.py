"""Export web masters from the official Lot 7 design assets.

    python -I scripts/export-assets.py

Reads the raw camera files in design-assets/PICTURES (git-ignored, ~400 MB) and the
official artwork in design-assets/LOGOS, and writes:

  src/lib/assets/images/*.jpg   2400px photo masters; <enhanced:img> builds AVIF/WebP + srcset
  src/lib/assets/brand/*.png    trimmed, transparent wordmark and tagline artwork
  static/images/og-lot7.jpg     1200x630 link-preview image
  static/favicon.ico, static/apple-touch-icon.png

Re-run after swapping a photo in PHOTOS below. Requires Pillow.
"""

from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
PICTURES = ROOT / 'design-assets' / 'PICTURES'
LOGOS = ROOT / 'design-assets' / 'LOGOS'
IMAGES = ROOT / 'src' / 'lib' / 'assets' / 'images'
BRAND = ROOT / 'src' / 'lib' / 'assets' / 'brand'
STATIC = ROOT / 'static'

# Build inputs only (visitors get AVIF/WebP generated from these): big enough for a 2x
# full-width display, small enough to keep the repo and builds light
MASTER_EDGE = 2000
BRAND_BLUE = (0, 56, 138)  # sampled from the official sticker artwork (#00388A)

# web name -> camera file
PHOTOS = {
	'room-fisheye': '_DSC4645',
	'plate-wall': 'DSCF8117',
	'sign-closeup': 'DSCF8130',
	'espresso-bar': 'DSCF0536',
	'drink-pour': '_DSC4632',
	'drink-cup': '_DSC4637',
	'drink-soda': '_DSC4610',
	'dj-night': 'DSCF0667',
	'dj-controller': 'DSCF0610',
	'crowd-mirror': 'DSCF0629',
	'portrait-night': 'DSCF0719',
}


def open_photo(name: str) -> Image.Image:
	im = Image.open(PICTURES / f'{name}.JPG')
	return ImageOps.exif_transpose(im).convert('RGB')


def save_jpeg(im: Image.Image, path: Path) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	# No EXIF is passed through: camera serials and timestamps stay out of the site
	im.save(path, 'JPEG', quality=80, optimize=True, progressive=True)
	print(f'{path.relative_to(ROOT)}  {im.width}x{im.height}  {path.stat().st_size // 1024} KB')


def export_photos() -> None:
	for web_name, camera_name in PHOTOS.items():
		im = open_photo(camera_name)
		im.thumbnail((MASTER_EDGE, MASTER_EDGE), Image.Resampling.LANCZOS)
		save_jpeg(im, IMAGES / f'{web_name}.jpg')


def crop_band(path: Path, top: int, bottom: int) -> Image.Image:
	"""Rows [top, bottom) of an artwork file, trimmed to its visible pixels."""
	im = Image.open(path).convert('RGBA')
	band = im.crop((0, top, im.width, bottom))
	return band.crop(band.getbbox())


def save_png(im: Image.Image, path: Path) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	im.save(path, 'PNG', optimize=True, compress_level=9)
	print(f'{path.relative_to(ROOT)}  {im.width}x{im.height}  {path.stat().st_size // 1024} KB')


def export_brand() -> tuple[Image.Image, Image.Image]:
	# STICKER.png stacks the wordmark twice: cream (rows 140-660), blue (rows 850-1370)
	cream = crop_band(LOGOS / 'STICKER.png', 100, 760)
	blue = crop_band(LOGOS / 'STICKER.png', 760, 1420)
	save_png(cream, BRAND / 'wordmark-cream.png')
	save_png(blue, BRAND / 'wordmark-blue.png')

	save_png(rebreak_tagline(), BRAND / 'tagline-serif.png')
	return cream, blue


def rebreak_tagline() -> Image.Image:
	"""The SIGNAGE.png tagline, re-set as "your neighborhood, / just a little better."

	The artwork breaks after "just"; the site breaks after the comma. Words are moved as-is
	(no re-typesetting), so the official lettering is untouched. Coordinates are in SIGNAGE.png:
	line 1 ink spans rows 909-1039 (baseline 1013), line 2 rows 1100-1203 (baseline 1203).
	"""
	src = Image.open(LOGOS / 'SIGNAGE.png').convert('RGBA')
	your_neighborhood = src.crop((160, 905, 1172, 1042))  # "your neighborhood,"
	just = src.crop((1184, 905, 1380, 1042))  # "just" (baseline 1013 → row 108 of this crop)
	a_little_better = src.crop((472, 1096, 1070, 1207))  # "a little better." (baseline row 107)

	word_gap = 22  # line 2 word space, less the padding already around each crop
	line2_width = just.width + word_gap + a_little_better.width
	width = max(your_neighborhood.width, line2_width)
	line_pitch = 1203 - 1013  # baseline-to-baseline, as on the sign
	baseline1 = 108
	baseline2 = baseline1 + line_pitch

	out = Image.new('RGBA', (width, baseline2 + 40), (0, 0, 0, 0))
	out.alpha_composite(your_neighborhood, ((width - your_neighborhood.width) // 2, 0))
	x = (width - line2_width) // 2
	out.alpha_composite(just, (x, baseline2 - 108))
	out.alpha_composite(a_little_better, (x + just.width + word_gap, baseline2 - 107))
	return out.crop(out.getbbox())


def export_og_image() -> None:
	im = open_photo('DSCF8130')
	og = ImageOps.fit(im, (1200, 630), Image.Resampling.LANCZOS, centering=(0.5, 0.85))
	save_jpeg(og, STATIC / 'images' / 'og-lot7.jpg')


def icon_tile(cream: Image.Image, size: int, padding: float) -> Image.Image:
	"""Cream wordmark centred on a brand-blue square."""
	tile = Image.new('RGBA', (size, size), BRAND_BLUE + (255,))
	mark = cream.copy()
	inner = int(size * (1 - 2 * padding))
	mark.thumbnail((inner, inner), Image.Resampling.LANCZOS)
	tile.alpha_composite(mark, ((size - mark.width) // 2, (size - mark.height) // 2))
	return tile


def export_icons(cream: Image.Image) -> None:
	# The full lockup ("CAFE" included) turns to mush at 16px, so the favicon uses "LOT 7" only
	lot7 = crop_band(LOGOS / 'STICKER.png', 100, 570)
	icon_tile(lot7, 256, 0.12).save(
		STATIC / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)]
	)
	print('static/favicon.ico  16/32/48')
	# iOS rounds the corners itself; keep the mark inside its safe area
	touch = icon_tile(cream, 180, 0.16).convert('RGB')
	touch.save(STATIC / 'apple-touch-icon.png', 'PNG', optimize=True)
	print('static/apple-touch-icon.png  180x180')


if __name__ == '__main__':
	export_photos()
	cream, _ = export_brand()
	export_og_image()
	export_icons(cream)
