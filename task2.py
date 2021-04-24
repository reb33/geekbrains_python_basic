# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
from datetime import datetime


def main():
    # введите 1607176340 - 2020-12-05 16:52:20
    time_epoch = input('Введите дату в unix epoch time ')
    if not time_epoch.isdigit():
        print('Введенная сторка не подходит')
        return

    dt = datetime.fromtimestamp(float(time_epoch))

    print('Вы ввели {:%H:%M:%S}'.format(dt))


if __name__ == '__main__':
    main()
