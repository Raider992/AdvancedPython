class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Объект класса Cell с числом ячеек {self.quantity}'

    def __add__(self, other):
        try:
            if not isinstance(other, type(self)):
                raise TypeError
        except TypeError:
            print('\033[31m' +
                "Unsupported operand for: " +
                f"'{type(self).__name__}' and '{type(other).__name__}'"
                  + '\033[0m'
            )
        else:
            return self.quantity + other.quantity


c1 = Cell(100)
c2 = Cell(50)

c1 + 'hello'
print(c1 + c2)


