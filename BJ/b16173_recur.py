# DFS, S5
import sys
input = sys.stdin.readline

N = int(input())
district = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1]
dj = [1, 0]

visited = [[False] * N for _ in range(N)]

def dfs(i, j):
    if not (0 <= i < N and 0 <= j < N):
        return False
    # 오늘의 교훈.. visited를 잘 체크하자..
    if visited[i][j] == True:
        return False
    if district[i][j] == -1:
        print("HaruHaru")
        exit()
    visited[i][j] = True
    for d in range(2):
        ni = i + di[d] * district[i][j]
        nj = j + dj[d] * district[i][j]
        dfs(ni, nj)
    return True

if dfs(0, 0) == True:
    print("Hing")
