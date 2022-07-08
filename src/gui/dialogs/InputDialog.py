from PyQt6.QtWidgets import *

from src.model.core.Town import Town


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ввод данных")

        self.count = QSpinBox(self)
        self.btn = QPushButton(self)
        self.btn.setText("Подтвердить")
        self.btn.clicked.connect(self.ret)
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['x', 'y'])
        self.table.resizeColumnsToContents()

        clbl = QLabel('Количество городов:')
        tlbl = QLabel('Координаты')
        lt = QVBoxLayout()
        lt.addWidget(clbl)
        lt.addWidget(self.count)
        lt.addWidget(tlbl)
        lt.addWidget(self.table)
        lt.addWidget(self.btn)
        self.setLayout(lt)

        self.count.valueChanged.connect(self.table.setRowCount)
        self.towns: list[Town] = []

    def ret(self) -> None:
        i = 0
        try:
            self.towns.clear()
            for i in range(self.table.rowCount()):
                x, y = [self.table.item(i, j) for j in [0, 1]]
                if x is None or y is None:
                    raise ValueError()
                self.towns.append(Town(float(x.text()), float(y.text())))

        except (ValueError, TypeError):
            msg = QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Critical),
                'Ошибка',
                f'Некорректые данные в ряду: {i + 1}'
            )
            msg.exec()
            return

        self.accept()
