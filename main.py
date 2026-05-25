"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Ilona Svatošová
email: svatosova.ilona88@gmail.com
"""
from datetime import datetime

print ("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")

import random

def create_secret(length):
    """
    :param length: length of secret number
    :return: scret number
    """
    digits = list(range(10))
    secret = ""
    while len(secret)!=length:
        index = random.randint(0, len(digits)-1)  # Náhodné číslo mezi 1 a 10
        if len(secret) == 0 and index ==0:
            continue
        secret=secret+str(digits.pop(index))
    return secret


def start_game():
    """
    maim method
    """
    secrets_length = 4
    secrets=create_secret(secrets_length)
    attempt=None
    attempt_number = 0
    while secrets != attempt :
        attempt_number = attempt_number + 1
        print("-----------------------------------------------")
        attempt=input("Enter number: ")
        print("-----------------------------------------------")
        if len(attempt) != secrets_length:
            print("The number must have exactly 4 digits.")
            continue
        if not attempt.isdigit():
            print("Enter digits only.")
            continue
        if attempt[0] == '0':
            print("The number must not start with zero.")
            continue
        if len(set(attempt)) != secrets_length:
            print("The number must not contain repeating digits.")
            continue

        digits_to_compare = list(zip(attempt, secrets))
        bulls = sum([ a == b for (a,b) in digits_to_compare])

        cows=sum([x in secrets for x in attempt])-bulls
        print("bulls", bulls,",cows",cows)

    print("Correct, you've guessed the right number in",attempt_number,"guesses!")

if __name__ == '__main__':
    while True:
        start_time = datetime.now();
        start_game()
        end_time = datetime.now();

        print("Your time is: ", end_time - start_time)

        restart=input("Do you want to play again? (y/n): ")
        if restart.lower() == 'n':
            break
