def amount_of_basic_exchange():
    gender = input('Ваш пол? (м, ж): ')
    weigth = float(input('Ваш вес? (кг): '))
    height = float(input('Ваш рост? (см): '))
    age = float(input('Ваш возраст? (лет): '))
    if gender == 'м':
        print('Ваш ВОО =', 10 * weigth + 6.25 * height - 5 * age + 5)
        return
    elif gender == 'ж':
        print('Ваш ВОО =', 10 * weigth + 6.25 * height - 5 * age - 161)
        return
    else:
        print('Все данные вводятся кириллицей!')


amount_of_basic_exchange()
