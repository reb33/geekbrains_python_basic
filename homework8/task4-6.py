# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


import json
import typing
from abc import ABC
from contextlib import suppress
from copy import deepcopy
from functools import partial
from json import JSONEncoder


class Storage:

    def __init__(self):
        self.__storage = {}

    def take_to_storage(self, equipment: 'OfficeEquipment', count: int):
        if equipment in self.__storage:
            self.__storage[equipment]['count'] += count
            return
        self.__storage[equipment] = dict(
            equipment=equipment,
            count=count,
        )

    def issue(
            self, type_equipment: typing.Type['OfficeEquipment'], count: int, args_of_equipment
    ):
        try:
            position = next(v for k, v in self.__storage.items()
                            if isinstance(v['equipment'], type_equipment)
                            and all(v['equipment'][arg] == arg_val for arg, arg_val in args_of_equipment.items())
                            and v['count'] >= count)
        except StopIteration:
            print('подходящей позиции нет на складе')
            return
        self.__storage[position['equipment']]['count'] = position['count'] - count
        print(f"выдано {count} {str(position['equipment'])}")
        return position['equipment'], count

    def statistics(self):
        return deepcopy(self.__storage)

    def print_statistics(self):
        d = {str(k): v for k, v in self.__storage.items()}
        print(json.dumps(d, cls=OfficeEquipmentEncoder, indent=3))

    @staticmethod
    def _get_equipment_cls():
        equipment_types = {'1': Printer, '2': Scan, '3': Copier}
        equipment_type = ''
        while equipment_type not in equipment_types.keys():
            equipment_type = input('введите тип оборудования.'
                                   '\n1. printer\n2. scan\n3. copier\n')
        cls = equipment_types[equipment_type]
        return cls

    @staticmethod
    def _get_count():
        count = ''
        while not count.isdigit():
            count = input('введите число оборудования\n')
        return int(count)

    @staticmethod
    def input_position():
        cls = Storage._get_equipment_cls()
        equipment = cls(*cls._get_equipment_settings())
        count = Storage._get_count()
        return equipment, count

    @staticmethod
    def issue_position():
        cls = Storage._get_equipment_cls()
        count = Storage._get_count()
        params = {str(num + 1): param for num, param in enumerate(cls.params())}
        params_str = '\n'.join(f'{k} - {params[str(k)]}' for k in range(1, len(params) + 1))
        param_num = ''
        args_of_equipment = {}
        while param_num != 'cancel':
            param_num = input('укажите параметр. Для выхода введите cancel\n' + params_str + '\n')
            if param_num == 'cancel':
                break
            if param_num not in params:
                continue
            param = params[param_num]
            validator = cls.validators()[f'_{param}']
            value = validator()
            args_of_equipment[param] = value
        return cls, count, args_of_equipment


class OfficeEquipmentEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, OfficeEquipment):
            return {o.__class__.__name__: o.as_dict()}
        return super().default(0)


class OfficeEquipment(ABC):
    __slots__ = ['_price', '_is_color']

    @classmethod
    def validators(cls) -> typing.Dict[str, typing.Callable]:
        return {'_price': cls.price_validator, '_is_color': cls.is_color_validator}

    def __init__(self, price, is_color):
        self._price = price
        self._is_color = is_color

    def __getitem__(self, item):
        with suppress(AttributeError):
            return getattr(self, f'_{item}')

    def as_dict(self):
        return {k[1:]: getattr(self, k) for k in self.__slots__}

    def __hash__(self):
        return hash(tuple(self.as_dict().items()))

    def __eq__(self, other):
        return self.__class__ == other.__class__ and hash(self) == hash(other)

    def __str__(self):
        return self.__class__.__name__ + '(' + ','.join([f'{k}={v}' for k, v in self.as_dict().items()]) + ')'

    @staticmethod
    def price_validator():
        price = ''
        while not price.isdigit():
            price = input('введите число в поле price\n')
        return int(price)

    @staticmethod
    def is_color_validator():
        is_color = ''
        while is_color not in ('Y', 'N'):
            is_color = input('введите y/n в поле is_color\n').upper()
        is_color = is_color == 'Y'
        return is_color

    @classmethod
    def _get_equipment_settings(cls):
        args = tuple(cls.validators()[slot]() for slot in cls.__slots__)
        return args

    @classmethod
    def params(cls):
        return [k[1:] for k in cls.__slots__]


class Printer(OfficeEquipment):
    __slots__ = ['_price', '_is_color', '_print_type']

    def __init__(self, price, is_color, print_type):
        super().__init__(price, is_color)
        self._print_type = print_type

    @classmethod
    def validators(cls):
        return dict(super().validators(), _print_type=Printer.print_type_validator)

    @staticmethod
    def print_type_validator():
        print_types = {'1': 'laser', '2': 'matrix', '3': 'jet'}
        print_type = ''
        while print_type not in print_types:
            print_type = input('введите тип принтера 1-laser/ 2-matrix/ 3-jet\n')
        return print_types[print_type]


class Scan(OfficeEquipment):
    __slots__ = ['_price', '_is_color', '_max_quality_scan']

    def __init__(self, price, is_color, max_quality_scan):
        super().__init__(price, is_color)
        self._max_quality_scan = max_quality_scan

    @classmethod
    def validators(cls):
        return dict(super().validators(), _max_quality_scan=Scan.max_quality_scan_validator)

    @staticmethod
    def max_quality_scan_validator():
        max_quality_scan = ''
        while not max_quality_scan.isdigit():
            max_quality_scan = input('введите число в поле max_quality_scan\n')
        return int(max_quality_scan)


class Copier(OfficeEquipment):
    __slots__ = ['_price', '_is_color', '_print_type', '_max_quality_scan']

    def __init__(self, price, is_color, print_type, max_quality_scan):
        super().__init__(price, is_color)
        self._print_type = print_type
        self._max_quality_scan = max_quality_scan

    @classmethod
    def validators(cls):
        return dict(
            super().validators(),
            _print_type=Printer.print_type_validator,
            _max_quality_scan=Scan.max_quality_scan_validator
        )


def main():
    storage = Storage()
    actions = {
        '1': partial(lambda s: s.take_to_storage(*Storage.input_position()), storage),
        '2': partial(lambda s: s.issue(*Storage.issue_position()), storage),
        '3': partial(lambda s: s.print_statistics(), storage)
    }
    while True:
        action_num = ''
        while action_num not in actions:
            action_num = input(
                'введите номер действия. Для выхода введите cancel'
                '\n1 - добавить поизицию'
                '\n2 - выдать позицию'
                '\n3 - напечатать статистику\n'
            )
            if action_num == 'cancel':
                return
        actions[action_num]()


if __name__ == '__main__':
    main()
