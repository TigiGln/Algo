#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:58:34 2021

@author: Thierry Galliano
"""
from sys import argv

###############################################################################
def cryptage(sequence : str):
    """ 
    Function to encrypt the sequence of interest
    """
    #addition of special character allowing the encryption of the sequence
    sequence += "$"
    list_pattern = []
    list_pattern2 = []
    #creation of the list of different patterns with shift of the special character  
    for position in range(len(sequence), 0, -1):
        list_pattern.append(sequence[position:] + sequence[0:position])
    list_pattern2 = list_pattern[0:len(list_pattern)]
    list_pattern2.sort()
    bwt = ""
    #Retrieve the encrypted sequence from the last column of the matrix
    for pattern in list_pattern2:
        bwt += pattern[-1]
    return(list_pattern, list_pattern2, bwt)

##############################################################################
def decryptage(bwt:str):
    """
    Function to decrypt the sequence of interest
    """
    #creation of the bwt character list and the list with the transformation steps
    bwt_list = list(bwt)
    bwt_list_step = []
    #the copy method creates a duplicate of the list and not a path to the memory location
    bwt_list_step. append(bwt_list.copy())
    bwt_list.sort()
    bwt_list_step.append(bwt_list.copy())
    #add bwt in the first column in each loop 
    for turn in range(1, len(bwt), 1):  
        for add_bwt in range(0, len(bwt), 1):
            bwt_list[add_bwt] = bwt[add_bwt] + bwt_list[add_bwt]
        bwt_list_step.append(bwt_list.copy())
        #sorting of each line in lexicographical order
        if turn != (len(bwt)-1):
            bwt_list.sort()
        bwt_list_step.append(bwt_list.copy())
    #Recovery of the original decrypted sequence by searching for the special character
    seq_decryption = ""
    for elt in bwt_list:
        if elt[-1] == "$":
           seq_decryption = elt[0:len(elt)-1]
    return seq_decryption, bwt_list, bwt_list_step 
##############################################################################           

if __name__ == "__main__":
    if len(argv) == 2:
        print("Encryption using the BWT method: ")
        liste_pattern, liste_pattern2, bwt = cryptage(argv[1].upper())
        print(bwt, "\n")
        print("Decryption using the BWT method: ")
        seq, liste, liste2 = decryptage(bwt)
        print(seq)
    else:
        print("Please enter a sequence or respect the number of options")


