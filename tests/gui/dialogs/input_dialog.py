import sys
from PyQt6.QtWidgets import *
from src.gui import *

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

d = InputDialog()
r = d.exec()
print('Результат:', r)
print('Введено:', d.towns)
