from typing import Dict, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            content = json.load(file)

        return [Product(**product_info) for product_info in content]


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        products = []

        with open(self.path, "r", encoding="utf-8") as file:
            file_content = csv.DictReader(file)

            for row in file_content:
                products.append(
                    Product(
                        id=row["id"],
                        product_name=row["product_name"],
                        company_name=row["company_name"],
                        manufacturing_date=row["manufacturing_date"],
                        expiration_date=row["expiration_date"],
                        serial_number=row["serial_number"],
                        storage_instructions=row["storage_instructions"],
                    )
                )

        return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
