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
    _COLOR_OPTIONS = ('Красный', 'Жёлтый', 'Зелёный')

    __color = ''

    def _set_color(self, color):

        try:
            index = self._COLOR_OPTIONS.index(color)
            self.__color = color
            print(f'Цвет светофора сейчас {self.__color}')

        except ValueError:
            print('Wrong color of the traffic light')

    def running(self):
        for cnt in range(3):
            self._set_color('Красный')
            time.sleep(7)
            self._set_color('Жёлтый')
            time.sleep(2)
            self._set_color('Зелёный')
            time.sleep(10)
            self._set_color('Жёлтый')
            time.sleep(2)



tl = TrafficLight()

tl.running()