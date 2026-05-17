import random
import imageio.v2 as imageio
from PIL import Image, ImageDraw

frames = []
for frame in range(24):
    img = Image.new("RGB", (640, 400), color=(5, 5, 12))
    draw = ImageDraw.Draw(img)
    for _ in range(900):
        x = random.randint(0, 640)
        y = random.randint(0, 400)
        r = random.randint(1, 3)
        color = (0, random.randint(100, 255), random.randint(120, 255))
        draw.ellipse((x, y, x+r, y+r), fill=color)
    path = f"media/tmp/frame_{frame}.png"
    img.save(path)
    frames.append(imageio.imread(path))

imageio.mimsave("media/gifs/ecology.gif", frames, fps=8)
