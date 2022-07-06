import sys
from PyQt6.QtWidgets import *
from src.gui import *
from src.util import *
import threading
import time

qapp = QApplication.instance()
if not qapp:
    qapp = QApplication(sys.argv)

# Создаём виджет логгера
pw = LoggerWidget()
pw.show()

# Подключаем логгер к созданному виджету
Logger.connect(pw.print)

# Вывод логов
for i in range(25):
    Logger.log(f'sample log №{i}')


# Вывод логов из других потоков
def thr_f(n):
    for i in range(25):
        Logger.log(f'Daemon {n} log №{i}')
        time.sleep(0.1)


thr1 = threading.Thread(target=thr_f, args=[1])
thr1.start()
thr2 = threading.Thread(target=thr_f, args=[2])
thr2.start()

qapp.exec()
