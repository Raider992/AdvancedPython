# Задание 1.
#
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    a = int(input('a: '))
    b = int(input('b: '))

    try:
        if b == 0:
            raise DivZero('Деление на ноль')
        print(a/b)
    except DivZero as err:
        print(err)

    except ZeroDivisionError:
        print('на ноль делить нельзя')

    else:
        print(a/b)


division()
ArithmeticError