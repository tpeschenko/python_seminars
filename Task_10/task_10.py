# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

new_list = [1.1, 1.2, 3.1, 5, 10.01]


def find_difference_fraction_max_min(my_list):
    max_fraction = 0
    min_fraction = 1
    for i in my_list:
        value = i % 1
        if value > max_fraction:
            max_fraction = value
        if value < min_fraction and value != 0:
            min_fraction = value
    difference = max_fraction - min_fraction
    return round(difference, 2)


print(find_difference_fraction_max_min(new_list))