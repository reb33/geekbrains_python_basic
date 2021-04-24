# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))


def main():
    with open(os.path.join(BASE_DIR, 'files', 'task1', 'my_file'), mode='w') as file_:
        print('введите данные'+os.linesep)
        while True:
            text = input()
            if text == '':
                break
            else:
                file_.write(text+os.linesep)


if __name__ == '__main__':
    main()