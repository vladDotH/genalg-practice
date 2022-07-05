import random

from src.model import Population


# Отбор усечением (N раз выбирается особь из тех кто попал под threshold)
def trunc(pop: Population, N: int, threshold: float) -> Population:
    return Population.list(
        pop.dists,
        random.choices(
            pop.sorted()[:int(len(pop) * threshold) + 1], k=N
        )
    )


# Элитарный отбор (отбор N самых лучших)
def elite(pop: Population, N: int) -> Population:
    return Population.list(
        pop.dists, pop.sorted()[:N]
    )
