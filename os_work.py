import os

s = set()
for a, b, c in os.walk('main'):
    for f in c:
        if f.endswith('.py'):
            s.add(a)

with open('res.txt', 'w') as r:
    for line in sorted(s):
        r.write(line + '\n')
