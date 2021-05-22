#!/usr/bin/env python3

# Сделать копию скрипта задания 6.1a.
# Дополнить скрипт:
# Если адрес был введен неправильно, запросить адрес снова.


validIpAddress = False
while validIpAddress == False:
    ipAddressLs = input("Введите IP адрес в формате XXX.YYY.ZZZ.WWW: ").split('.')
    for octet in ipAddressLs:
        if octet.isdigit() and len(ipAddressLs) == 4 and 0 <= int(octet) <= 255:
            ipAddressInt = [ int(ip) for ip in ipAddressLs ]
            if ipAddressInt[0] >= 1 and ipAddressInt[0] <= 223:
                print("It's unicast")
                break
            elif ipAddressInt[0] >= 224 and ipAddressInt[0] <= 240:
                print("It's multicast")
                break
            elif ipAddressInt == [ 255, 255, 255, 255 ]:
                print("It's local broadcast")
                break
            elif ipAddressInt == [ 0, 0, 0, 0 ]:
                print("It's unassigned")
                break
            else:
                print("Unused")
                break
        else:
            print("IP адрес введен неверно. Введите IP адрес еще раз.")
            break
    validIpAddress == False
