# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:50:31 2021

@author: Thierry et Diana
"""


from class_tree import Tree
from class_tree import Node



###############################################################################
def frequency(sequence:str):
    """
    Fonction permettant de calculer la fréquence de chaque caractère dans la séquence
    """
    dict_element= {}
    for element in sequence:
        if element.upper() in dict_element:
            dict_element[element.upper()] += 1
        else:
            dict_element[element.upper()] = 1
    return dict_element

##############################################################################

def sort_dico(dict_element_first:dict):
    """
    Function that sorts the dictionary to put the frequency values in ascending order
    """
    dict_element_second = {}
    for keys, value in sorted(dict_element_first.items(), key=lambda x: x[1]):
        dict_element_second[keys] = value
    return dict_element_second

##############################################################################
def creation_list_node(dict_element_second:dict):
    """
    Creating the node list of our sequence characters
    """
    list_node = []
    for key, value in dict_element_second.items():
        list_node.append(Node(value, key))
    return list_node

##############################################################################
def binary_transformation(sequence:str, binary_dict:dict):
    """
    Function that transforms our sequence into a binary sequence
    """
    binary_sequence = ""
    for letter in sequence:
        binary_sequence += str(binary_dict[letter])
    return binary_sequence
    
##############################################################################    
def compression(binary_sequence:str):
    """
    function that transforms our binary string into a special character string
    """
    compressed_sequence = ""
    calcul_byte =(len(binary_sequence) % 8)
    if calcul_byte != 0:
        binary_sequence = (8 - calcul_byte)*'0' + binary_sequence
    """    
    Add the missing 0's at the beginning of the string so that its length 
    is divisible by 8 without remainder
    """
    for byte in range(0, len(binary_sequence), 8):
        compressed_sequence += chr(int(binary_sequence[byte:byte+8], 2))
    return (compressed_sequence, calcul_byte)

##############################################################################
def decompression(compressed_sequence:str):
    """
    function that transforms our compressed string of special characters 
    back into a binary sequence
    """
    decompressed_sequence=""
    for character in compressed_sequence:
        decompressed_sequence += bin(ord(character))[2:].zfill(8)
    return decompressed_sequence

##############################################################################
def dict_change(binary_dict:dict):
    """
    This function simplifies the reading of the dictionary by reversing 
    the keys and values for the DNA sequence transformation
    """
    dict_change= {}
    for key, value in binary_dict.items():
        dict_change[value] = key
    return dict_change

##############################################################################
def retransformation(decompressed_sequence:str, binary_dict:dict, calcul_byte:int):
    """
    Function transforming our binary sequence back into our original DNA sequence
    """
    if calcul_byte != 0:
        calcul_byte = (8-calcul_byte)
    decompressed_sequence = decompressed_sequence[calcul_byte:]
    """
    Allows you to remove the zeros added at the beginning of a binary 
    string to make a multiple of 8
    """
    decompress_sequence = ""
    counter = 0
    for position in range(0, len(decompressed_sequence)+1, 1):
        if decompressed_sequence[counter:position] in binary_dict.keys():
            decompress_sequence += binary_dict[decompressed_sequence[counter:position]]
            counter = position
    return decompressed_sequence, decompress_sequence  

#########################################################################################
def compression_huffman(sequence:str):
    """
    Function grouping the different stages of compression
    """
    dico_frequency = frequency(sequence)
    dico_sort = sort_dico(dico_frequency)
    list_leaf = creation_list_node(dico_sort)
    tree = Tree(list_leaf)
    dict_seq_binary = tree.convertion_binaire_arbre()
    seq_trans_binary = binary_transformation(sequence, dict_seq_binary)
    compress_seq, add_binary = compression(seq_trans_binary)
    return sequence, dict_seq_binary, compress_seq, add_binary, seq_trans_binary

########################################################################################
def decompression_huffman(compress_seq:str, add_binary:int, dict_seq_binary:dict):
    """
    Function grouping the different steps of the decompression
    """
    decompressed_seq = decompression(compress_seq)
    dict_bin_change = dict_change(dict_seq_binary)
    seq_decomp, sequence_restored = retransformation(decompressed_seq, dict_bin_change, add_binary)
    return seq_decomp, sequence_restored

#######################################################################################
if __name__ == "__main__":
    selected_sequence = "NNTNACTTNGNNGTTNCCTATACCT"
    origin_seq, dict_binary, sequence, add_binary, seq_bin = compression_huffman(selected_sequence)
    print(origin_seq)
    print(seq_bin)
    print(sequence)
    print(dict_binary)
    seq_decomp_bin, seq_fin= decompression_huffman(sequence, add_binary, dict_binary)
    print(sequence)
    print(seq_decomp_bin)
    print(seq_fin)

      