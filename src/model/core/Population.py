from __future__ import annotations
import numpy as np
from multipledispatch import dispatch
from src.model.core.Solution import Solution


class Population(list[Solution]):
    # Стандартный конструктор (пустая популяция)
    @dispatch(np.ndarray)
    def __init__(self, dists: np.ndarray):
        super().__init__()
        self.dists = dists

    # Конструктор со случайной генерацией
    @dispatch(np.ndarray, int)
    def __init__(self, dists: np.ndarray, psize: int):
        self.__init__(dists)
        self.extend([Solution(dists, dists.shape[0]) for i in range(psize)])

    # Приведение списка особей к популяции
    @dispatch(np.ndarray, list)
    def __init__(self, dists: np.ndarray, lst: list[Solution]):
        self.__init__(dists)
        self.extend(lst)

    # Получение лучшей особи (минимального по длине цикла)
    def min(self) -> Solution:
        return min(self, key=lambda x: x.F())

    # Копия популяции
    def copy(self) -> Population:
        return Population(self.dists, super().copy())

    # Сортировка особей по возрастанию длины
    def sorted(self) -> Population:
        return Population(self.dists, sorted(self, key=lambda x: x.F()))

    def __str__(self) -> str:
        return '\n'.join([f'{i}' for i in self])

    def __repr__(self) -> str:
        return str(self)
