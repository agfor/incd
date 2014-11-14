from .incd import INCD

class Mod(INCD):
    INCD_IGNORE = True
    def calculate_check_digit(self, number: int):
        return number % self.BASE

    def is_number_valid(self, number: str):
        return self.calculate_check_digit(number[:-1]) == number[-1]

class Mod7(Mod):
    """
    Airline Tickets
    PedEx & UPS Packages
    Avis & National Rental Cars
    """
    BASE = 7

class Mod9(Mod):
    "USPS Money Orders"
    BASE = 9
