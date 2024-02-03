#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
напишите простейший калькулятор, состоящий из двух текстовых полей, куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". 
Результат вычисления должен отображаться в метке. Если арифметическое действие выполнить невозможно (например, если были введены буквы, а не числа), 
то в метке должно появляться слово "ошибка".
"""
from tkinter import *


def sum_of_numbers(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        result = a + b
        lab["text"] = result
    except ValueError:
        lab["text"] = "Ошибка"


def sub_of_numbers(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        result = a - b
        lab["text"] = result
    except ValueError:
        lab["text"] = "Ошибка"


def mul_of_numbers(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        result = a * b
        lab["text"] = result
    except ValueError:
        lab["text"] = "Ошибка"


def div_of_numbers(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        if b == 0:
            lab["text"] = "Деление на ноль невозможно"
        else:
            result = a / b
            lab["text"] = result
    except ValueError:
        lab["text"] = "Ошибка"


root = Tk()

ent1 = Entry(width=20)
ent2 = Entry(width=20)
but1 = Button(text="+")
but2 = Button(text="-")
but3 = Button(text="*")
but4 = Button(text="/")
lab = Label(width=20, bg="black", fg="white")

but1.bind("<Button-1>", sum_of_numbers)
but2.bind("<Button-1>", sub_of_numbers)
but3.bind("<Button-1>", mul_of_numbers)
but4.bind("<Button-1>", div_of_numbers)

ent1.pack()
ent2.pack()
but1.pack(fill=X)
but2.pack(fill=X)
but3.pack(fill=X)
but4.pack(fill=X)
lab.pack()

root.mainloop()
