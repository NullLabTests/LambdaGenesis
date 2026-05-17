import uuid
import random
import networkx as nx

TOKENS = [
    'λ',
    'APP',
    'x',
    'y',
    'z',
    'S',
    'K',
    'I'
]

class MoleculeGraph:
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
        self.graph = nx.DiGraph()
        self.energy = random.uniform(10, 30)
        self.age = 0
        self.parent_ids = []

    @classmethod
    def random(cls, size=8):
        mol = cls()

        for i in range(size):
            mol.graph.add_node(
                i,
                token=random.choice(TOKENS)
            )

        nodes = list(mol.graph.nodes)

        for node in nodes:
            target = random.choice(nodes)

            if node != target:
                mol.graph.add_edge(node, target)

        return mol

    def mutate(self):
        nodes = list(self.graph.nodes)

        if not nodes:
            return

        node = random.choice(nodes)

        self.graph.nodes[node]['token'] = random.choice(TOKENS)

    def complexity(self):
        return (
            self.graph.number_of_nodes()
            + self.graph.number_of_edges()
        )

    def decay(self):
        self.energy -= 0.15
        self.age += 1

    def alive(self):
        return self.energy > 0

    def summary(self):
        return {
            'id': self.id,
            'nodes': self.graph.number_of_nodes(),
            'edges': self.graph.number_of_edges(),
            'energy': round(self.energy, 2),
            'age': self.age,
            'complexity': self.complexity()
        }
