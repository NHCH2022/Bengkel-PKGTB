#!/usr/bin/env python

import random

def main():
    """Start a gases guessing game."""
    print("Guess the name!")

    gases = [
        "Helium",
        "Argon",
        "Krypton",
        "Xenon",
        "Neon",
        "Radon",
        "Oganesson"
        ]

    x = random.choice(gases)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What element am I thinking of? "))

        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got wrong answer. Please try again!".format(guess))

main()