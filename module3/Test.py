import re
import requests

res1 = input()

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
resp = requests.get(res1).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text