from src.model import Solution
from src.model.algorithms.GA import GA
from src.util import *


# Partial Mapped Crossover
def pmx(p1: Solution, p2: Solution, ga: GA) -> tuple[Solution, Solution]:
    for a in ['cstart', 'csize']:
        ga.checkParam(a)

    start = ga.params.cstart
    size = ga.params.csize

    N = len(p1)

    if size < 0 or size > N or start < 0 or start > N - 1:
        raise ValueError('Incorrect start/size parameters')

    Logger.log(f'Рекомбинация. Параметры: начало: {start}, размер: {size}.\n'
               f'Родители: {p1}, {p2}')

    # Хромосомы сдвигаются так чтобы рекомбинируемая аллель была вначале (удобно для вычислений)
    p1, p2 = p1.shift(-start), p2.shift(-start)

    o1 = Solution(p1.reg, [-1] * N)
    o2 = Solution(p2.reg, [-1] * N)

    # Обмен аллелями
    o2[:size] = p1[:size]
    o1[:size] = p2[:size]

    Logger.log(f'Аллели после обмена: {o1} ; {o2}\n')

    # Вставка остальных генов
    for p, o in zip([p1, p2], [o1, o2]):
        for i in range(size, N):
            gen = p[i]
            # Пока ген есть в аллеле выбираем тот который он собой заменил
            while gen in o[0:size]:
                gen = p[o.index(gen)]
            o[i] = gen

    return (o1, o2)


# Ordered Crossover
def ox(p1: Solution, p2: Solution, ga: GA) -> tuple[Solution, Solution]:
    for a in ['cstart', 'csize']:
        ga.checkParam(a)

    start = ga.params.cstart
    size = ga.params.csize

    N = len(p1)

    if size < 0 or size > N or start < 0 or start > N - 1:
        raise ValueError('Incorrect start/size parameters')

    Logger.log(f'Рекомбинация. Параметры: начало: {start}, размер: {size}.\n'
               f'Родители: {p1}, {p2}')

    # Хромосомы сдвигаются так чтобы рекомбинируемая аллель была вначале (удобно для вычислений)
    p1, p2, start = p1.shift(-start), p2.shift(-start), 0

    o1 = Solution(p1.reg, [-1] * N)
    o2 = Solution(p2.reg, [-1] * N)

    # Обмен аллелями
    o2[:size] = p1[:size]
    o1[:size] = p2[:size]

    Logger.log(f'Аллели после обмена: {o1} ; {o2}\n')

    # Цепочки начинающиеся с гена сразу после аллели
    ps1 = p1.shift(-size)
    ps2 = p2.shift(-size)

    # Удаление присутсвующих генов
    for i in range(size):
        ps1.remove(o1[i])
        ps2.remove(o2[i])

    j = 0
    # Добавление оставшихся генов
    for i in range(size, N):
        o1[i] = ps1[j]
        o2[i] = ps2[j]
        j += 1

    return (o1, o2)


# Cycle Crossover
def cx(p1: Solution, p2: Solution, ga: GA) -> tuple[Solution, Solution]:
    ga.checkParam('cstart')
    start = ga.params.cstart

    N = len(p1)

    if start < 0 or start > N - 1:
        raise ValueError('Incorrect start parameter')

    Logger.log(f'Рекомбинация. Параметры: начало: {start}.\n'
               f'Родители: {p1}, {p2}')

    o1 = Solution(p1.reg, [-1] * N)
    o2 = Solution(p2.reg, [-1] * N)

    logs = []
    for o, p in zip([o1, o2], [[p1, p2], [p2, p1]]):
        g = start
        # Поиск цикла подстановки
        while True:
            # Добавление генов из цикла
            o[g] = p[1][g]
            g = p[1].index(p[0][g])
            if g == start:
                break
        logs.append(f'{o}')
        # Добавление остальных генов из другого родителя
        for i in range(N):
            if o[i] == -1:
                o[i] = p[0][i]

    Logger.log('Аллели после обмена: ' + ' ; '.join(logs) + '\n')

    return (o1, o2)
