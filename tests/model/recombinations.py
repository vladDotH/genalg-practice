from src.model import *

# Координаты городов
X = [1, 2, 3, 6, 2.73, 0, 10, 11, 12]
Y = [0, 2, 4, 5, 3.14, 1, 10, 11, 12]
towns = [Town(x, y) for x, y in zip(X, Y)]

# Инициализация ГА (особи не генерируеются)
ga = GA()
ga.params.psize = 0
ga.start(Region(towns))

# Создадим особи искусственно
p1 = Solution(ga.reg, [0, 4, 1, 8, 2, 7, 3, 5, 6])
p2 = Solution(ga.reg, [0, 1, 3, 7, 6, 5, 2, 8, 4])

# Родители
print('Родители: ', p1, p2, sep='\n')
print()

# PMX метод
ga.params.cstart = 4
ga.params.csize = 3
print('Особи полученные с помощью PMX:', *pmx(p1, p2, ga), sep='\n')
ga.params.cstart = 7
ga.params.csize = 3
print('Особи полученные с помощью PMX(разрез выходит за пределы хромосомы):', *pmx(p1, p2, ga), sep='\n')
print()

# OX метод
ga.params.cstart = 4
ga.params.csize = 3
print('Особи полученные с помощью OX:', *ox(p1, p2, ga), sep='\n')
ga.params.cstart = 7
ga.params.csize = 3
print('Особи полученные с помощью OX(разрез выходит за пределы хромосомы):', *ox(p1, p2, ga), sep='\n')
print()

# CX метод
ga.params.cstart = 1
print('Особи полученные с помощью CX:', *cx(p1, p2, ga), sep='\n')
