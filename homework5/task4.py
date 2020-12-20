# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))

translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def main():
    with open(os.path.join(BASE_DIR, "files", "task4", "file1")) as file_input, open(
        os.path.join(BASE_DIR, "files", "task4", "file2"),
        mode='w'
    ) as file_output:
        for line in file_input:
            els = line.split(' — ')
            s = f'{translate[els[0]]} - {els[1]}'
            file_output.write(s)


if __name__ == "__main__":
    main()
