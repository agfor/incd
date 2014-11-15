from .mod import ModBase

class Luhn10(ModBase):
    TESTS = ["4111111111111111", "371449635398431"]
    BASE = 10
    def check_digit(self, digits: list):
        total = sum(d * 2 % 10 for d in digits[-1::-2])
        total += sum(1 for d in digits[-1::-2] if d > 4)
        total += sum(digits[-2::-2])

        return -total % self.BASE
