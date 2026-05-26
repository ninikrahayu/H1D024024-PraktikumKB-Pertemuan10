import random

def two_point_crossover(parent1, parent2):
    titik1 = random.randint(1, len(parent1) - 2)
    titik2 = random.randint(titik1 + 1, len(parent1) - 1)

    anak1 = parent1[:titik1] + parent2[titik1:titik2] + parent1[titik2:]
    anak2 = parent2[:titik1] + parent1[titik1:titik2] + parent2[titik2:]

    return anak1, anak2