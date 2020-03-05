#!/usr/bin/env python3

from random import choice

"""
Rules of my tic tac toe
"""

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SIZE = 3 #Will determine the size of the grid. Normally, you play on a 3x3 grid.
PLAYER = {True: 'O', False: 'X', None: ' '}


def empty():
    """
    Creates an empty grid
    """
    return [[None for j in range(SIZE)] for i in range(SIZE)]

def is_playable(grid):
    """
    Tells if it is possible to continue playing on <grid>
    ie: is there an empty case in <grid>?
    """
    return any(None in row for row in grid)

def is_won(grid):
    """
    Tells if the player who just finished is turn won the game
    """
    for row in grid: #First, we check if one of the rows is full of the same symbol
        if all_same(row):
            return True

    for column in columns(grid): #Then, we work on the columns
        if all_same(column):
            return True

    for diag in diagonals(grid): #Finally, we do the same thing on diagonals
        if all_same(diag):
            return True

    return False #If nothing worked before, then it means it's not won

def columns(grid):
    """
    Returns all the columns of the grid (basically the transpose)
    """
    return zip(*grid)

def diagonals(grid):
    """
    Returns both diagonals of the grid
    """
    return [(grid[i][i] for i in range(SIZE)), (grid[i][SIZE - 1 - i] for i in range(SIZE))]

def all_same(iterable):
    """
    Tells if all the elements in an iterable are the same
    """
    shrink = set(iterable)
    return len(shrink) == 1 and not None in shrink
