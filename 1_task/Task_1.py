# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
number = int(input("Введите цифру: "))

if number == 6 or number == 7:
    print("Выходной день")
elif 0 < number < 6:
    print("Будни")
else:
    print("Такого дня недели нет")



