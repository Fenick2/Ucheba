'''Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
'''
#1
rez = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        rez += i
print(rez)

#2
print(sum(x for x in range(1000) if x%3==0 or x%5==0))
