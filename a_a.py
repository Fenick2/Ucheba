def average_attempts(a, n):
    t = {}
    rez = {}
    for i in a:
        i = list(i)
        del i[1]
        t.setdefault(i[0], []).append(i[1])
    for key, val  in t.items():
        t[key] = round(sum(val) / len(val), 1)
    for i in n:
        if i[0] in t:
            rez[i[1]] = t.get(i[0], 0)
    return rez
