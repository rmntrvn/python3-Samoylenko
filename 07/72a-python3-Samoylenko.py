#!/usr/bin/env python3

from sys import argv
configFile = argv[1]

# Сделать копию скрипта задания 7.2.
# Дополнить скрипт:
# Скрипт не должен выводить команды, в которых содержатся слова, которые
# указаны в списке ignore.

ignore = ['duplex', 'alias', 'Current configuration']

with open(configFile, 'r') as file:
    for line in file:
        words = line.split()
        intersectionWords = set(words) & set(ignore)
        if not line.startswith("!") and not intersectionWords:
            print(line.rstrip())