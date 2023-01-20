from heapq import *


def piramid_sort_1():
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heapSort(arr):
        n = len(arr)
        for i in range(n, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    arr = list(map(int, input("Введите элементы массива через пробел:").split()))
    heapSort(arr)
    n = len(arr)
    print("Отсортированый список:", arr)


def piramid_sort_2():
    def heapsort(iterable):
        h = []
        for value in iterable:
            heappush(h, value)
        return [heappop(h) for i in range(len(h))]

    iterable = list(map(int, input("Введите элементы массива через пробел:").split()))
    print(heapsort(iterable))