#!/usr/bin/python

# this script generates a hello world program, and also a random card from a deck of cards

import random

print("Hello World!")

# generate a random card from a deck of cards

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]


def main():

    card = random.randint(1, 13)

    suit = random.choice(suits)

    print(card, suit)


if __name__ == "__main__":
    main()
