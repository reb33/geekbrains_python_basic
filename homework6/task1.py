# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import itertools
from datetime import datetime, timedelta
from time import sleep


class TrafficLight:
    __color = ''

    def __color_iterator(self):
        colors = {'red': 7, 'yellow': 2, 'green': 10}
        yield from itertools.cycle(colors.items())

    def running(self):
        color = self.__color_iterator()
        stop = datetime.now()+timedelta(seconds=30)
        while datetime.now() < stop:
            self.__color, wait_time = next(color)
            print(datetime.now(), self.__color)
            sleep(wait_time)


def main():
    TrafficLight().running()


if __name__ == '__main__':
    main()
