#Copyright 2023 Bushuev Dmitrii
import sqlite3

#запрос выборки данных таблицы author
class select_author:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM author;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id автора
        max_len_id_auth=int(0)
        #масимальная длина фамилии автора
        max_len_surname=int(0)
        #масимальная длина имени автора
        max_len_name=int(0)
        #масимальная длина отчества автора
        max_len_patr=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_auth:
                max_len_id_auth=len(str(all_results[i][0]))
                if max_len_id_auth<3:
                    max_len_id_auth=3
            if len(str(all_results[i][1]))>max_len_surname:
                max_len_surname=len(str(all_results[i][1]))
                if max_len_surname<7:
                    max_len_surname=7
            if len(str(all_results[i][2]))>max_len_name:
                max_len_name=len(str(all_results[i][2]))
                if max_len_name<3:
                    max_len_name=3
            if len(str(all_results[i][3]))>max_len_patr:
                max_len_patr=len(str(all_results[i][3]))
                if max_len_patr<8:
                    max_len_patr=8
        #заголовок таблицы author
        column_name_author=["№","Фамилия","Имя","Отчество"]
        print(f'{column_name_author[0]:<{max_len_id_auth}}'+"|"+f'{column_name_author[1]:^{max_len_surname}}'+"|"+
             f'{column_name_author[2]:^{max_len_name}}'+"|"+f'{column_name_author[3]:^{max_len_patr}}'+"|")
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{max_len_id_auth}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_surname}}'+"|", end="")
                elif j==2:
                    print(f'{all_results[i][j]:<{max_len_name}}'+"|", end="")
                elif j==3:
                    print(f'{all_results[i][j]:<{max_len_patr}}'+"|", end="")
            print("")
          
#запрос выборки данных таблицы books
class select_books:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM books;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id книги
        max_len_id_book=int(0)
        #масимальная длина названия книги
        max_len_title=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_book:
                max_len_id_book=len(str(all_results[i][0]))
                if max_len_id_book<1:
                    max_len_id_book=1
            if len(str(all_results[i][1]))>max_len_title:
                max_len_title=len(str(all_results[i][1]))
                if max_len_title<8:
                    max_len_title=8
        #заголовок таблицы books
        column_name=["№","Название","Кол-во стр.","id_year","id_lang","id_abou","id_stat","id_catg"]               
        print(f'{column_name[0]:<{max_len_id_book}}'+"|"+f'{column_name[1]:^{max_len_title}}'+"|"+f'{column_name[2]:^11}'+
              "|"+f'{column_name[3]:^7}'+"|"+f'{column_name[4]:^7}'+"|"+f'{column_name[5]:^7}'+"|"+
              f'{column_name[6]:^7}'+"|"+f'{column_name[7]:^7}'+"|")
        #вывод таблицы books
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:{max_len_id_book}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:{max_len_title}}'+"|", end="")
                elif j==2:
                    print(f'{all_results[i][j]:<{11}}'+"|", end="")
                elif j==3:
                    print(f'{all_results[i][j]:<{7}}'+"|", end="")
                elif j==4:
                    print(f'{all_results[i][j]:<{7}}'+"|", end="")
                elif j==5:
                    print(f'{all_results[i][j]:<{7}}'+"|", end="")
                elif j==6:
                    print(f'{all_results[i][j]:<{7}}'+"|", end="")
                elif j==7:
                    print(f'{all_results[i][j]:<{7}}'+"|", end="")
            print("")
        
#запрос выборки данных таблицы year
class select_year:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM year;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id года
        max_len_id_year=int(0)
        #масимальная длина значения года
        max_len_year=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_year:
                max_len_id_year=len(str(all_results[i][0]))
                if max_len_id_year<1:
                    max_len_id_year=1
            if len(str(all_results[i][1]))>max_len_year:
                max_len_year=len(str(all_results[i][1]))
                if max_len_year<3:
                    max_len_year=3
        #заголовок таблицы year
        columns_year=["№","Год"]
        print(f'{columns_year[0]:<{max_len_id_year}}'+"|"+f'{columns_year[1]:^{max_len_year}}'+"|")          
        #вывод таблицы year
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{max_len_id_year}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_year}}'+"|", end="")
            print("")

