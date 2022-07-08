from typing import Callable
import random

from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Region import Region
from src.model.core.Solution import Solution


class Genitor(GA):
    def __init__(self, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
                 recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
                 mutationer: Callable[[Solution, GA], Solution] = None,
                 oSelector: Callable[[Population, GA], Population] = None):
        super().__init__(pSelector, recombinator, mutationer, oSelector)

    def start(self, reg: Region) -> None:
        super().start(reg)

    def parentsSelect(self) -> None:
        self.parents = [tuple(Solution(self.reg, i) for i in random.sample(self.population, 2))]

    def crossover(self) -> None:
        self.children = Population(self.reg)
        self.children.append(
            self.recombinator(
                self.parents[0][0], self.parents[0][1], self
            )[random.randint(0, 1)]
        )

    def mutation(self) -> None:
        self.mutChildren = Population(self.reg)
        c = self.children[0]
        if random.random() < self.params.mprob:
            self.mutChildren.append(self.mutationer(c, self))
        else:
            self.mutChildren.append(c)

    def offspringSelect(self) -> None:
        pass
        # self.offspring = Population(self.reg)
        # self.offspring.extend(self.population)
        # self.offspring.extend(self.mutChildren)
        # self.nextPopulation = self.oSelector(self.offspring, self)

    def newPopulation(self) -> None:
        self.population = self.nextPopulation
        self.parents = self.children = self.mutChildren = self.offspring = None

    def checkParam(self, attr: str) -> None:
        super().checkParam(attr)
