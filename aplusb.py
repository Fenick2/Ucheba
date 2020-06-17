n, m = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(n)]
x = 0
for i in s:
    a = sum(i)
    if a > x:
        x == a
print(x, s.index(x))