from src.model import *

# Координаты городов
X = [1, 2, 3, 6, 2.73]
Y = [0, 2, 4, 5, 3.14]
towns = [Town(x, y) for x, y in zip(X, Y)]

# Инициализация ГА (особи не генерируеются)
ga = GA(towns, 0)

# Искусственно создадим особь
p = Solution.list(ga.dists, [0, 1, 2, 3, 4])

# Исходная особь
print('Исходная особь: ', p)
print()

# Мутация обменом
print('Мутация обменом: ', swap(p))
print()

# Мутация вставкой
print('Мутация вставкой: ', insert(p))
print()

# Мутация инверсией
print('Мутация инверсией: ', inverse(p))
print()
