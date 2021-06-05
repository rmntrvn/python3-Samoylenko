#!/usr/bin/env python3

from sys import argv
configFile  = argv[1]
configFinal = argv[2]

# Переделать скрипт из задания 7.2b:
# передавать как аргументы скрипту:
# имя исходного файла конфигурации
# имя итогового файла конфигурации
# Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации, в
# которых содержатся слова из списка ignore. И затем записать оставшиеся строки в
# итоговый файл.
# Проверить работу скрипта на примере файла config_sw1.txt.
# Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']

with open(configFile, 'r') as file, open(configFinal, 'w') as destFile:
    for line in file:
        for string in ignore:
            if string in line:
                break
        else:
            destFile.writelines(line)
