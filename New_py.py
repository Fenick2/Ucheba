import time
from random import randint


N = 6000
lst = []
for i in range(N):
    lst.append(randint(1, 999))

time_start = time.perf_counter()

# def bubble_sort(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(n - i - 1):
#             #already_sorted = True
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 #already_sorted = False
#         # if already_sorted:
#         #     break
#     return array


# bubble_sort(lst)
# time_end = time.perf_counter()
# total_time = time_end - time_start
# print(f'Время исполнения: {total_time:0.2f}')


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array


insertion_sort(lst)
time_end = time.perf_counter()
total_time = time_end - time_start
print(f'Время исполнения: {total_time:0.2f}')
