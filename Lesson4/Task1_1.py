# Задание 1
#
# Напишите декоратор для замеров времени выполнения любой функции
# Для реализации замеров воспользуйтесь модулем timeit
#
# Реализуйте декоратор в виде функции

import timeit
from functools import wraps

def ext_decor(number):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res_time = timeit.timeit(lambda: func(*args), number=number)
            res = func(*args)

            return res, res_time

        return wrapper
    return decor

@ext_decor(1000000)
def func1(a,b):
    return a+b

print(func1(5,7))
print(func1.__name__)
