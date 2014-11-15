from .mod import ModBase

class TravelersCheck(ModBase):
    LENGTH = 11
    BASE = 9
    "Amex and Visa Travelers' Checks"
    def check_digit(self, number: int):
        return number % self.BASE
