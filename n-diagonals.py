# put d diagonals on an nxn board
# 0 represents no line
# 1 represents line from TL->BR
# 2 represents line from BL->TR
def is_valid(board, n):
    # check if board is valid and can be extended
    i = len(board) - 1
    
    # check cell to the left
    if i % n > 0:
        if board[i] + board[i-1] == 3:
            return False
    # now check cells above
    if i - n >= 0:
        # directly above
        if board[i] + board[i-n] == 3:
            return False
        # upper-left
        if i % n > 0:
            if board[i] == 1 and  board[i-n-1] == 1:
                return False
        # upper-right
        if (i + 1) % n != 0:
            if board[i] + board[i-n+1] == 4:
                return False
    return True

def count_diagonals(board):
    # count the diagonals on the board
    count = 0
    for cell in board:
        if cell > 0:
            count += 1
    return count

def extend(board, n, d):
    if len(board) == n**2 and count_diagonals(board) == d:
        for i in range(n):
            print(board[i*n:i*n+n])
        exit()
    
    if len(board) < n**2:
        for k in [2,1,0]:
            board.append(k)

            if is_valid(board, n):
                extend(board, n, d)

            board.pop()

n = 5
d = 16
board = []
extend(board, n, d)
