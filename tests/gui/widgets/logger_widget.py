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
for i in range(10):
    Logger.log(f'sample log №{i}', LogLevel.Warn)


# Вывод логов из других потоков
def thr_f(n, lvl):
    i = 0
    while pw.isVisible():
        Logger.log(f'Thread {n} log №{i}', lvl)
        time.sleep(0.5)
        i += 1


thr1 = threading.Thread(target=thr_f, args=[1, LogLevel.Debug])
thr1.start()
thr2 = threading.Thread(target=thr_f, args=[2, LogLevel.Info])
thr2.start()

qapp.exec()
