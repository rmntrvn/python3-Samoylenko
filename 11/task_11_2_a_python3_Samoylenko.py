#!/usr/bin/env python3

# С помощью функции parse_cdp_neighbors из задания 11.1 и функции draw_topology из
# файла draw_network_graph.py, сгенерировать топологию, которая соответствует
# выводу команды sh cdp neighbor из файлов:
# sh_cdp_n_sw1.txt
# sh_cdp_n_r1.txt
# sh_cdp_n_r2.txt
# sh_cdp_n_r3.txt
# Не копировать код функций parse_cdp_neighbors и draw_topology.
# В итоге, должен быть сгенерировано изображение топологии.

# При этом:
# Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
# Расположение устройств на схеме может быть другим
# Соединения должны соответствовать схеме
# Ограничение: Все задания надо выполнять используя только пройденные темы.

from task_11_1_python3_Samoylenko import parse_cdp_neighbors
from pprint import pprint

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    network_map = {}

    for filename in filenames:
        with open(filename) as show_command:
            parsed = parse_cdp_neighbors(show_command.read())
            network_map.update(parsed)
    return network_map


if __name__ == "__main__":
    topology = create_network_map(infiles)
    pprint(topology)