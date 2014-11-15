from .mod import ModBase
from itertools import cycle

class RoutingNumber(ModBase):
    TESTS = ["031000503"]
    LENGTH = 9
    BASE = 10
    def check_digit(self, digits: list):
        weights = cycle((7, 3, 9))
        total = sum(d * next(weights) for d in digits)
        return total % self.BASE
