from .incd import INCD

class ModBase(INCD):
    INCD_IGNORE = True
    LENGTH = None
    def is_valid(self, number: str) -> bool
        if self.LENGTH:
            assert len(number) == self.LENGTH
        return self.check_digit(number[:-1]) == number[-1]

    def number_with_check_digit(self, number: str):
        return number + self.check_digit(number)

    def check_digit(self, number: int):
        return -number % self.BASE

class USPSMoneyOrder(ModBase):
    BASE = 9
    LENGTH = 11

class AirlineTicket(ModBase):
    BASE = 7
    LENGTH = 13

class ZipPlus4(ModBase):
    BASE = 10
    LENGTH = 10

class ZipPlus4Plus2(ModBase):
    BASE = 10
    LENGTH = 12
