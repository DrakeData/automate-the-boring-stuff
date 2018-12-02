# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:16:49 2018

@author: Nicholas
"""

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')