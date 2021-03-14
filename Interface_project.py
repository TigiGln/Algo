# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:44:20 2021

@author: Thierry et Diana
"""
#ACTTGATC
import sys
sys.path.append("subparts/")
from BWT import cryptage
from BWT import decryptage
from huffman import compression_huffman
from huffman import decompression_huffman
from os import path
from os import mkdir
from tkinter import Button
from tkinter import DISABLED
from tkinter import BOTH
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
    """
    This function resets the global variables to the initial state 
    when the window is minimised or saved
    """
    global original_seq, compteur, compteur2, list_pattern, list_pattern_sort, \
    bwt, seq_decrypt, list_decrypt, seq_fasta, button, list_decrypt_step
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
    text_step.config(state = NORMAL)
    text_sort.config(state = NORMAL)
    text_step2.config(state = NORMAL)
    sequence.delete("1.0", "end-1c")
    text_step.delete("1.0", "end-1c")
    text_sort.delete("1.0", "end-1c")
    text_step2.delete("1.0", "end-1c")
    lab_file["text"] = ": "

##############################################################################
def hidden():
    """
    This function allows you to empty each window of its widgets each 
    time you close it. This is because I only use two Toplevel windows for all displays
    """
    
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
    button_step2.pack_forget()
    text_step2.pack_forget()
    button_pass2.pack_forget()
    lab_pass2.pack_forget()
    seq_step2.pack_forget()
    title_bwt.pack_forget()
    title_huffman.pack_forget()

##############################################################################    
def error(message:str):
    """
    function to control errors with showwarning. This function asks 
    for the message to be displayed as an argument
    """
    showwarning(title="Error", message = message)

##############################################################################
def creation_directory(directory:str):
    """
    This function allows you to factor out the verification 
    for the creation of the results file
    """
    if path.isdir(directory):
        pass
    else:
        mkdir(directory)
##############################################################################
def destroy():
    """
    This function defines the protocol to be executed when closing the main window
    """
    win_no_step.quit()
    win_step.quit()
    main_win.destroy()

##############################################################################
def red_cross_win_no_step():
    """
    Manages the closing of the window without step through the cross
    """
    hidden()
    win_no_step.withdraw()
    delete_var()

##############################################################################    
def red_cross_win_step():
    """
    Manages the closing of the window with step by step cross
    """
    hidden()
    win_step.withdraw()
    delete_var()
    
##############################################################################
def recovery_dict(dict_string:str):
    """
    Transform a string as a python dictionary in a file into a real python object dict
    """
    char = " {}'\""
    for characterspecial in char:
        dict_string = dict_string.replace(characterspecial,"")
    dict_string = dict_string.split(",")
    i=0
    while i < len(dict_string):
        binary_dict[dict_string[i].split(":")[0]] = dict_string[i].split(":")[1]
        i += 1
    return binary_dict

##############################################################################
def check_dollars(sequence_file:str):
    """
    This function allows to know if the file sequence is encrypted or normal
    """
    for character in sequence_file:
        if character == "$":
            return True    
    return False

##############################################################################    
def bwt_check(buttonId:str):
    """
    This function makes it possible to recover for each of the buttons where 
    the sequence to be analysed comes from. In this case it is for 
    the "Encryption" and "Decryption" buttons
    """
    global  button
    global original_seq, list_pattern, list_pattern_sort, seq_fasta
    global seq_decrypt, list_decrypt, bwt, list_decrypt_step
    button = buttonId
    if button == "Encryption":
        if sequence.get("1.0", "end-1c") != "" :
            original_seq = sequence.get("1.0", "end-1c")
        elif seq_fasta != "":
            original_seq = seq_fasta
        elif path.exists("Results/decrypt_sequence.txt"):
            with open("Results/decrypt_sequence.txt", "r") as file_encrypt:
                original_seq = file_encrypt.readline().strip()
        elif path.exists("Results/decompress_sequence.txt"):
            with open("Results/decompress_sequence.txt", "r") as file_decomp:
                test_seq = file_decomp.readline().strip()
                if check_dollars(test_seq) == False:
                    original_seq = test_seq
                else:
                    original_seq = ""
                    error("Please give a sequence to encrypted")
        else:
            error("Please give a sequence to encrypted")
        #This condition makes it possible to decide whether to launch the analysis or not
        if original_seq != "":
            list_pattern, list_pattern_sort, bwt = cryptage(original_seq.upper())
    elif button == "Decryption":
        if path.exists("Results/encrypt_sequence.txt"):
            with open("Results/encrypt_sequence.txt", "r") as file_decrypt:
                bwt = file_decrypt.readline().strip()
                seq_decrypt, list_decrypt, list_decrypt_step = decryptage(bwt)
        elif path.exists("Results/decompress_sequence.txt"):
            with open("Results/decompress_sequence.txt", "r") as file_decomp2:
                test_seq = file_decomp2.readline().strip()
                if check_dollars(test_seq) == True:
                    bwt = test_seq
                else:
                    error("The encryption file does not exist")
        #This function makes it possible to recover for each of the buttons where the sequence to be analysed comes from.
        if bwt != "":
            seq_decrypt, list_decrypt, list_decrypt_step = decryptage(bwt)
                
        else:
            error("The encryption file does not exist")
                
##############################################################################
def huffman_check(buttonId:str):
    """
    This function makes it possible to recover for each of the buttons where 
    the sequence to be analysed comes from. In this case it is for 
    the "Compression" and "Decompression" buttons
    """
    global button, seq_fasta, origin_seq
    global given_sequence, binary_sequence, binary_dict, add_zero
    global decompress_seq, compress_seq
    button = buttonId
    if button == "Compression":
        if sequence.get("1.0", "end-1c") != "" :
            origin_seq = sequence.get("1.0", "end-1c")
        elif seq_fasta != "":
            origin_seq = seq_fasta
        elif path.exists("Results/encrypt_sequence.txt"):
            with open("Results/encrypt_sequence.txt", "r") as file_encrypt:
                origin_seq = file_encrypt.readline().strip()
        elif path.exists("Results/decrypt_sequence.txt"):
            with open("Results/decrypt_sequence.txt", "r") as file_decrypt:
                origin_seq = file_decrypt.readline().strip()
        elif path.exists("Results/decompress_sequence.txt"):
            with open("Results/decompress_sequence.txt", "r") as file_decompression:
                origin_seq = file_decompression.readline().strip()
        else:
            error("Please give a study sequence")
        #This condition makes it possible to decide whether to launch the analysis or not
        if origin_seq != "":
            given_sequence, binary_dict, compress_seq, add_zero, binary_sequence = compression_huffman(origin_seq.upper())
    elif button == "Decompression" :
        if path.exists("Results/compress_sequence.txt") and path.exists("Results/add_compress_sequence.txt"):
            with open("Results/compress_sequence.txt", "r", encoding="utf-8") as file_compression:
                process_file = file_compression.readline()
                compress_seq = process_file.replace("\n", "")
            with open("Results/add_compress_sequence.txt", "r") as file_annexe:
                process_file2 = file_annexe.readlines()
                add_zero = int(process_file2[0].strip())
                dico_string = process_file2[1]
                recovery_dict(dico_string)
                binary_sequence, decompress_seq = decompression_huffman(compress_seq, add_zero, binary_dict)
        else:
            error("No file for decompression analysis")
            
###############################################################################
def duo_check(buttonId:str):
    """
    This function makes it possible to recover for each of the buttons where 
    the sequence to be analysed comes from. In this case it is for 
    the "Encryption/Compression" and "Decompression/Decryption" buttons
    """
    global button, seq_fasta, origin_seq
    global bwt, list_pattern, list_pattern_sort
    global given_sequence, binary_dict, compress_seq, add_zero, binary_sequence
    global decompress_seq, seq_decrypt, list_decrypt, list_decrypt_step
    button = buttonId
    if button == "Encryption/compression":
        if sequence.get("1.0", "end-1c") != "" :
            origin_seq = sequence.get("1.0", "end-1c")
        elif seq_fasta != "":
            origin_seq = seq_fasta
        elif path.exists("Results/decrypt_sequence.txt"):
            with open("Results/decrypt_sequence.txt", "r") as file_encrypt:
                origin_seq = file_encrypt.readline().strip()
        elif path.exists("Results/decompress_decrypt_sequence.txt"):
            with open("Results/decompress_decrypt_sequence.txt", "r") as file_duo:
                origin_seq = file_duo.readline().strip()
        else:
            error("Please give a study sequence")
        #This condition makes it possible to decide whether to launch the analysis or not
        if origin_seq != "":
            list_pattern, list_pattern_sort, bwt = cryptage(origin_seq.upper())
            given_sequence, binary_dict, compress_seq, add_zero, binary_sequence = compression_huffman(bwt)
    elif button == "Decompression/decryption":
        if path.exists("Results/encrypt_compress_sequence.txt") and path.exists("Results/add_encrypt_compress_sequence.txt"):
            with open("Results/encrypt_compress_sequence.txt", "r", encoding="utf-8") as file_duo2:
                process_file = file_duo2.readline()
                compress_seq = process_file.replace("\n", "")
            with open("Results/add_encrypt_compress_sequence.txt", "r") as file_duo_annexe:
                process_file2 = file_duo_annexe.readlines()
                add_zero = int(process_file2[0].strip())
                dico_string = process_file2[1]
                binary_dict = recovery_dict(dico_string)
            #This condition makes it possible to decide whether to launch the analysis or not
            if compress_seq != "" and add_zero != None and binary_dict != {}:
                binary_sequence, decompress_seq = decompression_huffman(compress_seq, add_zero, binary_dict)
                seq_decrypt, list_decrypt, list_decrypt_step = decryptage(decompress_seq)
            else:
                error("Please re-encrypt/re_compress")
        else:
            error("No file for decompression analysis")            
###############################################################################
def display_step_encrypt():
    """
    Display of the first encryption step of the sequence
    """
    global compteur, compteur2
    global list_pattern, list_pattern_sort, bwt
    text_step.configure(height = compteur2 , width = len(list_pattern[0]))
    text_step.insert("1.0", list_pattern[compteur] + "\n")
    text_step.delete("end-1c")
    text_step.config(state = DISABLED)
    text_sort.config(state = NORMAL)
    text_sort.insert(str(compteur2) + ".0", list_pattern_sort[compteur] + "\n")
    text_sort.tag_configure('red', foreground='red')
    text_sort.tag_add('red', str(compteur2) + '.' + str(len(bwt)-1))
    text_sort.config(state = DISABLED)
    button_step.configure(text="Next BWT", command= next_bwt)
    button_step.pack()
    text_step.pack(padx=2)
    compteur += 1
    compteur2 += 1
    
##############################################################################
def display_step_decrypt():
    """
    Display of the first step of the decoding of the sequence
    """
    global seq_decrypt, list_decrypt, compteur, compteur2, list_decrypt_step
    for i in range(0, len(seq_decrypt)+1, 1):
        text_step.configure(height = i+1 , width = i+1, state = NORMAL)
        text_step.insert( str(i+1) + "." + str(len(list_decrypt_step[i])), list_decrypt_step[compteur][i] + "\n")
    text_step.delete("end-1c")
    text_step.configure(state=DISABLED)
    button_step.config(text= "Next BWT", command=next_bwt)
    button_step.pack()
    text_step.pack(padx=2)
    compteur += 1        

##############################################################################
def display_step_comp():
    """
    Display of the first step of the sequence compression
    """
    global list_compress, compteur_huffman, compteur_huffman2
    text_step2.configure(height = 15 , width = 100, state = NORMAL)
    text_step2.insert(str(compteur_huffman2) + ".0", list_compress[compteur_huffman] + "\n")
    text_step2.configure(state = DISABLED)
    button_step2.configure(text = "Next Huffman", command=next_huffman)
    button_step2.pack()
    text_step2.pack(padx=2)
    compteur_huffman += 1
    compteur_huffman2 += 2
    
##############################################################################
def display_step_decomp():
    """
    Display of the first step in the decompression of the sequence
    """
    global list_decompress, compteur_huffman2, compteur_huffman
    text_step2.configure(height = 10, width= 100, state = NORMAL)
    text_step2.insert(str(compteur_huffman2) + ".0", list_decompress[compteur_huffman] + "\n")
    text_step2.configure(state = DISABLED)
    button_step2.configure(text = "Next Huffman", command=next_huffman)
    button_step2.pack()
    text_step2.pack(padx=2)
    compteur_huffman += 1
    compteur_huffman2 += 2
        
##############################################################################
def encryption():
    """
    This function allows you to decide for encryption which window should be 
    displayed according to the selected radio button
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
            title_bwt.pack()
            button_pass_final.configure(text = "Pass", command = pass_step_bwt)
            button_pass_final.pack()
            display_step_encrypt()
            
        
