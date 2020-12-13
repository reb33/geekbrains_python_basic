# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def div(*args):
    if args[1] == 0:
        print('делить на 0 нельзя')
        return
    return args[0]/args[1]


def input_int():
    while True:
        try:
            return int(input('введите число '))
        except ValueError:
            print('вы ввели не число')


def main():
    number_1 = input_int()
    number_2 = input_int()
    result = div(number_1, number_2)
    if result is not None:
        print(result)


if __name__ == '__main__':
    main()