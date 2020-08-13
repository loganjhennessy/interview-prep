# place n queens on an n x n board
# recursively backtracking to check extensions as they are made
def is_valid(board):
    # check if current board is valid
    i = len(board) - 1
    for j in range(i):
        if i - j == abs(board[i] - board[j]):
            return False
    return True

def extend(board, n):
    # extend if possible, return if done
    if len(board) == n:
        print(board)
        exit()

    for k in range(n):
        if k not in board:
            board.append(k)

            if is_valid(board):
                extend(board, n)

            board.pop()

n = 8 
board = []
extend(board, n)
