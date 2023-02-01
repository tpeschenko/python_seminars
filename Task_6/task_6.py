# Напишите программу, которая принимает на вход
# число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

numbers = int(input("Введите число: "))


def find_numbers(number):
    lst_numbers = []
    num = 1
    for i in range(1, number + 1):
        num *= i
        lst_numbers.append(num)
    return lst_numbers


print(find_numbers(numbers))