import random

#Constants
BOARD_SIZE = 5
NUM_SHIPS = 5
HIDDEN = "O"
SHIPS = "S"
GUESS = "X"

#Create board
board = []
for i in range(BOARD_SIZE):
    board.append([HIDDEN]* BOARD_SIZE)

def print_board(board):
    """
    Generates the starting board.
    """
    for row in board:
        print(" ".join(row))

print_board(board)