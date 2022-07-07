from PyQt6.QtWidgets import *


class SettingsDialog(QDialog):
    def _initGA(self):
        self.classic = QRadioButton('Классический ГА')
        self.genitor = QRadioButton('Генитор')
        self.interbalance = QRadioButton('Прер. Равновесия')

        box = QGroupBox('Модификация ГА')
        lt = QHBoxLayout()
        for r in [self.classic, self.genitor, self.interbalance]:
            lt.addWidget(r)
        box.setLayout(lt)
        self.lt.addWidget(box)

    def _initPS(self):
        self.panmixion = QRadioButton('Панмиксия')
        self.tournament = QRadioButton('Турнир')
        self.roulette = QRadioButton('Рулетка')

        box = QGroupBox('Оператор отбора родителей')
        lt = QHBoxLayout()
        for r in [self.panmixion, self.tournament, self.roulette]:
            lt.addWidget(r)
        box.setLayout(lt)
        self.lt.addWidget(box)

    def _initRCMB(self):
        self.pmx = QRadioButton('PMX')
        self.ox = QRadioButton('OX')
        self.cx = QRadioButton('CX')

        box = QGroupBox('Оператор рекомбинации')
        lt = QHBoxLayout()
        for r in [self.pmx, self.ox, self.cx]:
            lt.addWidget(r)
        box.setLayout(lt)
        self.lt.addWidget(box)

    def _initMT(self):
        self.swap = QRadioButton('Обмен')
        self.insert = QRadioButton('Вставка')
        self.inverse = QRadioButton('Инверсия')

        box = QGroupBox('Оператор мутации')
        lt = QHBoxLayout()
        for r in [self.swap, self.insert, self.inverse]:
            lt.addWidget(r)
        box.setLayout(lt)
        self.lt.addWidget(box)

    def _initOS(self):
        self.trunc = QRadioButton('Отбор усечением')
        self.elite = QRadioButton('Элитарный отбор')

        box = QGroupBox('Оператор отбора в новую популяцию')
        lt = QHBoxLayout()
        for r in [self.trunc, self.elite]:
            lt.addWidget(r)
        box.setLayout(lt)
        self.lt.addWidget(box)

    def _initParams(self):
        labels = [
            QLabel('Размер популяции'),
            QLabel('Максимальное поколение'),
            QLabel('Вероятность кроссинговера (%)'),
            QLabel('Вероятность мутации (%)'),
            QLabel('Размер турнира'),
            QLabel('Порог отбора (%)'),
        ]
        self.psize = (QSpinBox())
        self.maxGen = QSpinBox()
        self.rprob = QDoubleSpinBox()
        self.mprob = QDoubleSpinBox()
        self.tsize = QSpinBox()
        self.threshold = QDoubleSpinBox()

        box = QGroupBox("Параметры")
        lt = QVBoxLayout()
        for r, l in zip([self.psize, self.maxGen, self.rprob, self.mprob, self.tsize, self.threshold], labels):
            lt.addWidget(l)
            lt.addWidget(r)
        box.setLayout(lt)
        self.lt.addWidget(box)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройка ГА")

        self.btn = QPushButton(self)
        self.btn.setText("Подтвердить")
        self.btn.clicked.connect(self.ret)

        self.lt = QVBoxLayout()
        self._initGA()
        self._initPS()
        self._initRCMB()
        self._initMT()
        self._initOS()
        self._initParams()
        self.lt.addWidget(self.btn)
        self.setLayout(self.lt)

    def ret(self):
        self.accept()
