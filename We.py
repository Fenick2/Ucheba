import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
s = r.text

url = 'https://stepic.org/media/attachments/course67/3.6.3/'
while 'We' not in s:
    url2 = url+s
    r = requests.get(url2)
    s = r.text
print(s)
