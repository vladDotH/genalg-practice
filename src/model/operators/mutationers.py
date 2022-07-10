import random
from src.model import Solution
from src.model.algorithms.GA import GA


# Мутация обменом (два гена меняются местами)
def swap(o: Solution, ga: GA) -> Solution:
    for a in ['mgen1', 'mgen2']:
        ga.checkParam(a)
    i, j = ga.params.mgen1, ga.params.mgen2

    co = o.copy()
    co[i], co[j] = co[j], co[i]
    return co


# Мутация вставкой (выбранный ген перемещается к другому)
def insert(o: Solution, ga: GA) -> Solution:
    for a in ['mgen1', 'mgen2']:
        ga.checkParam(a)
    i, j = ga.params.mgen1, ga.params.mgen2

    co = o.copy()
    if i != j:
        dir = bool(random.randint(0, 1))
        if dir:
            n = co[i]
            del co[i]
            co.insert(j - 1, n)
        else:
            n = co[j]
            del co[j]
            co.insert(i + 1, n)

    return co


# Мутация инверсией (инверсия генов между двумя генами)
def inverse(o: Solution, ga: GA) -> Solution:
    for a in ['mgen1', 'mgen2']:
        ga.checkParam(a)
    i, j = ga.params.mgen1, ga.params.mgen2

    co = o.copy()
    co[i:j + 1] = reversed(co[i:j + 1])
    return co
