# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


def main():
    seasons = {
        'winter': [12, 1, 2],
        'spring': [3, 4, 5],
        'summer': [6, 7, 8],
        'fall': [9, 10, 11]
    }
    month_number = input('введите номер месяца ')
    if not month_number.isdigit():
        print('вы ввели не число в поле номер месяца ')
        return
    month_number = int(month_number)
    if 1 > month_number or month_number > 13:
        print('число должно быть от 1 до 12')

    for k, v in seasons.items():
        if month_number in v:
            print(f'{month_number} месяц в {k}')
            return


if __name__ == '__main__':
    main()
