'''Как вычислить средневзвешенное значение списка.
'''
cost = [0.424, 0.4221, 0.4185, 0.4132, 0.413]
cases = [10, 20, 30, 40, 50]

print(sum(cost[i] * cases[i] / sum(cases) for i in range(len(cost)))) #1

print(sum(cost[i] * cases[i] for i in range(len(cost))) / sum(cases)) #2

print(sum([x * y for x, y in zip(cost, cases)]) / sum(cases)) #3

for i in range(len(cost)):
    cost[i] = cost[i] * cases[i] / sum(cases)
cost = sum(cost)
print(cost)                                                           #4
