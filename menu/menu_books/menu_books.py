from .add_books import*
from .search_books import*

def menu_books():
    while True:
        print("Выберите пункт:")
        print("1 - Найти книгу")
        print("2 - Добавление данных")
        print("3 - Вернуться в меню")
        choise = str(input())
        
        #Выбор пункта 1 Работа с книгой
        if choise=='1':
            search_main.search_main()
            
        #Выбор пункта 2 Добавление данных
        if choise=='2':
            add_main.add_main()
            
        #Выбор пункта 3 Выход 
        if choise=='3':
            break