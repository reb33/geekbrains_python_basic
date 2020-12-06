# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


def main():
    number = input('Введите целое положительное число ')
    if number.startswith('-') and number[1:].isdigit():
        print('Вы ввели не положительное число')
        return
    if not number.isdigit():
        if number.replace('.', '1', 1).isdigit():  # проверка на то что число float
            print('Вы ввели не целое число')
            return
        print('Вы ввели не число')
        return

    max_ = 0
    number_ = number
    while True:
        digit = number[0:1]
        if max_ < int(digit):
            max_ = int(digit)
        if len(number) == 1:
            break
        number = number[1:]

    print(f'самая большая цифра из число {number_} это {max_} ')


if __name__ == '__main__':
    main()
