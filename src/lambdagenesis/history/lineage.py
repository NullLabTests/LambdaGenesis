import networkx as nx

class LineageTracker:
    def __init__(self):
        self.graph = nx.DiGraph()

    def register(self, molecule):
        self.graph.add_node(
            molecule.id,
            complexity=molecule.complexity(),
            energy=molecule.energy
        )

        for parent in molecule.parent_ids:
            self.graph.add_edge(parent, molecule.id)

    def lineage_count(self):
        return self.graph.number_of_nodes()
