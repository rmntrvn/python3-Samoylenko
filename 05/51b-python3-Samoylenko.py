#!/usr/bin/env python3

# Преобразовать скрипт из задания 5.1a таким образом, чтобы сеть/маска не
# запрашивались у пользователя, а передавались как аргумент скрипту.

from sys import argv

IP_MASK_INPUT = ''.join(argv[1:])

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