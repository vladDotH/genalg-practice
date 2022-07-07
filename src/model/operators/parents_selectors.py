import random
from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Solution import Solution


# Панмиксия - каждой особи сопоставляется другая случайная особь (в т.ч. сама особь)
def panmixion(pop: Population, ga: GA = None) -> list[tuple[Solution, Solution]]:
    return [(pop[i], pop[random.randint(0, len(pop) - 1)]) for i in range(len(pop))]


# Турнирный отбор: N раз выбирается лучшая особь из случайных tsize выбранных, далее применяется панмиксия
def tournament(pop: Population, ga: GA) -> list[tuple[Solution, Solution]]:
    ga.checkParam('tsize')

    return panmixion(
        Population(
            pop.reg,
            [Population(pop.reg, random.sample(pop, ga.params.tsize)).min() for i in range(len(pop))]
        )
    )


# Рулетка: N раз выбирается случайная особь (выбор с весами), к полученной выборке применяется панмиксия
def roulette(pop: Population, ga: GA = None) -> list[tuple[Solution, Solution]]:
    weights = [p.rF() for p in pop]
    return panmixion(
        Population(
            pop.reg,
            Population(pop.reg, random.choices(pop, weights, k=len(pop)))
        )
    )
