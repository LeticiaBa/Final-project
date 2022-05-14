def one(n) -> int:
    if n == 1:
        return 1
    else:
        return n + one(n - 1)


def two(num, exp) -> int:
    if exp == 1:
        return num
    else:
        return num * two(num, exp - 1)


def three(n):
    if n == 0:
        return 1
    else:
        print(n, end=' ')
        three(n - 1)
