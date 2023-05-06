#Copyright 2023 Bushuev Dmitrii
from .create_db.New_database import new_database

def menu_db():
    while True:
        print("___________Работа с базой данных____________")
        print("Выберите пункт:")
        print("1 - Создать новую базу данных")
        print("2 - Выбрать другую базу данных")
        print("3 - Вернуться в меню")
        choise = str(input())
        
        if choise=='1':
            name_NDB = str(input("Введите название базы данных:"))
            name_NDB+='.dbo'
            f=open('settings.txt','w')
            f.write(name_NDB)
            f.close()
            NEW_DB=new_database(name_NDB)
            
        elif choise=='2':
            name_NDB = str(input("Введите название базы данных:"))
            f=open('settings.txt','w')
            f.write(name_NDB)
            f.close()
            
        elif choise=='3':
            break
