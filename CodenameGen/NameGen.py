#! python3 
#this file will create random combinations of words

import random, os

def namegen(a,b):
    partA = open(a + '.txt').readlines()
    Parta = random.choice(partA)

    partB = open(b + '.txt').readlines()
    Partb = random.choice(partB)

    print(str(Parta).rstrip()+ str(Partb).rstrip())

namegen('Adjective', 'Noun')