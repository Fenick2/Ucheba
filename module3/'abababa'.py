s = 'abababa'
t = 'aba'
count,i = 0,0
while s.find(t,i) >= 0:
  pos = s.find(t,i)
  count += 1
  i = pos + 1

print(count)

print(sum([s.startswith(t, i) for i in range(len(s)-len(t) + 1)]))