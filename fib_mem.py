import time
from functools import lru_cache


# def fib(num: int) -> int:
# 	if num == 0 or num == 1:
# 		return num
# 	return fib(num-1) + fib(num-2)

# start = time.time()
# fib(40)
# print(f'Duration: {round(time.time() - start, 3)} s')


@lru_cache(maxsize=512)
def fib_memoization(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    return fib_memoization(number - 1) + fib_memoization(number - 2)


start = time.time()
fib_memoization(40)

print(f'Duration: {round(time.time() - start, 3)} s')