##############################################################################
def decryption():
    """
    This function allows you to decide for decryption which window 
    should be displayed according to the selected radio button
    """
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
            title_bwt.pack()
            button_pass_final.configure(text = "Pass", command = pass_step_bwt)
            button_pass_final.pack()
            display_step_decrypt()
            
        

##############################################################################
def compression():
    """
    This function allows to decide for the compression which window should be 
    displayed according to the selected radio button
    """
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
            title_huffman.pack()
            display_step_comp()
            button_pass2.configure(text = "Pass", command = pass_step_huffman)
            button_pass2.pack()

##############################################################################
def decompression():
    """
    This function allows to decide for the decompression which window should be 
    displayed according to the selected radio button
    """
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
            title_huffman.pack()
            display_step_decomp()
            button_pass2.configure(text = "Pass", command = pass_step_huffman)
            button_pass2.pack()
                
##############################################################################
def encrypt_compress():
    """
    Display of the first step of the encryption/compression duo of the sequence
    """
    global compteur, compteur2, compteur_huffman, compteur_huffman2
    global original_seq, list_pattern, list_pattern_sort, bwt
    global given_sequence, binary_sequence, compress_seq, list_compress
    compteur_huffman2 = 1
    button_press = encrypt_compress["text"]
    duo_check(button_press)
    if bwt != "":
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
            button_pass_final.configure(text = "Pass", command = pass_duo)
            button_pass_final.pack()
            title_bwt.pack()
            display_step_encrypt()
            title_huffman.pack()
            display_step_comp()
            
            
