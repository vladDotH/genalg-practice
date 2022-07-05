from src.model import *

# Координаты городов
X = [1, 2, 3, 10, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]

# Инициализация ГА
ga = GA(towns, 15)

# Начальная популяция (для примера будем проводить отбор из начальной популяции)
print('Популяция:', ga.population)
print()

# Отбор усечением
print('Отбор усечением: ', trunc(ga.population, 5, 0.5))
print()

# Элитарный отбор
print('Элитарный отбор: ', elite(ga.population, 5))
print()