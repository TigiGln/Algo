#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:58:34 2021

@author: thierry
"""

# from pandas import DataFrame

def cryptage(sequence : str):
    """ 
    Fonction pour crypter la séquence donnée
    """
    #ajout caractère extérieur
    sequence += "$"
    list_pattern = []
    list_pattern2 = []
    #création des différents motifs avec décalage  
    for position in range(len(sequence), 0, -1):
        list_pattern.append(sequence[position:] + sequence[0:position])
    list_pattern2 = list_pattern[0:len(list_pattern)]
    list_pattern2.sort()
    bwt = ""
    for pattern in list_pattern2:
        bwt += pattern[-1]
    return(list_pattern, list_pattern2, bwt)


def decryptage(bwt:str):
    """
    Fonction pour décrypter la séquence donnée
    """
    bwt_list = list(bwt)
    bwt_list_step = []
    bwt_list_step. append(bwt_list.copy())
    bwt_list.sort()
    bwt_list_step.append(bwt_list.copy())
    for ajout_seq_initial in range(1, len(bwt), 1):  
        for j in range(0, len(bwt), 1):
            bwt_list[j] = bwt[j] + bwt_list[j]
        bwt_list_step.append(bwt_list.copy())
        if ajout_seq_initial != (len(bwt)-1):
            bwt_list.sort()
        bwt_list_step.append(bwt_list.copy())
    for elt in bwt_list:
        if elt[-1] == "$":
           seq_decrypt = elt[0:len(elt)-1]
    
    return seq_decrypt, bwt_list, bwt_list_step 
           

if __name__ == "__main__":
    liste_pattern = []
    # print("cryptage par la méthode de BWT : \n")
    liste_pattern, liste_pattern2, bwt = cryptage("ACTTGATC")
    # print(bwt)
    # print("Décryptage :  \n")
    seq, liste, liste2 = decryptage(bwt)
    print (liste, "\n")
    print(liste2, "\n")
    print(seq)


