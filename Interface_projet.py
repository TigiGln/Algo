# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:44:27 2021

@author: Thierry et Diana
"""
#ACTTGATC

from BWT import cryptage
from tkinter import Tk, Label, Button, Text

# def change_color():
#     entry.tag_add('red', '1.1')
#     entry.tag_add('red', '1.4'

def valide():
    """
    Permet de lancer l'analyse de cryptage de la séquence donnée'
    """
    global liste_pattern, liste_pattern2, bwt
    liste_pattern, liste_pattern2, bwt = cryptage(ent.get("1.0", "end-1c"))
    but.configure(text = "Suivant", command = suivant)
    return liste_pattern, liste_pattern2, bwt

def suivant():
    """
    Permet de faire l'affichage du cryptage de la séquence d'intérêt
    """
    global compteur, liste_pattern, liste_pattern2, bwt, string
    if compteur == len(liste_pattern):
        lab.configure(fg = "blue", wraplength = (compteur-2)*10)
        lab["text"] = liste_pattern2
        but.configure(text = "Terminé", command= "" )
        lab2["text"] = bwt
    else:
        lab["text"] += liste_pattern[compteur] + "\n"
        
        
    compteur += 1


sequence =""

bwt = ""
compteur = 0



win = Tk()

lab1 = Label(win, text= "Merci de rentrer votre séquence ici :")
ent = Text(win, height = 3, width = 20)
lab = Label(win)
lab2 = Label(win)
#lab3 = Label(win, text= "")

but = Button(win, text="Valide", command = valide)

lab1.pack()
ent.pack()
lab.pack()
lab2.pack()
#lab3.pack()
but.pack()





win.mainloop()