from .mod import ModBase

class UPC(ModBase):
    TESTS = ["043000126110", "043000102107"]
    LENGTH = 12
    BASE = 10
    def check_digit(self, digits: list):
        even = sum(digits[::2]) * 3
        odd = sum(digits[1::2])
        total = even + odd
        return -total % self.BASE
