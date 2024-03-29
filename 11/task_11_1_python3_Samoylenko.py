#!/usr/bin/env python3

# Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show
# cdp neighbors.
# Функция ожидает, как аргумент, вывод команды одной строкой (а не имя файла).
# Функция должна возвращать словарь, который описывает соединения между
# устройствами.
# Например, если как аргумент был передан такой вывод:
# R4>show cdp neighbors
# Device ID   Local Intrfce   Holdtme   Capability   Platform   Port ID
# R5          Fa 0/1          122       R S I        2811       Fa 0/1
# R6          Fa 0/2          143       R S I        2811       Fa 0/0
# Функция должна вернуть такой словарь:
# {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
# ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
# Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
# Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt
# Ограничение: Все задания надо выполнять используя только пройденные темы.

def parse_cdp_neighbors(output_command):
    """
    Функции передаётся имя команды одной строкой
    """
    result = {}
    for line in output_command.split("\n"):
        line    = line.strip()
        columns = line.split()
        if ">" in line:
            hostname = line.split(">")[0]
        elif len(columns) >=5 and columns[3].isdigit():
            r_host, l_int, l_int_num, *other, r_int, r_int_num = columns
            result[(hostname, l_int + l_int_num)] = (r_host, r_int + r_int_num)
    return result

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))