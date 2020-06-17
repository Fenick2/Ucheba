s = (input(''))
x = 0
buk = s[0]
for i in s[0:]:
    if i != buk:
        print(buk + str(x), end='')
        x = 0
    buk = i
    x += 1
print(buk + str(x))
