# prune
import sys

def nquene(n):
    return helper(n, 0, init_board(n))

def helper(n, i, board):
    if i == n:
        pprint(board)
        print("= " * n)
        return

    for j in range(n):
        if valid(i, j, board):
            board[i][j] = "Q"
            helper(n, i+1, board)
            board[i][j] = "."

def valid(x, y, board):
    return valid_col(x, y, board) and valid_upleft(x, y, board) and valid_upright(x, y, board)

def valid_col(x, y, board):
    return all(board[i][y] == '.' for i in range(x))

def valid_upleft(x, y, board):
    i, j = x - 1, y - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i, j = i - 1, j - 1
    return True
    
def valid_upright(x, y, board):
    n = len(board)
    i, j = x - 1, y + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i, j = i - 1, j + 1
    return True

def init_board(n):
    return [["."] * n for i in range(n)]

def pprint(board):
    for l in board:
        print(" ".join(l))

nquene(int(sys.argv[1]))
