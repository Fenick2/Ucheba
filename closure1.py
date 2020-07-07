def multiply(x):
    def inner(y):
        return x * y
    return inner


f = multiply(2)
print(f(15))
