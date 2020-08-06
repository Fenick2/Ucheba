#print([(x, y) for x in (1, 2, 3, 4) if not x % 2
# for y in ['a', 'b'] if y == 'b'])

total = sum(num * num for num in range(1, 1000))
print(total)