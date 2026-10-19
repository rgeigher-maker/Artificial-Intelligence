import random


def reproduce(pop1, pop2):
    c = random.randint(1, len(pop1) - 1)
    return pop1[:c] + pop2[c:]


def mutate(child):
    i = random.randint(0, len(child) - 1)
    return child[:i] + ('1' if child[i] == '0' else '0') + child[i + 1:]


def geneticAlgorithm(population, fitness):
    for generation in range(20):
        scores = [fitness(ind) for ind in population]
        total = sum(scores)
        weights = [s / total for s in scores] if total > 0 else [1 / len(population)] * len(population)

        population2 = []
        for _ in range(len(population)):
            p1, p2 = random.choices(population, weights=weights, k=2)

            child = reproduce(p1, p2)
            if random.random() < 0.1:
                child = mutate(child)

            population2.append(child)

        population = population2

    return max(population, key=fitness)


if __name__ == "__main__":
    fitness_fn = lambda ind: int(ind, 2) ** 2
    initial_pop = ["10011", "01000", "11000", "01101"]

    best = geneticAlgorithm(initial_pop, fitness_fn)
    print(f"Best Individual: {best} (Decimal: {int(best, 2)})")








