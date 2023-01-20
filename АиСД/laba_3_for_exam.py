from time import *
import random

'====LABA1===='
def laba_1(nomer):
    n = int(input('Введите размер массива:'))
    A = [random.randint(-100, 100) for i in range(n)]

    def bubble_sort(Q):
        start = time()
        sleep(0.05)
        for i in range(len(Q) - 1):
            for j in range(len(Q) - i - 1):
                if Q[j] > Q[j + 1]:
                    Q[j], Q[j + 1] = Q[j + 1], Q[j]
        return print(Q, f'Время работы кода: {time() - start - 0.05}', sep = '\n')

    def selection_sort(B): # Сортировка выбором
        start = time()
        sleep(0.05)
        c = 0
        for i in range(c, len(B) - 1):
            m = min(B[c:])
            k = B.index(m)
            B[c], B[k] = B[k], B[c]
            c += 1
        return print(B, f'Время работы кода: {time() - start - 0.05}', sep='\n')

    def insertion_sort(C): # Сортировка вставкой
        start = time()
        sleep(0.05)
        for i in range(1, len(C)):
            for j in range(i, 0, -1):
                if C[j] < C[j - 1]:
                    C[j - 1], C[j] = C[j], C[j - 1]
        return print(C, f'Время работы кода: {time() - start - 0.05}', sep='\n')

    if nomer == 1:
        bubble_sort(A)
    elif nomer == 2:
        selection_sort(A)
    elif nomer == 3:
        insertion_sort(A)
    else:
        print('В первой лабе есть 1-е, 2-е и 3-е задания. Выберете одно из них!')



'====LABA2===='
def laba_2(nomer):
    def zadanie_1():
        n, m = map(int, input('Введите размер матрицы (n m):'). split())
        A = [[random.randint(-100, 100) for i in range(m)] for j in range(n)]
        [print(*row) for row in A]
        print('-----------')
        def sort_hoara(A):

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
                return sort_hoara(l_list) + m_list + sort_hoara(r_list)

        B = [[] for k in range(n)]
        for i in range(m):
            stolb = []
            for j in range(n):
                stolb.append(A[j][i])
            stolb = sort_hoara(stolb)
            for i in range(n):
                B[i].append(stolb[i])
        [print(*row) for row in B]

    def zadanie_2():
        def sort_slil(B):
            if len(B) > 1:
                mid = len(B)//2
                left = B[:mid]
                right = B[mid:]
                sort_slil(left)
                sort_slil(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        B[k] = left[i]
                        i+=1
                    else:
                        B[k] = right[j]
                        j+=1
                    k+=1

                while i < len(left):
                    B[k] = left[i]
                    i+=1
                    k+=1

                while j < len(right):
                    B[k] = right[j]
                    j+=1
                    k+=1

        c = int(input('Введите размер массива:'))
        B = [random.randint(-100, 100) for i in range(c)]
        print(B)
        sort_slil(B)
        print('---------')
        print(B)


    def zadanie_3():
        mas = list(map(int, input('Введите массив:').split()))
        mas.sort()
        x = int(input('Введите искомое значение:'))


        def binar_poisk(mas, x):
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

        binar_poisk(mas, x)
    if nomer == 1:
        zadanie_1()
    elif nomer == 2:
        zadanie_2()
    elif nomer == 3:
        zadanie_3()
    else:
        print('Во второй лабе есть 1-е, 2-е и 3-е задания. Выберете одно из них!')



def laba_3(nomer):
    def scobki(expr):
        stack = []
        for char in expr:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False
        if stack:
            return False
        return True

    def zadanie_2():
        polzap = list(map(str, input('Введите польскую запись:').split()))
        def polskay_zapis(polzap):
            mat_op = ["+", "-", "*", "/"]
            stack = []
            if len(polzap) == 0:
                return print('0')
            else:
                for a in polzap:
                    if a not in mat_op:
                        stack.append(a)
                    else:
                        b = int(stack.pop())
                        c = int(stack.pop())
                        if a == "+":
                            stack.append(str(c + b))
                        elif a == "-":
                            stack.append(str(c - b))
                        elif a == "*":
                            stack.append(str(c * b))
                        elif a == "/":
                            stack.append(str(int(c / b)))
            return print(*stack)
        polskay_zapis(polzap)


    if nomer == 1:
        zadanie_1()
    elif nomer == 2:
        zadanie_2()
    else:
        print('В третьей лабе есть 1-е и 2-е задания. Выберете одно из них!')






laba = int(input('Введите номер лабы:'))
nomer = int(input('Введите номер задания:'))

while laba in [1, 2, 3]:
    if laba == 1:
        laba_1(nomer)
    elif laba == 2:
        laba_2(nomer)
    elif laba == 3:
        laba_3(nomer)
    else:
        break
    laba = int(input('Введите номер лабы:'))
    nomer = int(input('Введите номер задания:'))