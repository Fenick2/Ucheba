import requests

numbers = []
with open('/home/kolya/Ucheba/ucheba/module3/dataset_24476_3.txt') as inf:
    for line in inf.readlines():
        numbers.append(int(line.strip()))

for url in numbers:
    api_url = f'http://numbersapi.com/{url}/math?json=true'
    res = requests.get(api_url)
    ans = res.json()
    if ans['found']:
        print('Interesting')
    else:
        print('Boring')