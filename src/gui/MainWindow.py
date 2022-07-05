from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from src.gui.LoggerWidget import LoggerWidget
from src.gui.ControlWidget import ControlWidget
from src.gui.PopulationWidget import PopulationWidget


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
        self.control = ControlWidget()

        for w in [self.parents, self.offspring, self.mutations]:
            popSplitter.addWidget(w)

        infoSplitter.addWidget(self.control)
        infoSplitter.addWidget(self.logger)
        infoSplitter.setStretchFactor(1, 1)

        mainSplitter.addWidget(popSplitter)
        mainSplitter.addWidget(infoSplitter)
        mainSplitter.setOrientation(Qt.Orientation.Vertical)
        self.setCentralWidget(mainSplitter)

        self.input = QMenu('Ввести данные', self)
        self.settings = QMenu('Настройки', self)
        self.start = QMenu('Запуск', self)
        self.info = QMenu('Справка', self)

        for m in [self.input, self.settings, self.start, self.info]:
            self.menuBar().addMenu(m)
