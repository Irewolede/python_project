def print_board(example_board):
    for i in range(len(example_board)):
        if i % 3 == 0 and i != 0:
            print("......+......+.......")
        for j in range(len(example_board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(example_board[i][j])
            else:
                print(str(example_board[i][j]) + " ", end="")
    



def get_empty_cells(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
            
    return None, None


def get_valid_guess(board, row, col, guess):

    row_num = board[row]
    if guess in row_num:
        return False
    
    col_num = [board[i][col] for i in range(9)]
    if guess in col_num:
        return False
    
    start_row = (row//3) * 3
    start_col = (col//3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == guess:
                return False
            
    return True



def solve_sudoku(board):

    row, col = get_empty_cells(board)

    if row == None:
        return True
    
    for guess in range(1, 10):

        if get_valid_guess(board, row, col, guess):
            board[row][col] = guess

            if solve_sudoku(board):
                return True
            
        board[row][col] = 0

    return False
    

if __name__ == '__main__':
    example_board =  [
        [8, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 3,  6, 0, 0,  0, 0, 0],
        [0, 7, 0,  0, 9, 0,  2, 0, 0],
        [0, 5, 0,  0, 0, 7,  0, 0, 0],
        [0, 0, 0,  0, 4, 5,  7, 0, 0],
        [0, 0, 0,  1, 0, 0,  0, 3, 0],
        [0, 0, 1,  0, 0, 0,  0, 6, 8],
        [0, 0, 8,  5, 0, 0,  0, 1, 0],
        [0, 9, 0,  0, 0, 0,  4, 0, 0],
        ]
    print("solving sudoku.......")
    print_board(example_board)
    print(solve_sudoku(example_board))
    print("solved sudoku>>>>>>")
    print_board(example_board)
