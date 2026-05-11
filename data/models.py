"""
Datenstrukturen definieren
https://www.kaggle.com/datasets/shivam2503/diamonds?resource=download
"""

from dataclasses import dataclass
from enum import StrEnum
from typing import Literal


class Cut(StrEnum):  # erbe von StrEnum
    FAIR = "Fair"
    GOOD = "Good"
    VERYGOOD = "Very Good"
    PREMIUM = "Premium"
    IDEAL = "Ideal"

    # def __repr__(self) -> str:
    #     return self.name


Color = Literal["J", "I", "H", "G", "F", "E", "D"]
Clarity = Literal["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]


@dataclass
class Diamond:
    id: int
    carat: float
    cut: Cut
    color: Color
    clarity: Clarity
    depth: float
    table: float
    price: int
    x: float
    y: float
    z: float

    def __post_init__(self):
        assert self.id >= 0, "id must be non-negative"
        assert self.carat > 0, "carat must be positive"
        assert self.depth > 0, "depth must be positive"
        assert self.table > 0, "table must be positive"
        assert self.price > 0, "price must be positive"
        assert self.x >= 0, "x must be non-negative"
        assert self.y >= 0, "y must be non-negative"
        assert self.z >= 0, "z must be posinon-negativetive"
