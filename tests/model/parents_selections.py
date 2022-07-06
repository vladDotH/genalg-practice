from src.model import *

# Координаты городов
X = [1, 2, 3, 6, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]

# Инициализация ГА
ga = GA(towns, 5)

# Начальная популяция
print('Популяция:\n', ga.population, '\n')

# Пары полученные панмиксией
print('Панмиксия:', *panmixion(ga.population), '', sep='\n')

# Пары полученные турнирным методом
print('Турнирный отбор:', *tournament(ga.population, 2), '', sep='\n')

# Пары полученные методом рулетки
print('Рулетка:', *roulette(ga.population), sep='\n')
