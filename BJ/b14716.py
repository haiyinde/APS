# DFS
import sys
sys.setrecursionlimit(10**9) ## 재귀 10^9까지 풀어주는 함수?? 이게 머람

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, 1, -1] # 상, 하, 좌, 우, 대각선

def DFS(i, j):
    banner[i][j] = 0  # 지나간 곳을 0으로 처리하면서 visited 처리하는듯

    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < M and 0 <= nj < N and banner[ni][nj] == 1:
            DFS(ni, nj)

M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]
result = 0

for i in range(M):
    for j in range(N):
        if banner[i][j] == 1:
            DFS(i, j)
            result += 1

print(result)

