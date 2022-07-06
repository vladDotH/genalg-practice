from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class LoggerWidget(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Логи")

        lt = QVBoxLayout(self)

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        lt.addWidget(self.text)
        self.setLayout(lt)

    # Вывод лога в виджет (можно использовать в качестве слота для логгера из util.Logger)
    def print(self, s) -> None:
        self.text.append(s)
