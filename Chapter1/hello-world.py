# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:37:01 2018

@author: Nicholas
"""

print('Hello world!')
print('What is your name?')
#ask for name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
#ask for age
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')