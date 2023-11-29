"""
Sylvan Final, Dylan Pizura project, ultimate TicTac toe. 
The current working version of this game is using unicode symbols, 
which may not render on some systems, especially Windows, but are worth a shot
"""
# I imported this in order to make it more clear that the board is an array of arrays
from typing import List
from enum import Enum


# I used this enum to define the different states a space could be
class Player(Enum):
    X = "X"
    O = "O"
    EMPTY = " "


# I made this to represent the different ways that you can win
WIN_PATTERNS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


# pass this function a board, and it will tell you if X, O, or neither wins
def check_win(board: List[Player]) -> Player:
    for pattern in WIN_PATTERNS:
        # the pattern object is an array indicies, checking that all indicies are the same will tell us if someone has three in a row
        if all([board[i] == Player.X for i in pattern]):
            return Player.X
        elif all([board[i] == Player.O for i in pattern]):
            return Player.O

    return Player.EMPTY


# prints that board, given a 2d array (an array of arrays), the outer array represents the big board, and the innner the smaller boards


def print_board(board: List[List[Player]]):
    # This print statement adds some blank space before the board
    print("\n" * 2)

    # This is a kinda confusing quadrupal nested for loop, but basically it just prints out all the squares in the board,
    # but adds some dividers on every third square so that it looks nice
    for y in range(3):
        for x in range(3):
            for k in range(3):
                for j in range(3):
                    print(f" {board[k + (y * 3)][j + (x * 3)].value} ", end="")

                if k != 2:
                    print("│", end="")
            print()

        if y != 2:
            print("─────────┼" * 2, end="")
            print("─────────")

    # This print statement adds some blank space after the board
    print("\n" * 2)


if __name__ == "__main__":
    # here is what making a big board and printing it looks like
    board = [[Player.X for _ in range(9)] for _ in range(9)]
    print_board(board)

    # this is just so that I could check the check win function. You can mess with what is x / o and what is empty to get different results
    lil_board = [
        Player.X, Player.EMPTY, Player.EMPTY,
        Player.X, Player.EMPTY, Player.EMPTY,
        Player.X, Player.EMPTY, Player.EMPTY,
    ]
    print(f"{check_win(lil_board).value} wins")

    while False:
        PLAYER_STATUS = input("Will you be playing with a "second player" or against the "computer"?")
        if PLAYER_STATUS.lower() == "second player":
            FIRST_MOVE_GRID = 10
            while FIRST_MOVE_GRID not in range(1, 10):
                FIRST_MOVE = input("Pick a grid for your first move (1-9).")
            while 
        elif PLAYER_STATUS.lower() == "computer":
            True

    
    


