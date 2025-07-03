# Задание 1.
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from random import randint

class ReRunner:
    def __init__(self, number):
        self.number = number

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            res = []
            if self.number == 1:
                return func(*args)
            for i in range(self.number):
                res.append(func(*args))
            return res

        return wrapper

@ReRunner(10)
def grn():
    return randint(1,10)

print(grn())