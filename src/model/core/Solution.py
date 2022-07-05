from __future__ import annotations
import math
import random

import numpy as np


# Класс особи
class Solution(list[int]):
    def __init__(self, dists: np.ndarray):
        super().__init__()
        self.dists = dists

    # Генерация случайного решения
    @staticmethod
    def rand(length: int, dists: np.ndarray) -> Solution:
        sln = Solution(dists)
        sln.extend(list(range(length)))
        random.shuffle(sln)
        return sln

    # Приведение списка к особи
    @staticmethod
    def list(dists: np.ndarray, lst: list[int]) -> Solution:
        pop = Solution(dists)
        pop.extend(lst)
        return pop

    # Целевая функция (сумма длин весов рёбер графа)
    def F(self) -> float:
        return sum([self.dists[self[i - 1]][self[i]] for i in range(len(self))])

    # Обратная к целевой функция (чем она больше тем приспособленне особь)
    def rF(self) -> float:
        return np.tril(self.dists).sum() / self.F() if self.F() != 0 else math.inf

    # Рекурсивный сдвиг решения (цикла графа)
    def shift(self, n: int) -> Solution:
        return Solution.list(self.dists, list(np.roll(self, n)))

    # Копия особи
    def copy(self) -> Solution:
        return Solution.list(self.dists, super().copy())

    def __str__(self) -> str:
        return f'{{genome: {super().__repr__()}, F: {self.F()}}}'

    def __repr__(self) -> str:
        return str(self)
