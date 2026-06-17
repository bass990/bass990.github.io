"""Generate og-image.png (1200x630) for LinkedIn / Slack / Twitter share previews."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1200, 630
NAVY = (10, 22, 40)
NAVY_DEEP = (15, 23, 42)
WHITE = (248, 250, 252)
SLATE_300 = (203, 213, 225)
SLATE_400 = (148, 163, 184)
AMBER = (245, 158, 11)

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)

# Subtle diagonal accent bar
for i in range(60):
    alpha = int(20 - i * 0.3)
    if alpha > 0:
        d.line([(0, H - 60 + i), (W, H - 60 + i)], fill=(NAVY_DEEP[0] + alpha, NAVY_DEEP[1] + alpha, NAVY_DEEP[2] + alpha), width=1)

# Amber accent strip on the left
d.rectangle([(0, 0), (8, H)], fill=AMBER)

# Try several font fallbacks (Windows -> arial; mac -> Helvetica; linux -> DejaVu)
def load(size, bold=False):
    candidates = []
    if bold:
        candidates = ["arialbd.ttf", "Helvetica-Bold.ttf", "DejaVuSans-Bold.ttf", "arial.ttf"]
    else:
        candidates = ["arial.ttf", "Helvetica.ttf", "DejaVuSans.ttf"]
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()

eyebrow_font = load(28, bold=True)
name_font = load(76, bold=True)
tag_font = load(36)
meta_font = load(26)

X = 80
y = 110

# EYEBROW
d.text((X, y), "DATA SCIENCE  •  AI ENGINEERING  •  PRODUCT ANALYTICS",
       font=eyebrow_font, fill=AMBER)
y += 60

# NAME
d.text((X, y), "Mamadou Bassirou Diallo", font=name_font, fill=WHITE)
y += 110

# TAGLINE
d.text((X, y), "I build production-shaped ML and AI systems", font=tag_font, fill=SLATE_300)
y += 50
d.text((X, y), "and document them honestly, including where they break.", font=tag_font, fill=SLATE_300)
y += 90

# META
d.text((X, y), "M.S. Business Analytics + AI  •  UT Dallas  •  May 2027",
       font=meta_font, fill=SLATE_400)
y += 38
d.text((X, y), "bass990.github.io  •  github.com/bass990",
       font=meta_font, fill=SLATE_400)

out = Path(__file__).parent / "og-image.png"
img.save(out, "PNG", optimize=True)
print(f"wrote {out} ({out.stat().st_size} bytes, {W}x{H})")
