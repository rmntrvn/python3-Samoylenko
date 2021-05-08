#!/usr/bin/env python3

# Переделать скрипт из задания 5.2a таким образом, чтобы, при запросе параметра,
# отображался список возможных параметров.
# Вывести информацию о соответствующем параметре, указанного устройства.
# Ограничение: нельзя изменять словарь london_co.
# Все задания надо выполнять используя только пройденные темы. То есть эту задачу
# можно решить без использования условия if.

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

deviceName      = input("Enter device name: ")
showParameters  = list(london_co[deviceName].keys())
showMessageForGetInput = "Enter parameter name (" + ', '.join(showParameters) + "): "
paramName       = input(showMessageForGetInput) 
print(london_co[deviceName][paramName])