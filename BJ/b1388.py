import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
graph = []
for _ in range(N):
  graph.append(list(INPUT()[:-1]))
answer = 0

def dfs(x, y):
  if graph[x][y] == '|':
    graph[x][y] = 'o'

    for _x in [1, -1]:
      X = x + _x
      if (X > 0 and X < N) and graph[X][y] == '|':
        dfs(X, y)

  if graph[x][y] == '-':
    graph[x][y] = 'o'

    for _y in [1, -1]:
      Y = y + _y
      if (Y > 0 and Y < M) and graph[x][Y] == '-':
        dfs(x, Y)

for i in range(N):
  for j in range(M):
    if graph[i][j] == '|' or graph[i][j] == '-':
      dfs(i, j)
      answer += 1
print(answer)