# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'


import os


def creates_path():
    """ Создает путь до папки где лежат нужные файлы """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Migrations')
    return path


def forming_list_files_sql(path):
    """ Формирует список файлов с расширением .sql, на ввод приниает путь к папке где эти файлы лежат """
    # path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Migrations')
    list_files_sql = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if '.sql' in file:
                list_files_sql.append(file)
    return list_files_sql


def search_file(list_files, path):
    """ Ищет нужные файлы в списке отобранных, по содержащимуся в нем слову, слово вводится пользователем.
    На ввод принимается исходный список с которого начитнать поиск, и ссылка на папку где лежат файлы """
    word = None
    while word != 'q':
        list_required_files = []
        word = input('ВВедите слово которое должно быть в файле, или введите q, для выхода из программы ')
        if word == 'q':
            print('Программа завершена')
            break
        else:
            for file in list_files:
                with open(os.path.join(path, file), encoding='utf-8') as f:
                    if word in f.read():
                        list_required_files.append(file)
            print("Найдено файлов {}: {}".format(len(list_required_files), list_required_files))
            list_files = list_required_files


path = creates_path()
list_files = forming_list_files_sql(path)
search_file(list_files, path)
