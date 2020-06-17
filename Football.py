s = []  # список из ввода
tabl = []  # список из словарей
spis = set() # временное множество
result = {} # сводная таблица (словарь)
with open(r'D:\Progr\Test.txt') as inf:
    for line in inf:
        line = line.strip().split(';')
        line[1], line[3] = int(line[1]), int(line[3])
        s.append(line)

for i in s:  
    p = dict.fromkeys([i[0], i[2]])
    p[i[0]] = i[1]
    p[i[2]] = i[3]
    tabl.append(p)                   # Результат игр
    
for i in tabl:
    for key in i:
        spis.add(key)                # Список команд (временный)
        
for i in spis:
    result[i]=[]                     
    
for k in tabl:
    
     

print(spis); print(result)

#for q, w in tabl.items():
    #print((q+':'), *w, end='\n')
