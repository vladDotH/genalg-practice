import sys
from PyQt6.QtWidgets import *
from src.gui import *

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

d = SettingsDialog()
r = d.exec()
print(r)