##############################################################################
def decompress_decrypt():
    """
    Affichage de la première étape du duo décompression /décryptage de la séquence
    """
    global compteur, compteur2
    global compress_seq, decompress_seq, binary_sequence, list_decompress
    global seq_decrypt, list_decrypt
    button_press = decompress_decryp["text"]
    duo_check(button_press)
    list_decompress = ["Your compressed sequence: \n" + compress_seq,
                           "Your binary sequence: \n"+ binary_sequence,
                           "Your decompressed sequence: \n", decompress_seq]
    text_step.delete("1.0", "end-1c")
    if compress_seq != "" :
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
            title_huffman.pack()
            display_step_decomp()
            title_bwt.pack()
            display_step_decrypt()
            button_pass_final.configure(text = "Pass", command = pass_duo)
            button_pass_final.pack()
       
############################################################################### 
def next_bwt():
    """
    Function to display the encryption/decryption step by step of the sequence of interest
    """
    global button, compteur, compteur2
    global list_pattern, list_pattern_sort, bwt
    global list_decrypt, seq_decrypt, list_decrypt_step
    if button == "Encryption" or button == "Encryption/compression":
        text_step.config(state = NORMAL)
        text_step.configure(height = compteur2, width = len(list_pattern[0]))
        text_step.insert(str(compteur2) + ".0", list_pattern[compteur] + "\n")
        text_step.delete("end-1c")
        text_step.config(state = DISABLED)
        text_sort.config(state = NORMAL)
        text_sort.insert(str(compteur2) + ".0", list_pattern_sort[compteur] + "\n")
        text_sort.tag_configure('red', foreground='red')
        text_sort.tag_add('red', str(compteur2) + '.' + str(len(bwt)-1))
        text_sort.config(state = DISABLED)
        if compteur == len(list_pattern)-1:
            if button == "Encryption":
                button_step.configure(text = "Trier", command = result_bwt)
            else:
                button_step.configure(text = "Trier", command = result_duo_bwt)
            button_pass_final.pack_forget()
    elif button == "Decryption" or button == "Decompression/decryption":
        text_step.configure(state = NORMAL)
        text_step.delete("1.0", "end-1c")
        for position in range(0, len(seq_decrypt)+1, 1):
            text_step.configure(state = NORMAL)
            text_step.insert(str(position+1) + "." + str(0), list_decrypt_step[compteur][position] + "\n")
        text_step.delete("end-1c")
        text_step.config(state= DISABLED)
        if compteur == len(list_decrypt_step)-1:
            if button == "Decryption":
                button_step.config(text="Result", command = result_bwt)
            else:
                button_step.configure(text = "Trier", command = result_duo_bwt)
            button_pass_final.pack_forget()
    compteur += 1
    compteur2 += 1
            
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def result_bwt():
    """
    Display of the last step of the encryption/decryption of the BW transform of the sequence of interest
    """
    global compteur, button
    global list_decrypt, seq_decrypt, list_pattern_sort, bwt
    hidden()
    title_bwt.pack()
    lab_step.pack()
    seq_step.pack()
    button_step.pack()
    if button == "Encryption":
        text_sort.config(state = NORMAL)
        text_sort.delete("end-1c")
        text_sort.configure(height = compteur,
                            width = len(list_pattern_sort[0]),  
                            state = DISABLED)
        lab_step.configure(text = "Here is your encrypted sequence: ")
        seq_step.configure(text = bwt, fg = "red")
        button_step.configure(text = "Save", command = save_bwt)
        text_sort.pack()
    elif button == "Decryption":
        line = 0
        for elt in list_decrypt:
            if elt[-1] == "$":
                line += list_decrypt.index(elt) + 1
        text_step.configure(state=NORMAL)
        text_step.tag_configure('red', foreground='red')
        text_step.tag_add('red', str(line) + ".0", str(line) + "." + str(len(list_decrypt)))
        text_step.configure(state = DISABLED)
        button_step.configure(text="Save", command=save_bwt)
        lab_step.configure(text = "Votre séquence décryptée: ")
        seq_step.configure(text = seq_decrypt, fg="red")
        text_step.pack()

