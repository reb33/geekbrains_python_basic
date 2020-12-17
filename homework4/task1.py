# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


def calculate_salary(work_in_hours, rate_per_hour, bonus):
    return work_in_hours * rate_per_hour + bonus


def main():
    if len(argv) != 4 or any(not i.isdigit() for i in argv[1:]):
        print('должно быть 3 целочисленных параметра - выработка в часах, ставка в час, премия')
        return
    work_in_hours, rate_per_hour, bonus = [int(i) for i in argv[1:]]

    print(calculate_salary(work_in_hours, rate_per_hour, bonus))


if __name__ == '__main__':
    main()
