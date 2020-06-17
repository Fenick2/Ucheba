d = []
t = {}
with open(r'/home/nick/Загрузки/dataset_3380_5.txt') as inf:
    for l in inf:
        l = l.strip().split()
        d.append(l[::2])

for i in range(1, 12):
    t[str(i)] = []
    
for i in d:
    t.setdefault(i[0], []).append(int(i[1]))

for key, val in t.items():
    if len(t.get(key)) == 0:
        t[key] = ['-']
    else:
        t[key] = [(sum(val) / len(val))]
    print(key, *t[key]) 
