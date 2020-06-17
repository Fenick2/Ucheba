import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/603.txt')
t = r.text.splitlines()
print(len(t))
