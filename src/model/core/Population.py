from __future__ import annotations
import numpy as np
from multipledispatch import dispatch
from src.model.core.Solution import Solution
from src.model.core.Region import Region


# Папуляция особей
class Population(list[Solution]):
    # Стандартный конструктор (пустая популяция)
    @dispatch(Region)
    def __init__(self, reg: Region):
        super().__init__()
        self.reg = reg

    # Конструктор со случайной генерацией
    @dispatch(Region, int)
    def __init__(self, reg: Region, psize: int):
        self.__init__(reg)
        self.extend([Solution(reg, len(reg)) for i in range(psize)])

    # Приведение списка особей к популяции
    @dispatch(Region, list)
    def __init__(self, reg: Region, lst: list[Solution]):
        self.__init__(reg)
        self.extend(lst)

    # Получение лучшей особи (минимального по длине цикла)
    def min(self) -> Solution:
        return min(self, key=lambda x: x.F())

    # Худшая особь
    def max(self) -> Solution:
        return max(self, key=lambda x: x.F())

    # Среднее значение целевой функции
    def meanF(self) -> float:
        return np.mean([x.F() for x in self])

    # Среднее значение обратной к целевой ф.
    def meanrF(self) -> float:
        return np.mean([x.rF() for x in self])

    # Нормализация всех особей
    def normalized(self) -> Population:
        return Population(self.reg, [i.normalized() for i in self])

    # Копия популяции
    def copy(self) -> Population:
        return Population(self.reg, super().copy())

    # Сортировка особей по возрастанию длины
    def sorted(self) -> Population:
        return Population(self.reg, sorted(self, key=lambda x: x.F()))

    def __str__(self) -> str:
        return '\n'.join([f'{i}' for i in self])

    def __repr__(self) -> str:
        return str(self)
