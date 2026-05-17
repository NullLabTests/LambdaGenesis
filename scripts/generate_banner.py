from PIL import Image
from PIL import ImageDraw

WIDTH = 1200
HEIGHT = 400

img = Image.new(
    "RGB",
    (WIDTH, HEIGHT),
    color=(10, 10, 20)
)

draw = ImageDraw.Draw(img)

for i in range(400):
    x = (i * 37) % WIDTH
    y = (i * 91) % HEIGHT

    r = 2 + (i % 4)

    draw.ellipse(
        (x, y, x + r, y + r),
        fill=(0, 255, 180)
    )

draw.text(
    (60, 160),
    "LambdaGenesis",
    fill=(255, 255, 255)
)

img.save("assets/banner.png")
