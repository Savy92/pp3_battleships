from random import randint

#Constants
BOARD_SIZE = 5

#Create board
board = []
for i in range(BOARD_SIZE):
    board.append(["O"]* BOARD_SIZE)


def print_board(board):
    """
    Generates the starting board.
    """
    for row in board:
        print(" ".join(row))


def populate_board(board):
    """
    Random placement of ships allocated to board.
    """
    ships = 5
    while ships > 0:
        ship_row = randint(0, len(board)-1)
        ship_col = randint(0, len(board)-1)
        if board[ship_row][ship_col] != "S":
            board[ship_row][ship_col] = "S"
            ships -= 1
    return board

board_with_ships = populate_board(board)
for row in board_with_ships:
    print(" ".join(row))


def make_guess():
    """
    Provides the player with the option to take a guess.
    """
    while True:
        try:
            row = int(input("Enter a row number (0-4): "))
            col = int(input("Enter a column number (0-4): "))
            if row < 0 or row > 4 or col < 0 or col > 4:
                raise ValueError
            return (row, col)
        except ValueError:
            print("Invalid input, PLease enter a number between 0 and 4.")


def computer_guess():
    """
    Generates a random numbers between 0-4 for the computer.
    """
    row = random.randint(0, 4)
    col = random.randint(0, 4)
    return (row, col)



