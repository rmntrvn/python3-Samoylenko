
# Задание 5.1
# Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
# Затем вывести информацию о сети и маске в таком формате:
# Network:
# 10       1        1        0
# 00001010 00000001 00000001 00000000
#
# Mask:
# /24
# 255      255      255      0
# 11111111 11111111 11111111 00000000
# Проверить работу скрипта на разных комбинациях сеть/маска.

IP_MASK_INPUT = input('Введите IP адрес сети в формате: 10.1.1.0/24\n')

IP = IP_MASK_INPUT.split('/')[0].split('.')
MASK = IP_MASK_INPUT.split('/')[1]

BINARY_MASK_LINE = str('1' * int(MASK))
FULL_BINARY_MASK_LINE = "{:<032}".format(BINARY_MASK_LINE)

TEMPL_TABLE = """{0:<10} {1:<10} {2:<10} {3:<10}
{0:0>8b} {1:0>8b} {2:0>8b} {3:0>8b}"""

print("\nNetwork:")
print(TEMPL_TABLE.format(int(IP[0]),
                         int(IP[1]),
                         int(IP[2]), 
                         int(IP[3])))
print("\nMask:")
print("/" + MASK)

print(TEMPL_TABLE.format(int(FULL_BINARY_MASK_LINE[0:8], 2),
                         int(FULL_BINARY_MASK_LINE[8:16], 2),
                         int(FULL_BINARY_MASK_LINE[16:24], 2), 
                         int(FULL_BINARY_MASK_LINE[24:32], 2)))