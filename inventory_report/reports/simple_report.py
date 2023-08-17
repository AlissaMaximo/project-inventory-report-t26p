from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from datetime import date
from typing import List, Dict


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def get_oldest_manufacturing_date(self) -> str:
        manufacturing_dates = [
            product.manufacturing_date
            for inventory in self.inventories
            for product in inventory.data
        ]

        return min(manufacturing_dates)

    def get_nearest_expiration_date(self) -> str:
        all_valid_expiration_dates = [
            product.expiration_date
            for inventory in self.inventories
            for product in inventory.data
            if product.expiration_date >= str(date.today())
        ]

        return min(all_valid_expiration_dates)

    def get_largest_inventory_company(self) -> str:
        duos: Dict[str, int] = {}

        for inventory in self.inventories:
            for product in inventory.data:
                if duos.get(product.company_name):
                    duos[product.company_name] += 1
                else:
                    duos[product.company_name] = 1

        return max(duos, key=lambda product: duos[product])

    def generate(self) -> str:
        return (
            "Oldest manufacturing date: "
            + f"{self.get_oldest_manufacturing_date()}\n"
            + "Closest expiration date: "
            + f"{self.get_nearest_expiration_date()}\n"
            + "Company with the largest inventory: "
            + f"{self.get_largest_inventory_company()}\n"
        )
