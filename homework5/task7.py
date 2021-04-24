# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))


def main():
    with open(os.path.join(BASE_DIR, "files", "task7", "file")) as file_:
        res = {}
        count_firm_with_profit = 0
        sum_profit = 0
        for line in file_:
            data_firm = line.split()
            if int(data_firm[2]) > int(data_firm[3]):
                count_firm_with_profit += 1
                sum_profit += int(data_firm[2]) - int(data_firm[3])
                res[data_firm[0]] = int(data_firm[2]) - int(data_firm[3])
            else:
                res[data_firm[0]] = int(data_firm[3]) - int(data_firm[2])
    average_profit = sum_profit / count_firm_with_profit

    with open(os.path.join(BASE_DIR, "files", "task7", "result.json"), mode='w') as file_:
        json.dump([res, dict(average_profit=average_profit)], file_)


if __name__ == "__main__":
    main()
