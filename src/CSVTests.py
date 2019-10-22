import unittest
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('employee_birthday.txt')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csv_reader, CsvReader)
     
     


if __name__ == '__main__':
    unittest.main()
