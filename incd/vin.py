from .incd import INCD
from collections import defaultdict

class VehicleIdentificationNumber(INCD):
    TABLE = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9,
        'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9}
    WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    BASE = 11
    LENGTH = 17
    TESTS = ["1M8GDM9AXKP042788"]

    def check_digit(self, number: str):
        total = sum(self.TABLE[c] * i for i, c in zip(self.WEIGHTS, number))
        check = total % 11
        return 'X' if check == 10 else check

    def is_valid(self, number: str) -> bool:
        check = self.check_digit(number)
        return check == number[8]

    def number_with_check_digit(self, number: str):
        "Expects a 17 digit 'number' and replaces the checksum digit"
        return number[:8] + self.check_digit(number) + number[9:]
