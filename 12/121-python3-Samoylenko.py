#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess

# Задание 12.1
# Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.
# Функция ожидает как аргумент список IP-адресов. И возвращает два списка:
# - список доступных IP-адресов
# - список недоступных IP-адресов
# Для проверки доступности IP-адреса, используйте ping. Адрес считается доступным,
# если на три ICMP-запроса пришли три ответа.

def check_ip_addresses(ip_list, count):
    ip_list = ip_list.replace(',', ' ').split()
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