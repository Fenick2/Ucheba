s1, s2 = input(), input()
o1, o2 = input(), input()
tab, bat = {}, {}

for i in range(len(s1)):
    tab[s1[i]] = s2[i]
    bat[s2[i]] = s1[i]

for i in o1:
    if i in tab:
        print(tab[i], sep ='', end='')
print()
for i in o2:
    if i in bat:
        print(bat[i], sep='', end='')