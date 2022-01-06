#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import ipaddress

# Задание 12.2
# Функция check_ip_addresses из задания 12.1 принимает только список адресов, но
# было бы удобно иметь возможность указывать адреса с помощью диапазона,
# например, 192.168.100.1-10.
# Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.
# Функция ожидает как аргумент список IP-адресов.
# IP-адреса могут быть в формате:
# - 10.1.1.1
# - 10.1.1.1-10.1.1.10
# - 10.1.1.1-10
# Если адрес указан в виде диапазона, надо проверить доступность всех адресов
# диапазона включая последний.
# Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
# последний октет адреса.
# Функция возвращает два списка:
# - список доступных IP-адресов
# - список недоступных IP-адресов
# Для выполнения задачи можно воспользоваться функцией check_ip_addresses из
# задания 12.1.

def check_ip_addresses(ip_list, count):
    ip_list_raw = ip_list.replace(',', ' ').split()
    ip_list = []
    for ip_address in ip_list_raw:
        if '-' in ip_address:
            start_ip, stop_ip = ip_address.split('-')
            if not '.' in stop_ip:
                stop_ip = '.'.join(start_ip.split('.')[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip  = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip) + 1):
                ip_list.append(str(ipaddress.ip_address(ip)))
        else:
            ip_list.append(str(ip_address))
    ip_list_available   = []
    ip_list_unavailable = []
    for ip in ip_list:
        reply = subprocess.run(f'ping -c {count} {ip}',
                                shell    = True,
                                stdout   = subprocess.PIPE,
                                stderr   = subprocess.PIPE,
                                encoding = 'utf-8')
        is_lossless = True if f"{count} packets transmitted, {count} received," in reply.stdout else False
        if is_lossless:
            ip_list_available.append(ip)
        elif not is_lossless:
            ip_list_unavailable.append(ip)
        else:
            print(reply.stdout + reply.stderr)
    return ip_list_available, ip_list_unavailable

def main():
    parser = argparse.ArgumentParser(description='Check availability IP addresses')
    parser.add_argument('hosts',
                        action='store',
                        help='Hosts to ping')
    parser.add_argument('-c',
                        action="store",
                        dest="count",
                        default=3,
                        type=int,
                        help="Number of packets")
    args = parser.parse_args()
    ip_list_available, ip_list_unavailable = check_ip_addresses(args.hosts, args.count)
    print(f"IP list available: {', '.join(ip_list_available)}")
    print(f"IP list unavailable: {', '.join(ip_list_unavailable)}")


if __name__ == "__main__":
    main()