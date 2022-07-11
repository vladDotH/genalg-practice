from src.model.core.Town import Town
from src.model.core.Region import Region


def file_input(path: str) -> Region:
    file = open(path)
    towns = []
    for i in file:
        x, y = list(map(float, i.split()))
        towns.append(Town(x, y))
    file.close()
    reg = Region(towns)
    return reg
