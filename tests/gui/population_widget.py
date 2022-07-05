import sys
from src.gui import *
from src.model import *
from PyQt6.QtWidgets import *

X = [-6, -4, 0, 5, 6, 3, 0, -4]
Y = [0, -4, -6, -3, 1.5, 5.2, 6.2, 4.2]
towns = [Town(x, y) for x, y in zip(X, Y)]
print(f'Towns: {towns}\n')

ga = GA(towns, 15)

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

pw = PopulationWidget()
pw.show()

pw.setPopulation(ga.population, towns)

qapp.exec()
