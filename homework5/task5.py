# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))


def main():
    with open(os.path.join(BASE_DIR, "files", "task5", "file"), mode='w') as file_:
        file_.write('1 3 5 1 1 2 1 1 2 1 1 1 1 2 1 12 2 1 1 2 1 12')
    with open(os.path.join(BASE_DIR, "files", "task5", "file")) as file_:
        s = file_.read()
        sum_ = sum(int(el) for el in s.split())
        print(sum_)


if __name__ == '__main__':
    main()
