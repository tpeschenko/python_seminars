# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

new_list = [2, 3, 4, 5, 6]

half_new_list = round((len(new_list) / 2) + 0.1)


def find_two_numbers(my_list, half_list):
    for i in range(half_list):
        print(f"{my_list[i] * my_list.pop()} ", end="")


find_two_numbers(new_list, half_new_list)
