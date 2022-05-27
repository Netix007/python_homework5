
import is_error
import os

def start_menu():
    os.system('CLS')
    print('База учеников 2022')
    print('''Выберете вариан:
        1 - Добавить данные
        2 - Просмотр информации
        3 - Выход''')
    return is_error.is_error_data('Ваш выбор', 1)

def add_student():
    os.system('CLS')
    print('Ввод данных об ученике\n')
    data_name = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Класс', 'Статус ученика', 'Город', 'Улица', 'Дом', 'Крартира', 'Статус адреса']
    s = [is_error.is_error_data(data_name[i], 1) for i in range(len(data_name))]
    return s

    #surname = input('Фамилия: ')
    #name = input('Имя: ')
    #patronymic = input('Отчество: ')
    #birthday = input('Дата рождения: ')
    #school_class = input('Класс: ')
    #student_status = input('Статус ученика: ')
    #town = input('Город: ')
    #street = input('Улица: ')
    #house = input('Дом: ')
    #flat = input('Квартира: ')
    #adress_status = input('Статус адреса: ')
    
print(add_student())