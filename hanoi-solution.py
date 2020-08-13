def towers(n, a, b, c, count):
    if n == 1:
        c.append(a.pop())
        return count + 1

    count = towers(n-1, a, c, b, count)
    c.append(a.pop())
    count += 1
    count = towers(n-1, b, a, c, count)
    return count

n = 6
a = list(range(n, 0, -1))
b = []
c = []
print('Before...')
print(a)
print(b)
print(c)
moves = towers(n, a, b, c, 0)
print('After...')
print(a)
print(b)
print(c)
print('Total moves: ' + str(moves))
