# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))


def main():
    with open(os.path.join(BASE_DIR, 'files', 'task2', 'my_file')) as file_:
        res = file_.readlines()
        print(f'Всего строк {len(res)}')
        print('Количество слов в строках')
        for i, line in enumerate(res):
            print(f'{i+1} - {len(line.split())}')


if __name__ == '__main__':
    main()