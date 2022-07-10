from typing import Type, Callable
from PyQt6.QtWidgets import *

from src.model import *
from src.util import Logger


class SettingsDialog(QDialog):
    # Обработка кнопок выбора ГА
    def _onGA(self, state: bool, gaType: Type[GA]) -> None:
        if state:
            self.gaType = gaType

        if gaType is Genitor:
            # Выключаем/выключаем уникальность кнопок в группах (операторы выборов родителей и потомков)
            self.psGroup.setExclusive(not state)
            self.osGroup.setExclusive(not state)
            # Выключаем кнопки
            if state:
                for rb in [self.panmixion, self.tournament, self.roulette, self.trunc, self.elite]:
                    if rb.isChecked():
                        rb.setChecked(False)
            # Включаем кнопки по муолчанию
            if not state:
                self.panmixion.toggle()
                self.trunc.toggle()
            # Вкл/Выкл группы кнопок
            self.psBox.setEnabled(not state)
            self.osBox.setEnabled(not state)

        if gaType is InterBalance:
            if state:
                self.panmixion.setChecked(True)
            self.psBox.setEnabled(not state)

    # Инициализация блока кнопок выбора ГА
    def _initGA(self) -> None:
        self.classic = QRadioButton('Классический ГА')
        self.genitor = QRadioButton('Генитор')
        self.interbalance = QRadioButton('Прер. Равновесия')

        self.classic.toggled.connect(lambda state: self._onGA(state, ClassicGA))
        self.genitor.toggled.connect(lambda state: self._onGA(state, Genitor))
        self.interbalance.toggled.connect(lambda state: self._onGA(state, InterBalance))

        self.gaBox = QGroupBox('Модификация ГА')
        lt = QHBoxLayout()
        for r in [self.classic, self.genitor, self.interbalance]:
            lt.addWidget(r)
        self.gaBox.setLayout(lt)
        self.lt.addWidget(self.gaBox)

    # Обработка кнопок выбора оператора выбора родителей
    def _onPS(self, state: bool, pSelector: Callable[[Population, GA], list[tuple[Solution, Solution]]]) -> None:
        if state:
            self.pSelector = pSelector
        if pSelector is tournament:
            # Включаем размер турнира если выбран турнирый метод
            self.tsize.setEnabled(state)

    # Инициализация блока кнопок выбора оператора выбора родителей
    def _initPS(self) -> None:
        self.panmixion = QRadioButton('Панмиксия')
        self.tournament = QRadioButton('Турнир')
        self.roulette = QRadioButton('Рулетка')

        self.panmixion.toggled.connect(lambda state: self._onPS(state, panmixion))
        self.tournament.toggled.connect(lambda state: self._onPS(state, tournament))
        self.roulette.toggled.connect(lambda state: self._onPS(state, roulette))

        self.psGroup = QButtonGroup(self)
        self.psBox = QGroupBox('Оператор отбора родителей')
        lt = QHBoxLayout()
        for r in [self.panmixion, self.tournament, self.roulette]:
            lt.addWidget(r)
            self.psGroup.addButton(r)
        self.psBox.setLayout(lt)
        self.lt.addWidget(self.psBox)

    # Обработка кнопок выбора оператора рекомбинации
    def _onRCMB(self, state: bool, recombinator: Callable[[Solution, Solution, GA], tuple[Solution, Solution]]) -> None:
        if state:
            self.recombinator = recombinator

    # Инициализация блока кнопок выбора оператора рекомбинации
    def _initRCMB(self) -> None:
        self.pmx = QRadioButton('PMX')
        self.ox = QRadioButton('OX')
        self.cx = QRadioButton('CX')

        self.pmx.toggled.connect(lambda state: self._onRCMB(state, pmx))
        self.ox.toggled.connect(lambda state: self._onRCMB(state, ox))
        self.cx.toggled.connect(lambda state: self._onRCMB(state, cx))

        self.rcmbBox = QGroupBox('Оператор рекомбинации')
        lt = QHBoxLayout()
        for r in [self.pmx, self.ox, self.cx]:
            lt.addWidget(r)
        self.rcmbBox.setLayout(lt)
        self.lt.addWidget(self.rcmbBox)

    # Обработка кнопок выбора оператора мутации
    def _onMT(self, state: bool, mutationer: Callable[[Solution, GA], Solution]) -> None:
        if state:
            self.mutationer = mutationer

    # Инициализация блока кнопок выбора оператора мутации
    def _initMT(self) -> None:
        self.swap = QRadioButton('Обмен')
        self.insert = QRadioButton('Вставка')
        self.inverse = QRadioButton('Инверсия')

        self.swap.toggled.connect(lambda state: self._onMT(state, swap))
        self.insert.toggled.connect(lambda state: self._onMT(state, insert))
        self.inverse.toggled.connect(lambda state: self._onMT(state, inverse))

        self.mtBox = QGroupBox('Оператор мутации')
        lt = QHBoxLayout()
        for r in [self.swap, self.insert, self.inverse]:
            lt.addWidget(r)
        self.mtBox.setLayout(lt)
        self.lt.addWidget(self.mtBox)

    # Обработка кнопок выбора оператора выбора потомков
    def _onOS(self, state: bool, oSelector: Callable[[Population, GA], Population]) -> None:
        if state:
            self.oSelector = oSelector
        if oSelector is trunc:
            # Включаем порог отбора если выбран отбор усечением
            self.threshold.setEnabled(state)

    # Инициализация блока кнопок выбора оператора выбора потомков
    def _initOS(self) -> None:
        self.trunc = QRadioButton('Отбор усечением')
        self.elite = QRadioButton('Элитарный отбор')

        self.trunc.toggled.connect(lambda state: self._onOS(state, trunc))
        self.elite.toggled.connect(lambda state: self._onOS(state, elite))

        self.osGroup = QButtonGroup(self)
        self.osBox = QGroupBox('Оператор отбора в новую популяцию')
        lt = QHBoxLayout()
        for r in [self.trunc, self.elite]:
            lt.addWidget(r)
            self.osGroup.addButton(r)
        self.osBox.setLayout(lt)
        self.lt.addWidget(self.osBox)

    # Инициализация блока числовых параметров
    def _initParams(self) -> None:
        labels = [
            QLabel('Размер популяции'),
            QLabel('Максимальное поколение'),
            QLabel('Вероятность кроссинговера (%)'),
            QLabel('Вероятность мутации (%)'),
            QLabel('Размер турнира'),
            QLabel('Порог отбора (%)'),
        ]
        self.psize = QSpinBox()
        self.maxGen = QSpinBox()
        self.rprob = QDoubleSpinBox()
        self.mprob = QDoubleSpinBox()
        self.tsize = QSpinBox()
        self.threshold = QDoubleSpinBox()

        self.tsize.setEnabled(False)
        self.threshold.setEnabled(False)

        self.psize.valueChanged.connect(lambda v: setattr(self.params, 'psize', v))
        self.maxGen.valueChanged.connect(lambda v: setattr(self.params, 'maxGen', v))
        self.rprob.valueChanged.connect(lambda v: setattr(self.params, 'rprob', v / 100))
        self.mprob.valueChanged.connect(lambda v: setattr(self.params, 'mprob', v / 100))
        self.tsize.valueChanged.connect(lambda v: setattr(self.params, 'tsize', v))
        self.threshold.valueChanged.connect(lambda v: setattr(self.params, 'threshold', v / 100))

        for sb in [self.rprob, self.mprob, self.threshold]:
            sb.setMinimum(0)
            sb.setMaximum(100)
        self.maxGen.setMaximum(10 ** 6)
        self.psize.setMaximum(10 ** 3)
        self.tsize.setMaximum(10 ** 3)

        box = QGroupBox("Параметры")
        lt = QVBoxLayout()
        for r, l in zip([self.psize, self.maxGen, self.rprob, self.mprob, self.tsize, self.threshold], labels):
            r.valueChanged.emit(r.value())
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

        self.gaType = None
        self.pSelector = None
        self.recombinator = None
        self.mutationer = None
        self.oSelector = None
        self.params = GA.Params()

        self.subResult = 0
        sbLbl = QLabel('Промежуток отображения популяции (при вычислении результата)')
        self.subResultSB = QSpinBox()
        self.subResultSB.valueChanged.connect(lambda v: setattr(self, 'subResult', v))

        self.lt = QVBoxLayout()
        self._initGA()
        self._initPS()
        self._initRCMB()
        self._initMT()
        self._initOS()
        self._initParams()
        self.lt.addWidget(sbLbl)
        self.lt.addWidget(self.subResultSB)
        self.lt.addWidget(self.btn)
        self.setLayout(self.lt)

        # Значения по умолчанию (radio button)
        self.classic.toggle()
        self.panmixion.toggle()
        self.pmx.toggle()
        self.swap.toggle()
        self.trunc.toggle()
        # Значения по умолчанию (spin box)
        self.psize.setValue(10)
        self.maxGen.setValue(50)
        self.rprob.setValue(80)
        self.mprob.setValue(5)
        self.tsize.setValue(2)
        self.threshold.setValue(50)
        self.subResultSB.setValue(5)

        self.cfgFile = 'config'
        # Загрузка настроек из файла (если настрока есть - значние по умолчанию перезаписывается, иначе оно остаётся)
        self.load()

    def ret(self) -> None:
        self.save()
        self.accept()

    def load(self) -> None:
        try:
            with open(self.cfgFile, 'r') as f:
                for line in f:
                    data = line.split()
                    if len(data) == 1:
                        name = data[0]
                        getattr(self, name).toggle()
                    elif len(data) == 2:
                        name = data[0]
                        val = float(data[1])
                        if type(getattr(self, name)) is QSpinBox:
                            val = int(val)
                        getattr(self, name).setValue(val)
        except Exception as e:
            Logger.log(f'Ошибка чтения настроек: {e}\n')

    def save(self) -> None:
        try:
            with open(self.cfgFile, 'w') as f:
                for box in [
                    ['classic', 'genitor', 'interbalance'],
                    ['panmixion', 'tournament', 'roulette'],
                    ['pmx', 'ox', 'cx'],
                    ['swap', 'insert', 'inverse'],
                    ['trunc', 'elite'],
                ]:
                    for op in box:
                        if getattr(self, op).isChecked():
                            f.write(f'{op}\n')

                for sb in ['psize', 'maxGen', 'rprob', 'mprob', 'tsize', 'threshold', 'subResultSB']:
                    f.write(f'{sb} {getattr(self, sb).value()}\n')

        except Exception as e:
            Logger.log(f'Ошибка записи настроек: {e}\n')
