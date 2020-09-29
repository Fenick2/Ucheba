n = int(input())
triangle = []

for i in range(n+1):
	triangle.append([1]+[0]*n)

for i in range(1, n+1):
	for j in range(1, i+1):
		triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]

for i in range(0, n+1):
	for j in range(0, i+1):
		print(triangle[i][j], end=' ')
	print()


def pascal_triangle(n):
   row = [1]
   y = [0]
   for x in range(max(n, 0)):
      print(*row)
      row = [left + right for left, right in zip(row + y, y + row)]
   
pascal_triangle(6)
