# File Manager
## My python project


Ru
### Немного о создании
Создан на PyQT5. Цель проекта - что можно сделать на этой библиотеке.
Цель к сожалению не была выполнена, в связи с маленькими сроками, 
я неуспел все вовремя. 

### Описание проекта
Проект представляет из себя 2 работоспособные программы: 
1. Текстовый редактор. Способен запускать питонские файлы,
и работать сразу с несколькими файлами (вкладки)
2. Сжатие изображений. Уменьшает качество изображения, сохраняя пропорции.
3. Просмотр STL моделей. Планировалась, но не была реализована (сроки)

Все библиотеки, необходимые для работы программ, записаны в файле requirements.txt


### Небольшое описание к файлам
`main.py` - главный файл, для старта работы запускать необходимо его
`active_lang.py` - файл в котором записаны все названия (планировалась смена языка)
`image_edit.py` - сжатие изображений
`text_manager.py` - текстовый редактор
`newfile.py` - окно создания файла
`doc.txt` - документация к функциям и переменным в файлах, для __продвинутых пользователей__

В процессе работы с файлами, программа может создать файлы `temp.py` и `temp.txt` - 
через эти файлы программа передает данные, по закрытию программы они будут удалены.

Окно создания файла можно было сделать через **`QInputDialog`**, но меня устроил
вариант со своим окном

### Установка

Для обычного использования можно скачать только файл `FileManager.exe`

Если вам нужно сплагиатить мой код, то - все файлы вы найдете в папке `src`

Все необходимые библиотеки написаны в `requirements.txt`

Чтобы сразу их установить вы можете написать в терминал:

'''
pip install > requirements.txt
'''

После нужно запустить файл `main.py`


En
### About creating
Created on PyQt5. The goal of the project is what can be done on this library.
Unfortunately, the goal was not fulfilled, due to the short deadlines, 
I failed everything in time. 

### Project Description
The project consists of 2 workable programs: 
1. Text editor. Able to run python files,
and work with multiple files at once (tabs)
2. Image compression. Reduces the image quality while maintaining the proportions.
3. View STL models. Planned, but not implemented (deadlines)

All libraries necessary for the operation of programs are written in a file requirements.txt


### A short description of the files
`main.py ` is the main file, you need to run it to start the work
`active_lang.py ` - a file in which all the names are recorded (a language change was planned)
`image_edit.py ` - image compression
`text_manager.py ` - text editor
`newfile.py ` - file creation window
`doc.txt ` - documentation for functions and variables in files, for __advanced users__

In the process of working with files, the program can create files `temp.py ` and `temp.txt ` -
the program transmits data through these files, they will be deleted when the program is closed.

The file creation window could be done via **`QInputDialog`**, but I was satisfied
with the option with my own window

### Installation

For normal use, you can download only the file `FileManager.exe `

If you need to plagiarize my code, then - you will find all the files in the `src` folder

All necessary libraries are written in `requirements.txt `

To install them immediately, you can write to the terminal:

'''
pip install > requirements.txt
'''

Then you need to run the file `main.py `
