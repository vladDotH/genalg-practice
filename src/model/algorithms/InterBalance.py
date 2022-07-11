from typing import Callable
from src.model.algorithms.ClassicGA import ClassicGA
from src.model.algorithms.GA import GA
from src.model.core.Population import Population
from src.model.core.Solution import Solution
from src.model.operators.parents_selectors import panmixion
from src.util import *


# ГА с методом промежуточного баланаса (модификация с ограничением)
class InterBalance(ClassicGA):
    def __init__(self, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
                 recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
                 mutationer: Callable[[Solution, GA], Solution] = None,
                 oSelector: Callable[[Population, GA], Population] = None):
        super().__init__(panmixion, recombinator, mutationer, oSelector)
        # Максимальное расширение популяции
        self.maxExpandCoef = 3 ** 3

    def offspringSelect(self) -> None:
        Logger.log('Отбор потомков:')
        self.tempPop = Population(self.reg, self.population + self.mutChildren)
        # Если размер популяции вырос в maxExpandCoef раз, урезаем её до начального размера выбранным оператором отбора
        if len(self.tempPop) > self.params.psize * self.maxExpandCoef:
            self.offspring = self.oSelector(self.tempPop, self)
        else:
            mean = self.tempPop.meanF()
            self.offspring = Population(
                self.reg,
                [i for i in self.tempPop if i.F() <= mean]
            )

    def __str__(self) -> str:
        return 'ГА промежуточного равновесия:\n' + super().__str__()

    def __repr__(self) -> str:
        return str(self)
