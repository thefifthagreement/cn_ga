from deap import algorithms
from deap import base
from deap import creator
from deap import tools

import random
import numpy

import ga_reinforcement_deap.mountain_car as mountain_car

# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# create a Mountain Car instance:
car = mountain_car.MountainCar(RANDOM_SEED)

toolbox = base.Toolbox()

# define a single objective, maximizing fitness strategy:
# TODO check that the definition suits the problem
creator.create("FitnessMax", base.Fitness, weights=(1.0,)) 

# TODO adapt the fitness based on the fitness you defined:
creator.create("Individual", list, fitness=creator.FitnessMax)

# TODO create an operator that fits the definition of an Individual:
# HINT: what are the possible actions ?
toolbox.register("myOperator", random.randint, 0, 1)

# create an operator that generates a list of individuals:
toolbox.register("individualCreator",
                 tools.initRepeat,
                 creator.Individual,
                 toolbox.myOperator, # TODO change the name accordingly
                 len(car))

# create the population operator to generate a list of individuals:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# fitness calculation
def getCarScore(individual):
    return car.getScore(individual),  # return a tuple

toolbox.register("evaluate", getCarScore)

toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxTwoPoint)

# TODO select a mutation method that suits the problem
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/len(car))


# Genetic Algorithm flow:
def algorithm(
    population_size, elite_percent, max_generation, crossover_percent, mutation_percent
):

    # create initial population (generation 0):
    population = toolbox.populationCreator(n=population_size)

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", numpy.min)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(population_size * elite_percent) if elite_percent > 0 else None

    # perform the Genetic Algorithm flow with hof feature added:
    population, logbook = algorithms.eaSimple(population,
                                                      toolbox,
                                                      cxpb=crossover_percent,
                                                      mutpb=mutation_percent,
                                                      ngen=max_generation,
                                                      stats=stats,
                                                      halloffame=hof,
                                                      verbose=True)

    # print best solution:
    if hof:
        best = hof.items[0]
        print()
        print("Best Solution = ", best)
        print("Best Fitness = ", best.fitness.values[0])

        # save best solution for a replay:
        car.saveActions(best)

        # replay the best solution
        best_car = mountain_car.MountainCar(RANDOM_SEED, render_mode="human")
        best_car.replaySavedActions()
