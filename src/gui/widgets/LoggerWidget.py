from PyQt6.QtWidgets import *
from src.util.Logger import *


# Виджет вывода логов
class LoggerWidget(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Логи")

        self.levels = [False] * 3
        box = QGroupBox("Уровни логов")
        boxlt = QVBoxLayout(box)
        self.debug = QCheckBox(LogLevel.Debug.name)
        self.info = QCheckBox(LogLevel.Info.name)
        self.warn = QCheckBox(LogLevel.Warn.name)

        self.debug.toggled.connect(lambda s: self.levelToggled(0, s))
        self.info.toggled.connect(lambda s: self.levelToggled(1, s))
        self.warn.toggled.connect(lambda s: self.levelToggled(2, s))

        for i, w in zip(list(range(3)), [self.debug, self.info, self.warn]):
            boxlt.addWidget(w)

        self.info.toggle()
        self.warn.toggle()
        box.setLayout(boxlt)

        lt = QHBoxLayout(self)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        lt.addWidget(box)
        lt.addWidget(self.text)
        self.setLayout(lt)

    def levelToggled(self, n: int, state: bool) -> None:
        self.levels[n] = state

    # Вывод лога в виджет (можно использовать в качестве слота для логгера из util.Logger)
    def print(self, s: str, lvl: LogLevel) -> None:
        if self.levels[lvl.value]:
            self.text.append(f'[{lvl.name}]: {s}')
