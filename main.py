"""
Sylvan Final, Dylan Pizura project, ultimate TicTac toe. 
The current working version of this game is using unicode symbols, 
which may not render on some systems, especially Windows, but are worth a shot
"""
# I imported this in order to make it more clear that the board is an array of arrays
from typing import List


# prints that board, given a 2d array (an array of arrays), the outer array represents the big board, and the innner the smaller boards
def print_board(board: List[List[str]]):
    # This print statement adds some blank space before the board
    print("\n" * 2)

    # This is a kinda confusing quadrupal nested for loop, but basically it just prints out all the squares in the board,
    # but adds some dividers on every third square so that it looks nice
    for y in range(3):
        for x in range(3):
            for k in range(3):
                for j in range(3):
                    print(f" {board[k+(y*3)][j+(x*3)]} ", end="")

                if k != 2:
                    print("│", end="")
            print()

        if y != 2:
            print("─────────┼" * 2, end="")
            print("─────────")

    # This print statement adds some blank space after the board
    print("\n" * 2)


if __name__ == "__main__":
    # This is the board, which I made with a list comprehension (just a faster way to write:
    # board = [] 
    # for _ in range(9):
    #     sub_board = []
    #     for _ in range(9):
    #         sub_board.append("x")

    #     board.append(sub_board)

    
    board = [["x" for _ in range(9)] for _ in range(9)]
 
    # Here I'm just calling the function, in the future we will do it in a loop with input validation, and update the board state with each move. 
    # For example if we wanted to place an "o", in board 5, space 6 you could do board[5][6] = "o"
    print_board(board)





