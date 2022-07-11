from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from src.gui.dialogs.InputDialog import InputDialog
from src.gui.dialogs.SettingsDialog import SettingsDialog
from src.gui.widgets.LoggerWidget import LoggerWidget
from src.gui.widgets.ControlWidget import ControlWidget
from src.gui.widgets.PopulationWidget import PopulationWidget
from src.model import *
from src.util import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генетические Алгоритмы")

        mainSplitter = QSplitter(self)
        popSplitter = QSplitter(self)
        infoSplitter = QSplitter(self)

        self.parents = PopulationWidget('Популяция', self)
        self.offspring = PopulationWidget('Потомки', self)
        self.mutations = PopulationWidget('Мутации', self)
        self.logger = LoggerWidget(self)
        Logger.connect(self.logger.print)
        self.control = ControlWidget(self)

        self.control.mutate.setEnabled(False)
        self.control.next.setEnabled(False)

        for w in [self.parents, self.offspring, self.mutations]:
            popSplitter.addWidget(w)

        infoSplitter.addWidget(self.control)
        infoSplitter.addWidget(self.logger)
        infoSplitter.setStretchFactor(1, 1)

        mainSplitter.addWidget(popSplitter)
        mainSplitter.addWidget(infoSplitter)
        mainSplitter.setOrientation(Qt.Orientation.Vertical)
        self.setCentralWidget(mainSplitter)

        self.inputMenu = QMenu('Ввести данные')
        self.manually = QAction('Ввести вручную')
        self.manually.triggered.connect(self.onInput)
        self.fromFile = QAction('Выбрать файл')
        self.fromFile.triggered.connect(self.onFile)
        self.inputMenu.addActions([self.manually, self.fromFile])

        self.menuBar().addMenu(self.inputMenu)
        self.settings = self.menuBar().addAction('Настройки', self.onSettings)
        self.start = self.menuBar().addAction('Запуск', self.onStart)
        self.info = self.menuBar().addAction('О программе', self.onInfo)

        self.statusBar().showMessage('Введите данные')
        self.ga: GA = None
        self.reg: Region = None
        self.subResult = 1

        self.control.offspring.clicked.connect(self.onChildren)
        self.control.mutate.clicked.connect(self.onMutate)
        self.control.next.clicked.connect(self.onNext)
        self.control.forceNext.clicked.connect(self.onForceNext)
        self.control.results.clicked.connect(self.onResults)

    # Проверка на ввод данных и установку настроек
    def checkSetup(self) -> bool:
        if self.reg is None:
            QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Critical),
                'Ошибка',
                f'Не введены данные'
            ).exec()
            return False
        if self.ga is None:
            QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Critical),
                'Ошибка',
                f'Алгоритм не настроен'
            ).exec()
            return False
        return True

    # Проверка на то что популяция сгенерирована
    def checkGenerated(self) -> bool:
        if self.ga.population is None:
            QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Critical),
                'Ошибка',
                f'Популяция не сгенерирована'
            ).exec()
            return False
        return True

    def onChildren(self) -> None:
        if not self.checkSetup() or not self.checkGenerated():
            return
        self.ga.parentsSelect()
        Logger.log('Выбраны родители:\n' + '\n'.join(map(str, self.ga.parents)) + '\n', LogLevel.Info)
        self.ga.crossover()
        self.offspring.setPopulation(self.ga.children)
        for w in [self.control.offspring, self.control.forceNext, self.control.results]:
            w.setEnabled(False)
        self.control.mutate.setEnabled(True)
        Logger.log(f'Полученные потомки:\n{self.ga.children}\n', LogLevel.Info)

    def onMutate(self) -> None:
        self.ga.mutation()
        Logger.log(f'Потомки с мутациями:\n{self.ga.mutChildren}\n', LogLevel.Info)
        self.mutations.setPopulation(self.ga.mutChildren)
        self.control.mutate.setEnabled(False)
        self.control.next.setEnabled(True)

    def onNext(self) -> None:
        self.ga.offspringSelect()
        Logger.log(f'Промежуточная популяция:\n{self.ga.tempPop}\n', LogLevel.Info)
        Logger.log(f'Новая популяция:\n{self.ga.offspring}\n', LogLevel.Info)
        self.ga.newPopulation()
        self.parents.setPopulation(self.ga.population)
        self.offspring.clear()
        self.mutations.clear()
        for b in [self.control.offspring, self.control.forceNext, self.control.results]:
            b.setEnabled(True)
        self.control.next.setEnabled(False)

    def onForceNext(self) -> None:
        if not self.checkSetup() or not self.checkGenerated():
            return
        self.ga.nextGeneration()
        self.parents.setPopulation(self.ga.population)

    def wait(self) -> None:
        self.setEnabled(False)
        QApplication.setOverrideCursor(QCursor(Qt.CursorShape.WaitCursor))
        self.statusBar().showMessage("Алгоритм выполняется...")

    def resume(self) -> None:
        self.setEnabled(True)
        QApplication.restoreOverrideCursor()
        self.statusBar().showMessage("Выполнение завершено")

    def onResults(self) -> None:
        if not self.checkSetup() or not self.checkGenerated():
            return

        self.wait()
        minSln = self.ga.population.min()
        while self.ga.gen < self.ga.params.maxGen:
            self.ga.nextGeneration()
            QApplication.processEvents()
            if self.ga.gen % self.subResult == 0 and minSln.F() != self.ga.population.min().F():
                minSln = self.ga.population.min()
                self.parents.setPopulation(self.ga.population)
                self.statusBar().showMessage(f'Алгоритм выполняется... Поколение: {self.ga.gen}')

        self.parents.setPopulation(self.ga.population.sorted())
        self.resume()

    def onInput(self) -> None:
        d = InputDialog(self)
        res = d.exec()
        if res:
            self.reg = d.reg
            self.statusBar().showMessage('Данные введены')
            Logger.log(f'Введены данные:\n{self.reg}\n', LogLevel.Info)
            self.setDefault()

    def onFile(self) -> None:
        d = QFileDialog.getOpenFileName(self, 'Выбрать файл с данными')
        if d[0] != '':
            try:
                reg = file_input(d[0])
                self.reg = reg
                self.statusBar().showMessage(f'Данные введены из файла {d[0]}')
                Logger.log(f'Введены данные:\n{self.reg}\n', LogLevel.Info)
                self.setDefault()
            except ArithmeticError:
                Logger.log(f'Файл {d[0]} cодержит некорректный регион', LogLevel.Warn)
                QMessageBox(
                    QMessageBox.Icon(QMessageBox.Icon.Critical),
                    'Ошибка',
                    f'Некорректный регион'
                ).exec()
                return
            except FileNotFoundError:
                Logger.log(f'Файл {d[0]} не найден', LogLevel.Warn)
                QMessageBox(
                    QMessageBox.Icon(QMessageBox.Icon.Critical),
                    'Ошибка',
                    f'Файл {d[0]} не найден'
                ).exec()
            except ValueError:
                Logger.log(f'Некорректные данные в файле {d[0]}', LogLevel.Warn)
                QMessageBox(
                    QMessageBox.Icon(QMessageBox.Icon.Critical),
                    'Ошибка',
                    f'Некорректные данные в файле {d[0]}'
                ).exec()

    def onSettings(self) -> None:
        d = SettingsDialog(self)
        res = d.exec()
        if res:
            self.ga = d.gaType(d.pSelector, d.recombinator, d.mutationer, d.oSelector)
            self.ga.params = d.params
            self.subResult = d.subResult
            self.statusBar().showMessage(f'Настройки применены')
            Logger.log(f'Текущие настройки ГА:\n{self.ga}\n', LogLevel.Info)
            self.setDefault()

    def onStart(self) -> None:
        if not self.checkSetup():
            return
        self.setDefault()
        self.ga.start(self.reg)
        self.ga.gen = 0
        self.parents.setPopulation(self.ga.population.sorted())
        Logger.log(f'Cгенерирована популяция:\n{self.ga.population.sorted()}\n', LogLevel.Info)

    def setDefault(self) -> None:
        for w in [self.control.offspring, self.control.forceNext, self.control.results]:
            w.setEnabled(True)
        for w in [self.control.mutate, self.control.next]:
            w.setEnabled(False)
        if self.ga is not None:
            self.ga.population = None
        self.parents.clear()
        self.offspring.clear()
        self.mutations.clear()

    def onInfo(self) -> None:
        msg = \
            'Программа предоставляет средства для решения задачи коммивояжёра с помощью генетического алгоритма.\n\n' \
            'Вввод данных возможен с вручную, либо из файла с координатами точек (координаты разделены пробелами, сами ' \
            'точки на разных строках).\n\n' \
            'Для запуска необходимо ввести данные и выбрать настройки алгоритма (настройки сохраняются в файле config).' \
            'Далее требуется сгенирировать начальную популяцию (кнопка меню: начать). После можно управлять процессом ' \
            'алгоритма с помощью кнопок управления. \n' \
            'С помощью кнопки получить результат алгоритм будет запущен' \
            'до указанного поколения (максимального), в процессе будут отображаться промежуточные результаты, ' \
            'промежуток отображения можно настроить (это влияет на производительность: чем меньше промежуток тем больше' \
            'графиков отрисовывается).\n\n' \
            'Параметры можно настравить различными способами. Однако эмпирически оказался успешными следующий подход:\n' \
            '1. Количество особей должно быть равно количеству городов, либо немногим больше (где-то на 5-10) \n' \
            '2. Количество поколений в среднем для классического алгоритма должно быть в 2-10 раз больше чем количество особей.' \
            ' Для метода прерывистого равновесия это число может быть значительно меньше (2-5 раз). Для генитора' \
            ' наоборот требуется больше поколений, в 100-500 раз больше размера популяции.\n' \
            '3. Операторы рекомбинации и мутации в среднем работают примерно одинаково и для выявления каких-то отличий' \
            ' требуется проводить статистические тесты. Однако по результатам тестирования алгоритмов на ' \
            'подготовленных регионах сочетание операторов OX и Инверсии дают чуть лучший результат (субъективно).\n' \
            '4. Вероятность кроссинговера должна быть достаточно высокая (80-100%).\n' \
            '5. Размеры аллели кроссинговера влияют на разнообразие популяции. Соответственно чем аллель больше, тем' \
            ' популяция разнообразнее, однако при этом алгоритм может колебаться вокруг оптимального решения. ' \
            'В целом если нужна быстрая сходимость этот параметр должен быть выше, если же нужно более точное решение, ' \
            'и есть возможность взять большое число поколений, то этот параметр можно уменьшить.\n' \
            '6. Вероятность мутации должна быть не слишком большая, и в зависимости от выбранных операторов она может' \
            ' быть в диапазоне (5-50)%. Если разнообразия с другими параметрами достаточно, вероятность мутации можно ' \
            'уменьшить, если же наоборот разнообразия не достаточно (например если использовать рулетку и элитный отбор), ' \
            'тогда этот параметр можно увеличивать вплоть до 50% (возможно и больше).\n' \
            '7. Отбор родителей. Панмиксия даёт достаточное разнообразие, однако уменьшает сходимость. Рулетка наоборот' \
            ' приводит к уменьшению разнообразия, однако и алгоритм сходится к оптимумам быстрее. При использовании' \
            ' панмиксии, другие параметры лучше настраивать на ускорение сходимости. А при использовании рулетки, наоборот' \
            ' остальные параметры рекомендуется настравивать на увеличение разнообразия (например размер аллели рекомбинации).' \
            ' Турнирный отбор можно гибко настроить с помощью размера турнира, чем размер турнира больше? тем больше будет ' \
            'более приспособленных особей, и тем меньше разнообразия.\n' \
            '8. Отбор в новую популяцию. Элитарный отбор аналогично рулетке уменьшает разнообразие популяции, однако ' \
            'обеспечивает более быструю сходимость. Отбор усечением можно настроить с помощью изменения пороговой величины, ' \
            'чем она больше тем популяции разнообразнее и тем медленнее алгоритм сходится.'

        QMessageBox(
            QMessageBox.Icon(QMessageBox.Icon.Information),
            'Справка',
            msg
        ).exec()
