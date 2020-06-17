a, b, c, d = int(input()), int(input()), int(input()), int(input())
for j in range(c, d+1):
    print('\t', j, '\t', end='')
print()
print()
for i in range(a, b+1):
    print(i, end='')
    for j in range(c, d+1):
        print('\t', i * j, '\t', end='')
    print()