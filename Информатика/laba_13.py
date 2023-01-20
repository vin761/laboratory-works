import math

def zadanie_1():
    a, b, c = map(int, input("Введите длины ребер a, b и c через пробел:").split())
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    print("Объем равен: " + str(V))
    print("Площади поверхности равна: " + str(S))

def zadanie_2():
    x = 1
    y = 5
    z = 10
    a = y + (x / (z**2 + abs(x**2 / (y + (x**3)/3))))
    b = (1 + math.asin(x**2) + (math.tan(z/2))**2)
    print("Значение a: " + str(round(a, 2)))
    print("Значение b: " + str(round(b, 2)))

def zadanie_3():
    a, b, c = map(int, input("Введите длины сторон треугольника a, b и c через пробел:").split())
    if a == b == c:
        print("Треугольник со сторонами a, b, c является равносторонним")
    else:
        print("Треугольник со сторонами a, b, c не является равносторонним")

def zadanie_4():
    A = []
    x = int(input("Введите число последовательности:"))
    while x < 0:
        A.append(x)
        x = int(input("Введите число последовательности:"))

    sred_arif = sum(A) / len(A)
    print("Среднее арифметическое равно: " + str(sred_arif))

zadanie_4()

