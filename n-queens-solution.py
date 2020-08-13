# for a square of size n x n, find an arrangement where n queens will
# fit on the board without attacking each other
def is_valid(res):
    i = len(res) - 1
    for j in range(i):
        if i - j == abs(res[i] - res[j]):
            return False
    return True

def extend(res, n):
    if len(res) == n:
        print(res)
        exit()

    for i in range(n):
        if i not in res:
            res.append(i)

            if is_valid(res):
                extend(res, n)

            res.pop()

extend([], 8)

