import random

def draw_board(board):
    print("   |   |")
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
    print("   |   |")

def check_win(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def get_computer_move(board):
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board, "O"):
                return i
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                board[i] = "O"
                return i
            board[i] = " "
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            board[i] = "O"
            return i
    if board[4] == " ":
        return 4
    for i in [1, 3, 5, 7]:
        if board[i] == " ":
            return i

def tic_tac_toe():
    board = [" " for _ in range(9)]
    draw_board(board)

    while True:
        player_move = int(input("Enter your move (0-8): "))
        if board[player_move] == " ":
            board[player_move] = "X"
            draw_board(board)
            if check_win(board, "X"):
                print("You win!")
                break
            elif " " not in board:
                print("Tie!")
                break

            computer_move = get_computer_move(board)
            board[computer_move] = "O"
            print("Computer chooses " + str(computer_move))
            draw_board(board)
            if check_win(board, "O"):
                print("Computer wins!")
                break
            elif " " not in board:
                print("Tie!")
                break

if __name__ == "__main__":
    tic_tac_toe()
