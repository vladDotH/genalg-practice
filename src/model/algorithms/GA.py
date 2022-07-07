from __future__ import annotations
from typing import Callable
import numpy as np
from multipledispatch import dispatch

from src.model.core.Town import Town
from src.model.core.Region import Region
from src.model.core.Solution import Solution
from src.model.core.Population import Population


class GA:
    class Params:
        def __init__(self):
            # Настраиваемые параметры
            self.psize = None
            self.maxGen = None
            self.rprob = None
            self.mprob = None
            self.tsize = None
            self.threshold = None
            # Генерируемые параметры
            self.cstart = None
            self.csize = None
            self.mgen1 = None
            self.mgen2 = None

        def __str__(self):
            return f'Размер популяции: {self.psize}\n' \
                   f'Максимальное кол-во поколений: {self.maxGen}\n' \
                   f'Вероятность кроссинговера: {self.rprob}\n' \
                   f'Вероятность мутаци: {self.mprob}\n' \
                   f'Размер турнира (турнирный отбор): {self.tsize}\n' \
                   f'Граница отбора (отбор усечением): {self.threshold}'

    def __init__(
            self,
            towns: list[Town],
            pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
            recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
            mutationer: Callable[[Solution, GA], Solution] = None,
            oSelector: Callable[[Population, GA], Population] = None
    ):
        self.reg = Region(towns)
        self.params = GA.Params()
        self.pSelector = pSelector
        self.recombinator = recombinator
        self.mutationer = mutationer
        self.oSelector = oSelector

    def start(self):
        self.population = Population(self.reg, self.params.psize)

    def parentSelect(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass

    def offspringSelect(self):
        pass

    def newPopulation(self):
        pass

    def checkParam(self, attr: str):
        if not hasattr(self.params, attr):
            raise AttributeError(f'GA has not parameter {attr}')
