# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('To Infinity, And Beyond!')

    def stop(self):
        print('All Back')

    def turn(self):
        print('left')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('вы превысили скорость')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('вы превысили скорость')


class PoliceCar(Car):
    pass


def main():
    town_car = TownCar(80, 'grey', 'Creta', False)
    sport_car = SportCar(60, 'red', 'Vanquish', False)
    work_car = WorkCar(60, 'yellow', 'tractor', False)
    police_car = PoliceCar(60, 'white-blue', 'priora', True)

    for car in (town_car, sport_car, work_car, police_car):
        print()
        for attr in ('speed', 'color', 'name', 'is_police'):
            print(getattr(car, attr))

    for car in (town_car, sport_car, work_car, police_car):
        print()
        for attr in ('go', 'stop', 'turn', 'show_speed'):
            getattr(car, attr)()


if __name__ == '__main__':
    main()
