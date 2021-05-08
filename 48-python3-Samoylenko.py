#!/usr/bin/env python3

# Задание 4.8
# Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод
# столбцами на стандартный поток вывода, таким образом:
# - первой строкой должны идти десятичные значения байтов
# - второй строкой двоичные значения
# Вывод должен быть упорядочен также, как в примере:
# - столбцами
# - ширина столбца 10 символов
# Пример вывода:
# 10       1        1        1
# 00001010 00000001 00000001 00000001

IP = '192.168.3.1'
SPLITTED_IP_DEC = IP.split('.')

TEMPL_TABLE = """
{0:<10} {1:<10} {2:<10} {3:<10}
{0:0<10b} {1:0<10b} {2:0<10b} {3:0<10b}
"""

print(TEMPL_TABLE.format(int(SPLITTED_IP_DEC[0]), int(SPLITTED_IP_DEC[1]), int(SPLITTED_IP_DEC[2]), int(SPLITTED_IP_DEC[3])))
