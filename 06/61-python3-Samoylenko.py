#!/usr/bin/env python3

# 1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1.
# 2. Определить какому классу принадлежит IP-адрес.
# 3. В зависимости от класса адреса, вывести на стандартный поток вывода:
# 'unicast' - если IP-адрес принадлежит классу A, B или C
# 'multicast' - если IP-адрес принадлежит классу D
# 'local broadcast' - если IP-адрес равен 255.255.255.255
# 'unassigned' - если IP-адрес равен 0.0.0.0
# 'unused' - во всех остальных случаях
# Подсказка по классам (диапазон значений первого байта в десятичном формате):
# A: 1-127
# B: 128-191
# C: 192-223
# D: 224-239
# Ограничение: Все задания надо выполнять используя только пройденные темы.

ipAddressLs = input("Введите IP адрес в формате XXX.YYY.ZZZ.WWW: ").split('.')

ipAddressInt = [ int(ip) for ip in ipAddressLs ]

if ipAddressInt[0] >= 1 and ipAddressInt[0] <= 223:
    print("It's unicast")
elif ipAddressInt[0] >= 224 and ipAddressInt[0] <= 240:
    print("It's multicast")
elif ipAddressInt == [ 255, 255, 255, 255 ]:
    print("It's local broadcast")
elif ipAddressInt == [ 0, 0, 0, 0 ]:
    print("It's unassigned")
else:
    print("Unused")
