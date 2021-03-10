#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:08:29 2021

@author: thierry
"""

from tkinter import Tk
from tkinter import Toplevel


root = Tk()

fen = Toplevel(root)
fen.withdraw()

root.mainloop()



# from tkinter import Text
# from tkinter import Tk
# from tkinter import Button

# def delete():
#     txt.delete("1.0", "end-1c")
#     txt.insert()

# win =Tk()
# txt = Text(win)
# txt.insert("1.0", "hgjygyjgjy")
# but = Button(win, text = "Effacer", command=delete )

# txt.pack()
# but.pack()



# win.mainloop()

# dico = {"a":1, "b":2, "c":3}
# print(dico)
# dico1 = {}
# with open("file.txt", "r") as file:
#     dico = file.readline()
#     char = "{},':\""
#     for character in char:
#         dico = dico.replace(character,"")
#     dico = dico.split()
#     i=0
#     while i < len(dico) -1:
#         dico1[dico[i]] = dico[i+1]
#         i += 2

# dico2 = {}
# string = "{'A': '00', 'T': '01', 'C': '010', 'G': '100', 'N': '110', '$': '111'}"
# char = " {}'\""
# for character in char:
#     string = string.replace(character,"")
#     print(string)
# string = string.split(",")
# print(string)
# i=0
# while i < len(string):
#     dico2[string[i].split(":")[0]] = string[i].split(":")[1]
#     i += 1
# print(dico2)
# for k, v in dico2.items():
#     print(k)
#     print(v)

# s = "o\x1e"
# s = s.encode("utf-8")
# print(s.decode())

string = ""
a = "bonjour"
b = "salut"
liste = ["votre a => " + a, "votre b => " + b, "jyfyfy"]
string = liste[0:-1]
print(string)





  