import numpy as np
from src.model.core.Town import Town
from src.model.core.Population import Population


class GA:
    def __init__(self, towns: list[Town], psize: int):
        self.towns = towns
        self.startSize = psize
        N: int = len(towns)
        self.dists: np.ndarray = np.zeros((N, N))
        for i in range(N):
            for j in range(i, N):
                self.dists[i][j] = self.dists[j][i] = towns[i].dist(towns[j])

        self.population = Population(self.dists, psize)

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
