from abc import ABCMeta, abstractmethod
from functools import wraps

def convert_input(func):
    "Converts the argument to the annotated type before passing it to the function"
    if func.__annotations__.get("number", None) == int:
        func = use_int(func)
    elif func.__annotations__.get("number", None) == str:
        func = use_str(func)
    elif func.__annotations__.get("number", None) == bytes:
        func = use_bytes(func)
    return func

def use_bytes(func):
    "Converts input to bytes before passing it to the function"
    @wraps(func)
    def bytes_func(self, number):
        if isinstance(number, int):
            number = str(number)
        if isinstance(number, str):
            number = number.encode('ascii')
        return func(self, number)
    return bytes_func

def use_str(func):
    "Converts input to str before passing it to the function"
    @wraps(func)
    def str_func(self, number):
        if isinstance(number, int):
            number = str(number)
        if isinstance(number, bytes):
            number = number.decode('ascii')
        return func(self, number)
    return str_func

def use_int(func):
    "Converts any input to an integer before passing it to the function"
    @wraps(func)
    def int_func(self, number):
        return func(self, int(number))
    return int_func

def return_input_type(func):
    "Converts the output of the function to the same type as it received"
    @wraps(func)
    def input_returning_func(self, number):
        result = func(self, number)
        if isinstance(result, int):
            result = str(result)
        elif isinstance(result, bytes):
            result = result.decode('ascii')

        if isinstance(number, int):
            result = int(result)
        elif isinstance(number, bytes):
            result = result.encode('ascii')

        return result
    return input_returning_func

class INCDMeta(ABCMeta):
    "Wraps the input and output types of required methods for classes not marked as ignored"
    def __new__(cls, name, bases, namespace, **kwargs):
        if 'INCD_IGNORE' in namespace:
            del namespace['INCD_IGNORE']
            ignore = True
        else:
            ignore = False

        result = super().__new__(cls, name, bases, namespace, **kwargs)

        if not ignore:
            result.calculate_check_digit = return_input_type(convert_input(result.calculate_check_digit))
            result.is_number_valid = convert_input(result.is_number_valid)
        return result

class INCD(metaclass=INCDMeta):
    "Describes required methods of INCD classes and provides convenience methods"
    INCD_IGNORE = True
    @abstractmethod
    def is_number_valid(self, number):
        pass

    @abstractmethod
    def calculate_check_digit(self, number):
        pass

    @return_input_type
    @convert_input
    def number_with_check_digit(self, number: str):
        return number + self.calculate_check_digit(number)

    def verify_cycle(self, number):
        return self.is_number_valid(self.number_with_check_digit(number)) == True
