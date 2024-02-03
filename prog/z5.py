#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
виджеты Radiobatton и Checkbutton поддерживают большинство свойств оформления внешнего вида, которые есть у других элементов графического интерфейса. 
При этом у Radiobutton есть особое свойство indicatoron . По-умолчанию он равен единице, в этом случае радиокнопка выглядит как нормальная радиокнопка. 
Однако если присвоить этой опции ноль, то виджет Radiobutton становится похожим на обычную кнопку по внешнему виду. Но не по смыслу. 
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок, индикатор которых выключен ( indicatoron=0 ). 
Если какая-нибудь кнопка включается, то в метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть не должно.
"""
from tkinter import *

def change_button(argument:str):
    match argument:
        case 'up':
            lab['text'] = '+7 9182347684'
        case 'middle':
            lab['text'] = '+7 9583456149'
        case 'down':
            lab['text'] = '+7 9084512783'

root = Tk()

frame = Frame()
frame.pack(side=LEFT, fill=Y)

var = IntVar()
var.set(0)
Radiobutton(frame, text="Вася", command=lambda: change_button('up'), width=15, variable=var, value=0, indicatoron=0).pack()
Radiobutton(frame, text="Петя", command=lambda: change_button('middle'), width=15, variable=var, value=1, indicatoron=0).pack()
Radiobutton(frame, text="Миша", command=lambda: change_button('down'), width=15, variable=var, value=2, indicatoron=0).pack()

lab = Label(width=30, height=5, bg='white')
lab.pack(side=RIGHT)

root.mainloop()
