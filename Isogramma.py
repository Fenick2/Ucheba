def isogr(x):
    c = 0
    for i in x.lower():
        c = x.count(i)
        if c >= 2:
            return 'not isogramma'
        return 'isogramma'

a = 'asdjfhgitu'
b = 'dndndjkfkv va'
print(isogr(a))
print(isogr(b))