##############################################################################
def next_huffman():
    """
    Function to display the step-by-step compression/decompression of the sequence of interest
    """
    global button, compteur_huffman, compteur_huffman2
    global list_decompress, list_compress
    if button == "Compression" or button == "Encryption/compression":
        text_step2.configure(state=NORMAL)
        text_step2.insert(str(compteur_huffman2) + ".0", list_compress[compteur_huffman] + "\n" )
        text_step2.configure(state = DISABLED)
        if compteur_huffman == len(list_compress[0:-1])-1:
            if button == "Compression":
                button_step2.configure(text = "Result", command = result_huffman)
                button_pass2.pack_forget()
            else:
                button_step2.configure(text = "Result", command = result_duo_huffman)
                button_pass2.pack_forget()
    if button == "Decompression" or button == "Decompression/decryption":
        text_step2.configure(state=NORMAL)
        text_step2.insert(str(compteur_huffman2) + ".0", list_decompress[compteur_huffman] + "\n" )
        text_step2.configure(state = DISABLED)
        if compteur_huffman == len(list_decompress[0:-1])-1:
            if button == "Decompression":
                button_step2.configure(text = "Result", command = result_huffman)
                button_pass2.pack_forget()
            else:
                button_step2.configure(text = "Result", command = result_duo_huffman)
                button_pass2.pack_forget()
    compteur_huffman += 1
    compteur_huffman2 += 2 
    
