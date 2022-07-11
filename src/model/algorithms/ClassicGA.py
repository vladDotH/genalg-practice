from typing import Callable
import random
from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Region import Region
from src.model.core.Solution import Solution


# Классический ГА
class ClassicGA(GA):
    def __init__(self, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
                 recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
                 mutationer: Callable[[Solution, GA], Solution] = None,
                 oSelector: Callable[[Population, GA], Population] = None):
        super().__init__(pSelector, recombinator, mutationer, oSelector)

    def start(self, reg: Region) -> None:
        super().start(reg)

    def parentsSelect(self) -> None:
        super().parentsSelect()
        self.parents = self.pSelector(self.population, self)

    def crossover(self) -> None:
        super().crossover()
        self.children = Population(self.reg)
        for p in self.parents:
            if random.random() < self.params.rprob:
                # Генерация начала аллели кроссинговера
                self.params.cstart = random.randint(0, self.N - 1)
                # Генерация размера аллели (от 1 до N-1, т.к. при значения 0 и N изменений не будет)
                self.params.csize = random.randint(int(self.N * self.params.minR), int(self.N * self.params.maxR))
                self.children.extend(self.recombinator(p[0], p[1], self))
            else:
                self.children.extend(p)

    def mutation(self) -> None:
        super().mutation()
        self.mutChildren = Population(self.reg)
        for c in self.children:
            if random.random() < self.params.mprob:
                self.params.mgen1, self.params.mgen2 = sorted([random.randint(0, self.N - 1) for i in range(2)])
                self.mutChildren.append(self.mutationer(c, self))
            else:
                self.mutChildren.append(c)

    def offspringSelect(self) -> None:
        super().offspringSelect()
        self.tempPop = Population(self.reg, self.population + self.mutChildren)
        self.offspring = self.oSelector(self.tempPop, self)

    def newPopulation(self) -> None:
        super().newPopulation()
        self.population = self.offspring
        self.parents = self.children = self.mutChildren = self.tempPop = self.offspring = None

    def __str__(self) -> str:
        return 'Классический ГА:\n' + super().__str__()

    def __repr__(self) -> str:
        return str(self)
