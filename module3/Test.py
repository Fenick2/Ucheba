import requests
import re

res1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
res2 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'

def addr(res):
    '''Принимает URL, возвращает список ссылок'''
    pattern = r"<a.*href=(http.*html)\1"
    tx = requests.get(res).text
    adr = (re.findall(pattern, tx))
    return adr


c = addr(res1)
b = []
for ref in c:
    b.extend(addr(ref))
    if res2 in b:
        print('Yes')
        break
    else:
        print('No')
