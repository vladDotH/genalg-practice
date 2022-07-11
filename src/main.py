import sys
from PyQt6.QtWidgets import *
from src.gui import *

if __name__ == "__main__":
    qapp = QApplication.instance()
    if not qapp:
        qapp = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    qapp.exec()
