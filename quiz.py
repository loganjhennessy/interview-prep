def change(amount):
    arr = []

    if amount == 5:
        arr == [5]
        return arr
    if amount == 7:
        arr = [7]
        return arr
    if amount == 14:
        arr = [7, 7]
        return arr
    if amount == 21:
        arr = [7, 7, 7]
        return arr
    if amount == 28:
        arr = [7, 7, 7, 7]
        return arr

    #result = change(amount - 5)
    #result.append(5)
    arr = change(amount - 5)
    return arr.append(5)

print(change(49))
