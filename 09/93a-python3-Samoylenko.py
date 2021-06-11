#!/usr/bin/env python3

# Сделать копию скрипта задания 9.3.
# Дополнить скрипт:
# - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
#   interface FastEthernet0/20
#   switchport mode access
#   duplex auto
# То есть, порт находится в VLAN 1
# В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
# Пример словаря:
#   {'FastEthernet0/12':10,
#   'FastEthernet0/14':11,
#   'FastEthernet0/20':1 }
# Функция ожидает в качестве аргумента имя конфигурационного файла.
# Проверить работу функции на примере файла config_sw2.txt
# Ограничение: Все задания надо выполнять используя только пройденные темы.

def get_int_vlan_map(configFile):
    accessDict = {}
    trunkDict  = {}
    with open(configFile, 'r') as file:
        for line in file:
            if 'interface FastEthernet' in line:
                interface = line.rstrip().split()[-1]
                accessDict.update({interface: 1})
            elif 'access vlan' in line:
                vlan = int(line.rstrip().split()[-1])
                accessDict.update({interface: vlan})
            elif 'trunk allowed vlan' in line:
                vlans = [int(vlan) for vlan in line.rstrip().split()[-1].split(',')]
                trunkDict.update({interface: vlans})
                del accessDict[interface]
    return accessDict, trunkDict

print(get_int_vlan_map('09/config_sw2.txt'))