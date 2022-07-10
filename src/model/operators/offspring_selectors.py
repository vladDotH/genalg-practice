import random
from src.model.core.Population import Population
from src.model.algorithms.GA import GA


# Отбор усечением (psize раз выбирается особь из тех кто попал под threshold)
def trunc(pop: Population, ga: GA) -> Population:
    for a in ['psize', 'threshold']:
        ga.checkParam(a)
    return Population(
        pop.reg,
        random.choices(
            pop.sorted()[:int(len(pop) * ga.params.threshold) + 1], k=ga.params.psize
        )
    )


# Элитарный отбор (отбор psize самых лучших)
def elite(pop: Population, ga: GA) -> Population:
    ga.checkParam('psize')
    return Population(
        pop.reg, pop.sorted()[:ga.params.psize]
    )
