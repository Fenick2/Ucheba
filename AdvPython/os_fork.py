import time, os

pid = os.fork()

if pid == 0:
    while True:
        print(f'child: {os.getpid()}')
        time.sleep(5)
else:
    print(f'parent: {os.getpid()}')
    os.wait()
