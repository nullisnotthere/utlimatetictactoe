"""
Sylvan Final, Dylan Pizura project, ultimate TicTac toe. 
The current working version of this game is using unicode symbols, 
which may not render on all systems, especially Windows, but are worth a shot

"""


def print_board(board):
    print("\n" * 2)
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

    print("\n" * 2)


if __name__ == "__main__":
    # example board is a 2d array
    board = [["x" for _ in range(9)] for _ in range(9)]
    print_board(board)
