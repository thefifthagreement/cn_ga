import string

ALPHABET = string.ascii_letters + " !'.,"

KEY = "Genetic Algorithms are powerful! It's due to their ability to evolve solutions through a process of Selection, Crossover, and Mutation!"  # noqa: E501


# TODO compare a chromosome with the solution
# => how many character are in the correct position?
def get_score(chrom) -> float:
    global KEY

    return 0.0


def get_mean_score(population) -> float:
    global KEY

    # compute the average score of the population
    scores = [get_score(chrom) for chrom in population]
    return sum(scores) / len(population)


def is_answer(chrom) -> bool:
    global KEY

    return chrom == KEY


def answer_len() -> int:
    global KEY
    return len(KEY)
