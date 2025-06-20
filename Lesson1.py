# Итераторы и генераторы



# Задание 1.
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

import re


def gen1():
    for el in range(0,101,2):
        if sum([int(x) for x in re.findall(r'\d',str(el))]) == 8:
            continue
        yield el


for elem in gen1():
    print(elem)

# # Второе решение:

one_str_gen = (x for x in range(0,101,2) if sum([int(el) for el in str(x)]) != 8)

for i in one_str_gen: print(i)


# Задание 2.
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


def gen2():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            yield 'FizzBuzz'
            continue
        if i % 3 == 0:
            yield 'Fizz'
            continue
        if i % 5 == 0:
            yield 'Buzz'
            continue
        if not (i % 3 == 0) or (i % 5 == 0):
            yield i
            continue

for i in gen2():
    print(i)

# Второе решение:

gen2 = ('FizzBuzz' if (el % 3 == 0) & (el % 5 == 0) else
        'Fizz' if (el % 3 == 0) else
        'Buzz' if (el % 5 == 0) else
        el
        for el in range(1,101))

print(*gen2)

# Домашнее задание:
# Задание 1
# ✔ Создайте функцию генератор четных чисел от 0 до n.
# """

def gen_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
        else:
            continue

for j in gen_even(10):
    print(j)

# # Задание 2
# # ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
# # """


def gen_fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a + b

for el in gen_fib(10):
    print(el)
