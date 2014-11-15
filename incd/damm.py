from .mod import ModBase

TABLE = ['0317598642',
         '7092154863',
         '4206871359',
         '1750983426',
         '6123045978',
         '3674209581',
         '5869720134',
         '8945362017',
         '9438617205',
         '2581436790']

class Damm(ModBase):
    TESTS = [5724]
    def check_digit(self, number: list):
        interim = 0
        for d in number:
            interim = int(TABLE[interim][d])

        return interim
