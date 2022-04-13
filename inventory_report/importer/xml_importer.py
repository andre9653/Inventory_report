import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, file_path):
        if file_path.split('.')[-1] != 'xml':
            raise ValueError('Arquivo inválido')

        tree = ET.parse(file_path)
        root = tree.getroot()

        inventory_list = []

        for lines in root:
            product_dict = dict()
            for line in lines:
                product_dict[line.tag] = line.text

            inventory_list.append(product_dict)

        return inventory_list


print(XmlImporter.import_data('inventory_report/data/inventory.xml'))