##############################################################################
def result_huffman():
    """
    Final step of Huffman's step-by-step compression/decompression
    """
    global button, list_decompress, compteur_huffman2, list_compress
    hidden()
    title_huffman.pack()
    text_step2.pack()
    button_step2.pack()
    text_step2.configure(state = NORMAL)
    text_step2.delete("end-1c")
    if button == "Compression" :
        text_step2.insert(str(compteur_huffman2-1) + ".0", list_compress[-1])
        text_step2.tag_configure('red', foreground='red')
        text_step2.tag_add('red', str(compteur_huffman2-1) + ".0", str(compteur_huffman2-1) 
                          + "." + str(len(list_compress[-1])))
        
    elif button == "Decompression":
        text_step2.insert(str(compteur_huffman2-1) + ".0", list_decompress[-1])
        text_step2.tag_configure('red', foreground='red')
        text_step2.tag_add('red', str(compteur_huffman2-1) + ".0", str(compteur_huffman2-1) 
                          + "." + str(len(list_decompress[-1])))
    text_step2.configure(state = DISABLED)
    button_step2.configure(text="Save", command=save_huffman)

##############################################################################
def result_duo_bwt():
    """
    Final stage of the Burrows Weeler duo transformation in step by step
    """
    global button, compteur, compteur_huffman2
    global list_decrypt, seq_decrypt, list_pattern_sort, bwt
    global  list_decompress, list_compress, seq_decrypt
    if button == "Encryption/compression":
        hidden()
        text_sort.config(state = NORMAL)
        text_sort.delete("end-1c")
        text_sort.configure(height = compteur,
                            width = len(list_pattern_sort[0]),  
                            state = DISABLED)
        lab_step.configure(text = "Here is your encrypted sequence: ")
        seq_step.configure(text = bwt, fg = "red")
        button_step.configure(text="Save", command = save_duo)
        title_bwt.pack() 
        lab_step.pack()
        seq_step.pack()
        button_step.pack()
        text_sort.pack()
        title_huffman.pack()
        button_step2.pack()
        text_step2.pack()
        
    else:
        line = 0
        for elt in list_decrypt:
            if elt[-1] == "$":
                line += list_decrypt.index(elt) + 1
        text_step.configure(state=NORMAL)
        text_step.tag_configure('red', foreground='red')
        text_step.tag_add('red', str(line) + ".0", str(line) + "." + str(len(list_decrypt)))
        text_step.configure(state = DISABLED)
        button_step.configure(text="Save", command=save_bwt)
        lab_step.configure(text = "Votre séquence décryptée: ")
        seq_step.configure(text = seq_decrypt, fg="red")
        
