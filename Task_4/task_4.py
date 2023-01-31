# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# d:=sqrt(sqr(x2-x1)+sqr(y2-y1));
import math

x1 = int(input("Задайте координату x1: "))
y1 = int(input("Задайте координату y1: "))
x2 = int(input("Задайте координату x2: "))
y2 = int(input("Задайте координату y2: "))


def find_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)


print(find_distance(x1, y1, x2, y2))
