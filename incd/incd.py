from abc import ABCMeta, abstractmethod
from functools import wraps

def convert_to_list(number):
    if isinstance(number, int):
        number = str(number)
    if isinstance(number, str):
        number = [int(d) for d in number]
    if not isinstance(number, list):
        raise
    return number

def convert_to_str(number):
    if isinstance(number, int):
        number = str(number)
    elif isinstance(number, list):
        number = ''.join(str(d) for d in number)
    if not isinstance(number, str):
        raise
    return number

def convert_to_int(number):
    if isinstance(number, list):
        number = ''.join(str(d) for d in number)
    if isinstance(number, str):
        number = int(number)
    if not isinstance(number, int):
        raise
    return number

TYPES = {int: convert_to_int, str: convert_to_str, list: convert_to_list}

def convert_input(func):
    "Converts the argument to the annotated type before passing it to the function"
    convert_to = next((value for key, value in func.__annotations__.items() if key != 'return'), None)

    if not convert_to:
        return func

    if convert_to in TYPES:
        convert = TYPES[convert_to]
    else:
        raise

    @wraps(func)
    def converter(self, number):
        return func(self, convert(number))

    return converter

def return_input_type(func):
    "Converts the output of the function to the same type as it received"
    if 'return' in func.__annotations__:
        return func

    @wraps(func)
    def input_returning_func(self, number):
        result = func(self, number)
        result = convert_to_str(result)

        if isinstance(number, int):
            result = int(result)
        elif isinstance(number, list):
            result = [int(d) for d in number]

        return result
    return input_returning_func

REGISTRY = []

class INCDMeta(type):
    "Wraps the input and output types of required methods for classes not marked as ignored"
    def __new__(cls, name, bases, namespace, **kwargs):
        if 'INCD_IGNORE' in namespace:
            del namespace['INCD_IGNORE']
            ignore = True
        else:
            ignore = False

        for attr, obj in dict(namespace).items():
            if name[0] != '_' and callable(obj):
                obj = convert_input(obj)
                obj = return_input_type(obj)
                namespace[attr] = obj

        result = super().__new__(cls, name, bases, namespace, **kwargs)

        if not ignore:
            if not all(name in dir(result) for name in ['check_digit', 'is_valid', 'number_with_check_digit']):
                raise
            REGISTRY.append(result)

        return result

def test():
    for cls in REGISTRY:
        tests = getattr(cls, 'TESTS', [])
        print(cls.__name__, "- {} Tests".format(len(tests)))
        for test in tests:
            print('', test)
            assert cls().is_valid(test) == True

class INCD(metaclass=INCDMeta):
    INCD_IGNORE = True
