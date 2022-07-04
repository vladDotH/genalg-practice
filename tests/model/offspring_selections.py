from src.model import *

X = [1, 2, 3, 10, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]

ga = GA(towns, 15)

print('population:', ga.population)
print()

print('truncation: ', trunc(ga.population, 5, 0.5))
print()

print('elite selection: ', elite(ga.population, 5))
print()