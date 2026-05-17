import random
from PIL import Image, ImageDraw

WIDTH = 1200
HEIGHT = 700
img = Image.new("RGB", (WIDTH, HEIGHT), color=(5, 5, 12))
draw = ImageDraw.Draw(img)

for _ in range(4000):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.randint(1, 4)
    color = (
        random.randint(0, 80),
        random.randint(140, 255),
        random.randint(140, 255)
    )
    draw.ellipse((x, y, x+r, y+r), fill=color)

draw.text((40, 40), "LambdaGenesis Ecology Snapshot", fill=(255, 255, 255))
img.save("media/screenshots/ecology.png")
