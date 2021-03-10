# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 12:15:32 2021

@author: Thierry et Diana
"""

#ACTTGATC

from BWT import cryptage
from tkinter import Tk, Label, Button, Text, DISABLED, NORMAL

def change_color():
    global liste_pattern2
    ent2.pack_forget()
    ent3.delete("end-1c")
    ent3.configure(height = compteur2 , width = len(liste_pattern2[0]) + 1,  state = DISABLED)
    ent3.pack()
    lab2["text"] = "Voici votre séquence cryptée : " + bwt
    lab2.pack()
    # ent2.tag_add('red', str(len(liste_pattern))'.8')
    #ent2.tag_add('red', '2.8')
    

def valide():
    """
    Permet de lancer l'analyse de cryptage de la séquence donnée'
    """
    ent2.pack()
    global liste_pattern, liste_pattern2, bwt, compteur
    liste_pattern, liste_pattern2, bwt = cryptage(ent.get("1.0", "end-1c"))
    but.configure(text = "Suivant", command = suivant)
    ent2.configure(height = compteur2 , width = len(liste_pattern[0]) + 1)
    ent2.insert("1.0", liste_pattern[compteur] + "\n")
    ent2.config(state = DISABLED)
    compteur += 1
    lab1.pack_forget()
    ent.pack_forget()
    return liste_pattern, liste_pattern2, bwt
    

def suivant():
    """
    Permet de faire l'affichage du cryptage de la séquence d'intérêt
    """
    global compteur, compteur2, liste_pattern, liste_pattern2, bwt, string
    ent2.config(state = NORMAL)
    ent2.configure(height = compteur+1 , width = len(liste_pattern[0]) + 1)
    ent2.insert(str(compteur+1) + ".0", liste_pattern[compteur] + "\n")
    ent2.config(state = DISABLED)
    ent3.insert(str(compteur2+1) + ".0", liste_pattern2[compteur2] + "\n")
    #string += liste_pattern2[compteur] + "\n"
    ent3.tag_configure('red', foreground='red')
    # ent2.tag_add('red', str(compteur+1) + '.8')
    ent3.tag_add('red', str(compteur) + '.8')
    compteur += 1
    compteur2 += 1
    if compteur == len(liste_pattern):
        but.configure(text = "Trier", command= change_color)
        but.pack(side="bottom")
        # lab.configure(fg = "blue", wraplength = (compteur-2)*10)
            
        

sequence =""

bwt = ""
compteur = 0
compteur2 = 0
string = ""


win = Tk()

lab1 = Label(win, text= "Merci de rentrer votre séquence ici :")
ent = Text(win, height = 5, width = 20)
ent2 = Text(win, height=0, width=0)
ent3 = Text(win,  height=0, width=0)
lab = Label(win)
lab2 = Label(win)
#lab3 = Label(win, text= "")

but = Button(win, text="Valide", command = valide)

lab1.pack()
ent.pack()
ent2.pack_forget()
ent3.pack_forget()
# lab.pack()
lab2.pack_forget()
# #lab3.pack()
but.pack()


#, state=DISABLED


win.mainloop()