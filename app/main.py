from __future__ import annotations

from typing import Any


class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, self.__class__):
            new_km = self.km + other.km
        elif isinstance(other, (int, float)):
            new_km = self.km + other
        else:
            return NotImplemented
        return self.__class__(new_km)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, self.__class__):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Any) -> Distance:
        if isinstance(other, (int, float)):
            new_km = self.km * other
            return self.__class__(new_km)
        else:
            return NotImplemented

    def __truediv__(self, other: Any) -> Distance:
        if isinstance(other, (int, float)):
            new_km = round(self.km / other, 2)
            return self.__class__(new_km)
        else:
            return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented
