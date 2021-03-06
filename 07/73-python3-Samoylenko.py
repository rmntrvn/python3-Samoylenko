#!/usr/bin/env python3

# Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:
# - считывались только строки, в которых указаны MAC-адреса
# - каждая строка, где есть MAC-адрес, должна обрабатываться таким образом,
# чтобы на стандартный поток вывода была выведена таблица вида:
# 100 01bb.c580.7000 Gi0/1
# 200 0a4b.c380.7010 Gi0/2
# 300 a2ab.c5a0.2000 Gi0/3
# 100 0a1b.1c80.7300 Gi0/4
# 500 02b1.3c80.7000 Gi0/5
# 200 1a4b.c580.5000 Gi0/6
# 300 0a1b.5c80.9010 Gi0/7

with open('07/CAM_table.txt', 'r') as file:
    for line in file:
        sline = line.split()
        for string in sline:
            if string.count('.') == 2:
                print(''.join(string + '\t' for string in sline if sline.index(string) != 2))