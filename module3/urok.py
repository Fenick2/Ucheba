import re, sys

'''Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
'''
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"[\b\\B]cat[\b\\B]", line):
        print(line)

'''Выведите строки, содержащие две буквы "z", между которыми ровно три символа.'''
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r".*z.{3}z.*", line):
        print(line)

'''Выведите строки, содержащие слово, 
состоящее из двух одинаковых частей (тандемный повтор).
'''
print(*[line.rstrip() for line in sys.stdin if re.search(r"\b(\w+)\1\b", line)], sep='\n')

'''В каждой строке замените все вхождения подстроки "human"
на подстроку "computer" и выведите полученные строки.
'''
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"human", r"computer", line))

'''В каждой строке замените первое вхождение слова,
состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
'''
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b[aA]+\b", "argh", line, count=1))

'''В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
'''
for line in sys.stdin:
	line = line.rstrip()
	print(re.sub(r"\b(\w)(\w)", r"\2\1", line))

'''В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
'''
for line in sys.stdin:
	line = line.rstrip()
	print(re.sub(r"(\w)\1+", r"\1", line))

