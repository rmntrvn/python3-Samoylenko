#!/usr/bin/env python3

# Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного
# режима, задавались разные вопросы в запросе о номере VLANа или списка VLANов:
# для access: 'Enter VLAN number:'
# для trunk: 'Enter allowed VLANs:'
# Ограничение: Все задания надо выполнять используя только пройденные темы. То
# есть эту задачу можно решить без использования условия if и циклов for/while.

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']

templ = { "access" : access_template, "trunk" : trunk_template }
requests = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}

modeVlanInterface       = input("Enter interface mode (access/trunk): ")
typeAndNumberInterface  = input("Enter interface type and number: ")
numberOfVlan            = input(requests[modeVlanInterface])

print("interface {}".format(typeAndNumberInterface))
print("\n".join(templ[modeVlanInterface]).format(numberOfVlan))