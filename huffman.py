# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:50:31 2021

@author: Thierry et Diana
"""

#"NNTNACTTNGNNGTTNCCTATACCT"
from essai_arbres import Arbre
from essai_arbres import Noeud

sequence_choisie = "TACCTCGCGTCGTGTCGTGTCGTGCGTCGTCGTGCGATGACT"

def frequence(sequence:str):
    """
    Fonction permettant de calculer la fréquence de chaque caractère dans la séquence
    """
    dico_element= {}
    for element in sequence:
        if element.upper() in dico_element:
            dico_element[element.upper()] += 1
        else:
            dico_element[element.upper()] = 1
    return dico_element

##############################################################################

def trie_dico(dico1):
    """
    fonction qui trie le dictionnaire pour mettre les valeurs de fréquence par
    ordre croissantes
    """
    dico2 = {}
    for k, v in sorted(dico1.items(), key=lambda x: x[1]):
        dico2[k] = v
    return dico2

##############################################################################
def creation_noeud(dico):
    """
    Création de la liste de noeud de nos caractères de séquence
    """
    liste_noeud = []
    for k, v in dico.items():
        liste_noeud.append(Noeud(v, k))
    return liste_noeud

##############################################################################
def transformation_binaire(sequence:str, dico_binaire:dict):
    """
    fonction qui transforme notre séquence en séquence binaire
    """
    sequence_binaire = ""
    for lettre in sequence:
        sequence_binaire += str(dico_binaire[lettre])
    return sequence_binaire
    
##############################################################################    
def compression(sequence_binaire:str):
    """
    fonction de compression qui prend notre séquence binaire et la transforme
    en caractère associé par groupe de 8 bits
    """
    sequence_compressee = ""
    calcul_octet =(len(sequence_binaire) % 8)
    if calcul_octet != 0:
        sequence_binaire = (8 - calcul_octet)*'0' + sequence_binaire
    for octet in range(0, len(sequence_binaire), 8):
        sequence_compressee += chr(int(sequence_binaire[octet:octet+8], 2))
    return (sequence_compressee, calcul_octet)

##############################################################################
def decompression(sequence_compressee:str):
    """
    fonction qui retransforme notre chaine compressée de caractères spéciaux
    en sequence binaire
    """
    seq_decomp=""
    for caractere in sequence_compressee:
        seq_decomp += bin(ord(caractere))[2:].zfill(8)
    return seq_decomp

##############################################################################
def modif_dico_clef_valeur(dico:dict):
    """
    Cette fonction permet de simplifié la lecture du dictionnaire en inversant
    les clés et les valeurs pour la retransformation en séquence ADN
    """
    dico_modif= {}
    for clef, valeur in dico.items():
        dico_modif[valeur] = clef
    return dico_modif

##############################################################################
def retransformation(seq_decomp:str, dico_binaire:dict, calcul_octet:int):
    """
    Fonction retransformant notre séquence binaire en notre séquence d'ADN 
    originel
    """
    if calcul_octet != 0:
        calcul_octet = (8-calcul_octet)
    seq_decomp = seq_decomp[calcul_octet:]
    seq_retour = ""
    compteur = 0
    for position in range(0, len(seq_decomp)+1, 1):
        if seq_decomp[compteur:position] in dico_binaire.keys():
            seq_retour += dico_binaire[seq_decomp[compteur:position]]
            compteur = position
    return seq_decomp, seq_retour  

def compression_huffman(sequence:str):
    dico_frequence = frequence(sequence)
    dico_ordone = trie_dico(dico_frequence)
    list_feuille = creation_noeud(dico_ordone)
    tree = Arbre(list_feuille)
    dico_seq_binaire = tree.convertion_binaire_arbre()
    seq_trans_binaire = transformation_binaire(sequence, dico_seq_binaire)
    seq_compress, ajout_binaire = compression(seq_trans_binaire)
    return sequence, dico_seq_binaire, seq_compress, ajout_binaire, seq_trans_binaire

def decompression_huffman(seq_comp:str, bin_ajout, dico_bin):
    seq_decompressee = decompression(seq_comp)
    dico_bin_modif = modif_dico_clef_valeur(dico_bin)
    seq_decomp, sequence_retablie = retransformation(seq_decompressee, dico_bin_modif, bin_ajout)
    return seq_decomp, sequence_retablie

if __name__ == "__main__":
    seq_originel, dico, seq, binai, seq_bin = compression_huffman("ACTTGATC")
    print(seq_originel)
    print(seq)
    print(seq_bin)
    print(dico)
    seq_decomp_bin, seq_fin= decompression_huffman(seq, binai, dico)
    print(seq)
    print(seq_decomp_bin)
    print(seq_fin)

      