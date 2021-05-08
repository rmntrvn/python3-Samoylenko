#!/usr/bin/env python3

# Задание 4.6
# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в
# виде:
# Protocol:             OSPF
# Prefix:               10.0.24.0/24
# AD/Metric:            110/41
# Next-Hop:             10.0.13.3
# Last update:          3d18h
# Outbound Interface:   FastEthernet0/0

ospf_route = 'O     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

clear_route = ospf_route.replace("[","").replace("]","").replace(","," ").split()

clear_route[0] = "OSPF"

templ_format = """
Protocol:           {0:20}
Prefix:             {1:20}
AD/Metric:          {2:20}
Next-Hop:           {3:20}
Last update:        {4:20}
Outbound Interface: {5:20}
"""

print(templ_format.format(
    clear_route[0],
    clear_route[1],
    clear_route[2],
    clear_route[4],
    clear_route[5],
    clear_route[6]
    ))