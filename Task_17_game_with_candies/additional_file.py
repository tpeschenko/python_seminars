import random


def find_winner_two_players(candies, step):
    """
    Игра с двумя игроками
    """
    while candies > 0 and step == 0:
        print("Ходит первый игрок")
        count = int(input("Первый игрок введите кол-во конфет: "))

        while count <= 0 or count > 28:
            print("Введено неверное кол-во конфет!, введите значение заново")
            count = int(input("Первый игрок введите кол-во конфет: "))
        candies -= count
        if candies <= 0:
            print("Выиграл Второй игрок")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")

        print("Ходит второй игрок")
        count = int(input("Второй игрок введите кол-во конфет: "))

        while count <= 0 or count > 28:
            print("Введено неверное кол-во конфет!, введите значение заново")
            count = int(input("Второй игрок введите кол-во конфет:  "))
            print("Введено больше конфет чем нужно, начните игру заново")

        candies -= count
        if candies <= 0:
            print("Выиграл Первый игрок")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")

    while candies > 0 and step == 1:
        print("Ходит Второй игрок")
        count = int(input("Второй игрок введите кол-во конфет: "))

        while count <= 0 or count > 28:
            print("Введено неверное кол-во конфет!, введите значение заново")
            count = int(input("Второй игрок введите кол-во конфет: "))
        candies -= count
        if candies <= 0:
            print("Выиграл Первый игрок")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")

        print("Ходит первый игрок")
        count = int(input("Второй игрок введите кол-во конфет: "))

        while count <= 0 or count > 28:
            print("Введено неверное кол-во конфет!, введите значение заново")
            count = int(input("Первый игрок введите кол-во конфет:  "))
            print("Введено больше конфет чем нужно, начните игру заново")

        candies -= count
        if candies <= 0:
            print("Выиграл Второй игрок")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")


def find_winner_with_bot(candies, step):
    """
    Игра с ботом
    """
    while candies > 0 and step == 0:
        print("Ходит игрок")
        count = int(input("Игрок введите кол-во конфет: "))

        while count <= 0 or count > 28:
            print("Введено неверное кол-во конфет!, введите значение заново")
            count = int(input("Игрок введите кол-во конфет: "))
        candies -= count
        if candies <= 0:
            print("Выиграл Второй игрок")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")

        print("Ходит бот")
        count = random.randint(1, 28)
        print(f"Бот взял {count} конфет")
        candies -= count
        if candies <= 0:
            print("Выиграл игрок")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")

    while candies > 0 and step == 1:
        print("Ходит Бот")
        count = random.randint(1, 28)
        print(f"Бот взял {count} конфет")
        candies -= count
        if candies <= 0:
            print("Выиграл игрок")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")

        print("Ходит игрок")
        count = int(input("Второй игрок введите кол-во конфет: "))

        while count <= 0 or count > 28:
            print("Введено неверное кол-во конфет!, введите значение заново")
            count = int(input("Игрок введите кол-во конфет:  "))
            print("Введено больше конфет чем нужно, начните игру заново")

        candies -= count
        if candies <= 0:
            print("Выиграл Бот")
            break
        else:
            print(f"Ход сделан, Осталось конфет: {candies}")

