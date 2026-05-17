import random

from lambdagenesis.chemistry.symbolic_chemistry import (
    random_molecule,
    react
)

class World:
    def __init__(self, population=100):
        self.population = [
            random_molecule()
            for _ in range(population)
        ]

        self.tick_count = 0

    def step(self):
        self.tick_count += 1

        random.shuffle(self.population)

        new_population = []

        for i in range(
            0,
            len(self.population) - 1,
            2
        ):
            a = self.population[i]
            b = self.population[i + 1]

            child = react(a, b)

            a.decay()
            b.decay()
            child.decay()

            if a.alive():
                new_population.append(a)

            if b.alive():
                new_population.append(b)

            if child.alive():
                new_population.append(child)

        while len(new_population) < 50:
            new_population.append(
                random_molecule()
            )

        self.population = new_population

    def stats(self):
        return {
            "tick": self.tick_count,
            "population": len(self.population),
            "avg_energy": (
                sum(m.energy for m in self.population)
                / len(self.population)
            ),
            "avg_length": (
                sum(len(m.code) for m in self.population)
                / len(self.population)
            )
        }
