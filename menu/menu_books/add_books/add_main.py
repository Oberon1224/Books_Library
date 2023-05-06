#Copyright 2023 Bushuev Dmitrii
from sql_query.sql_select.Select import*
from sql_query.sql_insert.Insert import*

def add_main():
    while True:
        print("___________Добавление данных____________")
        print("Выберите пункт:")
        print("1 - Автор")
        print("2 - Язык")
        print("3 - Категория")
        print("4 - Хэштэг")
        print("5 - Год")
        print("6 - Книга")
        print("7 - Меню")
        choise = str(input())
    
        #1 - Автор
        if choise == '1':
            print("Выберите пункт:")
            print("1 - Показать всех авторов")
            print("2 - Добавить автора")
            print("3 - Меню")
            choise = str(input())
            if choise == '1':
                sel_author=select_author()
            if choise == '2':
                surname=str(input("Введите фамилию:"))
                name=str(input("Введите имя:"))
                patr=str(input("Введите отчество:"))
                ins_author=insert_author(surname,name,patr)
            if choise == '3':
                continue
            
        #2 - Язык
        if choise == '2':
            print("Выберите пункт:")
            print("1 - Показать все языки")
            print("2 - Добавить язык")
            print("3 - Меню")
            choise = str(input())
            if choise == '1':
                sel_language=select_language()
            if choise == '2':
                name=str(input("Введите название языка:"))
                ins_language=insert_language(name)
            if choise == '3':
                continue
                         
        #3 - Категория  
        if choise == '3':
            print("Выберите пункт:")
            print("1 - Показать все категории")
            print("2 - Добавить категорию")
            print("3 - Меню")
            choise = str(input())
            if choise == '1':
                sel_category=select_category()
            if choise == '2':
                name=str(input("Введите категорию:"))
                ins_category=insert_category(name)
            if choise == '3':
                continue
                         
        #4 - Хэштэг 
        if choise == '4':
            print("Выберите пункт:")
            print("1 - Показать все хэштэги")
            print("2 - Добавить хэштэг")
            print("3 - Меню")
            choise = str(input())
            if choise == '1':
                sel_hashtag=select_hashtag()
            if choise == '2':
                name=str(input("Введите хэштэг:"))
                ins_hashtag=insert_hashtag(name)
            if choise == '3':
                continue
                
        #5 - Год 
        if choise == '5':
            print("Выберите пункт:")
            print("1 - Показать все года")
            print("2 - Добавить год")
            print("3 - Меню")
            choise = str(input())
            if choise == '1':
                sel_year=select_year()
            if choise == '2':
                try:
                    name=int(input("Введите год"))
                except:
                    print("Ошибка!Значение года должно быть целочисленным типом")
                    continue
                ins_year=insert_year(name)
                if choise == '3':
                    continue
                    
        #6 - Книга 
        if choise == '6':
            print("Выберите пункт:")
            print("1 - Показать все книги")
            print("2 - Добавить книгу")
            print("3 - Меню")
            choise = str(input())
            if choise == '1':
                sel_books=select_books()         
            if choise == '2':
                try:
                    title=str(input("Введите название книги:"))
                    page=int(input("Введите количество страниц книги:"))
                    year=int(input("Введите год выпуска книги:"))
                    language=str(input("Введите язык книги:"))
                    category=str(input("Введите категорию книги:"))
                    ins_books=insert_books(title,page,year,language,category)
                except:
                    print("Ошибка! Проверьте правильность введенных данных и наличие их в базе данных")
                    continue
            if choise == '3':
                continue
                
        #7 Выбор пункта Выход      
        if choise == '7':
            break
