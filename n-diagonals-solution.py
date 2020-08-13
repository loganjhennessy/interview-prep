def is_valid(board, n):
    i = len(board) - 1  # current position

    # check conflicts
    # check left unless we're at left edge
    if i % n > 0:
        # left
        if board[i] + board[i-1] == 3:
            return False

    # check above unless we're at the top edge
    if i // n > 0:
        # above
        if board[i] + board[i-n] == 3:
            return False
        # above left
        if i % n > 0:
            if board[i] == 1 and board[i-n-1] == 1:
                return False
        # above-right
        if (i+1) % n < n:
            if board[i] + board[i-n+1] == 4:
                return False
    return True


def count_diagonals(board):
    count = 0
    for cell in board:
        if cell > 0:
            count += 1
    return count


def extend(board, n, d):
    if len(board) == n**2 and count_diagonals(board) == d:
        for i in range(n):
            row_start = n*i
            row_end = row_start + n
            print(board[row_start:row_end])
        exit()

    if len(board) < n**2:
        for k in [2,1,0]:
            board.append(k)
            if is_valid(board, n):
                extend(board, n, d)
            board.pop()


board = []
n = 5
d = 16
extend(board, n, d)
