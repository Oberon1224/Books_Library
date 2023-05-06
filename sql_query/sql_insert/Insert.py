#Copyright 2023 Bushuev Dmitrii
import sqlite3

#запрос добавление в таблицу author
class insert_author:
    def __init__(self,surname,name,patr):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        #запрос проверки отсутствия автора в базе данных
        query1="""SELECT id_author FROM author 
                  WHERE surname LIKE ?
                  AND name LIKE ?
                  AND patr LIKE ?"""
        cursor.execute(query1,(surname, name, patr))
        result = cursor.fetchone()
        #переменная проверки автора
        check_author = str(result)
        if check_author=="None":
            #запрос на добавление данных в таблицу
            query2="""INSERT INTO author (surname,name,patr)
                        VALUES(?,?,?);"""
            cursor.execute(query2,(surname,name,patr))
            self.sqlite_connection.commit()
        else:
            print("Ошибка! Введенный автор уже есть в базе данных")
        self.sqlite_connection.close()
          
#запрос добавление в таблицу language
class insert_language:
    def __init__(self,name):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        #запрос проверки отсутствия языка в базе данных
        query1="""SELECT id_language FROM language
                   WHERE name LIKE ?"""
        cursor.execute(query1,(name,))
        result = cursor.fetchone()
        #переменная проверки языка
        check_language = str(result)
        if check_language=="None":
            #запрос на добавление данных в таблицу
            query2="""INSERT INTO language (name)
                        VALUES(?);"""
            cursor.execute(query2,(name,))
            self.sqlite_connection.commit()
        else:
            print("Ошибка! Введенный язык уже есть в базе даных")
        self.sqlite_connection.close()
          
#запрос добавление в таблицу category
class insert_category:
    def __init__(self,name):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        #запрос проверки отсутствия категории в базе данных
        query1="""SELECT id_category FROM category
                   WHERE name LIKE ?"""
        cursor.execute(query1,(name,))
        result = cursor.fetchone()
        #переменная проверки категории
        check_category=str(result)
        if check_category =="None":      
            #запрос на добавление данных в таблицу
            query2="""INSERT INTO category (name)
                        VALUES(?);"""
            cursor.execute(query2,(name,))
            self.sqlite_connection.commit()
        else:
            print("Ошибка! Введенная категория уже есть в базе данных")
        self.sqlite_connection.close()
          
#запрос добавление в таблицу hashtag
class insert_hashtag:
     def __init__(self,name):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        #запрос проверки отсутствия хэштэга в базе данных
        query1 ="""SELECT id_hashtag FROM hashtag
                   WHERE name LIKE ?"""
        cursor.execute(query1,(name,))
        result = cursor.fetchone()
        #переменная проверки хэштэга
        check_hashtag=str(result)
        if check_hashtag =="None":
            #запрос на добавление данных в таблицу
            query2="""INSERT INTO hashtag (name)
                        VALUES(?);"""
            cursor.execute(query2,(name,))
            self.sqlite_connection.commit()
        else:
            print("Ошибка! Введенный хэштэг уже есть в базе данных")
        self.sqlite_connection.close()

#запрос добавление в таблицу year
class insert_year:
    def __init__(self,name):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        #запрос проверки отсутствия хэштэга в базе данных
        query1="""SELECT id_year FROM year
                  WHERE year LIKE ?"""
        cursor.execute(query1,(name,))
        result=cursor.fetchone()
        #переменная проверки года
        check_year=str(result)
        if check_year =="None":
            #запрос на добавление данных в таблицу
            query2="""INSERT INTO year (year)
                        VALUES(?);"""
            cursor.execute(query2,(name,))
            self.sqlite_connection.commit()
        else:
            print("Ошибка! Введенный год уже есть в базе данных")
        self.sqlite_connection.close()
          
