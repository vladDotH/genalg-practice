from src.model import *

X = [1, 2, 3, 6, 2.73, 0, 10, 11, 12]
Y = [0, 2, 4, 5, 3.14, 1, 10, 11, 12]
towns = [Town(x, y) for x, y in zip(X, Y)]

ga = GA(towns, 0)

p1 = Solution.list(ga.dists, [0, 4, 1, 8, 2, 7, 3, 5, 6])
p2 = Solution.list(ga.dists, [0, 1, 3, 7, 6, 5, 2, 8, 4])

print('parents: ', p1, p2, sep='\n')
print()

print('pmx children:', *pmx(p1, p2, 4, 3), sep='\n')
print('pmx (bounding) children:', *pmx(p1, p2, 7, 4), sep='\n')
print()

print('ox children:', *ox(p1, p2, 4, 3), sep='\n')
print('ox (bounding) children:', *ox(p1, p2, 6, 4), sep='\n')
print()

print('cx children:', *cx(p1, p2), sep='\n')
