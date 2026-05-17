import random

from lambdagenesis.graphs.molecule_graph import MoleculeGraph
from lambdagenesis.rewrite.reduction import combine
from lambdagenesis.spatial.grid import SpatialGrid
from lambdagenesis.history.lineage import LineageTracker
from lambdagenesis.metrics.entropy import shannon_entropy

class World:
    def __init__(self, population=80):
        self.population = []
        self.tick = 0

        self.grid = SpatialGrid()
        self.lineage = LineageTracker()

        for _ in range(population):
            mol = MoleculeGraph.random()
            self.population.append(mol)
            self.grid.place(mol)
            self.lineage.register(mol)

    def step(self):
        self.tick += 1

        next_population = []

        id_map = {
            m.id: m
            for m in self.population
        }

        for mol in self.population:
            self.grid.move(mol.id)

            neighbors = self.grid.neighbors(mol.id)

            if neighbors:
                partner_id = random.choice(neighbors)

                if partner_id in id_map:
                    partner = id_map[partner_id]

                    child = combine(mol, partner)

                    self.grid.place(child)
                    self.lineage.register(child)

                    next_population.append(child)

            mol.decay()

            if mol.alive():
                next_population.append(mol)

        if len(next_population) < 40:
            for _ in range(20):
                m = MoleculeGraph.random()
                self.grid.place(m)
                self.lineage.register(m)
                next_population.append(m)

        self.population = next_population[:200]

    def entropy(self):
        tokens = []

        for mol in self.population:
            for _, data in mol.graph.nodes(data=True):
                tokens.append(data['token'])

        return shannon_entropy(tokens)

    def stats(self):
        complexity = sum(
            m.complexity()
            for m in self.population
        )

        avg_energy = sum(
            m.energy
            for m in self.population
        ) / len(self.population)

        return {
            'tick': self.tick,
            'population': len(self.population),
            'avg_energy': round(avg_energy, 3),
            'avg_complexity': round(
                complexity / len(self.population),
                3
            ),
            'entropy': round(self.entropy(), 3),
            'lineages': self.lineage.lineage_count()
        }
