#!/usr/bin/env python3

"""
Basic Tic Tac Toe
"""

from rules import *
from display import show

def game(first_player):
    """
    A game of tic tac toe
    """
    grid = empty()
    player = first_player
    list_turns_played = {lettre:[range(SIZE, 27)]
                         for lettre in ALPHABET if ALPHABET.index(lettre) < SIZE}
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
            random_player = input("Do you want a random player to start ? Y/N\n").lower() == 'y'
        if random_player:
            player = choice((True, False))
        game(player)
        player = not player
        wants_to_play = input("Play again? Y/N\n").lower() == "y"
    print("Bye!")

if __name__ == "__main__":
    tictactoe()
