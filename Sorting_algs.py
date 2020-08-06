import time
from random import randint


lst = [randint(1, 99) for i in range(10_000)]

time_start = time.perf_counter()

# def bubble_sort(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(n - i - 1):
#             already_sorted = True
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 already_sorted = False
#         if already_sorted:
#             break
#     return array


# bubble_sort(lst)
# time_end = time.perf_counter()
# total_time = time_end - time_start
# print(f'Время исполнения: {total_time:0.2f}')


# def insertion_sort(array):
#     for i in range(1, len(array)):
#         key_item = array[i]
#         j = i - 1
#         while j >= 0 and array[j] > key_item:
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = key_item

#     return array


# insertion_sort(lst)
# time_end = time.perf_counter()
# total_time = time_end - time_start
# print(f'Время исполнения: {total_time:0.2f}')


# def merge(left, right):
#     if len(left) == 0:
#         return right
#     if len(right) == 0:
#         return left

#     result = []
#     index_left = index_right = 0

#     while len(result) < len(left) + len(right):
#         # The elements need to be sorted to add them to the
#         # resultant array, so you need to decide whether to get
#         # the next element from the first or the second array
#         if left[index_left] <= right[index_right]:
#             result.append(left[index_left])
#             index_left += 1
#         else:
#             result.append(right[index_right])
#             index_right += 1

#         # If you reach the end of either array, then you can
#         # add the remaining elements from the other array to
#         # the result and break the loop
#         if index_right == len(right):
#             result += left[index_left:]
#             break
#         if index_left == len(left):
#             result += right[index_right:]
#             break
#     return result


# def merge_sort(array):
#     if len(array) < 2:
#        return array

#     midpoint = len(array) // 2

#     # Sort the array by recursively splitting the input
#     # into two equal halves, sorting each half and merging them
#     # together into the final result
#     return merge(
#         left=merge_sort(array[:midpoint]),
#         right=merge_sort(array[midpoint:]))


# merge_sort(lst)
# time_end = time.perf_counter()
# total_time = time_end - time_start
# print(f'Время исполнения: {total_time:0.2f}')


# def quicksort(array):
#     if len(array) < 2:
#         return array

#     low, same, high = [], [], []

#     # Select your `pivot` element randomly
#     pivot = array[randint(0, len(array) - 1)]

#     for item in array:
#         if item < pivot:
#             low.append(item)
#         elif item == pivot:
#             same.append(item)
#         elif item > pivot:
#             high.append(item)
#     return quicksort(low) + same + quicksort(high)


# quicksort(lst)
# time_end = time.perf_counter()
# total_time = time_end - time_start
# print(f'Время исполнения: {total_time:0.2f}')


def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # Loop from the element indicated by
    # `left` until the element indicated by `right`
    for i in range(left + 1, right + 1):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if the `key_item` is smaller than its adjacent values.
        while j >= left and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition `j` to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, position
        # the `key_item` in its correct location
        array[j + 1] = key_item

    return array


def timsort(array):
    min_run = 32
    n = len(array)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2

    return array