#запрос выборки данных таблицы language
class select_language:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM language;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id языка
        max_len_id_lang=int(0)
        #масимальная длина значения языка
        max_len_lang=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_lang:
                max_len_id_lang=len(str(all_results[i][0]))
                if max_len_id_lang<1:
                    max_len_id_lang=1
            if len(str(all_results[i][1]))>max_len_lang:
                max_len_lang=len(str(all_results[i][1]))
                if max_len_lang<4:
                    max_len_lang=4
        #заголовок таблицы language
        column_lang=["№","Язык"]
        print(f'{column_lang[0]:<{max_len_id_lang}}'+"|"+f'{column_lang[1]:^{max_len_lang}}'+"|")
        #вывод таблицы language          
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{max_len_id_lang}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_lang}}'+"|", end="")
            print("")

#запрос выборки данных таблицы about          
class select_about:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM about;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id справки
        max_len_id_about=int(0)
        #масимальная длина значения справки
        max_len_about=int(0)
        #масимальная длина id_books
        max_len_id_books=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_about:
                max_len_id_about=len(str(all_results[i][0]))
                if max_len_id_about<1:
                    max_len_id_about=1
            if len(str(all_results[i][1]))>max_len_about:
                max_len_about=len(str(all_results[i][1]))
                if max_len_about<4:
                    max_len_about=4
            if len(str(all_results[i][2]))>max_len_id_books:
                max_len_id_books=len(str(all_results[i][2]))
                if max_len_id_books<8:
                    max_len_id_books=8
        #заголовок таблицы about
        column_about=["№","Путь","id_books"]
        print(f'{column_about[0]:<{max_len_id_about}}'+"|"
              +f'{column_about[1]:^{max_len_about}}'+"|"
              +f'{column_about[2]:^{max_len_id_books}}'+"|")
        #вывод таблицы about  
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:{max_len_id_about}}'+"|", end="")
                if j==1:
                    print(f'{all_results[i][j]:{max_len_about}}'+"|", end="")
                if j==2:
                    print(f'{all_results[i][j]:{max_len_id_books}}'+"|", end="")
            print("")
               
#запрос выборки данных таблицы state    
class select_state:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM state;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id состояния
        max_len_id_state=int(0)
        #масимальная длина имени состояния
        max_len_name_state=int(0)
        #масимальная длина страницы состояния
        max_len_page_state=int(0)
        #масимальная длина id_books
        max_len_id_books=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_state:
                max_len_id_state=len(str(all_results[i][0]))
                if max_len_id_state<1:
                    max_len_id_state=1
            if len(str(all_results[i][1]))>max_len_name_state:
                max_len_name_state=len(str(all_results[i][1]))
                if max_len_name_state<9:
                    max_len_name_state=9
            if len(str(all_results[i][2]))>max_len_page_state:
                max_len_page_state=len(str(all_results[i][2]))
                if max_len_page_state<4:
                    max_len_page_state=4
            if len(str(all_results[i][3]))>max_len_id_books:
                max_len_id_books=len(str(all_results[i][3]))
                if max_len_id_books<8:
                    max_len_id_books=8
        #заголовок таблицы state
        column_about=["№","Состояние","Стр.","id_books"]
        print(f'{column_about[0]:<{max_len_id_state}}'+"|"
              +f'{column_about[1]:^{max_len_name_state}}'+"|"
              +f'{column_about[2]:^{max_len_page_state}}'+"|"
              +f'{column_about[3]:^{max_len_id_books}}'+"|")
        #вывод таблицы about 
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{max_len_id_state}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_name_state}}'+"|", end="")
                elif j==2:
                    print(f'{all_results[i][j]:<{max_len_page_state}}'+"|", end="")
                elif j==3:
                    print(f'{all_results[i][j]:<{max_len_id_books}}'+"|", end="")
            print("")
               
