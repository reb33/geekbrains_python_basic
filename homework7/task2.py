# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


class Clothes:

    def __init__(self, title):
        self.title = title

    def calc_amount_fabric(self):
        raise NotImplementedError


class Coat(Clothes):

    def __init__(self, size):
        super().__init__('Coat')
        self.size = size

    def calc_amount_fabric(self):
        return self.size/6.5 + 0.5


class Costume(Clothes):

    def __init__(self, height):
        super().__init__('Costume')
        self.height = height

    def calc_amount_fabric(self):
        return 2 * self.height + 0.3


def main():
    print('{:.2f}'.format(Coat(20).calc_amount_fabric()))
    print(Costume(1.8).calc_amount_fabric())


if __name__ == '__main__':
    main()