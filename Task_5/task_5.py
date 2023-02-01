# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

numbers = input("Введите число: ")


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def sum_number(str):
    sum = 0
    if is_number(numbers):
        for i in str:
            if i == ".":
                continue
            else:
                sum += int(i)

    else:
        print("Это не число, запустите заново \nпрограмму и введите именно число!")
        sum = None
    return sum


print(f"\nСумма такого числа равна: {sum_number(numbers)}")

