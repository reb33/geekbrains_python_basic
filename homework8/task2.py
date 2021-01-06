# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.
from contextlib import suppress


class MyOwnGreatDivisionByZeroException(Exception):

    @classmethod
    def check_args(cls, dividend, divider):
        if divider == 0:
            raise cls


def div(dividend, divider):
    with suppress(MyOwnGreatDivisionByZeroException):
        MyOwnGreatDivisionByZeroException.check_args(dividend, divider)
        return dividend / divider
    print(f'{dividend}/{divider} деление на ноль')


def main():
    while True:
        args = input('введите 2 int аргумента через пробел. Для выхода введите str\n')
        nums = args.split(maxsplit=2)
        try:
            nums = tuple(map(int, nums[:2]))
        except ValueError:
            return
        print(div(*nums))


if __name__ == '__main__':
    main()
