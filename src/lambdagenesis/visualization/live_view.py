from rich.console import Console
from rich.table import Table

console = Console()

def render(world):
    console.clear()

    stats = world.stats()

    table = Table(title="LambdaGenesis V2")

    table.add_column("Metric")
    table.add_column("Value")

    for k, v in stats.items():
        table.add_row(k, str(v))

    console.print(table)

    console.print("\\nTop Structures\\n")

    ranked = sorted(
        world.population,
        key=lambda m: m.complexity(),
        reverse=True
    )

    for mol in ranked[:8]:
        s = mol.summary()

        console.print(
            f"[{s['id']}] "
            f"complexity={s['complexity']} "
            f"energy={s['energy']}"
        )
