# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной.

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


def menu():
    print("Меню телефонного справочника:\n"
          "Посмотреть все данные в файле, нажмите: 1\n"
          "Добавить данные в файл, нажмите: 2\n"
          "Найти запись по фамилии, нажмите: 3\n"
          "Удалить данные, нажмите: 4\n"
          "Изменить данные, нажмите: 5")
    number_choice = int(input("Введите номер: "))
    return number_choice


def find_data():
    data_find = input("Введите данные которые нужно найти: ")
    return data_find


def add_data():
    print("Впишите данные в формате как в этом примере:\n"
          "Пример ввода: Петров;Иван;Иванович;89342342")
    new_data = input("Введите новые данные: ")
    with open('fio.txt', 'a', encoding='utf-8') as file:
        file.write(f"{new_data}")


def read_data():
    with open('fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def screen_all(data):
    print("\nДанные в таблице:\n")
    count = 0
    for elem in data:
        new_elem = elem.replace(";", " ")
        print(f"{count}: {new_elem}"
              f"-----------------------------------")
        count += 1


def change_data():
    number_change = int(input("Напишите номер строки, которую хотите изменить:"))
    return number_change


def delete_data():
    number_delete = int(input("Введите номер строки которую хотите удалить: "))
    return number_delete


def main():
    number = menu()
    if number == 1:
        data_1 = read_data()
        screen_all(data_1)
    elif number == 2:
        add_data()
    elif number == 3:
        data_find = find_data()
        data_3 = read_data()
        sum = 0
        print("Результаты запроса:\n----------------------- ")
        for i in data_3:
            my_list = i.split(";")
            for j in my_list:
                if data_find in j:
                    print(i.replace(";", " "))
                    sum += 1
        if sum == 0:
            print("Таких данных нет")
        else:
            print(f"Найдено {sum} записи в файле")

    elif number == 4:
        data_4 = read_data()
        screen_all(data_4)
        number_delete = delete_data()
        data_4.pop(number_delete)
        with open('fio.txt', 'w', encoding='utf-8') as file:
            file.write("")
        for i in data_4:
            with open('fio.txt', 'a', encoding='utf-8') as file:
                file.write(i)
    elif number == 5:
        data_5 = read_data()
        screen_all(data_5)
        number_change = change_data()
        print("Впишите новые данные вместо выбранной вами строки в формате как в этом примере:\n"
              "Пример ввода: Петров;Иван;Иванович;89342342")
        new_data = input("Введите нувую строку сюда:")
        data_5[number_change] = new_data
        with open('fio.txt', 'w', encoding='utf-8') as file:
            file.write("")
        for i in data_5:
            with open('fio.txt', 'a', encoding='utf-8') as file:
                file.write(i)


    else:
        print("Вы ввели неверную команду")


if __name__ == '__main__':
    main()