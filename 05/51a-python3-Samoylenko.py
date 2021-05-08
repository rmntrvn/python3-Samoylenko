#!/usr/bin/env python3

# Задание 5.1a
# Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети, то
# надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в
# задании 5.1.
# 
# Пример адреса сети (все биты хостовой части равны нулю):
# - 10.0.1.0/24
# - 190.1.0.0/16
# Пример адреса хоста:
# - 10.0.1.1/24 - хост из сети 10.0.1.0/24
# - 10.0.5.1/30 - хост из сети 10.0.5.0/30
# 
# Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:
# 
# Network:
# 10       0        1        0
# 00001010 00000000 00000001 00000000
# 
# Mask:
# /24
# 255      255      255      0
# 11111111 11111111 11111111 00000000
#
# Проверить работу скрипта на разных комбинациях сеть/маска.

IP_MASK_INPUT = input('Введите IP адрес сети в формате: 10.1.1.0/24\n')

IP_HOST = IP_MASK_INPUT.split('/')[0].split('.')
MASK = IP_MASK_INPUT.split('/')[1]

BINARY_MASK_LINE = str('1' * int(MASK))
FULL_BINARY_MASK_LINE = "{:<032}".format(BINARY_MASK_LINE)

IP_NETWORK = [ "{:>08}".format(str( int(IP_HOST[0]) & int(FULL_BINARY_MASK_LINE[0:8], 2))),
               "{:>08}".format(str( int(IP_HOST[1]) & int(FULL_BINARY_MASK_LINE[8:16], 2))),
               "{:>08}".format(str( int(IP_HOST[2]) & int(FULL_BINARY_MASK_LINE[16:24], 2))),
               "{:>08}".format(str( int(IP_HOST[3]) & int(FULL_BINARY_MASK_LINE[16:32], 2)))]

TEMPL_TABLE = """{0:<8} {1:<8} {2:<8} {3:<8}
{0:0>8b} {1:0>8b} {2:0>8b} {3:0>8b}"""

print("\nNetwork:")
print(TEMPL_TABLE.format(int(IP_NETWORK[0], 10),
                         int(IP_NETWORK[1], 10),
                         int(IP_NETWORK[2], 10), 
                         int(IP_NETWORK[3], 10)))
print("\nMask:")
print("/" + MASK)

print(TEMPL_TABLE.format(int(FULL_BINARY_MASK_LINE[0:8], 2),
                         int(FULL_BINARY_MASK_LINE[8:16], 2),
                         int(FULL_BINARY_MASK_LINE[16:24], 2), 
                         int(FULL_BINARY_MASK_LINE[24:32], 2)))