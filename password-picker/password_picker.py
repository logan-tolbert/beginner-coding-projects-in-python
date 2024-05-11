#!/usr/bin/env python3
import random 
import string
'''
Password Picker

This program will create a new simple password 
combining words, numbers, and characters.
The password will be output to the terminal
You can continue to generate passwords until you
find one that you like
'''

# Word bank
adjectives = ['sleepy', 'slow', 'smelly', 
              'wet', 'fat', 'red',
              'orange', 'yellow', 'green',
              'blue', 'purple', 'fluffy',
              'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda']


print('Welcome to Password Picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break
    