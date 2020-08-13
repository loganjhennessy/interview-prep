def towers(n, a, b, c):
    if n == 1:
        c.append(a.pop())
        return

    towers(n-1, a, c, b)
    c.append(a.pop())
    towers(n-1, b, a, c)

n = 5
a = list(range(1, n+1))
b = []
c = []
print('before...')
print(a)
print(b)
print(c)
towers(n, a, b, c)
print('after...')
print(a)
print(b)
print(c)
    
