from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, products):
        relatorio_simples = super().generate(products)
        prod_by_company = super().products_by_company(products).items()
        prod_by_company_str = "Produtos estocados por empresa: \n"
        for prod in prod_by_company:
            prod_by_company_str += f"- {prod[0]}: {prod[1]}\n"
        relatorio = (
            f"{relatorio_simples}\n"
            f"{prod_by_company_str}"
        )

        return relatorio
