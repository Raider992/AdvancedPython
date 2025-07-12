# Например, возьмём код от задачи с сетками и ячейками из дз по дандерам.

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
                "Unsupported operand for + : "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

        return self.quantity + other.quantity

c1 = Cell(100)
print(c1 + 'hello')

# По моей задумке, конструкция try/except должна считывать строку, которую я передаю
# на оператор суммы, проверять, что она не является экземпляром класса Cell и поднимать
# описанное исключение TypeError. Вместо этого программа спокойно ест строку на сумму и
# выдаёт ошибку только на этапе попытки взять у строки атрибут quantity, и ошибка уже
# естественно не тайп, а: "AttributeError: 'str' object has no attribute 'quantity'"