from PIL import Image, ImageDraw, ImageFont

W, H = 2000, 1400
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 40)
    small = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 32)
except OSError:
    font = small = ImageFont.load_default()

# Border and title block
d.rectangle([40, 40, W - 40, H - 40], outline="black", width=5)
d.rectangle([W - 700, H - 260, W - 40, H - 40], outline="black", width=3)
d.text((W - 680, H - 240), "PART: SHAFT BRACKET", fill="black", font=font)
d.text((W - 680, H - 180), "SCALE 1:2   SHEET 1/1", fill="black", font=small)

# Main part: plate with holes
d.rectangle([400, 400, 1400, 900], outline="black", width=6)
for cx, cy in [(550, 550), (1250, 550), (550, 750), (1250, 750)]:
    d.ellipse([cx - 50, cy - 50, cx + 50, cy + 50], outline="black", width=5)
d.ellipse([850, 550, 950, 650], outline="black", width=5)
d.line([300, 650, 1500, 650], fill="black", width=2)
d.line([900, 330, 900, 970], fill="black", width=2)

# Dimension lines and text
d.line([400, 1000, 1400, 1000], fill="black", width=3)
d.text((850, 1020), "1000", fill="black", font=font)
d.line([1500, 400, 1500, 900], fill="black", width=3)
d.text((1520, 620), "500", fill="black", font=font)
d.text((460, 480), "4x O100 THRU", fill="black", font=small)
d.text((420, 1100), "R12   39.5   +0.05/-0.02", fill="black", font=small)
d.text((420, 1160), "Ra 1.6", fill="black", font=small)

# Balloons
balloons = [
    (1700, 300, 1400, 400, "1"),
    (1700, 600, 1250, 550, "2"),
    (200, 300, 400, 400, "3"),
    (200, 800, 550, 750, "4"),
    (900, 200, 900, 400, "5"),
]
r = 45
for bx, by, tx, ty, n in balloons:
    d.line([bx, by, tx, ty], fill="black", width=3)
    d.ellipse([bx - r, by - r, bx + r, by + r], fill="white", outline="black", width=4)
    d.text((bx - 10, by - 22), n, fill="black", font=font)

img.save("test_drawing.png")
img.save("test_drawing.pdf")
print("Saved test_drawing.png and test_drawing.pdf")
