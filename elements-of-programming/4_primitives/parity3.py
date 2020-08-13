# Problem 4.1

def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


print(parity(5))
print(parity(7))
print(parity(2345720987))
