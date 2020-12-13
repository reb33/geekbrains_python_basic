# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_pwr_without_operator(x, y):
    pwr = x
    for i in range(abs(y) - 1):
        pwr *= x
    return 1 / pwr


def my_pwr_with_operator(x, y):
    return x ** y


def input_int():
    while True:
        try:
            return int(input('введите число '))
        except ValueError:
            print('вы ввели не число')


def input_negative_int():
    while True:
        try:
            number = int(input('введите отрицательное число '))
            if number < 0:
                return number
            else:
                print('вы ввели не отрицательное число')
        except ValueError:
            print('вы ввели не число')


def main():
    x = input_int()
    y = input_negative_int()

    power = my_pwr_with_operator(x, y)
    print(f'результат функции с оператором  {power}')
    power = my_pwr_without_operator(x, y)
    print(f'результат функции без оператора {power}')


if __name__ == '__main__':
    main()
