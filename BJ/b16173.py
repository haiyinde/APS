# DFS 재귀말고 스택으로 풀어보기

di = [0, 1]
dj = [1, 0]  # 오른쪽, 아래

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
stack = []
stack.append((0, 0))
result = "Hing"

while stack:
    i, j = stack.pop()
    visited[i][j] = True

    if board[i][j] == -1:
        result = "HaruHaru"
        break

    for d in range(2):
        ni = i + di[d] * board[i][j]
        nj = j + dj[d] * board[i][j]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            stack.append((ni, nj))

print(result)