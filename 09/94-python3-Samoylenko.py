#!/usr/bin/env python3

# Создать функцию, которая обрабатывает конфигурационный файл коммутатора и
# возвращает словарь:
# - Все команды верхнего уровня (глобального режима конфигурации), будут
# ключами.
# - Если у команды верхнего уровня есть подкоманды, они должны быть в значении у
# соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
# - Если у команды верхнего уровня нет подкоманд, то значение будет пустым
# списком
# Функция ожидает в качестве аргумента имя конфигурационного файла.
# Проверить работу функции на примере файла config_sw1.txt
# При обработке конфигурационного файла, надо игнорировать строки, которые
# начинаются с '!', а также строки в которых содержатся слова из списка ignore.
# 
# Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
# Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если не
    т
    '''
    return any(word in command for word in ignore)

def check_config_file(config_filename):
    config_dict = {}
    with open(config_filename, 'r') as file:
        for line in file:
            line = line.rstrip()
            if line and not (line.startswith('!') or ignore_command(line, ignore)):
                if line[0].isalnum():
                    section = line
                    config_dict[section] = []
                else:
                    config_dict[section].append(line.strip())
    return config_dict

print(check_config_file('09/config_sw1.txt'))