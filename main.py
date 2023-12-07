"""
Sylvan Franklin, Dylan Pizura
Final project, Ultimate TicTacToe. 
More info in README.md
"""

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


# This allows us to attach a win status to an array
class Board:
    def __init__(self, board, win_status):
        self.board = board
        self.WIN_STATUS = win_status


# Different coordinates for a win
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


# checks to see if the board it full and nobody wins
def check_draw():
    if all([[c != Player.EMPTY for c in s] for s in board]):
        print_board(board)
        print("Nobody wins!")
        sys.exit()


# This is the final logic for when a player wins
def win(active):
    print_board(board)
    print(
        f"{fg.blue}{active.value}{fg.reset} Wins! {fg.green}Thank you for Playing{fg.reset}",
    )
    sys.exit()


# pass this function a board, and it will tell you if X, O, or neither wins


def check_win(b: Board) -> Player:
    if b.WIN_STATUS != Player.EMPTY:
        return Player.EMPTY

    for pattern in WIN_PATTERNS:
        # the pattern object is an array indicies, checking that all indicies are the same will tell us if someone has three in a row
        if all([b.board[i] == Player.X for i in pattern]):
            return Player.X
        elif all([b.board[i] == Player.O for i in pattern]):
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
                    status = board[k + (y * 3)].WIN_STATUS
                    cell = board[k + (y * 3)].board[j + (x * 3)]

                    if status == Player.X:
                        if cell == Player.X:
                            print(f" {fg.green}{cell.value}{fg.reset} ", end="")
                        else:
                            print(f" {fg.red}{cell.value}{fg.reset} ", end="")
                    elif status == Player.O:
                        if cell == Player.O:
                            print(f" {fg.green}{cell.value}{fg.reset} ", end="")
                        else:
                            print(f" {fg.red}{cell.value}{fg.reset} ", end="")
                    else:
                        print(f" {cell.value} ", end="")

                if k != 2:
                    print("│", end="")
            print()

        if y != 2:
            print("─────────┼" * 2, end="")
            print("─────────")

    print("\n" * 2)


# get a cell value, that is numeric, in the correct range, and not already taken


def choose_new_board():
    while True:
        try:
            grid = int(input(f"pick a grid for your move [1-9]: "))
            if grid in range(1, 10):
                target = board[grid - 1].board
                if all([c != Player.EMPTY for c in target]):
                    return grid
                else:
                    print("That grid is not empty")
            else:
                print(f"{grid} is not in range [1-9]")

        except ValueError:
            print(f"{fg.red}Invalid move entered!{fg.reset}")


# Player turn function for first and local second player
def make_move(active: Player, PREVIOUS_MOVE: int):
    # special case where board the you are trying to move in is full
    if all([c != Player.EMPTY for c in board[PREVIOUS_MOVE - 1].board]):
        print(f"This board is full, {active.value} pick a new one")
        PREVIOUS_MOVE = choose_new_board()

    while True:
        try:
            cell = int(
                input(
                    f"{fg.green}[{active.value} to play]{fg.reset} pick a spot in grid {fg.blue}{PREVIOUS_MOVE}{fg.reset} for your move [1-9]: "
                )
            )

            if cell in range(1, 10):
                target = board[PREVIOUS_MOVE - 1].board[cell - 1]
                if target == Player.EMPTY:
                    board[PREVIOUS_MOVE - 1].board[cell - 1] = active
                    if check_win(board[PREVIOUS_MOVE - 1]) != Player.EMPTY:
                        board[PREVIOUS_MOVE - 1].WIN_STATUS = active
                    return cell
                else:
                    print(f"{fg.yellow }That cell is not empty {fg.reset}")
            else:
                print(f"{fg.red}{cell} is not in range [1-9]{fg.reset}")

        except ValueError:
            print(f"{fg.red}Invalid move entered!{fg.reset}")


# Player turn function for computer (randomly-generated response)
def make_move_computer(active: Player, PREVIOUS_MOVE: int):
    while True:
        # case where the board is full
        while all(i != Player.EMPTY for i in board[PREVIOUS_MOVE - 1].board):
            PREVIOUS_MOVE = random.randint(1, 9)

        cell = random.randint(1, 9)
        target = board[PREVIOUS_MOVE - 1].board[cell - 1]

        if target == Player.EMPTY:
            board[PREVIOUS_MOVE - 1].board[cell - 1] = active
            if check_win(board[PREVIOUS_MOVE - 1]) != Player.EMPTY:
                board[PREVIOUS_MOVE - 1].WIN_STATUS = active
            break

    return cell


# Switches player characters/turns
def flop_player(player: Player):
    if player == Player.X:
        return Player.O
    return Player.X


# Main body of gameplay
if __name__ == "__main__":
    print(CLEAR)
    board: List[Board] = [
        Board([Player.EMPTY for _ in range(9)], Player.EMPTY) for _ in range(9)
    ]

    while True:
        player_status = input(
            "Will you be playing with a second player locally (L) or against the computer (C)? "
        ).upper()

        # Computer gameplay code
        if player_status.lower() == "c" or player_status.lower == "computer":
            print_board(board)
            active_player = random.choice((Player.X, Player.O))
            PREVIOUS_MOVE = 10

            while PREVIOUS_MOVE not in range(1, 10):
                PREVIOUS_MOVE = int(input("Pick a grid for your first move [1-9]: "))

            while True:
                print_board(board)
                PREVIOUS_MOVE = make_move(active_player, PREVIOUS_MOVE)
                if check_win_board(board) != Player.EMPTY:
                    win(active_player)
                check_draw()

                active_player = flop_player(active_player)
                # active_player = flop_player(active_player)
                PREVIOUS_MOVE = make_move_computer(active_player, PREVIOUS_MOVE)
                if check_win_board(board) != Player.EMPTY:
                    win(active_player)
                check_draw()

                active_player = flop_player(active_player)

        # Local player gameplay
        elif player_status.lower() == "l":
            print_board(board)
            active_player = random.choice((Player.X, Player.O))
            first_move_grid = 10
            while first_move_grid not in range(1, 10):
                first_move_grid = int(input("Pick a grid for your first move [1-9]: "))

            PREVIOUS_MOVE = make_move(active_player, first_move_grid)
            active_player = flop_player(active_player)

            while True:
                print_board(board)
                PREVIOUS_MOVE = make_move(active_player, PREVIOUS_MOVE)

                if check_win_board(board) != Player.EMPTY:
                    win(active_player)
                check_draw()

                active_player = flop_player(active_player)
