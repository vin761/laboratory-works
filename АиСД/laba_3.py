def scobki():
    expr = input("Введите скобочную последовательность:")
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return print(False)
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return print(False)
            if current_char == '{':
                if char != "}":
                    return print(False)
            if current_char == '[':
                if char != "]":
                    return print(False)
    if stack:
        return print(False)
    return print(True)


def polskay_zapis():
    polzap = list(map(str, input('Введите польскую запись:').split()))
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