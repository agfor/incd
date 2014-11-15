from .mod import ModBase
from itertools import cycle

class RoutingNumber(ModBase):
    TESTS = ["031000503"]
    LENGTH = 9
    def check_digit(self, number: str):
        weights = cycle((7, 3, 9))
        total = sum(int(d) * next(weights) for d in number)
        return total % 10
