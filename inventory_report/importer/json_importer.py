import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, file_path):
        if file_path.split('.')[-1] != 'json':
            raise ValueError('Arquivo inválido')

        with open(file_path) as file:
            inventory_list = json.load(file)

            return inventory_list
