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


def polute_ships(board):
    """
    Random placement of ships allocated to board.
    """
    for ship in range(NUM_SHIPS):
        ship_row, ship_col = randint(0, BOARD_SIZE), randint(0, BOARD_SIZE)
        while board[ship_row][ship_col] == SHIPS
        ship_row, ship_col = randint(0, BOARD_SIZE), randint(0, BOARD_SIZE)
        board[ship_row][ship_col] = SHIPS






