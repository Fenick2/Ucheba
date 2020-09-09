def spis(a, lv=1):
    print(*a, 'level= ', lv)
    for i in a:
        if type(i) == list:
            spis(i, lv + 1)


s = [1, 2, 3, [1, [2, 3, [4, 1, 5], 5], 3], 2, [3, 4]]
spis(s)
