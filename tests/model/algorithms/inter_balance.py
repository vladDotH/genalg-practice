import sys
from PyQt6.QtWidgets import QApplication
from src.gui import *
from src.model import *

# Координаты городов
X = [-6, -4, 0, 5, 6, 3, 0, -4]
Y = [0, -4, -6, -3, 1.5, 5.2, 6.2, 4.2]
towns = [Town(x, y) for x, y in zip(X, Y)]

ga = InterBalance(None, ox, swap, elite)
ga.params.psize = 10
ga.params.rprob = 0.9
ga.params.mprob = 0.05
ga.params.minR = 0.4
ga.params.maxR = 0.6
ga.params.maxGen = 10
ga.start(Region(towns))

print('Города:', ga.reg, '\n')
print('Нач. популяция:', ga.population, '', sep='\n')

ga.parentsSelect()
print('Родительские пары:', *ga.parents, '', sep='\n')

ga.crossover()
print('Полученные потомки:', ga.children, '', sep='\n')

ga.mutation()
print('Мутированные потомки:', ga.mutChildren, '', sep='\n')

ga.offspringSelect()
print('Промежуточная популяция:', ga.tempPop, '', sep='\n')
print('Отобранные в следующую популяцию::', ga.offspring, '', sep='\n')
ga.newPopulation()

while ga.gen < ga.params.maxGen:
    print(f'Популяция на {ga.gen} поколении:', ga.population.sorted().normalized(), '', sep='\n')
    ga.nextGeneration()

print(f'Популяция на {ga.gen} поколении:', ga.population.sorted().normalized(), sep='\n')

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

pw = PopulationWidget('итоговая популяция')
pw.show()

pw.setPopulation(ga.population.sorted().normalized())

qapp.exec()