##############################################################################
def result_duo_huffman():
    """
    Last step of the Huffman duo compression/decompression in step by step
    """
    global button, compteur, compteur_huffman2
    global list_decompress, list_compress, seq_decrypt
    if button == "Encryption/compression":
        text_step2.configure(state=NORMAL)
        text_step2.insert(str(compteur_huffman2-1) + ".0", list_compress[-1])
        text_step2.tag_configure('red', foreground='red')
        text_step2.tag_add('red', str(compteur_huffman2-1) + ".0", str(compteur_huffman2-1) 
                          + "." + str(len(list_compress[-1])))
        text_step2.configure(state=DISABLED)
        button_step2.pack_forget()
    else:
        text_step2.configure(state=NORMAL)
        text_step2.insert(str(compteur_huffman2-1) + ".0", list_decompress[-1])
        text_step2.tag_configure('red', foreground='red')
        text_step2.tag_add('red', str(compteur_huffman2-1) + ".0", str(compteur_huffman2-1) 
                          + "." + str(len(list_decompress[-1])))
        text_step2.configure(state=DISABLED)
    button_step2.pack_forget()
##############################################################################
def loop(list_element:list):
    """
    Factorisation of a redundant loop
    """
    string = ""
    for element in list_element:
        string += element + "\n"
    return string

##############################################################################
def pass_step_bwt():
    """
    Function to skip the steps of the Burrows Weeler transform
    """
    global button, list_pattern_sort, bwt, list_decrypt, seq_decrypt
    string_bwt = ""
    if button == "Encryption" :
        string_bwt = loop(list_pattern_sort)
        lab_pass.configure(text=string_bwt.strip())
        lab_step.configure(text="Votre séquence encryptée: ")
        seq_step.configure(text= bwt, fg="red")        
    elif button == "Decryption":
        string_bwt = loop(list_decrypt)
        lab_pass.configure(text=string_bwt.strip())
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
    
    
##############################################################################
def pass_step_huffman():
    """
    Function to skip the Huffman compression/decompression steps
    """
    global button, list_compress, list_decompress
    string_huffman = ""
    if button == "Compression":
        string_huffman = loop(list_compress[0:-1])
        lab_pass2.configure(text=string_huffman.strip())
        seq_step2.configure(text= list_compress[-1], fg="red")
    elif button == "Decompression":
        string_huffman = loop(list_decompress[0:-1])
        lab_pass2.configure(text=string_huffman.strip())
        seq_step2.configure(text= list_decompress[-1], fg="red")
    button_pass2.configure(text = "Save", command = save_huffman)
    lab_pass2.pack()
    seq_step2.pack()
    button_step2.pack_forget()
    text_step2.pack_forget()
    
