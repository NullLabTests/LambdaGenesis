from PIL import Image
from PIL import ImageDraw

WIDTH = 1600
HEIGHT = 500

img = Image.new(
    'RGB',
    (WIDTH, HEIGHT),
    color=(5, 5, 12)
)

ctx = ImageDraw.Draw(img)

for i in range(1200):
    x = (i * 37) % WIDTH
    y = (i * 91) % HEIGHT

    r = (i % 6) + 1

    ctx.ellipse(
        (x, y, x + r, y + r),
        fill=(0, 255, 180)
    )

ctx.text(
    (120, 200),
    'LambdaGenesis V2',
    fill=(255, 255, 255)
)

ctx.text(
    (120, 250),
    'Symbolic Ecology / Artificial Life',
    fill=(120, 255, 220)
)

img.save('assets/banner.png')
