"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Ilona Svatošová
email: svatosova.ilona88@gmail.com
"""
from venv import __main__

print ("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")

import random
def create_secret(length):
    cifry = list(range(10))
    secret = ""
    while len(secret)!=length:
        index = random.randint(0, len(cifry)-1)  # Náhodné číslo mezi 1 a 10 
        if len(secret) == 0 and index ==0:
            continue
        secret=secret+str(cifry.pop(index))
    return secret

#test
#tajemstvi="2017"

def start_game():
    tajemstvi=create_secret(4)

    print("---------------------------------------")

    print(tajemstvi)

    pokus=None
    cislo_pokusu = 0
    while tajemstvi != pokus :
        cislo_pokusu = cislo_pokusu + 1
        pokus=input("Enter number: ")
        if len(pokus) != 4:
            print("The number must have exactly 4 digits.")
            continue
        if not pokus.isdigit():
            print("Enter digits only.")
            continue
        if pokus[0] == '0':
            print("The number must not start with zero.")
            continue
        if len(set(pokus)) != 4:
            print("The number must not contain repeating digits.")
            continue

        porovnani_pole = list(zip(pokus, tajemstvi))
        bulls = sum([ a == b for (a,b) in porovnani_pole])

        cows=sum([x in tajemstvi for x in pokus])-bulls
        print("bulls", bulls,",cows",cows)

    print("Correct, you've guessed the right number in",cislo_pokusu,"guesses!")

if __name__ == '__main__':
    start_game()