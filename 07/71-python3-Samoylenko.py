
# Аналогично заданию 4.6 обработать строки из файла ospf.txt и вывести информацию
# по каждой в таком виде:
# Protocol: OSPF
# Prefix: 10.0.24.0/24
# AD/Metric: 110/41
# Next-Hop: 10.0.13.3
# Last update: 3d18h
# Outbound Interface: FastEthernet0/0

templ_format = """
Protocol:           {0:20}
Prefix:             {1:20}
AD/Metric:          {2:20}
Next-Hop:           {3:20}
Last update:        {4:20}
Outbound Interface: {5:20}
"""

with open('07/ospf.txt', 'r') as file:
    for line in file:
        cleanRoute = line.replace("[","").replace("]","").replace(","," ").split()
        cleanRoute[0] = 'OSPF'
        print(templ_format.format(
                cleanRoute[0],
                cleanRoute[1],
                cleanRoute[2],
                cleanRoute[4],
                cleanRoute[5],
                cleanRoute[6]
                ).rstrip())