from src.model import *

X = [1, 2, 3, 6, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]

ga = GA(towns, 5)

print('population:', ga.population, '\n')

print('panmixion:', panmixion(ga.population), '\n')

print('tournament:', tournament(2, ga.population), '\n ')

print('roulette:', roulette(ga.population))
