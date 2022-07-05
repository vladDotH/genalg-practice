import sys
from src.gui import *

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

pw = ControlWidget()
pw.show()

qapp.exec()
