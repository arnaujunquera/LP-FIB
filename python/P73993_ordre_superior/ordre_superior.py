from functools import reduce


def evens_product(L):
    return reduce(lambda acc, y: acc*y if y % 2 == 0 else acc, L, 1)


def reverse(L):
    return reduce(lambda a, x: [x] + a, L, [])


def zip_with(f, L1, L2):
    return [f(i, j) for i, j in zip(L1, L2)]


def count_if(f, L):
    return len(list(filter(f, L)))
