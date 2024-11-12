# ЗАДАНИЕ ПО ТЕМЕ "Try и Except"

from decimal import Decimal


def add_everything_up(a, b):
    try:
        if all(isinstance(x, (int, float)) for x in [a, b]):
            result = Decimal(str(a)) + Decimal(str(b))
        else:
            result = a + b
    except TypeError:
        result = str(a) + str(b)
    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
# print(add_everything_up(7.4, 3.6))
# print(add_everything_up(12, 3))