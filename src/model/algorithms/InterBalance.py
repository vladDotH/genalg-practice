from typing import Callable
import random

from src.model.algorithms.ClassicGA import ClassicGA
from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Region import Region
from src.model.core.Solution import Solution
from src.model.operators.parents_selectors import panmixion


class InterBalance(ClassicGA):
    def __init__(self, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
                 recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
                 mutationer: Callable[[Solution, GA], Solution] = None,
                 oSelector: Callable[[Population, GA], Population] = None):
        super().__init__(panmixion, recombinator, mutationer, None)

    def offspringSelect(self) -> None:
        self.tempPop = Population(self.reg)
        self.tempPop.extend(self.population)
        self.tempPop.extend(self.mutChildren)
        mean = self.tempPop.meanF()
        print(mean)
        self.offspring = Population(
            self.reg,
            [i for i in self.tempPop if i.F() <= mean]
        )

    def __str__(self):
        return 'ГА промежуточного равновесия:\n' + super().__str__()

    def __repr__(self):
        return str(self)
