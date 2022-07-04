from src.model import Solution
import random


# Мутация обменом (два гена меняются местами)
def swap(o: Solution, start: int = 0, end: int = None) -> Solution:
    if end is None:
        end = len(o)
    co = o.copy()
    a, b = (random.randint(start, end - 1) for i in range(2))
    co[a], co[b] = co[b], co[a]
    return co


# Мутация вставкой (выбранный ген перемещается к другому)
def insert(o: Solution, start: int = 0, end: int = None) -> Solution:
    if end is None:
        end = len(o)
    co = o.copy()
    i, j = sorted(random.randint(start, end - 1) for i in range(2))

    if i != j:
        dir = random.randint(0, 1)
        if dir == 0:
            n = co[i]
            del co[i]
            co.insert(j - 1, n)
        if dir == 1:
            n = co[j]
            del co[j]
            co.insert(i + 1, n)

    return co


# Мутация инверсией (инверсия генов между двумя генами)
def inverse(o: Solution, start: int = 0, end: int = None) -> Solution:
    if end is None:
        end = len(o)
    co = o.copy()
    i, j = sorted(random.randint(start, end - 1) for i in range(2))
    co[i:j + 1] = reversed(co[i:j + 1])
    return co
