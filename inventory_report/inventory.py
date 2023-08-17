from inventory_report.product import Product
from typing import Optional, List


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        self.__data = data or []

    def add_data(self, data: List[Product]) -> None:
        self.__data.extend(data)

    @property
    def data(self) -> List[Product]:
        return self.__data
