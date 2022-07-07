from src.model import *

# Координаты городов
X = [1, 2, 3, 6, 2.73, 6]
Y = [0, 2, 4, 5, 3.14, 7]
towns = [Town(x, y) for x, y in zip(X, Y)]

# Инициализация ГА (особи не генерируеются)
ga = GA(towns, 0)

# Искусственно создадим особь
p = Solution(ga.reg, [0, 1, 2, 3, 4, 5])

# Исходная особь
print('Исходная особь: ', p)
print()

ga.params.mgen1 = 1
ga.params.mgen2 = 4

# Мутация обменом
print('Мутация обменом: ', swap(p, ga))
print()

# Мутация вставкой
print('Мутация вставкой: ', insert(p, ga))
print()

# Мутация инверсией
print('Мутация инверсией: ', inverse(p, ga))
print()
