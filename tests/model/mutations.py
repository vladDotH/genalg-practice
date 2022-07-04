from src.model import *

X = [1, 2, 3, 6, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]

ga = GA(towns, 0)

p = Solution.list(ga.dists, [0, 1, 2, 3, 4])
print('source: ', p)
print()

print('swap: ', swap(p))
print()

print('insert: ', insert(p))
print()

print('inverse: ', inverse(p))
print()