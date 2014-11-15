from .mod import ModBase

class TravelersChecks(ModBase):
    LENGTH = 11
    "Amex and Visa Travelers' Checks"
    def check_digit(self, number: int):
        return -number % 9
