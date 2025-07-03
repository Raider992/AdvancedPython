# Задание 1
#
# Напишите декоратор для замеров времени выполнения любой функции
# Для реализации замеров воспользуйтесь модулем timeit
#
# Реализуйте декоратор в виде класса
import timeit


class Decor:
    def __init__(self, number):
        self.number = number

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            res_time = timeit.timeit(lambda: func(*args), number=self.number)
            res = func(*args)

            return res, res_time

        return wrapper


# @Decor(1000000)
def func1(a,b):
    return a+b

# print(func1(5,7))

print(Decor(1000000)(func1)(5,7))
