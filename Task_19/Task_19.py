# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


data_input = "aaabbbbaaccc"


def compression_data(data):
    value = data[0]
    my_sum = 0
    result = ""
    for i in data:
        if i == value:
            my_sum += 1
        else:
            result += (str(my_sum) + value)
            value = i
            my_sum = 1
    return result + str(my_sum) +i







print(compression_data(data_input))

