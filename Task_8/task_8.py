# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
#
#  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

new_list = [2, 3, 5, 9, 3, 1, 4, 1]


def find_not_even_position(my_list):
    total = 0
    long_list = len(my_list)
    for i in range(long_list):
        if i % 2 != 0:
            total += my_list[i]
    return total


print(find_not_even_position(new_list))