def is_error_data(s, v, c=''):
    is_ok = False
    input_data = input(f'{s}: ')
    while not is_ok:
        if v == 1:
            if input_data in c:
                is_ok = True
            else:
                input_data = input('Введено недопустимое значение, повторите ввод: ')
        elif v == 2:
             is_ok = True
    return input_data