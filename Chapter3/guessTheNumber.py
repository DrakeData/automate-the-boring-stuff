# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:46:34 2018

@author: Nicholas
"""

# This is guess the number
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  #This condition is the corret guess!
        
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of wa ' + str(secretNumber))