#!/usr/bin/env python3

# Задание 4.3
# Получить из строки CONFIG список VLANов вида:
# ['1', '3', '10', '20', '30', '100']

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

VLANS = CONFIG.split()
VLANS = VLANS[-1].split(',')

print(VLANS)
