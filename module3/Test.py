import requests
import re

res1 = 'http://pastebin.com/raw/7543p0ns'

pattern = r'<a[^>]*?(?:href=\"http://)([\w\.\-]*)[^>]*?>'
resp = requests.get(res1).text
cur_resp = set()

for url in re.findall(pattern ,  resp):
    cur_resp.add(url)

lst = list(sorted(cur_resp))

for i in lst:
    print(i)
