#!/usr/bin/env python3

# Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл
# коммутатора и возвращает два объекта:
# - словарь портов в режиме access, где ключи номера портов, а значения access
# VLAN:
# {'FastEthernet0/12':10,
# 'FastEthernet0/14':11,
# 'FastEthernet0/16':17}

# - словарь портов в режиме trunk, где ключи номера портов, а значения список
# разрешенных VLAN:
# {'FastEthernet0/1':[10,20],
# 'FastEthernet0/2':[11,30],
# 'FastEthernet0/4':[17]}

# Функция ожидает в качестве аргумента имя конфигурационного файла.
# Проверить работу функции на примере файла config_sw1.txt
# Ограничение: Все задания надо выполнять используя только пройденные темы.

def get_int_vlan_map(configFile):
    accessDict = {}
    trunkDict  = {}
    with open(configFile, 'r') as file:
        for line in file:
            if line.startswith('interface'):
                interface = line.rstrip().split()[1]
            elif 'access vlan' in line:
                vlan = int(line.rstrip().split()[-1])
                accessDict.update({interface: vlan})
            elif 'trunk allowed vlan' in line:
                vlans = [int(vlan) for vlan in line.rstrip().split()[-1].split(',')]
                trunkDict.update({interface: vlans})
    return accessDict, trunkDict

print(get_int_vlan_map('09/config_sw1.txt'))