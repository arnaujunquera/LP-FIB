def myLength(L):
    lenght = 0
    for i in L:
        lenght += 1
    return lenght

def myMaximum(L):
    maximum = L[0]
    for i in L:
        if i > maximum:
            maximum = i
    return maximum
