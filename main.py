"""
Sylvan Franklin, Dylan Pizura
Final project, Ultimate TicTacToe. 
The current working version of this game is using unicode symbols, 
which may not render on some systems, especially Windows, but are worth a shot
"""

# I imported this in order to make it more clear that the board is an array of arrays
from typing import List
from enum import Enum
import sys
import random


# color ANSI escape codes
class fg:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    reset = "\u001b[0m"

CLEAR = "\033[2J"

# I used this enum to define the different states a space could be
class Player(Enum):
    X = "X"
    O = "O"
    EMPTY = " "


class Board:
    def __init__(self, board):
        self.board = board
        self.WIN_STATUS = Player.EMPTY


# I made this to represent the different ways that you can win
WIN_PATTERNS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


# pass this function a board, and it will tell you if X, O, or neither wins


def check_win(board: List[Player]) -> Player:
    for pattern in WIN_PATTERNS:
        # the pattern object is an array indicies, checking that all indicies are the same will tell us if someone has three in a row
        if all([board[i] == Player.X for i in pattern]):
            return Player.X
        elif all([board[i] == Player.O for i in pattern]):
            return Player.O

    return Player.EMPTY


def check_win_board(board) -> Player:
    for pattern in WIN_PATTERNS:
        # the pattern object is an array indicies, checking that all indicies are the same will tell us if someone has three in a row
        if all([board[i].WIN_STATUS == Player.X for i in pattern]):
            return Player.X
        elif all([board[i].WIN_STATUS == Player.O for i in pattern]):
            return Player.O

    return Player.EMPTY


def print_board(board):
    print(CLEAR)
    print("\n" * 2)

    for y in range(3):
        for x in range(3):
            for k in range(3):
                for j in range(3):
                    print(f" {board[k + (y * 3)].board[j + (x * 3)].value} ", end="")

                if k != 2:
                    print("│", end="")
            print()

        if y != 2:
            print("─────────┼" * 2, end="")
            print("─────────")

    print("\n" * 2)


def make_move(active: Player, PREVIOUS_MOVE: int):
    while True:
        cell = 10
        try:
            while cell not in range(1, 10):
                cell = int(
                    input(
                        f"{fg.green}[{active.value} to play]{fg.reset} pick a spot in grid {fg.blue}{PREVIOUS_MOVE}{fg.reset} for your move [1-9]: "
                    )
                )

            break
        except ValueError:
            print(f"{fg.red}Invalid move entered!{fg.reset}")


        target = board[PREVIOUS_MOVE - 1].board[cell - 1]
        if target == Player.EMPTY:
            board[PREVIOUS_MOVE - 1].board[cell - 1] = active

            if check_win(board[PREVIOUS_MOVE - 1].board):
                board[PREVIOUS_MOVE-1].WIN_STATUS = active.value
            return cell

        else:
            print(f"Please enter a {fg.red} NON-EMPTY {fg.reset} cell.")




def make_move_computer(active: Player, PREVIOUS_MOVE: int):
    while True:
        cell = random.randint(1, 9)
        target = board[PREVIOUS_MOVE - 1].board[cell - 1]
        if target == Player.EMPTY:
            board[PREVIOUS_MOVE - 1].board[cell - 1] = active
            if check_win(board[PREVIOUS_MOVE - 1].board):
                board[PREVIOUS_MOVE - 1].WIN_STATUS = active.value
            break

    return cell


def flop_player(player: Player):
    if player == Player.X:
        return Player.O
    return Player.X


if __name__ == "__main__":
    board: List[Board] = [Board([Player.EMPTY for _ in range(9)]) for _ in range(9)]

    while True:
        player_status = input(
            "Will you be playing with a second player locally (L) or against the computer (C)? "
        ).upper()


        if player_status.lower() == "c":

            print_board(board)
            active_player = random.choice((Player.X, Player.O))
            first_move_grid = 10
            while first_move_grid not in range(1, 10):
                first_move_grid = int(input("Pick a grid for your first move [1-9]: "))

            PREVIOUS_MOVE = make_move(active_player, first_move_grid)
            print_board(board)
            active_player = flop_player(active_player)
            Win = False
            while Win == False:
                print_board(board)
                PREVIOUS_MOVE = make_move(active_player, PREVIOUS_MOVE)
                active_player = flop_player(active_player)
                print(check_win_board(board))
                if check_win_board(board) != Player.EMPTY:
                    print(f"{active_player} wins!")
                    Win = True

                print_board(board)
                PREVIOUS_MOVE = make_move_computer(active_player, PREVIOUS_MOVE)
                active_player = flop_player(active_player)
                print(check_win_board(board))
                if check_win_board(board) != Player.EMPTY:
                    print(f"{active_player} wins!")
                    Win = True

            print("Thank you for playing")
            sys.exit()

        elif player_status.lower() == "l":

            print_board(board)
            active_player = random.choice((Player.X, Player.O))
            first_move_grid = 10
            while first_move_grid not in range(1, 10):
                first_move_grid = int(input("Pick a grid for your first move [1-9]: "))
            
            PREVIOUS_MOVE = make_move(active_player, first_move_grid)


            print_board(board)
            active_player = flop_player(active_player)
            PREVIOUS_MOVE = make_move(active_player, PREVIOUS_MOVE)

            Win = False
            while Win == False:

                print_board(board)
                PREVIOUS_MOVE = make_move(active_player, PREVIOUS_MOVE)
                active_player = flop_player(active_player)
                if check_win_board(board) != Player.EMPTY:
                    print(f"{active_player} wins!")
                    Win = True

            print("Thank you for playing")
            sys.exit()
