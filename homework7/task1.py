# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
import typing


class Matrix:

    def __init__(self, matrix: typing.List[typing.List]) -> None:
        if any(len(row) != len(matrix[0]) for row in matrix[1:]):
            raise AttributeError('не матрица')
        self.__matrix = matrix

    def __str__(self):
        res = []
        for row in self.__matrix:
            res.append('\t'.join(map(str, row)))
        return '\n'.join(res)

    def __add__(self, other: 'Matrix'):
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise ArithmeticError('такие матрицы нельзя сложить')

        res = []
        for r, _ in enumerate(self.__matrix):
            res.append([self.__matrix[r][c] + other.__matrix[r][c] for c in range(len(self.__matrix[0]))])

        return Matrix(res)


def main():
    first = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    second = Matrix([[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24]])

    print(first + second)


if __name__ == '__main__':
    main()
