#!/usr/bin/env python3

from sys import argv
tableMac = argv[1]

# Сделать копию скрипта задания 7.3
# Дополнить скрипт:
# Отсортировать вывод по номеру VLAN
# Ограничение: Все задания надо выполнять используя только пройденные темы.

with open('07/CAM_table.txt', 'r') as file:
    output = []
    for line in file:
        sline = line.split()
        for string in sline:
            if string.count('.') == 2:
                vlan, mac, _, interface = sline
                output.append([int(vlan), mac, interface])
    for vlan, mac, interface in sorted(output):
        print(vlan, "\t", mac, "\t", interface)