# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def calculates(decimal_number):
    check = ""
    while decimal_number != 0:
        check += str(decimal_number % 2)
        decimal_number = decimal_number // 2
    check = int(check[::-1])
    return check


assert calculates(45) == 101101
assert calculates(3) == 11
assert calculates(2) == 10



