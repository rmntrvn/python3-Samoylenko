#!/usr/bin/env python3

# Сделать копию скрипта задания 7.3a
# Дополнить скрипт:
# Запросить у пользователя ввод номера VLAN.
# Выводить информацию только по указанному VLAN.
# Ограничение: Все задания надо выполнять используя только пройденные темы.

vlanNumber = input("Введите номер VLAN: ")

with open('07/CAM_table.txt', 'r') as file:
    output = []
    for line in file:
        sline = line.split()
        for string in sline:
            if string.count('.') == 2 and sline[0] == vlanNumber:
                vlan, mac, _, interface = sline
                output.append([int(vlan), mac, interface])
    for vlan, mac, interface in sorted(output):
        print(vlan, "\t", mac, "\t", interface)