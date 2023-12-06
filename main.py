"""
Sylvan Final, Dylan Pizura project, ultimate TicTac toe. 
The current working version of this game is using unicode symbols, 
which may not render on some systems, especially Windows, but are worth a shot
"""
# I imported this in order to make it more clear that the board is an array of arrays
from typing import List
from enum import Enum
import random


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


def player_turn(x, y):
    #print mark
 '''   
123
456
789

147
258
369

159
357
'''  
def win(d):
    for v in d.values():
        if 1 in lst:
            if 2 in lst:
                if 3 in lst:
                    return win = True
            if 4 in lst:
                if 7 in lst:
                    return win = True
            if 5 in lst:
                if 9 in lst:
                    return win = True
        if 2 in lst:
            if 5 in lst:
                if 8 in lst:
                    return win = True
        if 3 in lst:
            if 5 in lst:
                if 7 in lst:
                    return win = True
            if 6 in lst:
                if 9 in lst:
                    return win = True
        if 4 in lst:
            if 5 in lst:
                if 6 in lst:
                    return win = True
        if 7 in lst:
            if 8 in lst:
                if 9 in lst:
                    return win = True
        return False
    
    


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

    p1_MOVES_DCT = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[]}
    p2_MOVES_DCT = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[]}
    
    while False:
        PLAYER_STATUS = input("Will you be playing with a "second player" or against the "computer"?")
        FIRST_MOVE_GRID = 10
        while FIRST_MOVE_GRID not in range(1, 10):
            FIRST_MOVE_GRID = int(input("Pick a grid for your first move (1-9)."))
        P1_FIRST_MOVE = 10
        while P1_FIRST_MOVE not in range(1, 10):
            P1_FIRST_MOVE = int(input("Pick a spot in grid {FIRST_MOVE_GRID} for your first move (1-9)."))
        player_turn(FIRST_MOVE_GRID, P1_FIRST_MOVE) #Makes Move
        p1_MOVES_DCT[f'{FIRST_MOVE_GRID}'].append(P1_FIRST_MOVE) #Records Play
        if PLAYER_STATUS.lower() == "second player": 
            P2_FIRST_MOVE = 10
            while P2_FIRST_MOVE not in range(1, 10):
                P2_FIRST_MOVE = int(input("Player 2, pick a spot in grid {P1_FIRST_MOVE} for your first move (1-9)."))
            player_turn(P1_FIRST_MOVE, P2_FIRST_MOVE)
            p2_MOVES_DCT[f'{P1_FIRST_MOVE}'].append(P2_FIRST_MOVE)
            P2_FIRST_MOVE = PREVIOUS_MOVE
            while Win = False:
                P1_MOVE = 10
                while P1_MOVE not in range(1, 10):
                    P1_MOVE = int(input("Player 1, pick a spot in grid {PREVIOUS_MOVE} for your next move (1-9)."))
                player_turn(PREVIOUS_MOVE, P1_MOVE)
                p1_MOVES_DCT[f'PREVIOUS_MOVE'].append(P1_MOVE)
                P1_MOVE = PREVIOUS_MOVE
                P2_MOVE = 10
                while P2_MOVE not in range(1, 10):
                    P2_MOVE = int(input("Player 2, pick a spot in grid {PREVIOUS_MOVE} for your next move (1-9)."))
                player_turn(PREVIOUS_MOVE, P2_MOVE)
                p2_MOVES_DCT[f'PREVIOUS_MOVE'].append(P2_MOVE)
                P2_MOVE = PREVIOUS_MOVE
        elif PLAYER_STATUS.lower() == "computer":
            True
    
    while PLAYER_STATUS.lower() == "computer":
        P2_FIRST_MOVE = random.randint(range(1, 10))
        player_turn(P1_FIRST_MOVE, P2_FIRST_MOVE)
        P2_FIRST_MOVE = PREVIOUS_MOVE
        while Win = False:
            P1_MOVE = 10
            while P1_MOVE not in range(1, 10):
                P1_MOVE = int(input("Player 1, pick a spot in grid {PREVIOUS_MOVE} for your next move (1-9)."))
            player_turn(PREVIOUS_MOVE, P1_MOVE)
            p1_MOVES_DCT[f'PREVIOUS_MOVE'].append(P1_MOVE)
            P1_MOVE = PREVIOUS_MOVE
            P2_MOVE = random.randint(range(1, 10))
            player_turn(PREVIOUS_MOVE, P2_MOVE)
            p2_MOVES_DCT[f'PREVIOUS_MOVE'].append(P2_MOVE)
            P2_MOVE = PREVIOUS_MOVE
        
        
        

    
    
