from functools import reduce

def fctrl(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(fctrl(15))

def fctrl(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr
    

print(fctrl(13))
