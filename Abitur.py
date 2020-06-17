sp = []
sr = []
sr1 = 0
sr2 = 0
sr3 = 0
with open(r'D:\Progr\dataset_3363_4.txt') as inf:
    for line in inf:
        line = line.strip().split(';')
        sp.append(line)

for i in sp:
    sr.append((int(i[1])+int(i[2])+int(i[3])) / 3)
    sr1 += int(i[1])
    sr2 += int(i[2])
    sr3 += int(i[3])

sr1 = str(sr1/len(sp))
sr2 = str(sr2/len(sp))
sr3 = str(sr3/len(sp))
sp2 =str(sr1 + ' ' + sr2 + ' ' + sr3)
sr.append(sp2)

with open(r'D:\Progr\dataset_3363_4.txt', 'w') as inf:
    for i in sr:
        print(i, file=inf)
