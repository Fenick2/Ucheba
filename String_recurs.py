def rec(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s[0] + '*' + s[-1]
    return s[0] + '*' + rec(s[1:-1]) + '*' + s[-1]

a = input()
print(rec(a))
