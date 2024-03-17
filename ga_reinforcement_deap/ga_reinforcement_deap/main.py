import click

from ga_reinforcement_deap.ga_reinforcement_deap import algorithm


@click.command()
@click.argument("population_size", type=click.INT)
@click.argument("elite_percent", type=click.FLOAT)
@click.argument("max_generation", type=click.INT)
@click.argument("crossover_percent", type=click.FLOAT)
@click.argument("mutation_percent", type=click.FLOAT)
def cli(population_size, elite_percent, max_generation, crossover_percent, mutation_percent):
    algorithm(
        population_size,
        elite_percent,
        max_generation,
        crossover_percent,
        mutation_percent,
    )
