# D2
import sys
sys.stdin = open("input.txt", "r")

def rotate(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r9_arr = rotate(arr, N)
    r18_arr = rotate(r9_arr, N)
    r27_arr = rotate(r18_arr, N)

    print("#{}".format(t))
    for a1, a2, a3 in zip(r9_arr, r18_arr, r27_arr):
        print("{} {} {}".format("".join(map(str, a1)), "".join(map(str, a2)), "".join(map(str, a3))))