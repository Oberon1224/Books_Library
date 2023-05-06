#Copyright 2023 Bushuev Dmitrii
import os
import webbrowser
import sqlite3
import sys
sys.path.append(sys.path[0])

class Open_Book:
    def __init__(self,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        self.query="SELECT path FROM view_books WHERE id_book = ?"
        cursor=self.sqlite_connection.cursor()
        cursor.execute(self.query,(id_book,))
        all_results=cursor.fetchone()
        self.sqlite_connection.close()
        os.system(all_results[0])
