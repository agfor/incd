from .incd import INCD

class UPC(INCD):
    def calculate_check_digit(self, number: str):
        digits = [int(d) for d in number]
        even = sum(digits[::2]) * 3
        odd = sum(digits[1::2])
        return -1 * (odd + even) % 10

    def is_number_valid(self, number: str):
        assert len(number) == 12
        return self.calculate_check_digit(number[:-1]) == number[-1]
