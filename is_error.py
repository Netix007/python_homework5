def is_error_data(s, v):
    is_ok = False
    input_data = input(f'{s}: ')
    while not is_ok:
        if v == 1:
            if input_data in ('1', '2', '3'):
                is_ok = True
            else:
                input_data = input('Введено недопустимое значение, повторите ввод: ')
    return input_data