# Books_Library 📚
 It is a database for storing books
* [Manual](#manual) 
  * [Introduction](#introduction)
    * [Program menu](#program-menu)
  * [Instruction](#instruction)
    * [Create or select database](#create-or-select-database)
    * [Insert into database](#insert-into-database)
    * [Select from database](#select-from-database)
    * [Search in database](#search-in-database)
    * [Work with a book](#work-with-a-book)
  * [Database structure](#database-structure)
    * [Table relationships](#table-relationships)
    
# Manual
### Introduction
 #### Program menu structure:
 ![Program_menu](https://user-images.githubusercontent.com/73591672/236629303-a3dc0bde-8c92-4720-b700-11ae692d54f8.jpg)

### Instruction
  #### Create or select database
  If you want create database you must select in main menu "2 - Работа с базой данных"➡"1 - Создать новую базу данных"(name database necessery enter without extention .dbo) and if you want change database you must select in main menu "2 - Работа с базой данных"➡"2 - Выбрать другую базу данных" (name database necessery enter with extention .dbo)
  #### Insert into database
  If you want insert information in database you must select necessary item:
  ##### ---to add an author go in main menu ➡ "2 - Добавление данных" ➡ "1 - Автор"  ➡ "2 - Добавить автора"
  ##### ---to add an language go in main menu ➡ "2 - Добавление данных" ➡ "2 - Язык"  ➡ "2 - Добавить язык"
  ##### ---to add an category go in main menu ➡ "2 - Добавление данных" ➡ "3 - Категория"  ➡ "2 - Добавить категорию"
  ##### ---to add an hashtag go in main menu ➡ "2 - Добавление данных" ➡ "4 - Хэштэг"  ➡ "2 - Добавить хэштэш"
  ##### ---to add an year go in main menu ➡ "2 - Добавление данных" ➡ "5 - Год"  ➡ "2 - Добавить год"
  ##### ---to add an book go in main menu ➡ "2 - Добавление данных" ➡ "6 - Книга"  ➡ "2 - Добавить книгу"
  ##### Before add books in databse you must add other information necessery for books. 
  ##### Redundancy is eliminated in the database - when you enter a value, it will not be added. 
  #### Select from database
 
  ##### If you want see information from database you must select necessary item:
  ##### ---to see an all  books in reading  go in main menu ➡ "1 - Найти книгу" ➡ "5 - Показать книги на чтении"
  ##### ---to see an all readed books go in main menu ➡ "1 - Найти книгу" ➡ "6 - Показать прочитанные книги"
  ##### ---to see an all authors go in main menu ➡ "2 - Добавление данных" ➡ "1 - Автор"  ➡ "1 - Показать всех авторов"
  ##### ---to see an all language go in main menu ➡ "2 - Добавление данных" ➡ "2 - Язык"  ➡ "2 - Показать все язык"
  ##### ---to see an all category go in main menu ➡ "2 - Добавление данных" ➡ "3 - Категория"  ➡ "2 - Показать все категории"
  ##### ---to see an all hashtag go in main menu ➡ "2 - Добавление данных" ➡ "4 - Хэштэг"  ➡ "2 - Показать все хэштэги"
  ##### ---to see an all year go in main menu ➡ "2 - Добавление данных" ➡ "5 - Год"  ➡ "2 - Показать все года"
  ##### ---to see an all book go in main menu ➡ "2 - Добавление данных" ➡ "6 - Книга"  ➡ "2 - Показать все книги"
  
  
  #### Search in database
  ##### Search books in database making by four criterions:
  ##### 1. by title: main menu ➡ "1 - Найти книгу" ➡ "1 - Найти книгу по названию"
  ##### 2. by author: main menu ➡ "1 - Найти книгу" ➡ "2 - Найти книгу по автору"
  ##### 3. by category: main menu ➡ "1 - Найти книгу" ➡ "3 - Найти книгу по категории"
  ##### 4. by hashtag: main menu ➡ "1 - Найти книгу" ➡ "1 - Найти книгу по хэштэгу"
  
  
  #### Work with a book
  ##### For work in books program have next features:
  ##### ---open book (before open book you must add path for book selecting item "6 - Указать путь к файлу книге")
  ##### ---add notes and watching notes
  ##### ---update page books and state reading (if page more than one  - books is reading, if state name "Прочитано" book readed)
  ##### ---add and wathcing author in book (when adding author you must be sure in database having this author, else author not adding. The same rule when adding a hashtag)
  ##### ---add and wathcing hashtag in book

### Database structure
  #### Table relationships:
  ![Database_structure](https://user-images.githubusercontent.com/73591672/236622989-ae5acf5b-dc85-4ae9-8f5c-efb1f93b10e7.jpg)