#запрос добавление в таблицу books
class insert_books:
    def __init__(self,title,page,year,language,category):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
          
        #query1 - запрос нахождения id последней добавленной книги
        query1="SELECT id_book FROM books ORDER BY id_book DESC"
        cursor.execute(query1)
        result=cursor.fetchone()
          
        #переменная содержащая id добавляемой книги
        if result:
            id_state_book_about=int(result[0])+1
        else:
            id_state_book_about=1

        #query2 - запрос на добавление нового состояния книги
        query2="""INSERT INTO state (name,page,id_book)
        VALUES('На чтении','1',?);"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query2,(id_state_book_about,))
        self.sqlite_connection.commit()
          
        #query3 - запрос на добавление нового пути к книге
        query3="""INSERT INTO about (path,id_book) VALUES('Не указан',?);"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query3,(id_state_book_about,))
        self.sqlite_connection.commit()
          
        #query4- запрос на выбор id_year
        query4 ="""SELECT Y.id_year FROM year AS Y WHERE Y.year LIKE ?"""
        cursor=self.sqlite_connection.cursor()
        cursor.execute(query4,(year,))
        result = cursor.fetchone()
        id_year = int(result[0])
          
        #query5- запрос на выбор id_language
        query5 ="""SELECT L.id_language FROM language AS L WHERE L.name LIKE ?"""
        cursor=self.sqlite_connection.cursor()
        cursor.execute(query5,(language,))
        result = cursor.fetchone()
        id_language = int(result[0])
          
        #query6- запрос на выбор id_category
        query6 ="""SELECT C.id_category FROM category AS C WHERE C.name LIKE ?"""
        cursor=self.sqlite_connection.cursor()
        cursor.execute(query6,(category,))
        result = cursor.fetchone()
        id_category = int(result[0])
          
        #query7- запрос проверки отсутствия книги в базе данных
        query7="""SELECT id_book FROM books
                  WHERE title LIKE ? 
                  AND id_year LIKE ?
                  AND id_language LIKE ?
                  AND page LIKE ?"""
        cursor.execute(query7,(title,id_year,id_category,page))
        result = cursor.fetchone()
        #переменная проверки книги
        check_book=str(result)
        if check_book =="None":
            #query8 - запрос на добавление новой книги
            #id_state_book_about используется два раза для столбца about и state
            query8="""INSERT INTO books (title,page,id_year,id_language,
                                           id_about,id_state,id_category)
                      VALUES(?,?,?,?,?,?,?);"""
            cursor.execute(query8,(title,page,id_year,id_language,id_state_book_about,id_state_book_about,id_category))
            self.sqlite_connection.commit()
        else:
            print("Ошибка! Введенная книга уже есть в базе данных")
        self.sqlite_connection.close()
          
#запрос добавление в таблицу books_id_author
class insert_books_id_author:
    def __init__(self,surname,name,patr,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        #запрос нахождения id_author
        query1 ="""SELECT id_author FROM author
                   WHERE surname LIKE ?
                   AND name LIKE ?
                   AND patr LIKE ?"""
        cursor.execute(query1,(surname,name,patr))
        result = cursor.fetchone()
        if str(result) =="None":
            print("Ошибка! Введенного автора нет в базе данных")
        else:
            id_author = result[0]
            #запрос проверки на отсутствие данного автора у книги
            query2="""SELECT id_book FROM books_id_author
                        WHERE id_author LIKE ?
                        AND id_book LIKE ?"""
            cursor.execute(query2,(id_author,id_book))
            result = cursor.fetchone()
            #переменная проверки автора
            check_author_books = str(result)
            if check_author_books =="None":
                #query3 - запрос на добавление автора к книге
                query3="""INSERT INTO books_id_author (id_author,id_book)
                          VALUES(?,?);"""
                cursor.execute(query3,(id_author,id_book))
                self.sqlite_connection.commit()
            else:
                print("Ошибка! Данная книга уже имеет этого автора")
        self.sqlite_connection.close()
          
#запрос добавление в таблицу books_id_hashtag
class insert_books_id_hashtag:
    def __init__(self,hashtag,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        #запрос нахождения id_hashtag
        query1="SELECT id_hashtag FROM hashtag WHERE name LIKE ?"
        cursor.execute(query1,(hashtag,))
        result = cursor.fetchone()
        if str(result) =="None":
            print("Ошибка! Введенного хэштэга нет в базе данных")
        else:
            id_hashtag = int(result[0])
            #запрос проверки на отсутствие данного хэштэга у книги
            query2="""SELECT id_book FROM books_id_hashtag 
                        WHERE id_hashtag LIKE ?
                        AND id_book LIKE ?"""
            cursor.execute(query2,(id_hashtag,id_book))
            result=cursor.fetchone()
            #переменная проверки хэштэга
            check_hashtag_books=str(result)
            if check_hashtag_books =="None":
                #query3 - запрос на добавление хэштэга к книге
                query3="""INSERT INTO books_id_hashtag(id_hashtag,id_book)
                          VALUES(?,?);"""
                cursor.execute(query3,(id_hashtag,id_book))
                self.sqlite_connection.commit() 
            else:       
                print("Ошибка! Данная книга уже имеет этот хэштэг")
        self.sqlite_connection.close()
          
#запрос добавление в таблицу notes
class insert_notes:
    def __init__(self,text,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        cursor = self.sqlite_connection.cursor()
        query="""INSERT INTO notes(text_notes,id_book)
                  VALUES(?,?);"""
        cursor.execute(query,(text,id_book))
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
