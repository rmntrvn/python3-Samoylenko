#!/usr/bin/env python3

# Задание 4.1
# Обработать строку NAT таким образом, чтобы в имени интерфейса 
# вместо FastEthernet было GigabitEthernet.

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

print(NAT.replace('FastEthernet', 'GigabitEthernet'))