##############################################################################
def pass_duo():
    """
    Function to skip steps when combining two actions
    """
    global list_pattern_sort, bwt, list_decrypt, seq_decrypt
    global button, list_compress, list_decompress
    hidden()
    string_bwt = ""
    string_huffman = ""
    button_pass_final.configure(text="Save", command=save_duo)
    button_pass_final.pack()
    if button == "Encryption/compression":
        string_bwt = loop(list_pattern_sort)
        string_huffman = loop(list_compress[0:-1])
        lab_pass.configure(text=string_bwt.strip())
        lab_step.configure(text="Votre séquence encryptée: ")
        seq_step.configure(text= bwt, fg="red")
        lab_pass2.configure(text=string_huffman.strip())
        seq_step2.configure(text= list_compress[-1], fg="red")
        title_bwt.pack()
        lab_pass.pack()
        lab_step.pack()
        seq_step.pack()
        title_huffman.pack()
        lab_pass2.pack()
        seq_step2.pack()
    else:
        string_bwt = loop(list_decrypt)
        string_huffman = loop(list_decompress[0:-1])
        lab_pass2.configure(text=string_huffman.strip())
        seq_step2.configure(text= list_decompress[-1], fg="red")
        lab_pass.configure(text=string_bwt.strip())
        lab_step.configure(text="Votre séquence encryptée: ")
        seq_step.configure(text= seq_decrypt, fg="red")
        title_huffman.pack()
        lab_pass2.pack()
        seq_step2.pack()
        title_bwt.pack()
        lab_pass.pack()
        lab_step.pack()
        seq_step.pack()
        
##############################################################################
def save_bwt():
    """
    Function for saving the encryption and decryption 
    of the Burrows Weeler Transform to a file
    """
    global button, seq_decrypt, original_seq, bwt
    creation_directory("Results")
    if button == "Encryption":
        with open("Results/encrypt_sequence.txt", "w") as file:
                file.write(bwt)
    elif button == "Decryption" or button == "Decompression/decryption":
        with open("Results/decrypt_sequence.txt", "w") as file:
                file.write(seq_decrypt)
    hidden()
    win_no_step.withdraw()
    win_step.withdraw()
    delete_var()

##############################################################################
def save_huffman():
    """
    Function for saving the Huffman compression and decompression to a file
    """
    global button, compress_seq, add_zero, binary_dict, decompress_seq
    creation_directory("Results")
    if button == "Compression":
        with open("Results/compress_sequence.txt", "w", encoding="utf-8") as file2:
            file2.write(compress_seq)
        with open("Results/add_compress_sequence.txt", "w") as file3:
            file3.write(str(add_zero) + "\n" + str(binary_dict))
    elif button == "Decompression":
        with open("Results/decompress_sequence.txt", "w") as file2:
            file2.write(decompress_seq)
    hidden()
    win_no_step.withdraw()
    win_step.withdraw()
    delete_var()
    
##############################################################################
def save_duo():
    global button, compress_seq, add_zero, binary_dict, seq_decrypt
    creation_directory("Results")
    if button == "Encryption/compression":
         with open("Results/compress_sequence.txt", "w", encoding="utf-8") as file2:
            file2.write(compress_seq)
         with open("Results/add_compress_sequence.txt", "w") as file3:
            file3.write(str(add_zero) + "\n" + str(binary_dict))
         with open("Results/encrypt_compress_sequence.txt", "w", encoding="utf-8") as file_duo:
            file_duo.write(compress_seq)
         with open("Results/add_encrypt_compress_sequence.txt", "w") as file_duo2:
            file_duo2.write(str(add_zero) + "\n" + str(binary_dict))
    else:
         with open("Results/decompress_decrypt_sequence.txt", "w") as file_duo3:
                file_duo3.write(seq_decrypt)
    hidden()
    win_no_step.withdraw()
    win_step.withdraw()
    delete_var()
