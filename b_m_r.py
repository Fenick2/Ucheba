def basic_metabolism_rate():
    '''Программа расчета ВОО - величины основного обмена
    по формуле Миффлина-Джеора.
    Основной обмен — это минимальное количество энергии,
    необходимое для обеспечения нормальной жизнедеятельности организма
    в стандартных условиях.
    Возраст от 15-ти лет.
    '''

    age = float(input('Ваш возраст? (лет): '))
    if age < 15:
        print('Невозможно корректно расчитать ВОО в таком возрасте. До свиданья!')
        return

    weigth = float(input('Ваш вес? (кг): '))
    if weigth < 35 or weigth > 200:
        print('Вы больны. Обратитесь к врачу!')
        return

    height = float(input('Ваш рост? (см): '))
    if  not 130 < height < 250:
        print('Данные не корректны. Или у Вас гормональные проблемы.')
        return

    gender = input('Ваш пол? (м, ж): ')

    if gender.lower() == 'м':
        print('Ваш ВОО =', 10 * weigth + 6.25 * height - 5 * age + 5)
        return
    elif gender.lower() == 'ж':
        print('Ваш ВОО =', 10 * weigth + 6.25 * height - 5 * age - 161)
        return
    else:
        print('Науке известно только два пола (у людей)!')
        return


basic_metabolism_rate()
