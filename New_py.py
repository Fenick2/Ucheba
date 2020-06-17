x = int(input())
y = 2
a = 0
while y < x:
    if x % y == 0:
        a = 1
        break
    y += 1
if a:
    print('Составное')
else:
    print('Простое')