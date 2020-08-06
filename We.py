def hanoi(x: int):
    if x == 1:
        return 1
    return hanoi(x - 1) * 2 + 1


print(hanoi(9.0))
