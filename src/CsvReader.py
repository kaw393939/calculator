import csv
from pprint import pprint


class CsvReader:

    def __init__(self, filepath):
        filepath = filepath
        with open(filepath) as text_data:
            self.csv_data = csv.DictReader(text_data, delimiter=',')

            for row in self.csv_data:
                pprint(row)

        pass
