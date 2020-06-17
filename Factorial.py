def fact(n:int):
    assert n>0, "Факториал отрицательных чисел не определён"
    if n == 0:
        return 1
    fact(n-1) * n
    print(fact(n))


