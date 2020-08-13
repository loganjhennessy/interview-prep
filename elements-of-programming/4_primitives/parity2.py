# Problem 4.1

def parity(x):
    result = 1
    while x:
        result ^= x & 1
        x >>= 1
    return result

print(parity(5))
print(parity(7))
print(parity(32543245983210))
