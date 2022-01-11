str = list(input())
stack = []
c = 0  #

for s in str:
    if s == ')':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2*t)
                break
            elif top == '[':
                print(0)
                exit(0)  # 프로그램을 종료 exit()
            else:
                t = t + int(top)
    elif s == ']':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3*t)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                t = t + int(top)
    else:
        stack.append(s)

for s in stack:
    if s == '(' or s == '[':
        print(0)
        exit(0)
    else:
        c += s

print(c)
