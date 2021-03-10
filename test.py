# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:48:58 2021

@author: Thierry et Diana
"""

with open("my_save.txt", "r") as file:
    line_1 = file.readlines()[1].strip()
    print(line_1)