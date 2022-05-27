import csv

def in_base(date_header,s):
    base = open("base.csv", 'a+')
    all_students = csv.reader(base)
    count = len(list(all_students))
    print(count)
    if count == 0:
        #base.writelines(date_header)
        print()
    base.close()

in_base(" ".join(['id', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Класс', 'Статус ученика', 'Город', 'Улица', 'Дом', 'Крартира', 'Статус адреса']), 1)