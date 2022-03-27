# D3
import sys
sys.stdin = open("sample_input.txt", "r")
 
# di = [0, 0, -1, 1]
# dj = [-1, 1, 0, 0]
#
def checkNext(i, j, direction):
    if data[i][j] == "#":
        checkNext(i+1, j+1, )
    else:
        checkNext(i)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]

    for i in range(N):
        for j range(N):
            if data[i][j] == "#":

