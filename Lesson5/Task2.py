# Задание 1.
#
# Реализовать программу работы с органическими клетками, состоящими из ячеек.
#
# Необходимо создать класс Клетка (Cell).
#
# В его конструкторе инициализировать параметр (quantity),
# соответствующий количеству ячеек клетки (целое число).
#
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()),
# вычитание (sub()),
# умножение (mul()),
# деление (truediv()).
#
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
#
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
from linecache import cache


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Объект класса Cell с числом ячеек {self.quantity}'

    def __add__(self, other):
        try:
            isinstance(other, type(self))
        except:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

        return self.quantity + other.quantity

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for -: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        if other.quantity > self.quantity:
            raise ValueError('Вычитаемое больше уменьшаемого')

        self.quantity -= other.quantity

        return print(self)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for *: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for /: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        return Cell(self.quantity // other.quantity)

    def __floordiv__(self, other):
        self.__floordiv__ = self.__truediv__


print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
# print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print(cell1 + 'hello')

# Код на try/except в методе add не работает. Вместо того чтобы проверять, является ли строка, которую я