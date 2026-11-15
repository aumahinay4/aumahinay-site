"""Link-preview pictures for blog posts (Facebook, Messenger, Viber, LinkedIn, X).

Each post that has a picture gets its own 1200x630 card: the site's share card
(static/share.jpg, with its navy stripe, faint arches, rainbow edge and the
"Butch Mahinay · aumahinay.dev" line) with the post's picture in the middle
instead of the home illustration and slogan. The picture stays inside the
centre square, so phones that crop link previews to a square still show it.

Cards are made at build time into static/share/ (not kept in git). If Pillow
is missing, card_for() returns None and the page falls back to share.jpg.
"""
from pathlib import Path

STATIC = Path(__file__).parent / "static"
BASE = STATIC / "share.jpg"
OUT = STATIC / "share"
VERSION = "1"  # bump to remake every card after changing the layout below

# the area of share.jpg that holds the home illustration, slogan and name line (cleared, then refilled)
CLEAR = (322, 108, 880, 520)
NAME_LINE = (395, 455, 805, 512)  # "Butch Mahinay · aumahinay.dev" with his ringed photo
CARD_MIDDLE = 307                 # the white card runs from y=30 to y=585
MAX_W, MAX_H = 540, 400           # post picture size limit: inside the centre square, clear of the arches
GAP = 22                          # space between the picture and the name line


def card_for(photo):
    """Path (relative to static/) of the share card for a post picture, or None if it can't be made."""
    src = STATIC / photo
    if not src.exists() or not BASE.exists():
        return None
    name = f"share/{Path(photo).stem}.jpg"
    out = STATIC / name
    stamp = out.with_suffix(".v")
    key = f"{VERSION} {src.stat().st_size} {src.stat().st_mtime_ns} {BASE.stat().st_size}"
    if out.exists() and stamp.exists() and stamp.read_text() == key:
        return name
    try:
        from PIL import Image, ImageDraw, ImageFilter
    except ImportError:
        return name if out.exists() else None
    card = Image.open(BASE).convert("RGB")
    name_line = card.crop(NAME_LINE)
    bg = card.getpixel((600, 75))  # the card's own white
    ImageDraw.Draw(card).rectangle(CLEAR, fill=bg)
    pic = Image.open(src).convert("RGB")
    scale = min(MAX_W / pic.width, MAX_H / pic.height)
    pic = pic.resize((round(pic.width * scale), round(pic.height * scale)), Image.LANCZOS)
    # picture and name line together, centred up and down in the white card
    top = CARD_MIDDLE - (pic.height + GAP + name_line.height) // 2
    x, y = 600 - pic.width // 2, top
    card.paste(name_line, (NAME_LINE[0], y + pic.height + GAP))
    # a soft shadow and a thin border, like the site's picture frames
    shadow = Image.new("L", card.size, 0)
    ImageDraw.Draw(shadow).rectangle((x + 2, y + 6, x + pic.width + 2, y + pic.height + 6), fill=60)
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    card.paste(Image.new("RGB", card.size, (11, 33, 73)), (0, 0), shadow)
    card.paste(pic, (x, y))
    ImageDraw.Draw(card).rectangle((x - 1, y - 1, x + pic.width, y + pic.height), outline=(219, 227, 241))
    OUT.mkdir(exist_ok=True)
    card.save(out, "JPEG", quality=88, optimize=True, progressive=True)
    stamp.write_text(key)
    return name
