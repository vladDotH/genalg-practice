from PyQt6.QtWidgets import *


# Виджет кнопок управления
class ControlWidget(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
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

        for w in [self.offspring, self.mutate, self.next, self.forceNext, self.results]:
            lt.addWidget(w)

        self.setLayout(lt)
