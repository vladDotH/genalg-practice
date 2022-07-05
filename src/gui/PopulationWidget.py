from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure

from src.model.core import Population, Town


class PopulationWidget(QGroupBox):
    def __init__(self, name: str):
        super().__init__()
        self.setTitle(name)

        self.list = QListWidget()
        self.canvas = FigureCanvas(Figure())
        navbar = NavigationToolbar(self.canvas, self)

        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Orientation.Vertical)
        splitter.addWidget(self.list)
        splitter.addWidget(self.canvas)

        lt = QVBoxLayout(self)
        lt.addWidget(splitter)
        lt.addWidget(navbar)
        self.setLayout(lt)

        # Установка слота на сигнал изменения выбранного элемента
        self.list.currentRowChanged.connect(self.drawSolution)

        self.towns: list[Town]
        self.pop: Population

    # Слот отрисовки выбранного решения
    def drawSolution(self):
        x = [self.towns[i].x for i in self.pop[self.list.currentRow()]]
        y = [self.towns[i].y for i in self.pop[self.list.currentRow()]]
        self.canvas.figure.clf()
        self.canvas.figure.subplots().plot(list(x) + [x[0]], list(y) + [y[0]], linestyle='--', marker='o')
        self.canvas.draw()

    # Установка отображаемой популяции
    def setPopulation(self, pop: Population, towns: list[Town]):
        self.towns = towns
        self.pop = pop
        self.list.clear()
        self.canvas.figure.clf()
        for i in pop:
            self.list.addItem(str(i))

        self.list.setCurrentRow(0)
        # self.list.item(pop.index(pop.min())).setBackground(QColor('lime'))
        # self.list.setCurrentRow(pop.index(pop.min()))
