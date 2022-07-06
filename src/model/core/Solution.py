from __future__ import annotations
import math
import random
from multipledispatch import dispatch

import numpy as np


# Класс особи
class Solution(list[int]):
    # Стандартный конструктор (пустая особь)
    @dispatch(np.ndarray)
    def __init__(self, dists: np.ndarray):
        super().__init__()
        self.dists = dists

    # Конструктор со случайной генерацией особи
    @dispatch(np.ndarray, int)
    def __init__(self, dists: np.ndarray, length: int):
        self.__init__(dists)
        self.extend(list(range(length)))
        random.shuffle(self)

    # Приведение обычного списка к особи
    @dispatch(np.ndarray, list)
    def __init__(self, dists: np.ndarray, lst: list[int]):
        self.__init__(dists)
        self.dists = dists
        self.extend(lst)

    # Целевая функция (сумма длин весов рёбер графа)
    def F(self) -> float:
        return sum([self.dists[self[i - 1]][self[i]] for i in range(len(self))])

    # Обратная к целевой функция (чем она больше тем приспособленне особь)
    def rF(self) -> float:
        return np.tril(self.dists).sum() / self.F() if self.F() != 0 else math.inf

    # Рекурсивный сдвиг решения (цикла графа)
    def shift(self, n: int) -> Solution:
        return Solution(self.dists, list(np.roll(self, n)))

    # Копия особи
    def copy(self) -> Solution:
        return Solution(self.dists, super().copy())

    def __str__(self) -> str:
        return f'{{genome: {super().__repr__()}, F: {self.F()}}}'

    def __repr__(self) -> str:
        return str(self)
