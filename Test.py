import itertools

s = itertools.islice(range(50), 10, 20)
for x in s:
    print(x)