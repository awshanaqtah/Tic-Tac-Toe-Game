import  emnist as em
import cv2
from   emnist import  extract_training_samples
import sys
# Node for Depeth first search
# Tic-Tac-Toe Game






board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Board initialization
current_player = 'X'  # Player 1 starts as 'X'

def print_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_win():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]]:
            return True
    return False

def check_draw():
    return all(spot in ['X', 'O'] for spot in board)

def make_move():
    while True:
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                board[move] = current_player
                break
            else:
                print("Invalid move. This spot is already taken or out of range.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def play_game():
    global current_player
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        make_move()
        print_board()

        if check_win():
            print(f"Player {current_player} wins!")
            break

        if check_draw():
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'  # Switch player

if __name__ == "__main__":
    play_game()


