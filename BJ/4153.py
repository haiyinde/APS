while True:
    length = sorted(list(map(int, input().split())))
    a, b, c = length[0], length[1], length[2]
    if a == b == c == 0:
        break
    if (a**2) + (b**2) == (c**2):
        print("right")
    else:
        print("wrong")
