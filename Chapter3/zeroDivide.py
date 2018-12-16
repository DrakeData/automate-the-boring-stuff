# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:40:42 2018

@author: Nicholas
"""

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))