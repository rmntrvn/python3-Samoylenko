
# Задание 4.4
# Из строк command1 и command2 получить список VLANов, 
# которые есть и в команде command1 и в команде command2. 
# Для данного примера, результатом должен быть список: [1, 3, 100]. 
# Этот список содержит подсказку по типу итоговых данных.

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

VLANS1 = set([ int(vlan) for vlan in command1.split()[-1].split(',') ])
VLANS2 = set([ int(vlan) for vlan in command2.split()[-1].split(',') ])

VLANS = list(VLANS1 & VLANS2)

print(VLANS)