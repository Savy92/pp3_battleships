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


def computer_guess(board):
    """
    Generates a random numbers between 0-4 for the computer.
    """
    size = len(board)
    comp_row = random.randint(0, size - 1)
    comp_col = random.randint(0, size - 1)


def show_rules():
    """
    Explains the rules of the game to user & allows them to go back to main menu.
    """
    print("\nRULES:\n")
    print("- YOU VS THE COMPUTER.")
    print("- THE OBJECTIVE IS TO SINK ALL OF THE COMPUTER'S BATTLESHIPS.")
    print("- YOU & THE COMPUTER WILL TAKE TURNS IN GUESSING THE POSITION OF THE SHIPS.")
    print("- TOP LEFT CORNER IS ROW: 0, COL: 0")
    print("- 'S' = SHIPS, 'X' = HIT, '_' = MISS")
    print("- FIRST TO SINK ALL OF THE OPPONENTS SHIPS WIN!")
    
    print("\nENTER 'M' TO RETURN TO MAIN MENU..\n")
    back_main_screen = input("Enter here: ")

    if back_main_screen == "M":
        main()
    else:
        print("Invalid option, please enter 'M'..")


def play_game():
    print("Hello, this is were the code for the game will be stored.")


def main():
    """
    Main menu which provides user with two options.
    """
    print("\nWELCOME TO BATTLESHIPS!\n")
    print("    1 START GAME\n")
    print("    2. RULES\n")

    option = input("Enter your choice (1/2): ")

    if option == "1":
        play_game()
    elif option == "2":
        show_rules()
    else:
        print("Invalid option, please choose from 1 to start the game, or 2 to see the rules.")


main()