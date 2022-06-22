parenthesis: list = list(input())
stack: list = list()
result: int = 0
tmp: int = 1

for i in range(len(parenthesis)):
    if parenthesis[i] == "(":
        stack.append(parenthesis[i])
        tmp *= 2
    elif parenthesis[i] == "[":
        stack.append(parenthesis[i])
        tmp *= 3
    elif parenthesis[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if parenthesis[i-1] == "(":
            result += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if parenthesis[i-1] == "[":
            result += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(result)