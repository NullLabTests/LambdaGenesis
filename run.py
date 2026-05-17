import os
import sys
import time

sys.path.append(
    os.path.abspath('src')
)

from lambdagenesis.core.world import World
from lambdagenesis.visualization.live_view import render

world = World(population=100)

while True:
    world.step()
    render(world)
    time.sleep(0.12)
