def isogr(x):
    c = 0
    for i in x.lower():
        c = x.count(i)
        if c >= 2:
            print('not isogramma')
            return 
    print('isogramma')
    return

a = 'asdjfhgitu'
b = 'dndndjkfkv va'
isogr(a)
isogr(b)