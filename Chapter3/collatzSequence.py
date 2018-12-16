# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:14:51 2018

@author: Nicholas
"""
#collatz
#creating the function          
def collatz(number):
    #even number
   if number % 2 == 0:
       print(number // 2)
       return number // 2
    #odd number
   elif number % 2 == 1:
       result = 3 * number + 1
       print(result)
       return result

n = input("Enter a number: ")
while n != 1:
    n = collatz(int(n))