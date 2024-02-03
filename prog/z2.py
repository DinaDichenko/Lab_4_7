#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. 
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 оранжевый, #ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.
"""
from tkinter import *

def colors(argument:str):
    match argument:
        case 'red':
            lab['text'] = 'красный'
            ent.delete(0, END)
            ent.insert(0, '#ff0000')
        case 'orange':
            lab['text'] = 'оранжевый'
            ent.delete(0, END)
            ent.insert(0, '#ff7d00')
        case 'yellow':
            lab['text'] = 'желтый'
            ent.delete(0, END)
            ent.insert(0, '#ffff00')
        case 'green':
            lab['text'] = 'зеленый'
            ent.delete(0, END)
            ent.insert(0, '#00ff00')
        case 'blue':
            lab['text'] = 'голубой'
            ent.delete(0, END)
            ent.insert(0, '#007dff')
        case 'dark_blue':
            lab['text'] = 'синий'
            ent.delete(0, END)
            ent.insert(0, '#0000ff')
        case 'violet':
            lab['text'] = 'фиолетовый'
            ent.delete(0, END)
            ent.insert(0, '#7d00ff')

root = Tk()

ent = Entry(width=20)
ent.pack()
lab = Label(width=20, bg='grey', fg='white')
lab.pack()

Button(root, bg='#ff0000', command=lambda: colors('red')).pack(fill=X)
Button(root, bg='#ff7d00', command=lambda: colors('orange')).pack(fill=X)
Button(root, bg='#ffff00', command=lambda: colors('yellow')).pack(fill=X)
Button(root, bg='#00ff00', command=lambda: colors('green')).pack(fill=X)
Button(root, bg='#007dff', command=lambda: colors('blue')).pack(fill=X)
Button(root, bg='#0000ff', command=lambda: colors('dark_blue')).pack(fill=X)
Button(root, bg='#7d00ff', command=lambda: colors('violet')).pack(fill=X)

root.mainloop()

