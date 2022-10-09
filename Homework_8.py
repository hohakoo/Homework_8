# Функция generate_txt_data. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.
import random
from string import ascii_lowercase, ascii_uppercase, digits
import os
import json

def generate_txt_data() -> str:
    symbols_i_need = ascii_lowercase + ascii_uppercase + digits + " "
    random_len = random.randint(100,1000)
    my_string = ""
    while len(my_string) != random_len:
        my_string += random.choice(symbols_i_need)
    return my_string

# Функция generate_json_data. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
def generate_json_data():
    num_of_keys = random.randint(5,20)

    def create_key():
        key = "".join([random.choice(ascii_lowercase) for _ in range(5)])
        return key

    def create_value():
        value = random.choice([random.randint(-100, 100), random.random(), random.choice([True,False])])
        return value

    my_dict = {create_key():create_value() for _ in range(num_of_keys)}

    return my_dict

# Функция generate_and_write_file. Написать функцию которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

def generate_and_write_file(path):
    if os.path.splitext(path)[-1] == ".txt":
        with open(path, "w") as file:
            file.write(generate_txt_data())

    elif os.path.splitext(path)[-1] == ".json":
        with open(path, "w") as file:
            file.write(json.dumps(generate_json_data()))

    else:
        print("Unsupported file format")
# Разрешается создавать дополнительные (вспомогательные) функции.