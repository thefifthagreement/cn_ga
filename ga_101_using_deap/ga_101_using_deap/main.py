import click

from ga_101_using_deap.ga_101_using_deap import algorithm


@click.command()
@click.argument("population_size", type=click.INT)
@click.argument("elite_percent", type=click.FLOAT)
@click.argument("max_generation", type=click.INT)
@click.argument("crossover_percent", type=click.FLOAT)
@click.argument("mutation_percent", type=click.FLOAT)
def cli(
    population_size: int,
    elite_percent: float,
    max_generation: int,
    crossover_percent: float,
    mutation_percent: float,
):
    algorithm(
        population_size,
        elite_percent,
        max_generation,
        crossover_percent,
        mutation_percent,
    )


if __name__ == "__main__":
    cli()
