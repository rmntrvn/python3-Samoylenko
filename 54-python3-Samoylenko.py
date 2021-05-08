#!/usr/bin/env python3

# 5.4
# Найти индекс последнего вхождения элемента.
# Например, для списка num_list, число 10 последний раз встречается с индексом 4; в
# списке word_list, слово 'ruby' последний раз встречается с индексом 6.
# Сделать решение общим (то есть, не привязываться к конкретному элементу в
# конкретном списке) и проверить на двух списках, которые указаны и на разных
# элементах.
# Для этого надо запросить у пользователя сначала ввод числа из списка num_list и
# затем вывести индекс его последнего появления в списке. А затем аналогично для
# списка word_list.
# Ограничение: Все задания надо выполнять используя только пройденные темы.

num_list    = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list   = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

searchDigit     = int(input("Введите число, чтобы узнать индекс последнего вхождения элемента: "))
searchWord      = str(input("Введите слово, чтобы узнать индекс последнего вхождения элемента: "))

indxDigit       = len(num_list) - 1 - num_list[::-1].index(searchDigit)
indxWord        = len(word_list) - 1 - word_list[::-1].index(searchWord)

print("Индекс последнего вхождения числа ", searchDigit, ":", indxDigit)
print("Индекс последнего вхождения слова: ", searchWord, ":", indxWord)