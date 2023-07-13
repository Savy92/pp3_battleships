import random

#Constants
BOARD_SIZE = 5
NUM_SHIPS = 5

def create_board(size):
    """
    Creates the board game.
    """
    board = []
    for i in range(size):
        board.append(["O"]* size)
    return board


def print_board(board):
    """
    Generates the game board.
    """
    for row in board:
        print(" ".join(row))


def populate_board(board, num_ships):
    """
    Random placement of ships allocated to board.
    """
    size = len(board)
    ships = 0
    while ships < num_ships:
        ship_row = random.randint(0, size - 1)
        ship_col = random.randint(0, size - 1)
        if board[ship_row][ship_col] != "S":
            board[ship_row][ship_col] = "S"
            ships += 1


def validate_guess(guess_row, guess_col, board):
    """
    Checks to see if a guess hits or misses.
    """
    if board[guess_row][guess_col] == "S":
        print("Congratulations! You successfully hit a ship.")
        board[guess_row][guess_col] = "X"
        return True
    elif board[guess_row][guess_col] == "X":
        print("You already guessed that one!")
        return False
    else:
        board[guess_row][guess_col] = "_"
        return False


def computer_guess():
    """
    Generates a random numbers between 0-4 for the computer.
    """
    size = len(board)
    comp_row = random.randint(0, size - 1)
    comp_col = random.randint(0, size - 1)
    