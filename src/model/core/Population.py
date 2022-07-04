from __future__ import annotations
import numpy as np
from src.model.core.Solution import Solution


class Population(list[Solution]):
    def __init__(self, dists: np.ndarray):
        super().__init__()
        self.dists = dists

    # Генерация случайной популяции
    @staticmethod
    def rand(dists: np.ndarray, psize: int):
        pop = Population(dists)
        pop.extend([Solution.rand(dists.shape[0], dists) for i in range(psize)])
        return pop

    # Приведение списка особей к популяции
    @staticmethod
    def list(dists: np.ndarray, lst: list[Solution]):
        pop = Population(dists)
        pop.extend(lst)
        return pop

    # Получение лучшей особи (минимального по длине цикла)
    def min(self):
        return min(self, key=lambda x: x.F())

    # Копия популяции
    def copy(self) -> Population:
        return Population.list(self.dists, super().copy())

    # Сортировка особей по возрастанию длины
    def sorted(self) -> Population:
        return Population.list(self.dists, sorted(self, key=lambda x: x.F()))

    def __str__(self) -> str:
        return '\n'.join([f'{i}' for i in self])

    def __repr__(self):
        return str(self)
