# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(*args):
    if len(args) < 3:
        print('нужно передат 3 параметра')
        return
    args = sorted(args)
    return args[-1] + args[-2]


def main():
    res = my_func(6, 9, 10)
    if res is not None:
        print(res)


if __name__ == '__main__':
    main()
