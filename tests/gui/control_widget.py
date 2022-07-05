import sys
from PyQt6.QtWidgets import *
from src.gui import *

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

pw = ControlWidget()
pw.show()

qapp.exec()
