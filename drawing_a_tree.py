#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 10:31:41 2021

@author: bartlomiejgasyna
"""

"""prints out a tree with a crown of height specified by user with a trunk being rounded fifth of that value"""


import math
print('how high you want the crown to be?')
height = int(input())


s = [" "*(height-i-1)+'*'*(2*i+1) for i in range(height)]

for i in s: print(i)

    
for i in range(math.ceil(height/5)):
    print(' '*(height-1)+'|')
