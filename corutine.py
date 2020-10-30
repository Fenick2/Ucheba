def cor():
    count = 1
    while True:
        name = yield
        print(f'{name} занял {count} место')
        count += 1


finish = cor()
finish.send(None)
finish.send("Миша")
finish.send("Саша")
