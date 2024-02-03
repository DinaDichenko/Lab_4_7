#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
напишите программу, состоящую из однострочного и многострочного текстовых полей и двух кнопок "Открыть" и "Сохранить". 
При клике на первую должен открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла должно загружаться в поле типа Text . 
При клике на вторую кнопку текст, введенный пользователем в экземпляр Text , должен сохраняться в файле под именем, которое пользователь указал в однострочном текстовом поле. 
Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если указывать имена файлов без адреса. 
Для выполнения практической работы вам понадобится функция open языка Python и методы файловых объектов чтения и записи. 
Освежить знания о файлах можно из материала лабораторной работы 9
"""
from tkinter import *


def open_file():
    try:
        name = ent.get()
        with open(name, "r", encoding="utf-8") as f:
            content = f.read()
            text.delete(1.0, END)
            text.insert(1.0, content)
    except FileNotFoundError:
        text.delete(1.0, END)
        text.insert(1.0, "Файл не найден")


def save_file():
    try:
        name = ent.get()
        content = text.get(1.0, END)
        with open(name, "w") as f:
            f.write(content)
    except FileNotFoundError:
        text.delete(1.0, END)
        text.insert(1.0, "Сохранить не удалось")


root = Tk()

frame = Frame()
frame.pack()
ent = Entry(frame, width=30)
ent.pack(side=LEFT)
Button(frame, text="Открыть", command=open_file).pack(side=LEFT)
Button(frame, text="Сохранить", command=save_file).pack(side=LEFT)

text = Text(width=30)
text.pack(fill=X)

root.mainloop()
