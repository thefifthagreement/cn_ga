import click

from ga_101.ga_101 import algorithm


@click.command()
@click.argument("population_size", type=click.INT)
@click.argument("elite_percent", type=click.FLOAT)
@click.argument("max_iter", type=click.INT)
@click.argument("low_class_percent", type=click.FLOAT)
@click.argument("mutate_percent", type=click.FLOAT)
def cli(population_size, elite_percent, max_iter, low_class_percent, mutate_percent):
    algorithm(population_size, elite_percent, max_iter, low_class_percent, mutate_percent)
