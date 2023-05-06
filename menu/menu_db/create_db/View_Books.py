#Copyright 2023 Bushuev Dmitrii
import sqlite3

class View_Books:
    def __init__(self):
        self.view_books()
        self.view_read()
        self.view_read_finish()
          
    #функция удаления представлений из базы данных
    def view_drop(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        query1="DROP VIEW view_books;"
        query2="DROP VIEW view_read;"
        query3="DROP VIEW view_read_finish;"
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query1)
        cursor.execute(query2)
        cursor.execute(query3)
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
          
    #функция создания представления view_books    
    def view_books(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        query="""CREATE VIEW  view_books AS
                  SELECT B1.id_book, B1.title,B1.page,
                  Y1.year, L1.name, A2.path, S1.name, S1.page,
                  C1.name
                  FROM books AS B1
                  JOIN year AS Y1 ON B1.id_year=Y1.id_year
                  JOIN language AS L1 ON B1.id_language = L1.id_language
                  JOIN about AS A2 ON B1.id_about = A2.id_ab
                  JOIN state AS S1 ON B1.id_state=S1.id_state
                  JOIN category AS C1 ON B1.id_category=C1.id_category"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
          
    #функция создания представления view_read        
    def view_read(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        query="""CREATE VIEW  view_read AS
                 SELECT B1.id_book, B1.title,B1.page,
                 Y1.year, L1.name, A2.path, S1.name, S1.page,
                 C1.name
                 FROM books AS B1
                 JOIN year AS Y1 ON B1.id_year=Y1.id_year
                 JOIN language AS L1 ON B1.id_language = L1.id_language
                 JOIN about AS A2 ON B1.id_about = A2.id_ab
                 JOIN state AS S1 ON B1.id_state=S1.id_state
                 JOIN category AS C1 ON B1.id_category=C1.id_category
                 WHERE S1.name NOT LIKE 'Прочитано' 
                 AND S1.page>1"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
          
    #функция создания представления view_read_finish        
    def view_read_finish(self):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        query="""CREATE VIEW  view_read_finish AS
                 SELECT B1.id_book, B1.title,B1.page,
                 Y1.year, L1.name, A2.path, S1.name, S1.page,
                 C1.name
                 FROM books AS B1
                 JOIN year AS Y1 ON B1.id_year=Y1.id_year
                 JOIN language AS L1 ON B1.id_language = L1.id_language
                 JOIN about AS A2 ON B1.id_about = A2.id_ab
                 JOIN state AS S1 ON B1.id_state=S1.id_state
                 JOIN category AS C1 ON B1.id_category=C1.id_category
                 WHERE S1.name LIKE 'Прочитано'"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
