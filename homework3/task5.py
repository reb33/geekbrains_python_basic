# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
from typing import Tuple

SPECIAL_SYMBOL = '#'


def parse_input(s: str) -> Tuple[bool, list]:
    numbers = []
    exit_ = False
    for el in s.split():
        if el == SPECIAL_SYMBOL:
            exit_ = True
            break
        elif el.isdigit():
            numbers.append(int(el))
    return exit_, numbers


def my_sum(numbers):
    res = 0
    for num in numbers:
        res += num
    return res


def main():
    exit_ = False
    result = 0
    while not exit_:
        s = input(f'введите числа дял сумирования. Для выхода введите {SPECIAL_SYMBOL} \n>>> ')
        exit_, numbers = parse_input(s)
        result += my_sum(numbers)
        print(f'Сумма {result}')


if __name__ == '__main__':
    main()
