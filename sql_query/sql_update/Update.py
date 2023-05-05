import sqlite3
#запрос изменения прогресса состояния чтения
class update_state_progress:
    def __init__(self,progress,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        query="""UPDATE state SET name = ?
                 WHERE id_book= ?;"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query,(progress,id_book))
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
          
#запрос изменения страницы состояния чтения          
class update_state_page:
    def __init__(self,page,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        query="""UPDATE state SET page = ?
                 WHERE id_book = ?;"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query,(page,id_book))
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
          
#запрос изменения пути к книге
class update_about_path:
    def __init__(self,path,id_book):
        f=open('settings.txt','r')
        name_NDB=f.read()
        f.close()
        self.sqlite_connection=sqlite3.connect(name_NDB)
        query="""UPDATE about SET path = ?
                 WHERE id_book = ?;"""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(query,(path,id_book))
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
