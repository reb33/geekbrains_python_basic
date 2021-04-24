# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.imaginary+other.imaginary)

    def __mul__(self, other:'ComplexNumber'):
        # z1=a1+b1i и z2=a2+b2i
        # z=z1⋅z2=(a1a2−b1b2)+(a1b2+b1a2)i
        real = self.real*other.real-self.imaginary*other.imaginary
        imaginary = self.real*other.imaginary+self.imaginary*other.real
        return ComplexNumber(real, imaginary)

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'


def main():
    c1 = ComplexNumber(5, 10)
    c2 = ComplexNumber(8, 5)
    print(c1+c2)
    print(c1*c2)


if __name__ == '__main__':
    main()
