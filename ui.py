
import is_error
import os

def start_menu():
    os.system('CLS')
    print('База учеников 2022')
    print('''Выберете вариан:
        1 - Добавить данные
        2 - Просмотр информации
        3 - Выход''')
    return is_error.is_error_data('Ваш выбор', 1, ('1', '2', '3'))

def add_student():
    os.system('CLS')
    print('Ввод данных об ученике\n')
    data_name = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Класс',
                'id места в кабинете', 'Ряд', '№ парты', 'Вариант',
                'Статус ученика', 'Город', 'Улица', 'Дом', 'Крартира', 'Статус адреса']
    s = [is_error.is_error_data(data_name[i], 2) for i in range(len(data_name))]
    print('Вы ходите добавить дополнительный адрес? ', end='')
    if is_error.is_error_data('Да/Нет', 1, ('Да', 'Нет')) == 'Да':
        data_name = ['Город', 'Улица', 'Дом', 'Крартира', 'Статус адреса']
        s = s + [is_error.is_error_data(data_name[i], 2) for i in range(len(data_name))]
    return s

def choice_table():
    print('''Выберете вариан:
        1 - Вывести таблицу "Ученики"
        2 - Вывести таблицу "Кабинет"
        3 - Вывести таблицу "Адреса учеников"''')
    return is_error.is_error_data('Ваш выбор', 1, ('1', '2', '3'))