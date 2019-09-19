def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    i = 0
    total = 0
    product = 0

    if len(array) > 0:
        while i < len(array):
            if i % 2 == 0:
                total += array[i]
            i += 1
        
        product = total * array[-1]

    return product
    

print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
assert checkio([6]) == 36, "(6)*6=36"
assert checkio([]) == 0, "An empty array = 0"