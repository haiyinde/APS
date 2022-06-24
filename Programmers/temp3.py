di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def solution(N, bus_station: list):
    result = list([-1] * N for _ in range(N))
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = []

    for b in bus_station:
        x, y = b[0], b[1]
        result[x][y] = 0
        queue.append([x, y, 0])

    while queue:
        t = queue.pop(0)
        i, j, length = t[0], t[1], t[2]

        if visited[i][j]:
            continue
        visited[i][j] = True

        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                result[ni][nj] = length+1
                queue.append([ni, nj, length+1])

    return result

print(solution(3, [[0, 1]]))
print(solution(3, [[0, 1], [2, 2]]))