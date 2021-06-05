#!/usr/bin/env python3

# Запускать python3 07/72b-python3-Samoylenko.py 07/config_sw1.txt

from sys import argv
configFile = argv[1]

print(configFile)

# Дополнить скрипт из задания 7.2a:
# вместо вывода на стандартный поток вывода, скрипт должен записать полученные
# строки в файл config_sw1_cleared.txt
# При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
# Строки, которые начинаются на '!' отфильтровывать не нужно.
# Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']

with open(configFile, 'r') as file, open('07/config_sw1_cleared.txt', 'w') as destFile:
    for line in file:
        for string in ignore:
            if string in line:
                break
        else:
            destFile.writelines(line)
