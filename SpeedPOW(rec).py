def pow(a: float, n: int):
    if n == 0:
        return 1
    if n < 0:
        return 1 / pow(a, -n)
    if n % 2 == 1:
        return pow(a, n - 1) * a
    else:
        return pow(a, n // 2) * pow(a, n//2)


print(pow(3, -5))
