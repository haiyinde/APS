def solution(s):
    if len(s) == 1:
        return 0

    stack = []
    for i in s:
        stack.append(i)

        while len(stack) >= 2:
            c1 = stack.pop()  # a
            c2 = stack.pop()  # b
            if c1 != c2:
                stack.append(c2)
                stack.append(c1)
                break

    return 0 if len(stack) else 1