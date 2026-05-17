import random

class SpatialGrid:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height

        self.cells = {}

    def random_position(self):
        return (
            random.randint(0, self.width - 1),
            random.randint(0, self.height - 1)
        )

    def place(self, molecule):
        pos = self.random_position()
        self.cells[molecule.id] = pos

    def move(self, molecule_id):
        if molecule_id not in self.cells:
            return

        x, y = self.cells[molecule_id]

        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])

        nx = max(0, min(self.width - 1, x + dx))
        ny = max(0, min(self.height - 1, y + dy))

        self.cells[molecule_id] = (nx, ny)

    def neighbors(self, molecule_id, radius=2):
        if molecule_id not in self.cells:
            return []

        x, y = self.cells[molecule_id]

        result = []

        for mid, pos in self.cells.items():
            if mid == molecule_id:
                continue

            px, py = pos

            if abs(px - x) <= radius and abs(py - y) <= radius:
                result.append(mid)

        return result
