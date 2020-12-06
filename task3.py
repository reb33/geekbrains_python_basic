# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


def main():
    number_n = input('Введите число n ')
    if not number_n.isdigit():
        print('Вы ввели не число')
        return

    number_nn = int(f'{number_n}{number_n}')
    number_nnn = int(f'{number_n}{number_n}{number_n}')
    number_n = int(number_n)
    res = number_n+number_nn+number_nnn
    print(f'result {res}')


if __name__ == '__main__':
    main()
