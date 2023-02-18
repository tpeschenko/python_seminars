# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

number_min = 2
number_max = 5

numbers = [5, 1, 2, 4, 10, 21, 2]


def find_index(number_min, number_max, numbers):
    print(f'Индексы массива в диапозоне от {number_min} до {number_max}: ', end="")
    long = len(numbers)
    for i in range(long):
        if number_min <= numbers[i] <= number_max:

            print(f"{i} ", end="")


find_index(number_min, number_max, numbers)