from .mod import ModBase
from .incd import convert_input, return_input_type
from .upc import UPC

class ISBN10(ModBase):
    TESTS = ["8090273416", "080442957X"]
    LENGTH = 10
    BASE = 11
    def check_digit(self, digits: list):
        with_weights = enumerate(reversed(digits), 2)
        total = sum(i * d for i, d in with_weights)
        check = -total % self.BASE
        return 'X' if check == 10 else check

class ISBN13(UPC):
    TESTS = ["9780306406157"]
    LENGTH = 13

    def convert_from_isbn_10(self, number: str):
        return self.number_with_check_digit('978' + number[:-1])
