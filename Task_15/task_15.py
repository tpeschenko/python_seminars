# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

def print_list_not_repeat_elements(number):
    numbers = []
    for i in number:
        if i not in numbers:
            numbers.append(i)
    return numbers


if __name__ == '__main__':
    print(print_list_not_repeat_elements("222222222222111111111111"))
