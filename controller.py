import ui, is_error, base

def button_click():
    end = False
    while not end:
        choice = ui.start_menu()
        if choice == '1':
            s = ui.add_student()
            count = base.table_type(1, s)
            s.insert(5, ' ') # добавляем id места
            base.table_type(2, s)
            base.table_type(3, s + [count])
        elif choice == '2':
            user_input = ui.choice_table()
            if user_input == '1':
                base.out_data('students.csv', 78)
            elif user_input == '2':
                base.out_data('class.csv', 39)
            elif user_input == '3':
                base.out_data('adress.csv', 78)
            elif user_input == '4':
                base.out_all_data()
            input('Нажмите Enter для продолжения...')
        elif choice == '3':
            end = True
        