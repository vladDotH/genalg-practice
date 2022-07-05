from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class LoggerWidget(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Логи")
        lt = QVBoxLayout(self)
        self.text = QTextEdit()
        lt.addWidget(self.text)
        self.setLayout(lt)
        self.text.setReadOnly(True)

    def print(self, s):
        self.text.append(s)

