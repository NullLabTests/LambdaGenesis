import random
from dataclasses import dataclass

TOKENS = ['λ', 'x', 'y', 'z', '.', '(', ')']

@dataclass
class Molecule:
    code: str
    energy: float
    age: int = 0

    def mutate(self):
        if not self.code:
            return

        idx = random.randint(0, len(self.code) - 1)
        replacement = random.choice(TOKENS)

        self.code = (
            self.code[:idx]
            + replacement
            + self.code[idx + 1:]
        )

    def decay(self):
        self.energy -= 0.1
        self.age += 1

    def alive(self):
        return self.energy > 0


def random_molecule(length=12):
    return Molecule(
        code=''.join(random.choice(TOKENS) for _ in range(length)),
        energy=random.uniform(5.0, 20.0)
    )


def react(a: Molecule, b: Molecule):
    midpoint_a = len(a.code) // 2
    midpoint_b = len(b.code) // 2

    child_code = (
        a.code[:midpoint_a]
        + b.code[midpoint_b:]
    )

    child = Molecule(
        code=child_code,
        energy=(a.energy + b.energy) / 4
    )

    if random.random() < 0.30:
        child.mutate()

    a.energy *= 0.7
    b.energy *= 0.7

    return child
