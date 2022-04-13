import datetime


class SimpleReport():
    @classmethod
    def products_by_company(self, prod):
        prod_by_company = dict()
        for product in prod:
            if product['nome_da_empresa'] not in prod_by_company.keys():
                prod_by_company[product['nome_da_empresa']] = 1
            else:
                prod_by_company[product['nome_da_empresa']] += 1
        return prod_by_company

    @classmethod
    def generate(self, products):
        fabrication_dates = [
            datetime.date(
                int(product['data_de_fabricacao'].split('-')[0]),
                int(product['data_de_fabricacao'].split('-')[1]),
                int(product['data_de_fabricacao'].split('-')[2])
            )
            for product in products
        ]
        expiry_dates = [
            datetime.date(
                int(product['data_de_validade'].split('-')[0]),
                int(product['data_de_validade'].split('-')[1]),
                int(product['data_de_validade'].split('-')[2])
            )
            for product in products
        ]

        oldest_fabrication_date = min(fabrication_dates)

        for date in expiry_dates:
            if date < datetime.date.today():
                expiry_dates.remove(date)

        next_expiry_date = min(expiry_dates)

        company_with_most_products = max(
            self.products_by_company(products).items()
        )[0]

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {next_expiry_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_with_most_products}\n"
        )
