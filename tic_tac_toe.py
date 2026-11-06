"""
Tic-Tac-Toe Game in Python
Play 2-Player (X vs O) or Single-Player vs Computer.
"""

import math
import random


def print_board(board):
    """Prints the current state of the 3x3 board."""
    print()
    for row in range(3):
        print(f" {board[row*3]} | {board[row*3 + 1]} | {board[row*3 + 2]} ")
        if row < 2:
            print("---+---+---")
    print()


def print_instructions():
    """Prints board position layout instructions."""
    print("\nPositions are numbered from 1 to 9 as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")


def check_winner(board, player):
    """Checks if the given player ('X' or 'O') has won."""
    win_combinations = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)


def is_board_full(board):
    """Returns True if the board has no empty spaces remaining."""
    return all(cell in ['X', 'O'] for cell in board)


def get_available_moves(board):
    """Returns a list of available index positions (0-8)."""
    return [i for i, cell in enumerate(board) if cell not in ['X', 'O']]


def minimax(board, depth, is_maximizing, ai_player, human_player):
    """Minimax algorithm for the unbeatable AI."""
    if check_winner(board, ai_player):
        return 10 - depth
    if check_winner(board, human_player):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = ai_player
            score = minimax(board, depth + 1, False, ai_player, human_player)
            board[move] = str(move + 1)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = human_player
            score = minimax(board, depth + 1, True, ai_player, human_player)
            board[move] = str(move + 1)
            best_score = min(score, best_score)
        return best_score


def get_best_move(board, ai_player, human_player):
    """Finds the optimal move for the AI using minimax."""
    best_score = -math.inf
    best_move = None

    for move in get_available_moves(board):
        board[move] = ai_player
        score = minimax(board, 0, False, ai_player, human_player)
        board[move] = str(move + 1)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def get_player_move(board, player_symbol):
    """Prompts the player for a move and validates input."""
    while True:
        try:
            choice = input(f"Player {player_symbol}, enter position (1-9): ").strip()
            move = int(choice) - 1
            if move < 0 or move > 8:
                print("Invalid input! Please enter a number between 1 and 9.")
            elif board[move] in ['X', 'O']:
                print("That spot is already taken. Choose another one.")
            else:
                return move
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def play_game():
    """Main game loop."""
    print("=" * 35)
    print("       WELCOME TO TIC-TAC-TOE       ")
    print("=" * 35)
    print("Choose game mode:")
    print("1. 2 Players (Player X vs Player O)")
    print("2. 1 Player (You vs Computer AI)")

    mode = ""
    while mode not in ['1', '2']:
        mode = input("Enter 1 or 2: ").strip()

    vs_computer = (mode == '2')
    human_player = 'X'
    ai_player = 'O'

    while True:
        # Initialize empty board with position numbers 1-9
        board = [str(i + 1) for i in range(9)]
        current_player = 'X'

        print_instructions()

        while True:
            print_board(board)

            if vs_computer and current_player == ai_player:
                print(f"Computer ({ai_player}) is thinking...")
                move = get_best_move(board, ai_player, human_player)
                print(f"Computer chose position {move + 1}")
            else:
                move = get_player_move(board, current_player)

            board[move] = current_player

            # Check if current player won
            if check_winner(board, current_player):
                print_board(board)
                if vs_computer and current_player == ai_player:
                    print(f"Computer ({ai_player}) wins! Better luck next time!")
                else:
                    print(f"Congratulations! Player {current_player} wins! 🎉")
                break

            # Check for a tie
            if is_board_full(board):
                print_board(board)
                print("It's a draw! 🤝")
                break

            # Switch turns
            current_player = 'O' if current_player == 'X' else 'X'

        # Play again prompt
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing! Goodbye!\n")
            break


if __name__ == "__main__":
    play_game()
