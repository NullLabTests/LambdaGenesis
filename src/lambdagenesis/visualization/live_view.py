from rich.console import Console
from rich.table import Table

console = Console()

def render(world):
    stats = world.stats()

    table = Table(title="LambdaGenesis")

    table.add_column("Metric")
    table.add_column("Value")

    for k, v in stats.items():
        if isinstance(v, float):
            v = round(v, 3)

        table.add_row(k, str(v))

    console.clear()
    console.print(table)

    console.print("\\nTop Molecules:\\n")

    ranked = sorted(
        world.population,
        key=lambda m: m.energy,
        reverse=True
    )

    for mol in ranked[:10]:
        console.print(
            f"[{mol.energy:.2f}] {mol.code}"
        )
