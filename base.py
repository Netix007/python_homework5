import csv, os

def table_type(type_header, s):

    if type_header == 1:
        data_header = ['id', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения',
                     'Класс', 'id места в кабинете', 'Статус ученика']
        temp = [s[i] for i in range(6)] + [s[9]]
        count = in_data(data_header, temp, 'students.csv', True)
        return count
    elif type_header == 2:
        data_header = ['id места в кабинете', 'Ряд', '№ парты', 'Вариант']
        temp = [s[i] for i in range(5, 9)]
        in_data(data_header, temp, 'class.csv', False)
    elif type_header == 3:
        data_header = ['id', 'Город', 'Улица', 'Дом', 'Крартира', 'Статус адреса']
        temp = [s[-1]] + [s[i] for i in range(10, 15)]
        in_data(data_header, temp, 'adress.csv', False)
        if len(s) > 16:
            temp = [s[-1]] + [s[i] for i in range(15, 20)]
            in_data(data_header, temp, 'adress.csv', False)
    
def in_data(data_header, s, file_name, id_need):
    base = open(file_name, 'a+')
    base.close()
    with open(file_name) as f:
        base = csv.reader(f, delimiter = ',')
        count = sum(1 for row in base)
    if count == 0:
        with open(file_name, mode='w') as f:
            base = csv.writer(f, delimiter=',', lineterminator="\n")
            base.writerow(data_header)
            if id_need:
                count += 1
                base.writerow([count] + s)
                return count
            else:
                base.writerow(s)
    else:
        with open(file_name, mode='a') as f:
            base = csv.writer(f, delimiter=',', lineterminator="\n")
            if id_need:
                base.writerow([count] + s)
                return count
            else:
                base.writerow(s)

def out_data(file_name, n):
    os.system('CLS')
    base = open(file_name, 'a+')
    base.close()
    with open(file_name) as f:
        base = csv.reader(f, delimiter = ',')
        for row in base:
            print(*row, sep=' | ')
            print('-'*n)

#table_type(1, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])