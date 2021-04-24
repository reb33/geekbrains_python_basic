# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_user(*, name, surname, birth_year, city, email, phone):
    print(name, surname, birth_year, city, email, phone)



def main():
    print_user(
        name='Иван',
        surname='Иванов',
        birth_year=1990,
        city='Воронеж',
        email='ivan.ivanov@tezka.com',
        phone='111-111-11-11'
    )


if __name__ == '__main__':
    main()