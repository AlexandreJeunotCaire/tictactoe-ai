#!/usr/bin/env python3

"""
Basic functions in order to start a game of tic tac toe
"""

from random import choice

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

def game(first_player):
    """
    A game of tic tac toe
    """
    grid = empty()
    player = first_player
    list_turns_played = {lettre:[range(SIZE, 27)] for lettre in ALPHABET if ALPHABET.index(lettre) < SIZE}
    win = False
    while is_playable(grid):
        show(grid)
        current_turn = ""
        while len(current_turn) != 2 or current_turn[0] not in list_turns_played \
              or int(current_turn[1]) in list_turns_played[current_turn[0]]:
            current_turn = input("It's {} turn. Please enter a valid combination to play.\n"
                                .format(PLAYER[player])).upper()
        list_turns_played[current_turn[0]].append(int(current_turn[1]))
        grid[ALPHABET.index(current_turn[0])][int(current_turn[1])] = player
        if is_won(grid):
            print("Well played ! {} wins ;-)".format(PLAYER[player]))
            win = True
            break
        player = not player
    if not win:
        print("Oh... That's a draw!")
    show(grid)

def tictactoe():
    """
    Play several games
    """
    wants_to_play = True
    random_player = True
    first_game = True
    player = True

    while wants_to_play:
        print("Time to play!")
        if not first_game:
            random_player = "y" == input("Do you want a random player to start ? Y/N\n").lower()
        if random_player:
            player = choice((True, False))
        game(player)
        player = not player
        wants_to_play = "y" == input("Play again? Y/N\n").lower()
    print("Bye!")

if __name__ == "__main__":
    tictactoe()
