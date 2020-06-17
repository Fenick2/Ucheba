a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
x = [[0 for j in range(len(a[i]))] for i in range(len(a))]
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = a[i-1][j] + a[i-len(a)+1][j] + a[i][j-1] + a[i][j-len(a[i])+1]
for i in x:
    print(*i)
