'''Как поэлементно суммировать списки.
'''
from operator import add


list1=[1, 2, 3]
list2=[4, 5, 6]

print(list(map(add, list1, list2)))
print(tuple(sum(x) for x in zip(list1, list2)))
