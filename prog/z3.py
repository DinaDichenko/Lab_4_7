#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
перепишите программу из пункта 8 так, чтобы интерфейс выглядел примерно следующим образом
"""
from tkinter import *


def colors(argument: str):
    match argument:
        case "red":
            lab["text"] = "красный"
            ent.delete(0, END)
            ent.insert(0, "#ff0000")
        case "orange":
            lab["text"] = "оранжевый"
            ent.delete(0, END)
            ent.insert(0, "#ff7d00")
        case "yellow":
            lab["text"] = "желтый"
            ent.delete(0, END)
            ent.insert(0, "#ffff00")
        case "green":
            lab["text"] = "зеленый"
            ent.delete(0, END)
            ent.insert(0, "#00ff00")
        case "blue":
            lab["text"] = "голубой"
            ent.delete(0, END)
            ent.insert(0, "#007dff")
        case "dark_blue":
            lab["text"] = "синий"
            ent.delete(0, END)
            ent.insert(0, "#0000ff")
        case "violet":
            lab["text"] = "фиолетовый"
            ent.delete(0, END)
            ent.insert(0, "#7d00ff")


root = Tk()

lab = Label(width=20, bg="grey", fg="white")
lab.pack()

ent = Entry(width=20)
ent.pack()


Button(root, bg="#ff0000", command=lambda: colors("red")).pack(
    side=LEFT, fill="both", expand=True
)
Button(root, bg="#ff7d00", command=lambda: colors("orange")).pack(
    side=LEFT, fill="both", expand=True
)
Button(root, bg="#ffff00", command=lambda: colors("yellow")).pack(
    side=LEFT, fill="both", expand=True
)
Button(root, bg="#00ff00", command=lambda: colors("green")).pack(
    side=LEFT, fill="both", expand=True
)
Button(root, bg="#007dff", command=lambda: colors("blue")).pack(
    side=LEFT, fill="both", expand=True
)
Button(root, bg="#0000ff", command=lambda: colors("dark_blue")).pack(
    side=LEFT, fill="both", expand=True
)
Button(root, bg="#7d00ff", command=lambda: colors("violet")).pack(
    side=LEFT, fill="both", expand=True
)

root.mainloop()
