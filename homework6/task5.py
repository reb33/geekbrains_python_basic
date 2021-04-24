# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title) -> None:
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Чертим карандашом')


class Handle(Stationery):

    def draw(self):
        print('Помечаем маркером')


def main():

    for class_ in (Stationery, Pen, Pencil, Handle):
        class_(class_.__name__).draw()


if __name__ == '__main__':
    main()