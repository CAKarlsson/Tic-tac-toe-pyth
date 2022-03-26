# ------- Global Variables -------

board = {0: "-", 1: "-", 2: "-",
         3: "-", 4: "-", 5: "-",
         6: "-", 7: "-", 8: "-"}

game_running = True

current_player = "X"

# ------ Functions --------
def run_game():

    """
    Runs the game
    """


def display_board(board):
    """
    Display board
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


"""
Welcome message
"""
print("\nWelcome to tic-tac-toe!\n\n")
print("How to play: \n")
print("You will each take a turn to place your mark (X or O) on the board. ")
print("Whoever manages to place three marks in a row is the winner.")
print("These underscores is the board positions.")
print("Top left = 1 and bottom right = 9. Pick a number to place your mark.")
print("\n_ _ _")
print("_ _ _")
print("_ _ _\n")
run_game()