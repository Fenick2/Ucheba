d = [input() for i in range(int(input()))]
l = [[i.lower() for i in input().split()] for j in range(int(input()))]
v = set()
for i in l:
    for j in i:
        if j not in d:
            v.add(j)
for i in v:
    print(*i)

    text = set([j for i in range(int(input())) for j in input().lower().split()])