# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

from typing import List


def calculate_fibonacci(n: int) -> List[int]:
    """
    Calculate not Fibonacci numbers

    :param n: Number of elements to calculate

    :return: List with  not Fibonacci numbers
    """

    numbers_1 = []
    numbers_2 = []

    first, second = 0, 1
    n += 1
    while n > len(numbers_1):
        for i in range(n):
            if i % 2 == 0:
                numbers_1.append(-first)
            else:
                numbers_1.append(first)
            first, second = second, first + second

    first, second = 0, 1
    while n > len(numbers_2):
        while n > len(numbers_2):
            numbers_2.append(first)
            first, second = second, first + second
    numbers = numbers_1[::-1] + numbers_2

    return numbers


assert calculate_fibonacci(0) == [0, 0]
assert calculate_fibonacci(2) == [-1, 1, 0, 0, 1, 1]
assert calculate_fibonacci(4) == [-3, 2, -1, 1, 0, 0, 1, 1, 2, 3]
assert calculate_fibonacci(8) == [-21, 13, -8, 5, -3, 2, -1, 1, 0, 0, 1, 1, 2, 3, 5, 8, 13, 21]
assert calculate_fibonacci(10) == [-55, 34, -21, 13, -8, 5, -3, 2, -1, 1, 0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
