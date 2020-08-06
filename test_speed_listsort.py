from random import randint
from boxx import timeit


def list_sort(arr: list):
    return arr.sort()


def sorted_builting(arr: list):
    return sorted(arr)


def main():
    arr = [randint(1, 99) for _ in range(1_000_000)]

    with timeit(name='sorted(list)'):
        sorted_builting(arr)

    with timeit(name='list.sort()'):
        list_sort(arr)


if __name__=='__main__':
    main()