#запрос выборки данных таблицы hashtag                 
class select_hashtag:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM hashtag;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id hashtag
        max_len_id_hashtag=int(0)
        #масимальная длина имени hashtag
        max_len_name_hashtag=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_hashtag:
                max_len_id_hashtag=len(str(all_results[i][0]))
                if max_len_id_hashtag<1:
                    max_len_id_hashtag=1
            if len(str(all_results[i][1]))>max_len_name_hashtag:
                max_len_name_hashtag=len(str(all_results[i][1]))
                if max_len_name_hashtag<6:
                    max_len_name_hashtag=6
        #заголовок таблицы hashtag
        column_hashtag=["№","Хэштэг"]
        print(f'{column_hashtag[0]:<{max_len_id_hashtag}}'+"|"
              f'{column_hashtag[1]:^{max_len_name_hashtag}}'+"|")
        #вывод таблицы hashtag 
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{max_len_id_hashtag}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_name_hashtag}}'+"|", end="")
            print("")

#запрос выборки данных таблицы books_id_hashtag 
class select_books_id_hashtag:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM books_id_hashtag;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id books_id_hashtag
        max_len_books_id_hashtag=int(0)
        #масимальная длина id books 
        max_len_id_book=int(0)
        #масимальная длина id hashtag 
        max_len_id_hashtag=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_books_id_hashtag:
                max_len_books_id_hashtag=len(str(all_results[i][0]))
                if max_len_books_id_hashtag<1:
                    max_len_books_id_hashtag=1
            if len(str(all_results[i][1]))>max_len_id_book:
                max_len_id_book=len(str(all_results[i][1]))
                if max_len_id_book<8:
                    max_len_id_book=8
            if len(str(all_results[i][2]))>max_len_id_hashtag:
                max_len_id_hashtag=len(str(all_results[i][2]))
                if max_len_id_hashtag<10:
                    max_len_id_hashtag=10
        #заголовок длина id  hashtag
        column_hashtag=["№","id_books","id_hashtag"]
        print(f'{column_hashtag[0]:<{max_len_books_id_hashtag}}'+"|"+
              f'{column_hashtag[1]:^{max_len_id_book}}'+"|"+
              f'{column_hashtag[2]:^{max_len_id_hashtag}}'+"|")
        #вывод таблицы books_id_hashtag 
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{max_len_books_id_hashtag}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_id_book}}'+"|", end="")
                elif j==2:
                    print(f'{all_results[i][j]:<{max_len_id_hashtag}}'+"|", end="")
            print("")
               
#запрос выборки данных таблицы category                
class select_category:
    def __init__(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT * FROM category;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query)
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id категории
        max_len_id_categ=int(0)
        #масимальная длина названия категории
        max_len_name_categ=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_id_categ:
                max_len_id_categ=len(str(all_results[i][0]))
                if max_len_id_categ<1:
                    max_len_id_categ=1
            if len(str(all_results[i][1]))>max_len_name_categ:
                max_len_name_categ=len(str(all_results[i][1]))
                if max_len_name_categ<9:
                    max_len_name_categ=9
        #заголовок таблицы category
        column_categ=["№","Категория"]
        print(f'{column_categ[0]:<{max_len_id_categ}}'+"|"+f'{column_categ[1]:^{max_len_name_categ}}'+"|")
        #вывод таблицы category 
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{max_len_id_categ}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_name_categ}}'+"|", end="")
            print("")

#запрос выборки данных таблицы notes
class select_notes:
    def __init__(self,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT id_note,text_notes FROM notes WHERE id_book=?;"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query,(id_book,))
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина № notes
        max_len_id_notes = int(0)
        #переменная счетчик записей
        count_row_notes=int(0)
        #переменная для № notes
        num_note=int(1)
        #масимальная длина текста notes
        max_len_text_notes=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][1]))>max_len_text_notes:
                max_len_text_notes=len(str(all_results[i][1]))
                if max_len_text_notes<5:
                    max_len_text_notes=5
                elif max_len_text_notes>50:
                    max_len_text_notes=50
                count_row_notes+=1
        max_len_id_notes = len(str(count_row_notes))
        #заголовок таблицы notes
        column_categ=["№","Текст"]
        print(f'{column_categ[0]:<{max_len_id_notes}}'+"|"+
              f'{column_categ[1]:^{max_len_text_notes}}')
        #переменная для перевода строки
        enter_str=0
        #вывод таблицы notes
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{num_note:<{max_len_id_notes}}'+"|", end="")
                    num_note+=1
                elif j==1:
                    new_str=str(all_results[i][j])
                    for k in new_str:
                        print(k,end="")
                        enter_str+=1
                        if enter_str==150:
                            print("")
                            print("",end="")
                            enter_str=0
            enter_str=0     
            print("")
               
