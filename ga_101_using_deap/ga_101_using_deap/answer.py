import string
import pickle


ALPHABET = string.ascii_letters + " !'.,"


# read the key from a file
def get_key():
    with open("./ga_101_using_deap/key.pkl", "rb") as f:
        return pickle.load(f)


# TODO compare a chromosome with the solution
# => how many character are in the correct position?
def get_score(chrom) -> float:
    return 0.0


def get_mean_score(population) -> float:
    # compute the average score of the population
    scores = [get_score(chrom) for chrom in population]
    return sum(scores) / len(population)


def is_answer(chrom) -> bool:
    return chrom == get_key()


def answer_len() -> int:
    return len(get_key())