##############################################################################
def browse():
    """
    This function allows you to enter a fasta sequence for the study
    """
    global seq_fasta
    Filetypes= [('text files', '.fasta'),('all files', ['.fa', '.txt'])]
    name_file = askopenfilename(title="Open your document", filetypes= Filetypes)
    seq_fasta = ""
    lab_file["text"] = ": "
    if name_file:
        with open(name_file, "r") as file:
            for line in file:
                if line[0] != ">":
                    seq_fasta += line.strip()
            lab_file["text"] = lab_file.cget("text") + name_file.split("/")[-1]

    

    

#Creating the main window and its configuration
main_win = Tk()
main_win.title("Projet_Algo")
main_win.geometry()
main_win.resizable(width=False, height=False)
color = "#5bc2eb"
main_win.configure(bg=color)
main_win.protocol("WM_DELETE_WINDOW", destroy)

#Creation and element of the "no step" window
win_no_step=Toplevel(main_win)
win_no_step.title("No Step")
win_no_step.withdraw()
seq_no_step = Label(win_no_step)
seq_no_step2 = Label(win_no_step)
button_no_step = Button(win_no_step, text="Save")
win_no_step.protocol("WM_DELETE_WINDOW", red_cross_win_no_step)

#Creation and element of the window "with step".
font = font.Font(size = 14, weight = "bold")
win_step = Toplevel(main_win)
win_step.title("With step")
win_step.withdraw()
text_step = Text(win_step)
text_step2 = Text(win_step)
text_sort = Text(win_step)
title_bwt = Label(win_step, text = "The steps BWT", font=font)
title_huffman = Label(win_step, text = "The steps Huffman", font=font)
button_step = Button(win_step, width=20)
button_step2 = Button(win_step, width = 20)
button_pass_final = Button(win_step, text="Pass", width = 20)
button_pass2 = Button(win_step, text="Pass", width = 20)
lab_pass = Label(win_step, text="")
lab_pass2 = Label(win_step, text="")
lab_step = Label(win_step)
seq_step = Label(win_step)
seq_step2 = Label(win_step)
win_step.protocol("WM_DELETE_WINDOW", red_cross_win_step)

#global variable bwt
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

#global variable huffman
origin_seq = ""
given_sequence = ""
binary_sequence = ""
binary_dict = {}
compress_seq = ""
decompress_seq = ""
add_zero = 0
list_compress = []
list_decompress = []

#Main window widgets
step = StringVar()
step.set("no step")
no_step = Radiobutton(main_win, text= "No step", variable=step, value="no step", bg = color, font=font, activebackground = color)
with_step = Radiobutton(main_win, text= "With step", variable=step, value="with step", bg= color, font=font, activebackground = color)
sequence = Text(main_win, width = 30, height = 5)
browse = Button(main_win, text="Open file", command=browse)
lab_file = Label(main_win, text=": ", bg = color)
encryption = Button(main_win, text= "Encryption", command= encryption)
compression =  Button(main_win, text="Compression", command = compression)
decompression =  Button(main_win, text="Decompression", command = decompression)
decryption = Button(main_win, text="Decryption", command = decryption)
encrypt_compress = Button(main_win, text="Encryption/compression", command = encrypt_compress)
decompress_decryp = Button(main_win, text="Decompression/decryption", command = decompress_decrypt)
space1 = Label(main_win, bg = color)
space2 = Label(main_win, bg= color)
space3 = Label(main_win, bg = color)
space4 = Label(main_win, bg = color)
space5 = Label(main_win, bg = color)

#Creating the grid to place the widgets in the main window
no_step.grid(row = 0, column = 1, columnspan = 2)
with_step.grid(row = 0, column = 4, columnspan = 2)
space1.grid(row = 1, column = 0, columnspan= 7, sticky="we")
sequence.grid(row = 2, rowspan = 3, column = 2, columnspan= 3)
space2.grid(row=5, column = 0, columnspan = 7, sticky="we")
browse.grid(row=6, column=0, columnspan=3, sticky="we", padx = 5)
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

#Launching the main window and its Toplevels
main_win.mainloop()
