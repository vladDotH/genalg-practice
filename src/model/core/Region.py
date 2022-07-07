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

    def __str__(self) -> str:
        return f'Towns: {super().__repr__()}\n' \
               f'Dists:\n {self.dists}'

    def __repr__(self) -> str:
        return str(self)
