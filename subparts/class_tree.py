# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:56:04 2021

@author: Thierry Galliano
"""

class Node:
    """
    This class creates objects of type Node, elements for 
    the creation of a binary tree
    """
    def __init__(self, freq:int, letter=None, zero=None, one=None ):
        """
        Initialization of the attributes of the Node object
        """
        self.name = letter
        #Character of the sequence if it is a leaf otherwise None
        self.freq = freq
        #Value of the frequency of characters for a sheet or the sum of the frequencies
        self.zero_son = zero
        #link to the left node
        self.one_son = one
        #link to the right node
    def node_leaf(self):
        """
        This function allows to test if a node is a leaf or not
        """
        return self.zero_son is None and self.one_son is None
    def __repr__(self):
        """
        This function allows you to define what should be displayed when calling a node
        """
        if self.node_leaf():
            return self.name
        return str(self.freq) + " 0: [" + str(self.zero_son) + "]" + " 1: [" + str(self.one_son) + "]"
    def conversion_binaire(self, binary_path):
        """
        This function returns the path taken in the tree to reach a node in string 0 or 1
        """
        if self.node_leaf():
            return self.name + ':' + str(binary_path) + '\n'
        else:
            path = self.zero_son.conversion_binaire(str(binary_path) + '0')
            path += self.one_son.conversion_binaire(str(binary_path) + '1')
            #path determined by recursion
        return path


class Tree:
    """
    Cette classe crée des Arbres binaires
    """
    def __init__(self, liste_leaf):
        """
        Initialization of the list of nodes that constitute the tree
        """
        list_leaf = liste_leaf
        while len(list_leaf) != 1:
            first_node = list_leaf[0]
            second_node = list_leaf[1]
            new_node =  Node(first_node.freq + second_node.freq,
                               None, first_node, second_node)
            del list_leaf[1]
            del list_leaf[0]
            position = 0
            for index in range(0, len(list_leaf), 1):
                if new_node.freq >= list_leaf[index].freq:
                    position += 1
            list_leaf.insert(position, new_node)           
        self.root = list_leaf[0]
        #root attribute of the tree giving us the whole tree
    def __repr__(self):
        """
        Tree display function
        """
        return "Arbre: { " + str(self.root) + " }"
    def convertion_binaire_arbre(self):
        """
        Function to create the binary dictionary by assembling the binary paths of the Nodes
        """
        binary_code = self.root.conversion_binaire('')
        binary_dict = {}
        binary_code = binary_code.strip().split("\n")
        for element in binary_code:
            binary_dict[element.split(":")[0]] = element.split(":")[1]
        return binary_dict
        
    

        

       