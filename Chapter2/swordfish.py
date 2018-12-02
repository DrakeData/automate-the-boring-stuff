# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:07:09 2018

@author: Nicholas
"""

while True:
  print('Who are you?')
  name = input().capitalize()
  if name != 'Joe':
    continue        
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()
  if password == 'swordfish':
    break
print('Access granted.')