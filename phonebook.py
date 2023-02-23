# Необхоимо дополнить телефонный справочник возможностью изменения и удаления данных.

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts

# Добавление контакта
def ask_user():
    contact_surname = input('Введите фамилию: ')
    contact_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return contact_surname, contact_name, phone_number

def add_contact(file_name):
    info = ' '.join(ask_user())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')

# Вывод информации о контакте
def print_contacts(list_contacts: list):
    for contact in list_contacts:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()

# Поиск
def find_contact(list_contacts):
    print('Выберите критерий поиска:')
    search_index = input('1 - Фамилия \n2 - Имя \n3 - Номер телефона\n')
    search_param = None
    if search_index == '1':
        search_param = input('Введите фамилию: ')
    elif search_index == '2':
        search_param = input('Введите имя: ')
    elif search_index == '3':
        search_param = input('Введите номер телнфона: ')
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[search_value_dict[search_index]] == search_param:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)

# Вся телефонная книга
def show_phonebook(file_name):
    list_of_contacts = read_file(file_name)
    print_contacts(list_of_contacts)
    return list_of_contacts

# Поиск контакта для изменения или удаления
def search_to_modify(list_contacts: list):
    print('Выберите критерий поиска для изменения\удаления:')
    search_index = input('1 - Фамилия \n2 - Имя \n3 - Номер телефона\n')
    search_param = None
    if search_index == '1':
        search_param = input('Введите фамилию: ')
    elif search_index == '2':
        search_param = input('Введите имя: ')
    elif search_index == '3':
        search_param = input('Введите номер телнфона: ')
    search_result = []
    for contact in list_contacts:
        if contact[int(search_index) - 1] == search_param:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта для работы: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()

# Изменение контакта
def change_contact(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        list_contacts = []
        for line in file.readlines():
            list_contacts.append(line.split())
    change_index = search_to_modify(list_contacts)
    list_contacts.remove(change_index)
    print('Выберите данные для замены: ')
    field = input('1 - Фамилия \n2 - Имя \n3 - Номер телефона\n')
    if field == '1':
        change_index[0] = input('Введите новую фамилию: ')
    elif field == '2':
        change_index[1] = input('Введите новое имя: ')
    elif field == '3':
        change_index[2] = input('Введите новый номер телефона: ')
    list_contacts.append(change_index)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in list_contacts:
            line = ' '.join(contact) + '\n'
            file.write(line)

# Удаление контакта
def delete_contact(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        list_contacts = []
        for line in file.readlines():
            list_contacts.append(line.split())
    change_index = search_to_modify(list_contacts)
    list_contacts.remove(change_index)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in list_contacts:
            line = ' '.join(contact) + '\n'
            file.write(line)

# Пользовательское меню
def main_menu():
    file_contacts = 'Contacts.txt'
    while True:
        print()
        print('Введите номер, соответсвующий желаемому действию:')
        user_choice = input('1 - Добавить контакт \n2 - Найти контакт \n3 - Изменить контакт \n4 - Удалить контакт \n5 - Просмотр телефонной книги \n0 - Выход\n')
        #print()
        if user_choice == '1':
            print ('Добавляем новый контакт ')
            add_contact(file_contacts)
        elif user_choice == '2':
            print ('Поиск контакта ')
            contact_list = read_file(file_contacts)
            find_contact(contact_list)         
        elif user_choice == '3':
            print ('Изменить данные контакта ')
            change_contact(file_contacts)
        elif user_choice == '4':
            print ('Удаление контакта ')
            delete_contact(file_contacts)
        elif user_choice == '5':
            print ('Просмотр телефонной книги ')
            show_phonebook(file_contacts)
        elif user_choice == '0':
            print('Спасибо за использование нашего сервиса!')
            break
        else:
            print('Номер команды выбран некорректно.')
            print()
            continue

if __name__ == '__main__':
    main_menu()