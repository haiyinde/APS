T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        Y = N//H
        X = H
    else:
        Y = (N//H)+1
        X = N%H

    print("{}".format(100*X+Y))