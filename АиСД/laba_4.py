def poisc_v_glub():
    kolvo_versh = int(input("Введите количество вершин:"))
    start, fin = map(str, input("Введите вершину начала поиска и конца, через пробел:").split())
    A = [["0" for i in range(kolvo_versh)] for j in range(kolvo_versh)]
    for i in range(1, kolvo_versh + 1):
        for j in range(i, kolvo_versh + 1):
            c = input("Есть связь между вершиной " + str(i) + " и " + str(j) + "? Введите да/нет:")
            if c == "да":
                A[i - 1][j - 1], A[j - 1][i - 1] = "1", "1"
            else:
                A[i - 1][j - 1], A[j - 1][i - 1] = "0", "0"

    graf = {}
    for i in range(kolvo_versh):
        smej = []
        for j in range(kolvo_versh):
            if A[i][j] == "1":
                smej.append(str(j + 1))
        graf[str(i + 1)] = smej

    def dfs_paths(graph, start, fin):
        stack = [(start, [start])]  # (vertex, path)
        while stack:
            (vertex, path) = stack.pop()
            for next in set(graph[vertex]) - set(path):
                if next == fin:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    pyti = list(dfs_paths(graf, start, fin))
    for i in range(len(pyti)):
        print("Путь прохода: " + str(pyti[i]) + ". Расстояние:" + str(len(pyti[i]) - 1))


def dijkstra():
    def dijkstra_shortest_path(graph, start, p={}, u=[]):
        if len(p) == 0: p[start] = 0  # инициализация начального пути
        for x in graph[start]:
            if (x not in u and x != start):
                if (x not in p.keys() or (graph[start][x] + p[start]) < p[x]):
                    p[x] = graph[start][x] + p[start]

        u.append(start)

        min_v = 0
        min_x = None
        for x in p:
            if (p[x] < min_v or min_v == 0) and x not in u:
                min_x = x
                min_v = p[x]

        if (len(u) < len(graph) and min_x):
            return dijkstra_shortest_path(graph, min_x, p, u)
        else:
            return p

    kolvo_versh = int(input("Введите количество вершин:"))
    start = input("Введите вершину начала поиска:")
    A = [["0" for i in range(kolvo_versh)] for j in range(kolvo_versh)]
    for i in range(1, kolvo_versh + 1):
        for j in range(i, kolvo_versh + 1):
            c = input("Если есть связь между вершиной " + str(i) + " и " + str(j) + ". Введите его длину, если нет - введите 0:")
            A[i - 1][j - 1], A[j - 1][i - 1] = int(c), int(c)

    graf = {}
    for i in range(kolvo_versh):
        pyti = {}
        for j in range(kolvo_versh):
            if A[i][j] != 0:
                pyti[str(j + 1)] = A[i][j]
        graf[str(i + 1)] = pyti

    print(dijkstra_shortest_path(graf, start))