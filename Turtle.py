n = int(input())
s = {"север": 0, "юг": 0, "запад": 0, "восток": 0}

inf = [input().split() for line in range(n)]
for line in inf:
    s[line[0]] += int(line[1])

print(s['восток'] - s['запад'], s['север'] - s['юг'])
