import sys
from src.gui import *

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

pw = LoggerWidget()
pw.show()

for i in range(100):
    pw.print(f'sample log {i}')


qapp.exec()
