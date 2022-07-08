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

        self.parents = PopulationWidget('Популяция')
        self.offspring = PopulationWidget('Потомки')
        self.mutations = PopulationWidget('Мутации')
        self.logger = LoggerWidget()
        Logger.connect(self.logger.print)
        self.control = ControlWidget()

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

        self.control.offspring.clicked.connect(self.onChildren)
        self.control.mutate.clicked.connect(self.onMutate)
        self.control.next.clicked.connect(self.onNext)
        self.control.forceNext.clicked.connect(self.onForceNext)
        self.control.results.clicked.connect(self.onResults)

    def checkSetup(self):
        if self.reg is None:
            msg = QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Critical),
                'Ошибка',
                f'Не введены данные'
            )
            msg.exec()
            return False
        if self.ga is None:
            msg = QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Critical),
                'Ошибка',
                f'Алгоритм не настроен'
            )
            msg.exec()
            return False

        return True

    def checkGenerated(self):
        if self.ga.population is None:
            msg = QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Critical),
                'Ошибка',
                f'Популяция не сгенерирована'
            )
            msg.exec()
            return False
        return True

    def onChildren(self):
        if not self.checkSetup() or not self.checkGenerated():
            return

        self.ga.parentsSelect()
        Logger.log('Выбраны родители:\n' + '\n'.join(map(str, self.ga.parents)))
        self.ga.crossover()
        self.offspring.setPopulation(self.ga.children.sorted().normalized())
        self.control.offspring.setEnabled(False)
        self.control.forceNext.setEnabled(False)
        self.control.results.setEnabled(False)
        self.control.mutate.setEnabled(True)
        Logger.log(f'Полученные потомки:\n{self.ga.children}\n')

    def onMutate(self):
        self.ga.mutation()
        Logger.log(f'Потомки с мутациями:\n{self.ga.mutChildren}\n')
        self.mutations.setPopulation(self.ga.mutChildren.sorted().normalized())
        self.control.mutate.setEnabled(False)
        self.control.next.setEnabled(True)

    def onNext(self):
        self.ga.offspringSelect()
        Logger.log(f'Промежуточная популяция:\n{self.ga.tempPop}\n')
        Logger.log(f'Новая популяция:\n{self.ga.offspring}\n')
        self.ga.newPopulation()
        self.parents.setPopulation(self.ga.population.sorted().normalized())
        self.offspring.clear()
        self.mutations.clear()
        for b in [self.control.offspring, self.control.forceNext, self.control.results]:
            b.setEnabled(True)
        self.control.next.setEnabled(False)

    def onForceNext(self):
        if not self.checkSetup() or not self.checkGenerated():
            return
        self.ga.nextGeneration()
        self.parents.setPopulation(self.ga.population.sorted().normalized())

    def onResults(self):
        if not self.checkSetup() or not self.checkGenerated():
            return

        while self.ga.gen < self.ga.params.maxGen:
            self.ga.nextGeneration()

        self.parents.setPopulation(self.ga.population.sorted().normalized())
        self.parents.list.item(0).setBackground(QColor('lime'))

    def onInput(self):
        d = InputDialog()
        res = d.exec()
        if res:
            self.reg = Region(d.towns)
            self.statusBar().showMessage('Данные введены')
            Logger.log(f'Введены данные:\n{self.reg}\n')

    def onFile(self):
        d = QFileDialog.getOpenFileName(self, 'Выбрать файл с данными')
        if d[0] != '':
            try:
                reg = Region(file_input(d[0]))
                self.reg = reg
                self.statusBar().showMessage(f'Данные введены из файла {d[0]}')
                Logger.log(f'Введены данные:\n{self.reg}\n')
            except FileNotFoundError:
                msg = QMessageBox(
                    QMessageBox.Icon(QMessageBox.Icon.Critical),
                    'Ошибка',
                    f'Файл {d[0]} не найден'
                )
                msg.exec()
            except ValueError:
                msg = QMessageBox(
                    QMessageBox.Icon(QMessageBox.Icon.Critical),
                    'Ошибка',
                    f'Некорректные данные в файле {d[0]}'
                )
                msg.exec()

    def onSettings(self):
        d = SettingsDialog()
        res = d.exec()
        if res:
            self.ga = d.gaType(d.pSelector, d.recombinator, d.mutationer, d.oSelector)
            self.ga.params = d.params
            self.statusBar().showMessage(f'Настройки применены')
            Logger.log(f'Текущие настройки ГА:\n{self.ga}\n')

    def onStart(self):
        if not self.checkSetup():
            return
        self.ga.start(self.reg)
        self.ga.gen = 0
        self.parents.setPopulation(self.ga.population.sorted().normalized())
        Logger.log(f'Cгенерирована популяция:\n{self.ga.population.sorted().normalized()}\n')

        for w in [self.control.offspring, self.control.forceNext, self.control.results]:
            w.setEnabled(True)
        for w in [self.control.mutate, self.control.next]:
            w.setEnabled(False)
        self.offspring.clear()
        self.mutations.clear()

    def onInfo(self):
        pass
