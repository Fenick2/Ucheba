def binary_search(lst: list, item):
    lst.sort()
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return


my_list = list(range(484, 36890, 4))
print(binary_search(my_list, 6752))
