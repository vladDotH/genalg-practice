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
            # Размер популяции
            self.psize = None
            # Вероятность рекомбинации
            self.rprob = None
            # Вероятность мутации
            self.mprob = None
            # Размер турнира (для турнирного отбора)
            self.tsize = None
            # Начало аллели кроссинговера
            self.cstart = None
            # Размер аллели кроссинговера
            self.csize = None
            # Гены для мутации
            self.mgen1 = None
            self.mgen2 = None
            # Граница выбора (для отбора усечением)
            self.threshold = None

    def __init__(
            self,
            towns: list[Town],
            psize: int,
            pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
            recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
            mutationer: Callable[[Solution, GA], Solution] = None,
            oSelector: Callable[[Population, GA], Population] = None
    ):
        self.startSize = psize
        self.reg = Region(towns)
        self.population = Population(self.reg, psize)
        self.params = GA.Params()
        self.pSelector = pSelector
        self.recombinator = recombinator
        self.mutationer = mutationer
        self.oSelector = oSelector

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
