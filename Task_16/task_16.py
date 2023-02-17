# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import re

my_text = "Привет, у тебя бывает такое что?"
my_list = (re.split(" |, |\?", my_text))


def delete_words(any_text):
    for i in my_list:
        for j in i:
            if j == "а" or j == "б" or j == "в":
                any_text = any_text.replace(i, "")
                break
    return any_text


print(delete_words(my_text))
