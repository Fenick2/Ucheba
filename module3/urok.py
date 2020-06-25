import csv

lst = []
cnt = 0
crim = ''
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    a = header.index('Primary Type')
    for row in reader:
        if '2015' in row[2]:
            lst.append(row[a])

for i in lst:
    if lst.count(i) > cnt:
        cnt = lst.count(i)
        crim = i

print(crim)
