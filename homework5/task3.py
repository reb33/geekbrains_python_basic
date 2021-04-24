# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))


def main():
    with open(os.path.join(BASE_DIR, 'files', 'task3', 'file')) as file_:
        employees = file_.readlines()
        employees = [employee.split(' - ') for employee in employees]
        print('Сотрудники с зп < 20000')
        for employee in employees:
            if int(employee[1]) < 20000:
                print(employee[0])
        employees_salaries = [int(employee[1]) for employee in employees]
        employees_salaries_avg = sum(employees_salaries) / len(employees_salaries)
        print(f'средняя величина дохода сотрудников {employees_salaries_avg:.2f}')


if __name__ == '__main__':
    main()