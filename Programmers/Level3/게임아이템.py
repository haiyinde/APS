from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


def solution(n, m, images):
    visited = list([False] * m for _ in range(n))
    answer = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue

            color = images[i][j]
            visited[i][j] = True
            Q = deque([(i, j)])

            while Q:
                ci, cj = Q.popleft()

                for d in range(4):
                    ni = ci + di[d]
                    nj = cj + dj[d]

                    if 0 <= ni < n and 0 <= nj < m and color == images[ni][nj] and not visited[ni][nj]:
                        visited[ni][nj] = True
                        Q.append((ni, nj))

            answer += 1

    return answer