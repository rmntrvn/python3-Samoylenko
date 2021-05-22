
# Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в
# оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
# Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в
# новый список mac_cisco

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for macAddress in mac:
    mac_cisco.append(macAddress.replace(':', '.'))

print(mac_cisco)