L =[]
with open(r'D:\\test.txt') as inf:
    for line in inf:
        line = line.strip()
        L.append(line)

lst = []
for i in range(1, len(L)):
    if L[i-1] < 'A' and L[i] < 'A':
        L[i-1]+=L[i]
        L.pop(i)
        L.insert(i,'')
for i in L:
    if i == '':
        L.remove('')
        continue
    if i < 'A':
       int(i)
for i in range(0,len(L),2):
    x = L[i]*int(L[i+1])
    lst.append(x)
    
with open(r'D:\\result.txt', 'w') as ouf:
    ouf.write("''.join(lst)")