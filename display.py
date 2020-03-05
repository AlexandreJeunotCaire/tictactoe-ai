#!/usr/bin/env python3

"""
All functions meant to beautify the game
and display the grid
"""

from rules import SIZE, ALPHABET, PLAYER

def separation():
    """
    Visual separation between two lines
    """
    print("\n  +" + (4 * SIZE - 1) * "-" + "+")

def show(grid):
    """
    Visual function in order to make the game look nicer
    """
    print("    ", end="")
    for number in range(SIZE):
        print(number, end="   ")
    separation()
    for i, row in enumerate(grid):
        print('{} |'.format(ALPHABET[i]), end='')
        for elt in row:
            print(' {} '.format(PLAYER[elt]), end='|')
        separation()
