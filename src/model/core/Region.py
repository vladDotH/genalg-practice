import numpy as np
from src.model.core.Town import Town


# Регион городов, содержит список городов и матрицу расстояний
class Region(list[Town]):
    def __init__(self, towns: list[Town]):
        super().__init__()
        N = len(towns)
        self.extend(towns)
        self.dists = np.zeros((N, N))
        for i in range(N):
            for j in range(i, N):
                self.dists[i][j] = self.dists[j][i] = towns[i].dist(towns[j])

        if self.dists.sum() == 0:
            raise ArithmeticError('Region in one dot')

    def __str__(self) -> str:
        return f'Города: {super().__repr__()}\n' \
               f'Расстояния:\n' + \
               "\n".join(['[' + '\t'.join(['{:.5g}'.format(j) for j in i]) + ']' for i in self.dists])

    def __repr__(self) -> str:
        return str(self)
