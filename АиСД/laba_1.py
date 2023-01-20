from time import *


def bubble_sort():
    Q = list(map(int, input("Введите елементы массива через пробел:").split()))
    start = time()
    sleep(0.05)
    for i in range(len(Q) - 1):
        for j in range(len(Q) - i - 1):
            if Q[j] > Q[j + 1]:
                Q[j], Q[j + 1] = Q[j + 1], Q[j]
    return print(Q, f'Время работы кода: {time() - start - 0.05}', sep='\n')


def selection_sort():  # Сортировка выбором
    B = list(map(int, input("Введите елементы массива через пробел:").split()))
    start = time()
    sleep(0.05)
    c = 0
    for i in range(c, len(B) - 1):
        m = min(B[c:])
        k = B.index(m)
        B[c], B[k] = B[k], B[c]
        c += 1
    return print(B, f'Время работы кода: {time() - start - 0.05}', sep='\n')


def insertion_sort():  # Сортировка вставкой
    C = list(map(int, input("Введите елементы массива через пробел:").split()))
    start = time()
    sleep(0.05)
    for i in range(1, len(C)):
        for j in range(i, 0, -1):
            if C[j] < C[j - 1]:
                C[j - 1], C[j] = C[j], C[j - 1]
    return print(C, f'Время работы кода: {time() - start - 0.05}', sep='\n')
