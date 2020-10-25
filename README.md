# python3-Samoylenko
Репозиторий домашних работ курса Натальи Самойленко "Python для сетевых инженеров"

---

## Задание 3.1

>Выполните установку IPython в виртуальном окружении или глобально в системе, если виртуальные окружения не используются. После установки, по команде ipython должен открываться интерпретатор IPython (вывод может незначительно отличаться):

**Решение**:
```sh
pip3 install ipython
```

## Задание 4.1

Обработать строку NAT таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
```
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
```

**Решение**: [41-python3-Samoylenko.py](41-python3-Samoylenko.py)

## Задание 4.2

>Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

```
MAC = 'AAAA:BBBB:CCCC'
```

**Решение**: [42-python3-Samoylenko.py](42-python3-Samoylenko.py)

## Задание 4.3

>Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']

```
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
```

**Решение**: [43-python3-Samoylenko.py](43-python3-Samoylenko.py)

## Задание 4.4

>Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2. Для данного примера, результатом должен быть список: [1, 3, 100]. Этот список содержит подсказку по типу итоговых данных.

```
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
```

**Решение**: [44-python3-Samoylenko.py](44-python3-Samoylenko.py)

## Задание 4.5

## Задание 4.6

## Задание 4.7

## Задание 4.8