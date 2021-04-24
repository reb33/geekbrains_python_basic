# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


def main():
    revenue = input('введите прибыль компании ')
    if not revenue.isdigit():
        print('Вы ввели не число в значение прибыли')
        return

    expense = input('введите сумму издержек компании ')
    if not expense.isdigit():
        print('Вы ввели не число в значение суммы издержек')
        return
    revenue = int(revenue)
    expense = int(expense)

    if revenue > expense:
        print('Фирма в прибыли')
    elif revenue == expense:
        print('Нет ни прибыли ни убытков')
        return
    else:
        print('Фирма в убытке')
        return
    profitability = revenue/expense
    print(f'Рентабельность {profitability:.2f}')

    count_employees = input('введите число сотрудников фирмы ')

    if not count_employees.isdigit():
        print('Вы ввели не число в значение количества сотрудников')
        return
    print(f'Прибыль в расчете на 1 сотрудника {revenue/int(count_employees):.2f}')


if __name__ == '__main__':
    main()
