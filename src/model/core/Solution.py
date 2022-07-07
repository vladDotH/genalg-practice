from __future__ import annotations
from multipledispatch import dispatch
import math
import random
import numpy as np
from src.model.core.Region import Region


# Класс особи
class Solution(list[int]):
    # Стандартный конструктор (пустая особь)
    @dispatch(Region)
    def __init__(self, reg: Region):
        super().__init__()
        self.reg = reg

    # Конструктор со случайной генерацией особи
    @dispatch(Region, int)
    def __init__(self, reg: Region, length: int):
        self.__init__(reg)
        self.extend(list(range(length)))
        random.shuffle(self)

    # Приведение обычного списка к особи
    @dispatch(Region, list)
    def __init__(self, reg: Region, lst: list[int]):
        self.__init__(reg)
        self.extend(lst)

    # Целевая функция (сумма длин весов рёбер графа)
    def F(self) -> float:
        return sum([self.reg.dists[self[i - 1]][self[i]] for i in range(len(self))])

    # Обратная к целевой функция (чем она больше тем приспособленне особь)
    def rF(self) -> float:
        return np.tril(self.reg.dists).sum() / self.F() if self.F() != 0 else math.inf

    # Рекурсивный сдвиг решения (цикла графа)
    def shift(self, n: int) -> Solution:
        return Solution(self.reg, list(np.roll(self, n)))

    # Копия особи
    def copy(self) -> Solution:
        return Solution(self.reg, super().copy())

    def __str__(self) -> str:
        return f'{{genome: {super().__repr__()}, F: {self.F()}}}'

    def __repr__(self) -> str:
        return str(self)
