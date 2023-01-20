import random


def sort_hoara():
    n, m = map(int, input('Введите размер матрицы:').split())
    A = [[random.randint(-100, 100) for i in range(m)] for j in range(n)]
    [print(*row) for row in A]
    print('-----------')

    def hoara(A):
        if len(A) <= 1:
            return A
        else:
            rc = random.choice(A)
            l_list = []
            m_list = []
            r_list = []
            for value in A:
                if value < rc:
                    l_list.append(value)
                elif value > rc:
                    r_list.append(value)
                else:
                    m_list.append(value)
            return hoara(l_list) + m_list + hoara(r_list)

    B = [[] for k in range(n)]
    for i in range(m):
        stolb = []
        for j in range(n):
            stolb.append(A[j][i])
        stolb = hoara(stolb)
        for i in range(n):
            B[i].append(stolb[i])
    [print(*row) for row in B]


def sort_slil():
    def slil(B):
        if len(B) > 1:
            mid = len(B) // 2
            left = B[:mid]
            right = B[mid:]
            slil(left)
            slil(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    B[k] = left[i]
                    i += 1
                else:
                    B[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                B[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                B[k] = right[j]
                j += 1
                k += 1

    c = int(input('Введите размер массива:'))
    B = [random.randint(-100, 100) for i in range(c)]
    print(B)
    slil(B)
    print('---------')
    print(B)


def binar_poisk():
    mas = list(map(int, input('Введите массив:').split()))
    mas.sort()
    x = int(input('Введите искомое значение:'))

    def binar(mas, x):
        left = 0
        right = len(mas) - 1

        while left <= right:

            midl = (left + right) // 2
            if mas[midl] == x:
                return print(midl)
            elif mas[midl] > x:
                right = midl - 1
            else:
                left = midl + 1
        return print('Элемент в массиве не найден')

    binar(mas, x)
