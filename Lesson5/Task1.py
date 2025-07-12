# Задание 1
#  Создайте прямоугольник с методами расчета периметра и площади
#  Добавьте сравнение прямоугольников по площади
#  Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def perimeter(self):
        return 2*(self.width + self.height)

    @property
    def area(self):
        return self.height * self.width

    def __eq__(self, other):
        return self.area == other.area 

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area


r1 = Rectangle(5,6)
r2 = Rectangle(5,6)

# print(r1 == r2)
# print(r1 is r2)

a = [1]
b = [1]

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
