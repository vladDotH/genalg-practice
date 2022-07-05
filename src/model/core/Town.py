from __future__ import annotations


# Представление города (вектор)
class Town:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Расстояние между двумя городами
    def dist(self, t: Town) -> float:
        return ((self.x - t.x) ** 2 + (self.y - t.y) ** 2) ** (1 / 2)

    def __str__(self) -> str:
        return f'{{x: {self.x}, y: {self.y}}}'

    def __repr__(self) -> str:
        return str(self)
