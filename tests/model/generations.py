from src.model import *

# Координаты городов
X = [1, 2, 3, 10, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]

# Инициализация ГА
ga = GA()
ga.params.psize = 5
ga.start(Region(towns))

# Матрица весов
print('Регион:', ga.reg, '', sep='\n')

# Начальная популяция
print('Популяция:', ga.population, '', sep='\n')

# Лучшее решение (особь)
print('Особь с минимальной длиной: ', (ga.population.min()), '\n')
