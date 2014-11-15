from .mod import ModBase

class UPC(ModBase):
    TESTS = ["043000126110", "043000102107"]
    LENGTH = 12
    def check_digit(self, number: str):
        digits = [int(d) for d in number]
        even = sum(digits[::2]) * 3
        odd = sum(digits[1::2])
        return -(odd + even) % 10
