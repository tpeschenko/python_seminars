# Создайте программу для игры в ""Крестики-нолики"".
field = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]


def print_field(new_field):
    print("Поля игры:")
    for i in range(3):

        for j in range(3):
            print(new_field[i][j], end="    ")
        print("\n")


print_field(field)


def check_condition(value_input, conclusion):
    sum1 = ""
    sum2 = ""
    for i in range(3):
        for j in range(3):
            sum1 += field[i][j]
            sum2 += field[j][i]
        if (sum1 == value_input or field[0][2] + field[1][1] + field[2][0] == value_input
                or field[0][0] + field[1][1] + field[2][2] == value_input or sum2 == value_input):
            print(conclusion)
            return "Победа"


def game_tic_tac():
    while True:
        while True:
            x1 = int(input("Введите координаты для X по горизонтали: "))
            x2 = int(input("Введите координаты для X по вертикали: "))
            if field[x1][x2] != "x" and field[x1][x2] != "0":
                field[x1][x2] = "x"
                print_field(field)
                point = check_condition("xxx", "Выиграл Крестик")
                if point == "Победа":
                    return "До встречи"
                break
            else:
                print("В ячейке по этим координатам уже есть значение, введите его заново")

        while True:
            x1 = int(input("Введите координаты для 0 по горизонтали: "))
            x2 = int(input("Введите координаты для 0 по вертикали: "))
            if field[x1][x2] != "x" and field[x1][x2] != "0":
                field[x1][x2] = "0"
                print_field(field)
                check_condition("000", "Выиграл Нолик")
                if point == "Победа":
                    return "До встречи"
                break
            else:
                print("В ячейке по этим координатам уже есть значение, введите его заново")


print(game_tic_tac())
