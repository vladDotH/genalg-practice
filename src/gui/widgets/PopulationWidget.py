from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure
from src.model.core import Population, Town


class PopulationWidget(QGroupBox):
    def __init__(self, name: str, parent=None):
        super().__init__(parent)

        self.list = QListWidget()
        self.canvas = FigureCanvas(Figure())
        # Сам график
        self.plt = self.canvas.figure.subplots()
        # Линия пути
        self.line = None
        self.pop: Population = None

        navbar = NavigationToolbar(self.canvas, self)
        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Orientation.Vertical)
        splitter.addWidget(self.list)
        splitter.addWidget(self.canvas)

        lt = QVBoxLayout(self)
        lt.addWidget(splitter)
        lt.addWidget(navbar)
        self.setLayout(lt)
        self.setTitle(name)

        # Установка слота на сигнал изменения выбранного элемента
        self.list.currentRowChanged.connect(self.drawSolution)

    # Слот отрисовки выбранного решения
    def drawSolution(self) -> None:
        x = [self.pop.reg[i].x for i in self.pop[self.list.currentRow()]]
        y = [self.pop.reg[i].y for i in self.pop[self.list.currentRow()]]

        # Если путь не отрисован, рисуется. Иначе просто меняются точки
        if self.line is None:
            self.line = self.plt.plot(list(x) + [x[0]], list(y) + [y[0]], linestyle='--', marker='o')[0]
        else:
            self.line.set_data(list(x) + [x[0]], list(y) + [y[0]])

        self.canvas.draw()

    def clear(self) -> None:
        self.list.clear()
        self.canvas.figure.clf()
        self.plt = self.canvas.figure.subplots()
        self.canvas.draw()

    # Установка отображаемой популяции
    def setPopulation(self, pop: Population) -> None:
        self.clear()

        self.pop = pop
        for i in pop:
            self.list.addItem(str(i))

        # Подписи номеров к городам
        for i in range(len(self.pop.reg)):
            self.plt.annotate(
                i, (self.pop.reg[i].x, self.pop.reg[i].y),
                textcoords="offset points", xytext=(4, 4)
            )
        self.line = None

        # Выделение лучшей особи
        m = pop.index(pop.min())
        self.list.item(m).setBackground(QColor('lime'))
        self.list.setCurrentRow(m)
