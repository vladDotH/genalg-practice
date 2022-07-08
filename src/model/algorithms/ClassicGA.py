from typing import Callable
import random

from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Region import Region
from src.model.core.Solution import Solution


class ClassicGA(GA):
    def __init__(self, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
                 recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
                 mutationer: Callable[[Solution, GA], Solution] = None,
                 oSelector: Callable[[Population, GA], Population] = None):
        super().__init__(pSelector, recombinator, mutationer, oSelector)

    def start(self, reg: Region) -> None:
        super().start(reg)

    def parentsSelect(self) -> None:
        self.parents = self.pSelector(self.population, self)

    def crossover(self) -> None:
        self.children = Population(self.reg)
        for p in self.parents:
            if random.random() < self.params.rprob:
                self.params.cstart = random.randint(0, len(self.reg) - 1)
                self.params.csize = random.randint(1, len(self.reg) - 2)
                self.children.extend(self.recombinator(p[0], p[1], self))
            else:
                self.children.extend(p)

    def mutation(self) -> None:
        self.mutChildren = Population(self.reg)
        for c in self.children:
            if random.random() < self.params.mprob:
                self.params.mgen1, self.params.mgen2 = sorted([random.randint(0, len(self.reg) - 1) for i in range(2)])
                self.mutChildren.append(self.mutationer(c, self))
            else:
                self.mutChildren.append(c)

    def offspringSelect(self) -> None:
        self.tempPop = Population(self.reg)
        self.tempPop.extend(self.population)
        self.tempPop.extend(self.mutChildren)
        self.offspring = self.oSelector(self.tempPop, self)

    def newPopulation(self) -> None:
        super().newPopulation()
        self.population = self.offspring
        self.parents = self.children = self.mutChildren = self.tempPop = self.offspring = None

    def __str__(self):
        return 'Классический ГА:\n' + super().__str__()

    def __repr__(self):
        return str(self)
