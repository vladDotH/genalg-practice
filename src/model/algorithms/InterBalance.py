from typing import Callable

from src.model.algorithms.ClassicGA import ClassicGA
from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Solution import Solution
from src.model.operators.parents_selectors import panmixion


class InterBalance(ClassicGA):
    def __init__(self, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
                 recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
                 mutationer: Callable[[Solution, GA], Solution] = None,
                 oSelector: Callable[[Population, GA], Population] = None):
        super().__init__(panmixion, recombinator, mutationer, None)
        self.params.maxExpandCoef = 10

    def offspringSelect(self) -> None:
        self.tempPop = Population(self.reg)
        self.tempPop.extend(self.population)
        self.tempPop.extend(self.mutChildren)
        mean = self.tempPop.meanF()
        self.offspring = Population(
            self.reg,
            [i for i in self.tempPop if i.F() <= mean]
        )
        # Если размер популяции вырос в maxExpandCoef раз, урезаем её до начального
        if len(self.offspring) > self.params.psize * self.params.maxExpandCoef:
            self.offspring = Population(self.reg, self.offspring.sorted()[:self.params.psize])

    def __str__(self) -> str:
        return 'ГА промежуточного равновесия:\n' + super().__str__()

    def __repr__(self) -> str:
        return str(self)
