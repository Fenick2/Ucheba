def fib_recurs(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib_recurs(k - 1) + fib_recurs(k - 2)


def fib_gen(k):
    a, b = 0, 1
    count = 1

    while count <= k:
        yield b
        count += 1
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(fib_recurs(10))
    print(list(fib_gen(10)))