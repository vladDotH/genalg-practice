from typing import Callable
import random
from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Region import Region
from src.model.core.Solution import Solution


# ГА-Генитор
class Genitor(GA):
    def __init__(self, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
                 recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
                 mutationer: Callable[[Solution, GA], Solution] = None,
                 oSelector: Callable[[Population, GA], Population] = None):
        super().__init__(pSelector, recombinator, mutationer, oSelector)

    def start(self, reg: Region) -> None:
        super().start(reg)

    def parentsSelect(self) -> None:
        super().parentsSelect()
        self.parents = [tuple(Solution(self.reg, i) for i in random.sample(self.population, 2))]

    def crossover(self) -> None:
        super().crossover()
        self.children = Population(self.reg)
        self.params.cstart = random.randint(0, len(self.reg) - 1)
        self.params.csize = random.randint(int(self.N * self.params.minR), int(self.N * self.params.maxR))
        self.children.append(
            self.recombinator(
                self.parents[0][0], self.parents[0][1], self
            )[random.randint(0, 1)]
        )

    def mutation(self) -> None:
        super().mutation()
        self.mutChildren = Population(self.reg)
        c = self.children[0]
        if random.random() < self.params.mprob:
            self.params.mgen1, self.params.mgen2 = sorted([random.randint(0, len(self.reg) - 1) for i in range(2)])
            self.mutChildren.append(self.mutationer(c, self))
        else:
            self.mutChildren.append(c)

    def offspringSelect(self) -> None:
        super().offspringSelect()
        self.offspring = Population(self.reg)
        self.offspring.extend(self.population)
        self.offspring[self.offspring.index(self.offspring.max())] = self.mutChildren[0]

    def newPopulation(self) -> None:
        super().newPopulation()
        self.population = self.offspring
        self.parents = self.children = self.mutChildren = self.offspring = None

    def __str__(self) -> str:
        return 'Генитор:\n' + super().__str__()

    def __repr__(self) -> str:
        return str(self)
