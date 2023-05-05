from sql_query.sql_select import Select_View
from .action_books import action_books

def search_main():
    while True:
        print("Выберите пункт:")
        print("1 - Найти книгу по названию")
        print("2 - Найти книгу по автору")
        print("3 - Найти книгу по категории")
        print("4 - Найти книгу по хэштэгу")
        print("5 - Показать книги на чтения")
        print("6 - Показать прочитанные книги")
        print("7 - Вернуться в меню")
        choise = str(input())
        
        #Выбор пункта 1-4 Найти книгу по опредленному критерию
        if choise=='1' or choise=='2' or choise=='3' or choise=='4':
            if choise=='1':
                name=str(input("Введите название книги:"))
            elif choise=='2':
                name=str(input("Введите фамилию автора книги:"))
            elif choise=='3':
                name=str(input("Введите категорию книги:"))
            elif choise=='4':
                name=str(input("Введите хэштэг книги:"))
            Select_View.select_view_search(choise,name)
            action_books()
            
        #Выбор пункта 5 Показать книги на чтения
        elif choise=='5':
            Select_View.select_view_search(choise)
            action_books()
            
        #Выбор пункта 6 Показать прочитанные книги
        elif choise=='6':
            Select_View.select_view_search(choise)
            action_books()
            
        #Выбор пункта 7 Вернуться в меню
        elif choise=='7':
            break