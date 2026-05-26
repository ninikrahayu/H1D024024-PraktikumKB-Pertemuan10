import random

def swap_mutation(kromosom):
    kromosom = list(kromosom)

    posisi1, posisi2 = random.sample(range(len(kromosom)), 2)

    kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]

    return kromosom