import time


# Задание 2.
#
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет)
# и публичный метод running (запуск).
#
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
#
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
#
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
    __color = 'off'
    __time = 0

    def __init__(self):
        self._COLOR_TIME_OPTIONS = {'Красный': 7, 'Жёлтый': 2, 'Зелёный': 10}

    def _set_color(self, color):
        colors = self._COLOR_TIME_OPTIONS.keys()
        try:
            color in colors
            self.__color = color

        except ValueError:
            print('Wrong color of the traffic light')

    def _set_time(self, time):
        times = self._COLOR_TIME_OPTIONS.values()
        try:
            time in times
            self.__time = time

        except ValueError:
            print('Wrong color of the traffic light')

    @property
    def get_color(self):
        return print(self.__color)

    def running(self):

        for cnt in self._COLOR_TIME_OPTIONS:
            (self.__color, self.__time) = (cnt, self._COLOR_TIME_OPTIONS[cnt])
            self.get_color
            time.sleep(self.__time)


tl = TrafficLight()

tl.running()
