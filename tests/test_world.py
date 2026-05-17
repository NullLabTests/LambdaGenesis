import os
import sys

sys.path.append(
    os.path.abspath('src')
)

from lambdagenesis.core.world import World

def test_world_runs():
    world = World(population=20)

    for _ in range(10):
        world.step()

    stats = world.stats()

    assert stats['population'] > 0
