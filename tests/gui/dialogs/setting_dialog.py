import sys
from PyQt6.QtWidgets import *
from src.gui import *

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

d = SettingsDialog()
r = d.exec()

print('Результатат:', r)

print('Выбранные настройки:')
print('Тип ГА:', d.gaType)
print('Оператор выбора родителей:', d.pSelector)
print('Оператор рекомбинации:', d.recombinator)
print('Оператор мутации:', d.mutationer)
print('Оператор выбора в популяцию:', d.oSelector)
print('Параметры:', d.params)
