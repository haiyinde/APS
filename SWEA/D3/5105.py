# D3
import sys
sys.stdin = open("sample_input.txt", "r")

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]  # 상 하 좌 우

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def get_out(i, j):
    Q = [[i, j]]
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while Q:
        ti, tj = Q.pop(0)
        for d in range(4):
            ni = ti + di[d]
            nj = tj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] == 0 and visited[ni][nj] == 0:
                    Q.append([ni, nj])
                    visited[ni][nj] = visited[ti][tj] + 1
                elif maze[ni][nj] == 3:
                    return visited[ti][tj] -1

    return 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    start_i, start_j = find_start()

    print("#{} {}".format(t, get_out(start_i, start_j)))