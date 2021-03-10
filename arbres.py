# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:56:04 2021

@author: Thierry et Diana
"""

class Noeud:
    """
    Cette classe crée des objets de type Noeud permettant la création
    d'un arbre binaire
    """
    def __init__(self, freq:int, lettre=None, zero=None, one=None ):
        self.nom = lettre
        self.freq = freq
        self.fils_zero = zero
        self.fils_un = one
    def node_feuille(self):
        if self.fils_zero is None and self.fils_un is None:
            return True
    def __repr__(self):
        if self.node_feuille():
            return self.nom
        return str(self.freq) + " 0: [" + str(self.fils_zero) + "]" + " 1: [" + str(self.fils_un) + "]"
    def convertion_binaire(self, chemin_binaire):
        if self.node_feuille():
            return self.nom + ':' + str(chemin_binaire) + '\n'
        else:
            chemin = self.fils_zero.convertion_binaire(str(chemin_binaire) + '0')
            chemin += self.fils_un.convertion_binaire(str(chemin_binaire) + '1')
        return chemin


class Arbre:
    """
    Cette classe crée des Arbres binaires
    """
    def __init__(self, liste_feuille):
        liste = liste_feuille
        while len(liste) != 1:
            premier_noeud = liste[0]
            deuxieme_noeud = liste[1]
            new_noeud =  Noeud(premier_noeud.freq + deuxieme_noeud.freq,
                               None, premier_noeud, deuxieme_noeud)
            del liste[1]
            del liste[0]
            position = 0
            for i in range(0, len(liste), 1):
                if new_noeud.freq >= liste[i].freq:
                    position += 1
            liste.insert(position, new_noeud)           
        self.racine = liste[0]
    def __repr__(self):
       return "Arbre: { " + str(self.racine) + " }"
    def convertion_binaire_arbre(self):
        code_binaire = self.racine.convertion_binaire('')
        dico_binaire = {}
        code_binaire = code_binaire.strip().split("\n")
        for element in code_binaire:
            dico_binaire[element.split(":")[0]] = element.split(":")[1]
        return dico_binaire
        
    

        

       