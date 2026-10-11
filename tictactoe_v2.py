# Name: [Diesta,Macy T.]
# Date: [October 11,2026]
# Course: PROGCON IT261
# File: tictactoe_v2.py
# Description: Human vs. computer Tic-Tac-Toe (3x3), converted from my
#              Flowgorithm file tictactoe_v2_1.fprg.

import random


# Flowgorithm: DisplayBoard(board)
# Prints the 3x3 grid. Positions 1-9 are used (index 0 is not used),
# the same way the flowchart's board array works.
def display_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-+-+-")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-+-+-")
    print(board[7] + " | " + board[8] + " | " + board[9])


# Flowgorithm: GetComputerMove(board)
# Keeps picking a random box from 1 to 9 until it finds an empty one.
def get_computer_move(board):
    valid = False
    while not valid:
        comp_move = random.randint(1, 9)   # Flowgorithm: Random(9) + 1
        if board[comp_move] == " ":
            valid = True
    return comp_move


# Flowgorithm: CheckWinner(board)
# Returns "O" or "X" if a line of three matches, "Draw" if the board is
# full with no winner, otherwise "None".
def check_winner(board):
    result = "None"
    # The 8 winning lines: 3 rows, 3 columns, 2 diagonals
    lines = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7),
    ]
    for a, b, c in lines:
        # A blank space must not count as a win, so check it is not " "
        if board[a] != " " and board[a] == board[b] and board[b] == board[c]:
            result = board[a]

    # Flowgorithm: count filled spaces to detect a draw
    filled_count = 0
    for k in range(1, 10):
        if board[k] != " ":
            filled_count = filled_count + 1
    if result == "None" and filled_count == 9:
        result = "Draw"
    return result


# Flowgorithm: Main
def main():
    # Flowgorithm: set all 9 spaces to blank (index 0 unused)
    board = [" "] * 10
    game_over = False
    winner = "None"

    # Flowgorithm: r = random(2); 0 = user (O) starts, otherwise computer (X)
    r = random.randint(0, 1)
    if r == 0:
        current_player = "O"
    else:
        current_player = "X"

    # Flowgorithm: While gameOver == False
    while not game_over:
        display_board(board)

        if current_player == "O":
            # Human turn: keep asking until the move is valid
            valid_move = False
            while not valid_move:
                print("Enter your move (1-9):")
                text = input()
                if not text.strip().lstrip("-").isdigit():
                    # Extra check: stops a crash if a letter is typed
                    print("Invalid choice! Enter 1-9.")
                    continue
                human_move = int(text)
                if human_move >= 1 and human_move <= 9:
                    if board[human_move] == " ":
                        valid_move = True
                    else:
                        print("Space occupied! Try again.")
                else:
                    print("Invalid choice! Enter 1-9.")
            board[human_move] = "O"
        else:
            # Computer turn
            print("Computer's turn...")
            comp_choice = get_computer_move(board)
            board[comp_choice] = "X"

        # Flowgorithm: winner = CheckWinner(board)
        winner = check_winner(board)
        if winner != "None":
            game_over = True
        else:
            # Switch player
            if current_player == "O":
                current_player = "X"
            else:
                current_player = "O"

    # Flowgorithm: show the final board and the result
    display_board(board)
    if winner == "O":
        print("You win!")
    elif winner == "X":
        print("Computer wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
