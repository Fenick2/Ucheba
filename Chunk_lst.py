'''Функция разбивки листа
на равные части.'''
import pprint

# def chunks(lst, chSize):
#     '''Выводит последовательные куски
#     списка размера chSize.'''
#     for x in range(0, len(lst), chSize):
#         yield lst[x:x + chSize]


# pprint.pprint(list(chunks(range(10, 76), 10)))


'''То же с помощью
List comprehentions.'''

lst = range(0, 76)
chunk = 5

x = [lst[i:i + chunk] for i in range(0, len(lst), chunk)]
pprint.pprint(x)
