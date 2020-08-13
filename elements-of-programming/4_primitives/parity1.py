# Problem 4.1

def parity(x):
    count = 0
    while x:
        if x & 1:
            count +=1
        x = x >> 1
    return count % 2 == 0

print(parity(5))
print(parity(7))
print(parity(23984239812))
