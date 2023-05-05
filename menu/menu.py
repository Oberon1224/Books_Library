import os
from .menu_books import*
from .menu_db import*

def menu(): 
    print("***Добро пожаловать в карманную библиотеку***")
    while True:
        if os.path.isfile('settings.txt'):
            f_n=open('settings.txt','r')
            print("Выбранная база данных: ", f_n.read())
            f_n.close()
        else:
            print("База данных не выбрана")
        print("____________________Меню_____________________")
        print("Выберите пункт:")
        print("1 - Работа с книгой")
        print("2 - Работа с базой данных")
        print("3 - Выход")
        print("_____________________________________________")
        choise = str(input())
        
        # выбор пункта 1 - меню работы с книгами
        if choise =='1':
            menu_books()
            
        # выбор пункта 2 - меню работы с базой данных  
        if choise=='2':
            menu_db()
        # выбор пункта 3 - выход из программы  
        if choise =='3':
            break