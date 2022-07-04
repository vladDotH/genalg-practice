import random

from src.model.core.Population import Population
from src.model.core.Solution import Solution


# Панмиксия - каждой особи сопоставляется другая случайная особь (в т.ч. сама особь)
def panmixion(pop: Population) -> list[tuple[Solution, Solution]]:
    return [(pop[i], pop[random.randint(0, len(pop) - 1)]) for i in range(len(pop))]


# Турнирный отбор: N раз выбирается лучшая особь из случайных tsize выбранных, далее применяется панмиксия
def tournament(tsize: int, pop: Population) -> list[tuple[Solution, Solution]]:
    return panmixion(
        Population.list(
            pop.dists,
            [Population.list(pop.dists, random.sample(pop, tsize)).min() for i in range(len(pop))]
        )
    )


# Рулетка: N раз выбирается случайная особь (выбор с весами), к полученной выборке применяется панмиксия
def roulette(pop: Population) -> list[tuple[Solution, Solution]]:
    weights = [p.rF() for p in pop]
    return panmixion(
        Population.list(
            pop.dists,
            random.choices(pop, weights, k=len(pop))
        )
    )
