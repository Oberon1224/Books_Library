#Copyright 2023 Bushuev Dmitrii
import sqlite3

#запрос выборки представления view_books
class select_view_search:
    def __init__(self,choise,name="NULL"):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        word_search=f'%{name}%'
        self.sqlite_connection=sqlite3.connect(name_NDB)
          
        #поиск по названию книги
        if choise =='1':
            self.query="SELECT * FROM view_books WHERE title LIKE ?;"
            cursor=self.sqlite_connection.cursor()
            cursor.execute(self.query,(word_search,))
            
        #поиск по фамилии автора книги
        elif choise =='2':
            self.query="""SELECT * FROM view_books AS vb                            
                            WHERE vb.id_book IN
                            (SELECT ba.id_book FROM books_id_author AS ba 
                            JOIN author as a ON ba.id_author=a.id_author
                            WHERE a.surname LIKE ?);"""
            cursor=self.sqlite_connection.cursor()
            cursor.execute(self.query,(word_search,))
            
        #поиск по категории книги
        elif choise =='3':
            self.query="""SELECT * FROM view_books 
                            WHERE id_book IN
                            (SELECT id_book FROM books AS B
                            JOIN category AS C ON B.id_category = C.id_category
                            WHERE C.name LIKE ?);"""
            cursor=self.sqlite_connection.cursor()
            cursor.execute(self.query,(word_search,))
            
        #поиск по фамилии хэштэгу книги
        elif choise =='4':
            self.query="""SELECT * FROM view_books AS vb                            
                            WHERE vb.id_book IN
                            (SELECT bh.id_book FROM books_id_hashtag AS bh
                            JOIN hashtag as h ON bh.id_hashtag=h.id_hashtag
                            WHERE h.name LIKE ?);"""
            cursor=self.sqlite_connection.cursor()
            cursor.execute(self.query,(word_search,))
            
        #вывод книг на чтении
        elif choise =='5':
            self.query="SELECT * FROM view_read"
            cursor=self.sqlite_connection.cursor()
            cursor.execute(self.query)
            
        #вывод прочитанных книг
        elif choise =='6':
            self.query="SELECT * FROM view_read_finish"
            cursor=self.sqlite_connection.cursor()
            cursor.execute(self.query) 
           
        all_results=cursor.fetchall()
        self.sqlite_connection.close()
        #масимальная длина id книги
        vbook_max_len_id=int(0)
        #масимальная длина названия книги
        vbook_max_len_bookname=int(0)
        #масимальная длина количества страниц
        vbook_max_len_page=int(0)
        #масимальная длина значения года
        vbook_max_len_year=int(0)
        #масимальная длина названия языка
        vbook_max_len_lang=int(0)
        #масимальная длина пути справки
        vbook_max_len_about=int(0)
        #масимальная длина названия состояния
        vbook_max_len_statename=int(0)
        #масимальная длина страницы состояния
        vbook_max_len_statepage=int(0)
        #масимальная длина названия категории
        vbook_max_len_categname=int(0)
        for i in range(len(all_results)):
            if len(str(all_results[i][0]))>vbook_max_len_id:
                vbook_max_len_id=len(str(all_results[i][0]))
                if vbook_max_len_id<1:
                    vbook_max_len_id=1                
            if len(str(all_results[i][1]))>vbook_max_len_bookname:
                vbook_max_len_bookname=len(str(all_results[i][1]))
                if vbook_max_len_bookname<11:
                    vbook_max_len_bookname=11
            if len(str(all_results[i][2]))>vbook_max_len_page:
                vbook_max_len_page=len(str(all_results[i][2]))
                if vbook_max_len_page<11:
                    vbook_max_len_page=11 
            if len(str(all_results[i][3]))>vbook_max_len_year:
                vbook_max_len_year=len(str(all_results[i][3]))
                if vbook_max_len_year<3:
                    vbook_max_len_year=3
            if len(str(all_results[i][4]))>vbook_max_len_lang:
                vbook_max_len_lang=len(str(all_results[i][4]))
                if vbook_max_len_lang<4:
                    vbook_max_len_lang=4
            if len(str(all_results[i][5]))>vbook_max_len_about:
                vbook_max_len_about=len(str(all_results[i][5]))
                if vbook_max_len_about<4:
                    vbook_max_len_about=4
            if len(str(all_results[i][6]))>vbook_max_len_statename:
                vbook_max_len_statename=len(str(all_results[i][6]))
                if vbook_max_len_statename<9:
                    vbook_max_len_statename=9
            if len(str(all_results[i][7]))>vbook_max_len_statepage:
                vbook_max_len_statepage=len(str(all_results[i][7]))
                if vbook_max_len_statepage<9:
                     vbook_max_len_statepage=9
            if len(str(all_results[i][8]))>vbook_max_len_categname:
                vbook_max_len_categname=len(str(all_results[i][8]))
                if vbook_max_len_categname<9:
                     vbook_max_len_categname=9

          #заголовок представления view_books
        column_vbooks=["№","Назв. книги","Кол-во стр.",
                       "Год","Язык","Путь","Состояние","Посл стр.","Категория"]
        print(f'{column_vbooks[0]:<{vbook_max_len_id}}'+"|"+
        f'{column_vbooks[1]:^{vbook_max_len_bookname}}'+"|"+
        f'{column_vbooks[2]:^{vbook_max_len_page}}'+"|"+
        f'{column_vbooks[3]:^{vbook_max_len_year}}'+"|"+
        f'{column_vbooks[4]:^{vbook_max_len_lang}}'+"|"+
        f'{column_vbooks[5]:^{vbook_max_len_about}}'+"|"+
        f'{column_vbooks[6]:^{vbook_max_len_statename}}'+"|"+
        f'{column_vbooks[7]:^{vbook_max_len_statepage}}'+"|"+
        f'{column_vbooks[8]:^{vbook_max_len_categname}}'+"|")
        #вывод представления view_books                
        for i in range(len(all_results)):
            for j in range(len(all_results[i])):
                if j==0:
                    print(f'{all_results[i][j]:<{vbook_max_len_id}}'+"|", end="")
                elif j==1:
                    print(f'{all_results[i][j]:<{vbook_max_len_bookname}}'+"|", end="")
                elif j==2:
                    print(f'{all_results[i][j]:<{vbook_max_len_page}}'+"|", end="")
                elif j==3:
                    print(f'{all_results[i][j]:<{vbook_max_len_year}}'+"|", end="")
                elif j==4:
                    print(f'{all_results[i][j]:<{vbook_max_len_lang}}'+"|", end="")
                elif j==5:
                    print(f'{all_results[i][j]:<{vbook_max_len_about}}'+"|", end="")
                elif j==6:
                    print(f'{all_results[i][j]:<{vbook_max_len_statename}}'+"|", end="")
                elif j==7:
                    print(f'{all_results[i][j]:<{vbook_max_len_statepage}}'+"|", end="")
                elif j==8:
                    print(f'{all_results[i][j]:<{vbook_max_len_categname}}'+"|", end="")
            print("")