#запрос выборки данных таблицы books_id_author
class select_books_id_author:
    def __init__(self,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        id_book=int(id_book)
        self.query="""SELECT A.surname,A.name,A.patr
                       FROM author AS A JOIN books_id_author AS BA
                       ON A.id_author=BA.id_author
                       WHERE BA.id_book = ?;"""
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query,(id_book,))
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id автора 
        max_len_id_author=int(0)
        #переменная для нумерации строк авторов
        count_author = 1
        #масимальная длина фамилии автора 
        max_len_surname_author=int(0)
        #переменная счетчик записей
        count_row_author=int(0)
        #масимальная длина имени автора 
        max_len_name_author=int(0)
        #масимальная длина отчества автора 
        max_len_patr_author=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_surname_author:
                max_len_surname_author=len(str(all_results[i][0]))
                if max_len_surname_author<7:
                    max_len_surname_author=7
            if len(str(all_results[i][1]))>max_len_name_author:
                max_len_name_author=len(str(all_results[i][1]))
                if max_len_name_author<3:
                    max_len_name_author=3
            if len(str(all_results[i][2]))>max_len_patr_author:
                max_len_patr_author=len(str(all_results[i][2]))
                if max_len_patr_author<8:
                    max_len_patr_author=8
            count_row_author+=1
        max_len_id_author=len(str(count_row_author))
        #заголовок таблицы select_books_id_author
        column_books_id_author=["№","Фамилия","Имя","Отчество"]
        print(f'{column_books_id_author[0]:<{max_len_id_author}}'+"|"+
              f'{column_books_id_author[1]:^{max_len_surname_author}}'+"|"
              f'{column_books_id_author[2]:^{max_len_name_author}}'+"|"
              f'{column_books_id_author[3]:^{max_len_patr_author}}'+"|")
        #вывод таблицы select_books_id_author
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{count_author:<{max_len_id_author}}'+"|",end="")
                    print(f'{all_results[i][j]:<{max_len_surname_author}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{max_len_name_author}}'+"|", end="")
                elif j==2:
                    print(f'{all_results[i][j]:<{max_len_patr_author}}'+"|", end="")
            count_author+=1
            print("")

#запрос выборки данных таблицы books_id_hashtag
class select_books_id_hashtag:
    def __init__(self,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        id_book=int(id_book)
        self.query="""SELECT H.name
                       FROM hashtag AS H JOIN books_id_hashtag AS BH
                       ON H.id_hashtag=BH.id_hashtag
                       WHERE BH.id_book = ?;"""
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query,(id_book,))
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id хэштэга
        max_id_hashtag=int(0)
        #переменная счетчик записей
        count_row_hashtag=int(0)
        #переменная для нумерации строк хэштэгов
        count_hashtag = int(1)
        #масимальная длина названия хэштэга
        max_len_hashtag=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>max_len_hashtag:
                max_len_hashtag=len(str(all_results[i][0]))
                if max_len_hashtag<6:
                    max_len_hashtag=6
            count_row_hashtag+=1
        max_id_hashtag=len(str(count_row_hashtag))
        #заголовок таблицы select_books_id_hashtag
        column_books_id_author=["№","Хэштэг"]
        print(f'{column_books_id_author[0]:<{max_id_hashtag}}'+"|"+
              f'{column_books_id_author[1]:^{max_len_hashtag}}'+"|")
        #вывод таблицы select_books_id_hashtag
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{count_hashtag:<2}'+"|",end="")
                    print(f'{all_results[i][j]:<{max_len_hashtag}}'+"|", end="")
            count_hashtag+=1
            print("")
