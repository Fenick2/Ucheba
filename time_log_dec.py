from time import time

def logging_time(func):
	def logged(*args, **kwargs):
		start_time = time()
		func(*args, **kwargs)
		elapsed = time() - start_time
		print(f'{func.__name__} time elapsed: {elapsed: .5f}')

	return logged


@logging_time
def calculate_integer_square_sum(n):
	return sum(x * x for x in range(n))


# calculate_integer_square_sum(100000)

