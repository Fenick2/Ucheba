n = int(input())
lst = list(reversed([list(reversed(list(map(int, input().split())))) for i in range(n)]))

for i in range(n):
    for j in range(n):
        print(lst[j][i], '', end='')
    print()
