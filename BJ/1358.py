W, H, X, Y, P = map(int, input().split())
athletes = [list(map(int, input().split())) for _ in range(P)]
R = H//2
result = 0

for a in athletes:
    i, j = a[0], a[1]
    if ((i-X)**2 + (j-(Y+R))**2)**0.5 <= R:
        result += 1
    elif X <= i <= X+W and Y <= j <= Y+H:
        result += 1
    elif ((i-(X+W))**2 + (j-(Y+R))**2)**0.5 <= R:
        result += 1

print(result)