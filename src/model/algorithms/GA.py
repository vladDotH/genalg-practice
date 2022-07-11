from __future__ import annotations
from typing import Callable
from src.model.core.Region import Region
from src.model.core.Solution import Solution
from src.model.core.Population import Population
from src.model.algorithms.Params import Params
from src.util import *


# Абстрактный ГА
class GA:
    def __init__(
            self,
            pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]] = None,
            recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]] = None,
            mutationer: Callable[[Solution, GA], Solution] = None,
            oSelector: Callable[[Population, GA], Population] = None
    ):
        self.pSelector = pSelector
        self.recombinator = recombinator
        self.mutationer = mutationer
        self.oSelector = oSelector
        self.params = Params()
        self.gen = 0

        self.reg: Region = None
        self.N: int = 0
        self.population: Population = None
        self.parents: list[tuple[Solution, Solution]] = None
        self.children: Population = None
        self.mutChildren: Population = None
        self.tempPop: Population = None
        self.offspring: Population = None

    def start(self, reg: Region) -> None:
        self.reg = reg
        self.N = len(reg)
        self.population = Population(self.reg, self.params.psize).normalized()

    def parentsSelect(self) -> None:
        Logger.log('Выбор родителей:')

    def crossover(self) -> None:
        Logger.log('Скрещивание:')

    def mutation(self) -> None:
        Logger.log('Мутации:')

    def offspringSelect(self) -> None:
        Logger.log('Отбор потомков:')

    def newPopulation(self) -> None:
        self.gen += 1
        Logger.log(f'Новое поколение: {self.gen}\n')

    def nextGeneration(self) -> None:
        self.parentsSelect()
        self.crossover()
        self.mutation()
        self.offspringSelect()
        self.newPopulation()

    # Проверка существования параметра
    def checkParam(self, attr: str) -> None:
        if not hasattr(self.params, attr):
            raise AttributeError(f'GA has not parameter {attr}')

    def __str__(self) -> str:
        return f'Оператор выбора родителей: {self.pSelector}\n' \
               f'Оператор рекомбинации: {self.recombinator}\n' \
               f'Оператор мутации: {self.mutationer}\n' \
               f'Оператор отбора: {self.oSelector}\n' \
               + str(self.params)

    def __repr__(self) -> str:
        return str(self)
