from inventory_report.reports.simple_report import SimpleReport
from typing import Dict


class CompleteReport(SimpleReport):
    def get_stocks_by_company(self) -> Dict[str, int]:
        duos: Dict[str, int] = {}

        for inventory in self.inventories:
            for product in inventory.data:
                if duos.get(product.company_name):
                    duos[product.company_name] += 1
                else:
                    duos[product.company_name] = 1

        return duos

    def generate(self) -> str:
        stocks_by_company = self.get_stocks_by_company()
        duos = ""

        for company, quantity in stocks_by_company.items():
            duos += f"- {company}: {quantity}\n"

        return super().generate() + "Stocked products by company:\n" + duos
