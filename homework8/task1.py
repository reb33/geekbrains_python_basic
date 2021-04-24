# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def get_numbers(cls, str_date):
        try:
            return tuple(map(int, str_date.split('-')))
        except ValueError:
            print(f'{str_date} некорректная дата')

    @staticmethod
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    @staticmethod
    def validate_date(str_date):
        count_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        date_nums = Date.get_numbers(str_date)
        if date_nums is None:
            return False
        if len(date_nums) != 3:
            print(f'{str_date} некорректная дата')
            return False
        if Date.is_leap_year(date_nums[2]):
            count_days[2] = 29
        if date_nums[1] not in count_days or date_nums[0] > count_days[date_nums[1]]:
            print(f'{str_date} некорректная дата')
            return False
        return True


def main():
    assert Date.validate_date('31-01-1990')
    assert not Date.validate_date('32-01-1990')
    assert not Date.validate_date('32-13-1990')
    assert not Date.validate_date('32-00-1990')
    assert Date.validate_date('29-02-2004')
    assert Date.validate_date('29-02-2000')
    assert not Date.validate_date('29-02-2009')
    assert not Date.validate_date('29-02-1900')
    assert not Date.validate_date('23-as-1990')
    assert not Date.validate_date('23-1990')
    assert not Date.validate_date('23-01-01-1990')


if __name__ == '__main__':
    main()

