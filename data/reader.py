"""Daten aus der CSV in unser Model einlesen"""

from csv import DictReader

from .models import Cut, Diamond


def read(file_path: str = "data/diamonds.csv") -> list[Diamond]:
    result = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = DictReader(file)
        for row in reader:
            diamond = Diamond(
                id=int(row["id"]),  # type: ignore
                carat=float(row["carat"]),  # type: ignore
                cut=Cut(row["cut"]),  # type: ignore
                color=row["color"],  # type: ignore
                clarity=row["clarity"],  # type: ignore
                depth=float(row["depth"]),  # type: ignore
                table=float(row["table"]),  # type: ignore
                price=int(row["price"]),  # type: ignore
                x=float(row["x"]),  # type: ignore
                y=float(row["y"]),  # type: ignore
                z=float(row["z"]),  # type: ignore
            )
            result.append(diamond)

    return result
