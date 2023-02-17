# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def find_factors_number(number) -> list:
    list_factors_number = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_factors_number.append(i)
    return list_factors_number


if __name__ == '__main__':
    print(find_factors_number(10))