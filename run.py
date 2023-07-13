import random

#Constants
BOARD_SIZE = 5
NUM_SHIPS = 5

def create_board(BOARD_SIZE):
    """
    Creates the board game.
    """
    board = []
    for i in range(BOARD_SIZE):
        board.append(["O"] * BOARD_SIZE)
    return board


def print_board(board):
    """
    Generates the game board.
    """
    for row in board:
        print(" ".join(row))


def populate_board(board):
    """
    Random placement of ships allocated to board.
    """
    ships = 0
    while ships < NUM_SHIPS:
        ship_row = random.randint(0, BOARD_SIZE - 1)
        ship_col = random.randint(0, BOARD_SIZE - 1)
        if board[ship_row][ship_col] == "O":
            board[ship_row][ship_col] = "S"
            ships += 1


def validate_guess(board):
    """
    Checks players guess to check to see if it's a hit or miss.
    """
    print("Your turn")
    while True:
        try:
            guess_row = int(input("Enter the row coordinate (0-4): "))
            guess_col = int(input("Enter the col coordinate (0-4): "))
            if 0 <= x and x < BOARD_SIZE and 0 <= y and y < BOARD_SIZE:
                if board[guess_row][guess_col] == "S":
                    print("Congratulations! You successfully hit a ship.")
                    board[guess_row][guess_col] = "X"
                elif board[guess_row][guess_col] == "O":
                    print("You missed!")
                    board[guess_row][guess_col] = "_"
                else:
                    print("You already guessed this location.")
                    break
            else:
                print("Invalid choice, please try again..")
        except ValueError:
            print("Invalid input, Try again.")


def computer_guess(board):
    """
    Generates computer's guess.
    """
    print("Computers turn")
    while True:
        comp_row = random.randint(0, BOARD_SIZE - 1)
        comp_col = random.randint(0, BOARD_SIZE - 1)
        if board[comp_row][comp_col] == "S":
            print("The enemy has destroyed one of your ships!")
            board[comp_row][comp_col] = "X"
            break
        elif board[comp_row][comp_col] == "O":
            print("The enemy has missed.")
            board[comp_row][comp_col] = "_"
            break


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
        show_rules()

def game_over(board):
    """
    Checks to see if it's game over, if no "S" remain in the rows.
    """
    for row in board:
        if "S" in row:
            return False
    return True


def play_game(board):
    player_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)


def main():
    """
    Main menu which provides user with two options.
    """
    user_name = input("Please enter a username: ")
    while(True):
        print()
        print(f"\nWELCOME TO BATTLESHIPS!..{user_name} \n")
        print("    1 START GAME\n")
        print("    2. RULES\n")

        option = input("Enter your choice (1/2): ")

        if option == "1":
            game_board = create_board(BOARD_SIZE)
            populate_board(game_board, NUM_SHIPS)
            play_game(game_board)
        elif option == "2":
            show_rules()
        else:
            print("\nInvalid option, please choose from 1 to start the game, or 2 to see the rules.")
        

main()