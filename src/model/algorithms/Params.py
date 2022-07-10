class Params:
    def __init__(self):
        # Настраиваемые параметры
        self.psize: int = 0
        self.maxGen: int = 0
        self.rprob: float = 0
        self.minR: float = 0
        self.maxR: float = 0
        self.mprob: float = 0
        self.tsize: int = 0
        self.threshold: float = 0
        # Генерируемые параметры
        self.cstart: int = 0
        self.csize: int = 0
        self.mgen1: int = 0
        self.mgen2: int = 0

    def __str__(self):
        return f'Размер популяции: {self.psize}\n' \
               f'Максимальное кол-во поколений: {self.maxGen}\n' \
               f'Вероятность кроссинговера: {self.rprob}\n' \
               f'Границы размеров аллели: [{self.minR}; {self.maxR}]\n' \
               f'Вероятность мутации: {self.mprob}\n' \
               f'Размер турнира (турнирный отбор): {self.tsize}\n' \
               f'Граница отбора (отбор усечением): {self.threshold}'
