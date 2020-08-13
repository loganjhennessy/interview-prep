def reverse_bits(x):
    y = 0
    while x:
        y <<= 1
        y |= (x & 1)
        x >>= 1
    return y

print(reverse_bits(6))
