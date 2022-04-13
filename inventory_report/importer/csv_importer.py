import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, file_path):
        if file_path.split('.')[-1] != 'csv':
            raise ValueError('Arquivo inválido')

        with open(file_path) as file:
            inventory_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            inventory_list = [
                row for row in inventory_reader
            ]

            return inventory_list
