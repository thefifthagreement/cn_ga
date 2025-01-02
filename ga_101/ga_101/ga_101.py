import random

# it gives you the alphabet from which the answer is composed
# the length of the anwser and the mean score of a population
from ga_101.answer import ALPHABET, answer_len, get_mean_score, is_answer  # noqa:F401

# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)


# TODO Create a chromosome as a string of the right size
def create_chromosome(chrom_size):
    return " " * chrom_size


# TODO Select the best individuals
def selection(population, elite_percent, low_class_percent):
    return population[:2]


# TODO Select half of the parent genetic material
def crossover(parent1, parent2):
    return parent1


# TODO random gene mutation
def mutation(chrom):
    return chrom


# create the base population
def create_population(pop_size, chrom_size):
    return [create_chromosome(chrom_size) for _ in range(pop_size)]


# create a new generation
def generation(population, elite_percent, low_class_percent, mutate_percent):

    # selection
    select = selection(population, elite_percent, low_class_percent)

    # reproduction
    # As long as we need individuals in the new population, fill with children
    children = []

    # constant size of population
    while len(children) < len(population) - len(select):
        ## crossover
        parents = random.sample(select, k=2)  # randomly selected
        child = crossover(parents[0], parents[1])

        # TODO mutation: use the mutate percentage
        child = mutation(child)
        children.append(child)

    # return the new generation
    return select + children


# TODO Define the population size and the maximum number of iterations
def algorithm(population_size, elite_percent, low_class_percent, mutate_percent, max_iter):
    chrom_size = answer_len()

    # create the base population
    population = create_population(population_size, chrom_size)

    iteration = 0
    max_score = 0.0
    answers = []

    # while a solution has not been found :
    while not answers and iteration < max_iter:
        iteration += 1

        # create the next generation using the generation(population) function
        population = generation(
            population, elite_percent, low_class_percent, mutate_percent
        )

        # display the average score of the population
        score = get_mean_score(population)
        max_score = max(max_score, score)

        if iteration % 50 == 0:
            print(f"generation {iteration}: {score:.2%}")

        # check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)

    # print the solution
    if answers:
        print(f"Well done the answer was found at iteration {iteration}:\n{answers[0]}")
    else:
        print(f"No solution found... (best score {max_score:.2%})")
