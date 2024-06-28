
def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('phones.txt')

    while (choice != 5):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Ищем по фамилии: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Ищем по номеру: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            other_book_filename = input('Введите имя другого справочника:  ')
            print(add_from_other_book(phone_book, other_book_filename))

        choice = show_menu()


def show_menu():
    print("""
Меню телефонного справочника:
1. Отобразить весь справочник
2. Найти абонента по фамилии
3. Найти абонента по номеру телефона
4. Добавить абонента из другого справочника
5. Закончить работу""")
    choice = int(input('Выберите необходимое действие: '))
    return choice

def print_result(phone_list):
    print('\n=====   Список абонентов:   =====')
    print("{:<6} {:<23} {:<8} {:<15}".format('№','Фамилия, Имя','Телефон','Описание'))
    for (i, item) in enumerate(phone_list, start=1):
        print("{:<6} {:<25} {:<6} {:<15}".format(i, item['Фамилия'].strip() + " " + item['Имя'].strip(), item['Телефон'].strip(), item['Описание'].strip()))

def find_by_lastname(phone_list,last_name):
    pass

def find_by_number(phone_list,number):
    pass

def add_from_other_book(phone_list,other_book_filename):
    pass

def read_txt(filename): 
    phone_book=[]
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            if line.strip() == "": continue
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

work_with_phonebook()
