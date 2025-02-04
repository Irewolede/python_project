import random
winner = None
current_player = "x"
board = [" "] * 9

def print_board(board):
    for i in range(3):
        print (" | ".join(board[i * 3 : (i + 1) * 3]))
        if i < 2:
            print("..+...+..")

def get_move(board):
    while True:
        global current_player
        try:
            move = int(input(f"{current_player}'s turn. make a move from 0 - 8:"))
            if move < 0 or move > 8:
                print("invalid move. move should be between 0 - 8")
                continue
            if board[move] != " ":
                print(f"position has been already occupied by {board[move]}")
                continue
            print(f"{current_player} makes a move to board {move}")
            board[move] = current_player
            print_board(board)
            break

        except ValueError:
            print("invalid input! try again.")

def switch_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"
    
def get_computer_move(board):
    global current_player
    if current_player == "o":
        available_move = [i for i in range(9) if board[i] is " "]
        move = random.choice(available_move)
        print(f"{current_player} makes a move to board {move}")
        board[move] = current_player

def get_winner(board):
    global winner
    winners_combo = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [2, 4, 6], [0, 4, 8]
        ]

    for combo in winners_combo:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            winner = board[a]
            return winner

def get_tie(board):
    if " " not in board:
        return True
    

if __name__ == '__main__':
    while True:
        print()
        print_board(board)
        if current_player == "x":
            get_move(board)

        if get_winner(board):
            print(f"{winner} wins")
            print_board(board)
            break
        if get_tie(board):
            print("it's a tie")
            print_board(board)
            break
        switch_player()
        get_computer_move(board)


