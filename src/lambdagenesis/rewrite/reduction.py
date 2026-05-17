import random
import networkx as nx

from lambdagenesis.graphs.molecule_graph import MoleculeGraph

def combine(a: MoleculeGraph, b: MoleculeGraph):
    child = MoleculeGraph()

    g = nx.disjoint_union(a.graph, b.graph)

    child.graph = g

    nodes = list(g.nodes)

    for _ in range(random.randint(1, 3)):
        n1 = random.choice(nodes)
        n2 = random.choice(nodes)

        if n1 != n2:
            child.graph.add_edge(n1, n2)

    if random.random() < 0.4:
        child.mutate()

    child.energy = (
        a.energy + b.energy
    ) / 3

    child.parent_ids = [
        a.id,
        b.id
    ]

    a.energy *= 0.8
    b.energy *= 0.8

    return child
