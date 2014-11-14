from .incd import INCD

class AmexTravelersChecks(INCD):
    def calculate_check_digit(self, number: int):
        return -number % 9

    def is_number_valid(self, number: int):
        assert len(number) == 10
        return number % 9 == 0
