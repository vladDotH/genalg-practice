from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class ControlWidget(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Управление")
        lt = QVBoxLayout(self)

        self.offspring = QPushButton(self)
        self.offspring.setText("Сгенерировать потомство")

        self.mutate = QPushButton(self)
        self.mutate.setText("Провести мутацию")

        self.next = QPushButton(self)
        self.next.setText("Следующее поколение")

        self.forceNext = QPushButton(self)
        self.forceNext.setText("Следующий шаг")

        self.results = QPushButton(self)
        self.results.setText("Перейти к результату")

        lt.addWidget(self.offspring)
        lt.addWidget(self.mutate)
        lt.addWidget(self.next)
        lt.addWidget(self.forceNext)
        lt.addWidget(self.results)

        self.setLayout(lt)