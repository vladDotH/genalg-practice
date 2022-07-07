from src.model.core.Town import Town


def file_input(path: str) -> list[Town]:
    file = open(path)
    towns = []
    for i in file:
        x, y = list(map(float, i.split()))
        towns.append(Town(x, y))
    file.close()
    return towns
