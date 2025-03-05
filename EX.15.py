"""
Crear el joc de tres en ratlla i que permeti jugar a un jugador contra la màquina o a dos jugadors.
import random
"""
import random

def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def player_move(board, player):
    move = int(input(f"Jugador {player}, tria una casella (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player
    else:
        print("La casella ja està ocupada. Tria una altra.")
        player_move(board, player)

def ai_move(board):
    move = random.choice([i for i, spot in enumerate(board) if spot == ' '])
    board[move] = 'O'

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def is_draw(board):
    return all(spot != ' ' for spot in board)

def tic_tac_toe():
    board = create_board()
    print_board(board)
    current_player = 'X'

    mode = input("Tria un mode de joc (1: Un jugador, 2: Dos jugadors): ")

    while True:
        if mode == '1' and current_player == 'O':
            ai_move(board)
        else:
            player_move(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"El jugador {current_player} ha guanyat!")
            break
        elif is_draw(board):
            print("És un empat!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()