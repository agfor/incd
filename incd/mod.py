from .incd import INCD

class ModBase(INCD):
    INCD_IGNORE = True
    LENGTH = None
    def is_valid(self, number: str):
        if self.LENGTH:
            assert len(number) == self.LENGTH
        return self.check_digit(number[:-1]) == number[-1]

class Mod(ModBase):
    INCD_IGNORE = True
    def check_digit(self, number: int):
        return number % self.BASE


class USPSMoneyOrders(Mod):
    BASE = 9
    LENGTH = 11

class AirlineTickets(Mod):
    BASE = 7
    LENGTH = 13
