import random

def roulette_wheel_selection(populasi, fitness_populasi):
    total_fitness = sum(fitness_populasi)

    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx

    r = random.random()
    kumulatif = 0

    for i in range(len(populasi)):
        probabilitas = fitness_populasi[i] / total_fitness
        kumulatif += probabilitas

        if r <= kumulatif:
            return populasi[i], i

    return populasi[-1], len(populasi) - 1
