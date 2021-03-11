# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:44:20 2021

@author: Thierry et Diana
"""
#ACTTGATC

from BWT import cryptage
from BWT import decryptage
from huffman import compression_huffman
from huffman import decompression_huffman
from os import path
from os import mkdir
from tkinter import Button
from tkinter import DISABLED
from tkinter import BOTH
from tkinter import LEFT, RIGHT, BOTTOM, TOP
from tkinter import font
from tkinter import Label
from tkinter import NORMAL
from tkinter import Radiobutton
from tkinter import StringVar
from tkinter import Text
from tkinter import Tk
from tkinter import Toplevel
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename

##############################################################################
def delete_var():
    global original_seq, compteur, compteur2, list_pattern, list_pattern_sort, \
    bwt, seq_decrypt, list_decrypt, seq_fasta, button
    global origin_seq, given_sequence, binary_sequence, binary_dict, compress_seq, \
    add_zero, list_compress, list_decompress, decompress_seq, compteur_huffman, \
    compteur_huffman2
    original_seq = ""
    compteur = 0
    compteur2 = 1
    compteur_huffman  = 0
    compteur_huffman2 = 1
    list_pattern = []
    list_pattern_sort = []
    bwt = ""
    seq_decrypt= ""
    list_decrypt = []
    list_decrypt_step = []
    seq_fasta = ""
    button = ""
    
    origin_seq = ""
    given_sequence = ""
    binary_sequence = ""
    binary_dict = {}
    compress_seq = ""
    decompress_seq = ""
    add_zero = 0
    list_compress = []
    list_decompress = []
   
##############################################################################
def hidden():
    text_step.config(state = NORMAL)
    text_sort.config(state = NORMAL)
    text_step2.config(state = NORMAL)
    sequence.delete("1.0", "end-1c")
    text_step.delete("1.0", "end-1c")
    text_sort.delete("1.0", "end-1c")
    text_step2.delete("1.0", "end-1c")
    lab_file["text"] = ""
    win_no_step.withdraw()
    win_step.withdraw()
    text_sort.pack_forget()
    text_step.pack_forget()
    seq_no_step.pack_forget()
    seq_no_step2.pack_forget()
    button_no_step.pack_forget()
    seq_step.pack_forget()
    button_step.pack_forget()
    lab_pass.pack_forget()
    lab_step.pack_forget()
    seq_step.pack_forget()
    button_pass_final.pack_forget()
    text_step.config(state=NORMAL)
    button_step2.pack_forget()
    text_step2.pack_forget()
    button_pass2.pack_forget()
    lab_pass2.pack_forget()
    seq_step2.pack_forget()
    title_bwt.pack_forget()
    title_huffman.pack_forget()

##############################################################################    
def error(message:str):
    showwarning(title="Error", message = message)

##############################################################################
def creation_directory(directory:str):
    if path.isdir(directory):
        pass
    else:
        mkdir(directory)
##############################################################################
def destroy():
    """
    Détruire l'ensemble des fenêtre
    """
    win_no_step.quit()
    win_step.quit()
    main_win.destroy()

##############################################################################
def red_cross_win_no_step():
    """
    Gère l'évement de la fermeture de la fenetre sans étape par la croix
    """
    hidden()
    delete_var()

##############################################################################    
def red_cross_win_step():
    """
    Gère l'évement de la fermeture de la fenetre avec étape par la croix
    """
    hidden()
    delete_var()
    
##############################################################################    
def bwt_check(buttonId:str):
    global  button
    global original_seq, list_pattern, list_pattern_sort, seq_fasta
    global seq_decrypt, list_decrypt, bwt, list_decrypt_step
    button = buttonId
    if button == "Encryption" or button == "Encryption/compression":
        if sequence.get("1.0", "end-1c") != "" :
            original_seq = sequence.get("1.0", "end-1c")
        elif seq_fasta != "":
            original_seq = seq_fasta
        elif path.exists("Results/my_save.txt"):
            with open("Results/my_save.txt", "r") as file_encrypt:
                original_seq += file_encrypt.readlines()[0].strip()
        elif path.exists("Results/my_decompress_sequence.txt"):
            with open("Results/my_decompress_sequence.txt") as file_decompression:
                original_seq = file_decompression.readlines()[1].strip()
        else:
            error("Please give a sequence to encrypted")
        if original_seq != "":
            list_pattern, list_pattern_sort, bwt = cryptage(original_seq.upper())
    elif button == "Decryption" or button == "Decompression/decryption":
        if path.exists("Results/my_save.txt"):
            with open("Results/my_save.txt", "r") as file_decrypt:
                    bwt = file_decrypt.readlines()[0].strip()
                    seq_decrypt, list_decrypt, list_decrypt_step = decryptage(bwt)
        else:
            error("The encryption file does not exist")
                
##############################################################################
def huffman_check(buttonId:str):
    global button, seq_fasta, origin_seq
    global given_sequence, binary_sequence, binary_dict, add_zero
    global decompress_seq, compress_seq
    button = buttonId
    if button == "Compression" or button == "Encryption/compression":
        if sequence.get("1.0", "end-1c") != "" :
            origin_seq = sequence.get("1.0", "end-1c")
        elif seq_fasta != "":
            origin_seq = seq_fasta
        elif path.exists("Results/my_save.txt"):
            with open("Results/my_save.txt", "r") as file_encrypt:
                origin_seq = file_encrypt.readline().strip()
        elif path.exists("Results/my_decompress_sequence.txt"):
            with open("Results/my_decompress_sequence.txt", "r") as file_decompression:
                origin_seq = file_decompression.readlines()[1].strip()
        else:
            error("Please give a study sequence")
        if origin_seq != "":
            given_sequence, binary_dict, compress_seq, add_zero, binary_sequence = compression_huffman(origin_seq.upper())
    elif button == "Decompression" or button == "Decompression/decryption":
        if path.exists("Results/my_save2.txt") and path.exists("Results/my_save3.txt"):
            with open("Results/my_save2.txt", "r", encoding="utf-8") as file_compression:
                process_file = file_compression.readlines()
                compress_seq = process_file[0].replace("\n", "")
            with open("Results/my_save3.txt", "r") as file_annexe:
                process_file2 = file_annexe.readlines()
                add_zero = int(process_file2[0].strip())
                dico_string = process_file2[1]
                char = " {}'\""
                for characterspecial in char:
                    dico_string = dico_string.replace(characterspecial,"")
                dico_string = dico_string.split(",")
                i=0
                while i < len(dico_string):
                    binary_dict[dico_string[i].split(":")[0]] = dico_string[i].split(":")[1]
                    i += 1
                binary_sequence, decompress_seq = decompression_huffman(compress_seq, add_zero, binary_dict)
        else:
            error("No file for decompression analysis")
###############################################################################
def display_step_encrypt():
    """
    Affiche la première étape de la décryptage
    """
    global compteur, compteur2
    global list_pattern, list_pattern_sort, bwt
    button_step.configure(text="Suivant", command= next_bwt)
    button_pass_final.configure(text = "Pass", command = pass_step_bwt)
    text_step.configure(height = compteur2 , width = len(list_pattern[0]))
    text_step.insert("1.0", list_pattern[compteur] + "\n")
    text_sort.config(state = NORMAL)
    text_sort.insert(str(compteur2) + ".0", list_pattern_sort[compteur] + "\n")
    text_sort.tag_configure('red', foreground='red')
    text_sort.tag_add('red', str(compteur2) + '.' + str(len(bwt)-1))
    text_sort.config(state = DISABLED)
    title_bwt.pack()
    seq_step.pack_forget()
    lab_pass.pack_forget()
    button_step.pack()
    text_step.pack(padx=2)
    button_pass_final.pack()
    lab_pass.pack_forget()
    compteur += 1
    compteur2 += 1
    
##############################################################################
def display_step_decrypt():
    """
    Affiche la première étape du décryptage
    """
    global seq_decrypt, list_decrypt, compteur, compteur2, list_decrypt_step
    for i in range(0, len(seq_decrypt)+1, 1):
        text_step.configure(height = i+1 , width = i+1, state = NORMAL)
        text_step.insert( str(i+1) + "." + str(len(list_decrypt_step[i])), list_decrypt_step[compteur][i] + "\n")
    text_step.delete("end-1c")
    text_step.configure(state=DISABLED)
    button_pass_final.configure(text = "Pass", command = pass_step_bwt)
    button_step.config(text= "Suivant", command=next_bwt)
    title_bwt.pack()
    button_step.pack()
    text_step.pack(padx=2)
    button_pass_final.pack()
    seq_step.pack_forget()
    compteur += 1        

##############################################################################
def display_step_comp():
    """
    Affiche la première étape de la compression
    """
    global list_compress, compteur_huffman, compteur_huffman2
    text_step2.configure(height = 10 , width = 100)
    text_step2.configure(state=NORMAL)
    text_step2.insert(str(compteur_huffman2) + ".0", list_compress[compteur_huffman] + "\n")
    text_step2.configure(state = DISABLED)
    button_step2.configure(text = "Next", command=next_huffman)
    button_pass2.configure(text = "Pass", command = pass_step_huffman)
    title_huffman.pack()
    button_step2.pack()
    text_step2.pack(padx=2)
    button_pass2.pack()
    compteur_huffman += 1
    compteur_huffman2 += 2
    
##############################################################################
def display_step_decomp():
    """
    Affiche la première étape de la décompression
    """
    global list_decompress, compteur_huffman2, compteur_huffman
    text_step2.configure(state=NORMAL)
    text_step2.configure(height = 10, width= 100)
    text_step2.insert(str(compteur_huffman2) + ".0", list_decompress[compteur_huffman] + "\n")
    text_step2.configure(state = DISABLED)
    button_step2.configure(text = "Next", command=next_huffman)
    button_pass2.configure(text = "Pass", command = pass_step_huffman)
    title_huffman.pack()
    button_step2.pack()
    text_step2.pack(padx=2)
    button_pass2.pack()
    compteur_huffman += 1
    compteur_huffman2 += 2
        
##############################################################################
def encryption():
    """
    Gestion de l'appuie du bouton Encryption selon les cas
    """
    global compteur, compteur2
    global list_pattern, list_pattern_sort, bwt
    bwt_check(encryption["text"])
    if bwt != "":
        if step.get() == "no step":
            win_no_step.deiconify()
            button_no_step.configure(text="Save")
            seq_no_step.configure(text = "Here is your encrypted sequence: \n" + bwt)
            button_no_step.configure(command = save_bwt)
            seq_no_step.pack()
            button_no_step.pack()
        else:
            win_step.deiconify()
            display_step_encrypt()
        
##############################################################################
def decryption():
    global seq_decrypt, list_decrypt, compteur, compteur2
    bwt_check(decryption["text"])
    if seq_decrypt != "":
        if step.get() == "no step":
            win_no_step.deiconify()
            seq_no_step.configure(text = "Here is your decrypted sequence: \n" + seq_decrypt)
            button_no_step.configure(command = save_bwt)
            seq_no_step.pack()
            button_no_step.pack()
        else:
            win_step.deiconify()
            display_step_decrypt()
        

##############################################################################
def compression():
    global given_sequence, binary_sequence, compress_seq
    global list_compress, compteur_huffman, compteur_huffman2
    huffman_check(compression["text"])
    if given_sequence != "":
        list_compress = ["Your initial sequence: \n" + given_sequence,
                         "Your binary sequence: \n" + binary_sequence,
                         "Your compressed sequence: \n", compress_seq]
        if step.get() == "no step":
            win_no_step.deiconify()
            seq_no_step.configure(text = "Here is your compression sequence: \n" + compress_seq)
            button_no_step.configure(text="Save", command = save_huffman)
            seq_no_step.pack()
            button_no_step.pack()
        else:
            win_step.deiconify()
            display_step_comp()

##############################################################################
def decompression():
    global compress_seq, decompress_seq, binary_sequence, compteur_huffman
    global list_decompress, compteur_huffman2
    compteur_huffman2 = 1
    huffman_check(decompression["text"])
    if compress_seq != "":
        list_decompress = ["Your compressed sequence: \n" + compress_seq,
                           "Your binary sequence: \n"+ binary_sequence,
                           "Your decompressed sequence: \n", decompress_seq]
        if step.get() == "no step":
            win_no_step.deiconify()
            seq_no_step.configure(text= "Your decompressed sequence: \n" + decompress_seq)
            button_no_step.configure(text="Save", command = save_huffman)
            seq_no_step.pack()
            button_no_step.pack()
        else:
            win_step.deiconify()
            display_step_decomp()
                
##############################################################################
def encrypt_compress():
    """
    Permet de culmuler encryptage et compression
    """
    global compteur, compteur2, compteur_huffman, compteur_huffman2
    global original_seq, list_pattern, list_pattern_sort, bwt
    global given_sequence, binary_sequence, compress_seq, list_compress
    compteur_huffman2 = 1
    button_press = encrypt_compress["text"]
    bwt_check(button_press)
    if bwt != "":
        huffman_check(button_press)
        list_compress = ["Your initial sequence: \n" + given_sequence,
                         "Your binary sequence: \n" + binary_sequence,
                         "Your compressed sequence: \n", compress_seq]
        if step.get() == "no step":
            win_no_step.deiconify()
            seq_no_step.configure(text= "Your encrypted sequence: \n" + bwt)
            seq_no_step2.configure(text= "Your compressed sequence: \n" + compress_seq)
            button_no_step.configure(text="Save", command = save_duo)
            seq_no_step.pack()
            seq_no_step2.pack()
            button_no_step.pack()
        else:
            win_step.deiconify()
            display_step_encrypt()
            display_step_comp()

##############################################################################
def decompress_decrypt():
    """
    Fonction permettant de faire decompression et decryptage en même temps
    """
    global compteur, compteur2
    global compress_seq, decompress_seq, binary_sequence, list_decompress
    global seq_decrypt, list_decrypt
    button_press = decompress_decryp["text"]
    huffman_check(button_press)
    list_decompress = ["Your compressed sequence: \n" + compress_seq,
                           "Your binary sequence: \n"+ binary_sequence,
                           "Your decompressed sequence: \n", decompress_seq]
    text_step.delete("1.0", "end-1c")
    if compress_seq != "" :
        bwt_check(button_press)
        if step.get() == "no step":
            win_no_step.deiconify()
            seq_no_step.configure(text= "Your encrypted sequence: \n" + decompress_seq)
            seq_no_step2.configure(text= "Your compressed sequence: \n" + seq_decrypt)
            button_no_step.configure(text="Save", command = save_duo)
            seq_no_step.pack()
            seq_no_step2.pack()
            button_no_step.pack()
        else:
            win_step.deiconify()
            display_step_decomp()
            display_step_decrypt()
       
############################################################################### 
def next_bwt():
    """
    Permet de faire l'affichage du cryptage de la séquence d'intérêt
    """
    global button, compteur, compteur2
    global list_pattern, list_pattern_sort, bwt
    global list_decrypt, seq_decrypt, list_decrypt_step
    if button == "Encryption" or button == "Encryption/compression":
        text_step.config(state = NORMAL)
        text_step.configure(height = compteur2, width = len(list_pattern[0]))
        text_step.insert(str(compteur2) + ".0", list_pattern[compteur] + "\n")
        text_step.config(state = DISABLED)
        text_sort.config(state = NORMAL)
        text_sort.insert(str(compteur2) + ".0", list_pattern_sort[compteur] + "\n")
        text_sort.tag_configure('red', foreground='red')
        text_sort.tag_add('red', str(compteur2) + '.' + str(len(bwt)-1))
        text_sort.config(state = DISABLED)
        if compteur == len(list_pattern)-1:
            button_step.configure(text = "Trier", command = result_bwt)
            button_pass_final.pack_forget()
    elif button == "Decryption" or button == "Decompression/decryption":
        text_step.configure(state = NORMAL)
        text_step.delete("1.0", "end-1c")
        for position in range(0, len(seq_decrypt)+1, 1):
            text_step.configure(state = NORMAL)
            text_step.insert(str(position+1) + "." + str(0), list_decrypt_step[compteur][position] + "\n")
            text_step.config(state= DISABLED)
        if compteur == len(list_decrypt_step)-1:
            button_step.config(text="Result", command = result_bwt)
            button_pass_final.pack_forget()
    compteur += 1
    compteur2 += 1
            
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def result_bwt():
    """
    affichage du trie de la liste et de la séquence cryptée
    """
    global compteur, compteur2, button
    if button == "Encryption" or button == "Encryption/compression":
        global list_pattern_sort
        button_step.pack_forget()
        text_step.pack_forget()
        
        text_sort.config(state = NORMAL)
        text_sort.delete("end-1c")
        text_sort.config(state = DISABLED)
        text_sort.configure(height = compteur,
                            width = len(list_pattern_sort[0]) + 1,  
                            state = DISABLED)
        lab_step.configure(text = "Here is your encrypted sequence: ")
        seq_step.configure(text = bwt, fg = "red")
        button_step.configure(text = "Save", command = save_bwt)
        button_pass_final.pack_forget()
        text_sort.pack()
        lab_step.pack()
        seq_step.pack()
        button_step.pack()
              
    elif button == "Decryption" or button == "Decompression/decryption":
        line = 0
        global list_decrypt, seq_decrypt
        for elt in list_decrypt:
            if elt[-1] == "$":
                line += list_decrypt.index(elt) + 1
        text_step.configure(state=NORMAL)
        text_step.tag_configure('red', foreground='red')
        text_step.tag_add('red', str(line) + ".0", str(line) + "." + str(len(list_decrypt)))
        text_step.configure(state = DISABLED)
        button_step.configure(text="Save", command=save_bwt)
        lab_step.configure(text = "Votre séquence décryptée: \n")
        seq_step.configure(text = seq_decrypt, fg="red")
        lab_step.pack()
        seq_step.pack()
        button_step.pack() 
    if button == "Encryption/compression" or button == "Decompression/decryption":
            button_step.pack_forget()
            button_step2.pack_forget()
            text_step2.pack_forget()
            button_pass2.pack(side = BOTTOM)
            button_step2.pack()
            text_step2.pack()
               
##############################################################################
def next_huffman():
    global compteur_huffman, compteur_huffman2, list_decompress, button, list_compress
    if button == "Compression" or button == "Encryption/compression":
        text_step2.configure(state=NORMAL)
        text_step2.insert(str(compteur_huffman2) + ".0", list_compress[compteur_huffman] + "\n" )
        text_step2.configure(state = DISABLED)
        # button_step2.configure(text = "Next Huffman", command=next_huffman)
        if compteur_huffman == len(list_compress)-2:
            button_step2.configure(text = "Result", command = result_huffman)
            button_pass2.pack_forget()
    if button == "Decompression" or button == "Decompression/decryption":
        text_step2.configure(state=NORMAL)
        text_step2.insert(str(compteur_huffman2) + ".0", list_decompress[compteur_huffman] + "\n" )
        text_step2.configure(state = DISABLED)
        button_step2.configure(text = "Next", command=next_huffman)
        if compteur_huffman == len(list_decompress)-2:
            button_step2.configure(text = "Result", command = result_huffman)
            button_pass2.pack_forget()
    compteur_huffman += 1
    compteur_huffman2 += 2
    
##############################################################################
def result_huffman():
    global button, list_decompress, compteur_huffman2, list_compress
    if button == "Compression" or button == "Encryption/compression":
        text_step2.configure(state = NORMAL)
        text_step2.delete("end-1c")
        text_step2.insert(str(compteur_huffman2-1) + ".0", list_compress[-1])
        text_step2.tag_configure('red', foreground='red')
        text_step2.tag_add('red', str(compteur_huffman2-1) + ".0", str(compteur_huffman2-1) 
                          + "." + str(len(list_compress[-1])))
        text_step2.configure(state = DISABLED)
        button_step2.configure(text="Save", command=save_huffman)
        
    elif button == "Decompression" or button == "Decompression/decryption":
        text_step2.configure(state = NORMAL)
        text_step2.delete("end-1c")
        text_step2.insert(str(compteur_huffman2-1) + ".0", list_decompress[-1])
        text_step2.tag_configure('red', foreground='red')
        text_step2.tag_add('red', str(compteur_huffman2-1) + ".0", str(compteur_huffman2-1) 
                          + "." + str(len(list_decompress[-1])))
        text_step2.configure(state = DISABLED)
        button_step2.configure(text="Save", command=save_huffman)
    button_pass2.pack_forget()    
##############################################################################
def pass_step_bwt():
    global button, list_pattern_sort, bwt, list_decrypt, seq_decrypt
    string=""
    if button == "Encryption" or button == "Encryption/compression":
        for element in list_pattern_sort:
            string += element + "\n"    
        lab_pass.configure(text=string.strip())
        lab_step.configure(text="Votre séquence encryptée: ")
        seq_step.configure(text= bwt, fg="red")        
    elif button == "Decryption" or button == "Decompression/decryption":
        for element in list_decrypt:
            string += element + "\n"    
        lab_pass.configure(text=string.strip())
        lab_step.configure(text="Votre séquence encryptée: ")
        seq_step.configure(text= seq_decrypt, fg="red")
    button_pass_final.configure(text = "Save", command = save_bwt)
    button_pass_final.pack_forget()
    lab_step.pack()
    seq_step.pack()
    button_pass_final.pack(fill=BOTH)
    lab_pass.pack(padx=2, pady=2)
    button_step.pack_forget()
    text_sort.pack_forget()
    text_step.pack_forget()
    if button == "Encryption/compression":
            # button_pass_final.pack_forget()
            button_step.pack_forget()
            button_step2.pack_forget()
            text_step2.pack_forget()
            button_pass2.pack_forget()
            button_step2.pack()
            text_step2.pack()
            button_pass2.pack() 
    
##############################################################################
def pass_step_huffman():
    global button, list_compress, list_decompress
    string_huffman = ""
    if button == "Compression" or button == "Encryption/compression":
        for element in list_compress[0:-1]:
            string_huffman += element + "\n"
        lab_pass2.configure(text=string_huffman.strip())
        seq_step2.configure(text= list_compress[-1], fg="red")
    elif button == "Decompression" or button == "Decompression/decryption":
        for element in list_decompress[0:-1]:
            string_huffman += element + "\n"    
        lab_pass2.configure(text=string_huffman.strip())
        seq_step2.configure(text= list_decompress[-1], fg="red")
    button_pass2.configure(text = "Save", command = save_huffman)
    lab_pass2.pack()
    seq_step2.pack()
    button_step2.pack_forget()
    text_step2.pack_forget()
    if button == "Encryption/compression" or button == "Decompression/decryption":
        button_pass2.pack_forget()
    
##############################################################################
def save_bwt():
    global button, seq_decrypt, original_seq, bwt
    creation_directory("Results")
    if button == "Encryption" or button == "Encryption/compression":
        with open("Results/my_save.txt", "w") as file:
                file.write(bwt)
    elif button == "Decryption" or button == "Decompression/decryption":
        with open("Results/my_save.txt", "w") as file:
                file.write(seq_decrypt)
    hidden()
    delete_var()

##############################################################################
def save_huffman():
    global button, compress_seq, add_zero, binary_dict, decompress_seq
    creation_directory("Results")
    if button == "Compression" or button == "Encryption/compression":
        with open("Results/my_save2.txt", "w", encoding="utf-8") as file2:
            file2.write(compress_seq)
        with open("Results/my_save3.txt", "w") as file3:
            file3.write(str(add_zero) + "\n" + str(binary_dict))
    elif button == "Decompression" or button == "Decompression/decryption":
        with open("Results/my_decompress_sequence.txt", "w") as file2:
            file2.write("Voici votre séquence décompressée: " + "\n" + decompress_seq)
    hidden()
    delete_var()
    
###############################################################################
def save_duo():
    global button, original_seq, bwt, seq_decrypt, decompress_seq
    global add_zero, binary_dict, compress_seq
    creation_directory("Results")
    if button == "Encryption/compression":
        with open("Results/my_save.txt", "w") as file:
            file.write(bwt)
        with open("Results/my_save2.txt", "wb") as file2:
            file2.write(compress_seq)
        with open("Results/my_save3.txt", "w") as file3:
            file3.write(str(add_zero) + "\n" + str(binary_dict))
    else:
        with open("Results/my_save.txt", "w") as file:
            file.write(seq_decrypt)
        with open("Results/my_decompress_sequence.txt", "w") as file2:
            file2.write("Voici votre séquence décompressée: " + "\n" + decompress_seq)
    hidden()
    delete_var()
    
      
##############################################################################
def browse():
    global seq_fasta
    Filetypes= [('text files', '.txt'),('all files', ['.fa', '.fasta'])]
    name_file = askopenfilename(title="Open your document", filetypes= Filetypes)
    seq_fasta = ""
    lab_file["text"] = ""
    if name_file:
        with open(name_file, "r") as file:
            for line in file:
                if line[0] != ">":
                    seq_fasta += line.strip()
            lab_file["text"] = name_file.split("/")[-1]

    

    

#Création de la fenêtre principal
main_win = Tk()
main_win.title("Projet_Algo")
main_win.geometry()
main_win.resizable(width=False, height=False)
main_win.configure(bg="#aee789")
main_win.protocol("WM_DELETE_WINDOW", destroy)

#Création et element de la fenetre "sans étape"
win_no_step=Toplevel(main_win)
win_no_step.withdraw()
seq_no_step = Label(win_no_step)
seq_no_step2 = Label(win_no_step)
button_no_step = Button(win_no_step, text="Save")
win_no_step.protocol("WM_DELETE_WINDOW", red_cross_win_no_step)

#Creation et element de la fenetre "avec étape"
font = font.Font(size = 14, weight = "bold")
win_step = Toplevel(main_win)
win_step.withdraw()
text_step = Text(win_step, height=0, width=0)
text_step2 = Text(win_step, height=0, width=0)
text_sort = Text(win_step,  height=0, width=0)
title_bwt = Label(win_step, text = "The steps BWT", font=font)
title_huffman = Label(win_step, text = "The steps Huffman", font=font)
button_step = Button(win_step)
button_step2 = Button(win_step)
button_pass_final = Button(win_step, text="Pass")
button_pass2 = Button(win_step, text="Pass")
lab_pass = Label(win_step, text="")
lab_pass2 = Label(win_step, text="")
lab_step = Label(win_step)
seq_step = Label(win_step)
seq_step2 = Label(win_step)
win_step.protocol("WM_DELETE_WINDOW", red_cross_win_step)

#variable bwt
original_seq = ""
compteur = 0
compteur2 = 1
compteur_huffman  = 0
compteur_huffman2 = 1
list_pattern = []
list_pattern_sort = []
bwt = ""
seq_decrypt= ""
list_decrypt = []
list_decrypt_step = []
seq_fasta = ""
button = ""

#variable huffman
origin_seq = ""
given_sequence = ""
binary_sequence = ""
binary_dict = {}
compress_seq = ""
decompress_seq = ""
add_zero = 0
list_compress = []
list_decompress = []


step = StringVar()
step.set("no step")
no_step = Radiobutton(main_win, text= "No step", variable=step, value="no step", bg ="#aee789", font=font)
with_step = Radiobutton(main_win, text= "With step", variable=step, value="with step", bg="#aee789", font=font)
sequence = Text(main_win, width = 30, height = 5)
browse = Button(main_win, text="Browse", command=browse)
lab_file = Label(main_win, text="", bg ="#aee789")
encryption = Button(main_win, text= "Encryption", command= encryption)
compression =  Button(main_win, text="Compression", command = compression)
decompression =  Button(main_win, text="Decompression", command = decompression)
decryption = Button(main_win, text="Decryption", command = decryption)
encrypt_compress = Button(main_win, text="Encryption/compression", command = encrypt_compress)
decompress_decryp = Button(main_win, text="Decompression/decryption", command = decompress_decrypt)
space1 = Label(main_win, bg ="#aee789")
space2 = Label(main_win, bg="#aee789")
space3 = Label(main_win, bg ="#aee789")
space4 = Label(main_win, bg ="#aee789")
space5 = Label(main_win, bg ="#aee789")



no_step.grid(row = 0, column = 1, columnspan = 2)
with_step.grid(row = 0, column = 4, columnspan = 2)



space1.grid(row = 1, column = 0, columnspan= 7, sticky="we")
sequence.grid(row = 2, rowspan = 3, column = 2, columnspan= 3)
space2.grid(row=5, column = 0, columnspan = 7, sticky="we")
browse.grid(row=6, column=0, columnspan=3, sticky="we")
lab_file.grid(row = 6, column=3, columnspan=5, sticky="w")
space3.grid(row= 7, column = 0, columnspan = 7)
encryption.grid(row = 8, column=1, columnspan= 1, padx = 5)
compression.grid(row=8, column=2, columnspan = 1, padx = 2)
decompression.grid(row =8, column=4 , columnspan = 1, padx = 1)
decryption.grid(row=8, column = 5, columnspan = 1, padx = 5)
space4.grid(row= 9, column= 0, columnspan = 7)
encrypt_compress.grid(row =10 , column = 1, columnspan=2)
decompress_decryp.grid(row= 10, column= 4, columnspan = 2)
space5.grid(row=11, column = 0, columnspan = 7, sticky = "we")

main_win.mainloop()
