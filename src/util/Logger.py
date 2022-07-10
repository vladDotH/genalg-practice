from __future__ import annotations
from typing import Callable
from PyQt6.QtCore import pyqtSignal, QObject
import threading
from src.util.LogLevel import LogLevel


# Логгер-синглтон
class Logger(QObject):
    _instance = None
    _lock = threading.Lock()
    logSignal = pyqtSignal(str, LogLevel)

    def __init__(self):
        if Logger._instance is None:
            super().__init__()

    @staticmethod
    def _get() -> Logger:
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    # Функция логгирования, выпускает сигнал со строкой лога (обработчик получит её в слот)
    @staticmethod
    def log(msg: str, lvl: LogLevel = LogLevel.Debug) -> None:
        Logger._lock.acquire()
        Logger._get().logSignal.emit(msg, lvl)
        Logger._lock.release()

    # Присоединение слота обработчиков
    @staticmethod
    def connect(slot: Callable[[str], None]) -> None:
        Logger._lock.acquire()
        Logger._get().logSignal.connect(slot)
        Logger._lock.release()
