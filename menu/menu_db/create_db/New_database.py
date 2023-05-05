import sqlite3
from .View_Books import*

class new_database:
    def __init__(self,name_NDB):
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.table_books_id_author()
        self.table_author()
        self.table_books()
        self.table_year()
        self.table_language()
        self.table_about()
        self.table_notes()
        self.table_state()
        self.table_category()
        self.table_hashtag()
        self.table_books_id_hashtag()
        self.view_books=View_Books()
        self.sqlite_connection.close()
          
    #функция создания таблицы books
    def table_books(self):
        query="""CREATE TABLE books
                  (id_book INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                   title TEXT NOT NULL,
                   page INTEGER NULL,
                   id_year INTEGER,
                   id_language INTEGER,
                   id_about INTEGER,
                   id_state INTEGER,
                   id_category INTEGER,
                   FOREIGN KEY (id_year) REFERENCES year(id_year),
                   FOREIGN KEY (id_language) REFERENCES language(id_language),
                   FOREIGN KEY (id_about) REFERENCES about(id_about),
                   FOREIGN KEY (id_state) REFERENCES state(id_state),
                   FOREIGN KEY (id_category) REFERENCES category(id_category));"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы author
    def table_author(self):
        query="""CREATE TABLE author
                 (id_author INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                  surname TEXTNULL,
                  name TEXT NULL,
                  patr TEXT NULL);"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы year
    def table_year(self):
        query="""CREATE TABLE year
                 (id_year INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                  year TEXT NULL);"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()
          
    #функция создания таблицы language      
    def table_language(self):
        query="""CREATE TABLE language
                 (id_language INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                  name TEXT NULL);"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы about 
    def table_about(self):
        query="""CREATE TABLE about
                 (id_ab INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                  path TEXT NULL,
                  id_book INTEGER NOT NULL,
                  FOREIGN KEY(id_book) REFERENCES books(id_book));"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы notes 
    def table_notes(self):
        query="""CREATE TABLE notes
                 (id_note INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                  text_notes TEXT NULL,
                  id_book INTEGER NOT NULL,
                  FOREIGN KEY(id_book) REFERENCES books(id_book));"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы state 
    def table_state(self):
        query="""CREATE TABLE state
                 (id_state INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                 name TEXT NULL,
                 page TEXT NULL,
                 id_book INTEGER NOT NULL,
                 FOREIGN KEY(id_book) REFERENCES books(id_book));"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы category 
    def table_category(self):
        query="""CREATE TABLE category
                 (id_category INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                 name TEXT NULL);"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы hashtag         
    def table_hashtag(self):
        query="""CREATE TABLE hashtag
                  (id_hashtag INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                   name TEXT NULL);"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы books_id_hashtag  
    def table_books_id_hashtag(self):
        query="""CREATE TABLE books_id_hashtag
                  (id_books_hashtag INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                   id_hashtag INTEGER NOT NULL,
                   id_book INTEGER NOT NULL,
                   FOREIGN KEY(id_book) REFERENCES books(id_book),
                   FOREIGN KEY(id_hashtag) REFERENCES hashtag(id_hashtag));"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()

    #функция создания таблицы books_id_author 
    def table_books_id_author(self):
        query="""CREATE TABLE books_id_author
                 (id_books_author INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                  id_author INTEGER NOT NULL,
                  id_book INTEGER NOT NULL,
                  FOREIGN KEY(id_book) REFERENCES books(id_book),
                  FOREIGN KEY(id_author) REFERENCES author(id_author));"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query)
        self.sqlite_connection.commit()
