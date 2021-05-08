#!/usr/bin/env python3

# Задание 4.7
# Преобразовать MAC-адрес в двоичную строку (без двоеточий).

MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.replace(":","")
MAC_DEC = int(MAC, 16)
MAC_BIN = bin(MAC_DEC)[2:]

print(MAC_BIN)