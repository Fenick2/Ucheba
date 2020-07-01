import re
import requests

res1 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
res2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

pattern = r"http.*html"
tx = requests.get(res1).text
adr = re.findall(pattern.strip(), tx)

adr2 = []
for i in adr:
    tx2 = requests.get(i).text
    adr2.extend(re.findall(pattern.strip(), tx2))

print('Yes' if res2 in adr2 else 'No')
