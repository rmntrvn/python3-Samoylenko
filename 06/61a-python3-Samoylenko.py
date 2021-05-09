#!/usr/bin/env python3

# Сделать копию скрипта задания 6.1.
# Дополнить скрипт:
# Добавить проверку введенного IP-адреса.
# Адрес считается корректно заданным, если он:
# - состоит из 4 чисел разделенных точкой,
# - каждое число в диапазоне от 0 до 255.
# Если адрес задан неправильно, выводить сообщение:
# - 'Incorrect IPv4 address'
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
