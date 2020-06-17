import os

if os.fork():
    print(1, end='')
else:
    print(2, end='')