from src.model import *

X = [1, 2, 3, 10, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]
print(f'Towns: {towns}\n')

ga = GA(towns, 5)

print('distances:\n', ga.dists, '\n')
print('population:\n', ga.population, '\n')
print('minimal: ', (ga.population.min()), '\n')
