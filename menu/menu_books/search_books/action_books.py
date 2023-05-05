from .open_book.Open_Book import Open_Book
from sql_query.sql_update.Update import*
from sql_query.sql_insert.Insert import*
from sql_query.sql_select.Select import*

def action_books():
    id_book=input("Выберите ID книги:")
    if id_book:
        while True:
            print("Выберите пункт:")
            print("1 - Открыть книгу")
            print("2 - Прогресс чтения")
            print("3 - Заметки к книге")
            print("4 - Хэштэги к книге")
            print("5 - Авторы к книге")
            print("6 - Указать путь к файлу книги")
            print("7 - Вернуться в меню")
            choise = str(input())
            
            #Выбор пункта 1 Открыть книгу
            if choise=='1':
                Open_Book(id_book)
                
            #Выбор пункта 2 Прогресс чтения     
            elif choise=='2':
                print("Выберите пункт:")
                print("1 - Изменить стр. чтения")
                print("2 - Изменить прогресс чтения")
                print("3 - Вернуться в меню")
                choise = str(input())
                if choise=='1':
                    try:
                        page=int(input("Введите страницу:"))
                        update_state_page(page,id_book)
                    except:
                        print("Ошибка!Необходимо ввести целочисленное значение.")
                elif choise=='2':
                    progress=str(input("Введите прогресс:"))
                    update_state_progress(progress,id_book)
                elif choise=='3':
                    break
                    
            #Выбор пункта 3 Заметки к книге     
            elif choise=='3':
                print("Выберите пункт:")
                print("1 - Показать заметки книги")
                print("2 - Добавить заметку к книге")
                print("3 - Вернуться в меню")
                choise= str(input())
                if choise=='1':
                    select_notes(id_book)
                elif choise=='2':
                    while True:
                        text=str(input("Введите текст заметки:"))
                        insert_notes(text,id_book)
                        choice=str(input("Добавить еще одну заметку к этой книге(д/н)?"))
                        if choice=='н':
                            break
                elif choise=='3':
                    break
                                        
            #Выбор пункта 4 Хэштэги к книге    
            elif choise=='4':
                print("Выберите пункт:")
                print("1 - Показать хэштэги книги")
                print("2 - Добавить хэштэги к книге")
                print("3 - Вернуться в меню")
                choise= str(input())
                if choise=='1':
                    select_books_id_hashtag(id_book)
                elif choise=='2':
                    while True:
                        try:
                            hashtag=str(input("Введите хэштэг"))
                            insert_books_id_hashtag(hashtag,id_book)
                            choice=str(input("Добавить еще один хэштэг к этой книге(д/н)?"))
                            if choice=='н':
                                break
                        except:
                            print("Хэштэг отсутствует в базе данных")
                elif choise=='3':
                    break
                    
            #Выбор пункта 5 Авторы к книге    
            elif choise=='5':
                print("Выберите пункт:")
                print("1 - Показать авторов книги")
                print("2 - Добавить авторов к книге")
                print("3 - Вернуться в меню")
                choise= str(input())
                if choise=='1':
                    select_books_id_author(id_book)
                elif choise=='2':
                    while True:
                        surname=input("Введите фамилию автора")
                        name=input("Введите имя автора")
                        patr=input("Введите отчество автора")
                        insert_books_id_author(surname,name,patr,id_book)
                        choice=str(input("Добавить еще одного автора к этой книге(д/н)?"))
                        if choice=='н':
                            break
                elif choise=='3':
                    break
            #Выбор пункта 6 Указать путь к файлу книги    
            elif choise=='6':
                path=str(input("Введите путь в формате 'books\\book.pdf'"))
                update_about_path(path,id_book)
                
            #Выбор пункта 7 Вернуться в меню
            elif choise=='7':
                break