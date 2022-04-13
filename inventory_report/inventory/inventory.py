from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(self, file_path, report_type):
        extention = file_path.split('.')[-1]
        file_import = {
            'json': JsonImporter,
            'csv': CsvImporter,
            'xml': XmlImporter,
        }
        inventory_list = file_import[extention].import_data(file_path)

        if report_type == 'simples':
            return SimpleReport.generate(inventory_list)

        return CompleteReport.generate(inventory_list)
