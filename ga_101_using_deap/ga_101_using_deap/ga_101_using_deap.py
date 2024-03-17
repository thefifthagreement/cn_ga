import random

import matplotlib.pyplot as plt
import numpy
import seaborn as sns
from deap import algorithms, base, creator, tools

# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# TODO define the size of an individual
INDIVIDUAL_SIZE = 2

toolbox = base.Toolbox()

# TODO create an operator called 'anyLetter' that randomly returns any letter from ALPHABET
# Operator example: the following creates an operator that randomly returns 0 or 1:
toolbox.register("anyLetter", random.randint, 0, 1)

# define a single objective, maximizing fitness strategy:
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# create the Individual class based on list:
creator.create("Individual", list, fitness=creator.FitnessMax)

# create the individual operator to fill up an Individual instance:
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.anyLetter, INDIVIDUAL_SIZE)

# create the population operator to generate a list of individuals:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

# TODO fitness calculation
# compute the score of the individual
# return a tuple (score,)
def ga101Fitness(individual):
    return (0,)  # return a tuple


toolbox.register("evaluate", ga101Fitness)

# TODO define the selection method
toolbox.register("select", tools.selRandom)

# TODO define the crossover method:
toolbox.register("mate", tools.cxOnePoint)

# TODO define the mutation method
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0 / INDIVIDUAL_SIZE)

def algorithm(
    population_size, elite_percent, max_generation, crossover_percent, mutation_percent
):

    # create initial population (generation 0):
    population = toolbox.populationCreator(n=population_size)

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", numpy.max)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(population_size * elite_percent) if elite_percent > 0 else None

    # perform the Genetic Algorithm flow with hof feature added:
    population, logbook = algorithms.eaSimple(
        population,
        toolbox,
        cxpb=crossover_percent,
        mutpb=mutation_percent,
        ngen=max_generation,
        stats=stats,
        halloffame=hof,
        verbose=True,
    )

    # print best solution found:
    if hof:
        best = hof.items[0]
        print("-- Best Ever Individual = ", "".join(best))
        print("-- Best Ever Fitness = ", f"{best.fitness.values[0]:.2%}")

    # extract statistics:
    maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")

    # plot statistics:
    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, color="red")
    plt.plot(meanFitnessValues, color="green")
    plt.xlabel("Generation")
    plt.ylabel("Max / Average Fitness")
    plt.title("Max and Average Fitness over Generations")

    plt.show()
