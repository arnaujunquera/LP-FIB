def absValue(x):
    return -x if x < 0 else x

def power(x, p):
    res = 1
    for i in range(0, p):
        res *= x
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if (x%i == 0):
            return False
    return True
