import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M)//2):
        x, y = i, i
        temp = data[x][y]

        # 안쪽까지 계속 고려해야하기 때문에 n-i랑 m-i까지로 범위 설정
        for j in range(i+1, N-i):  # 좌
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i+1, M-i):  # 하
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i+1, N-i):  # 우
            x = N - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i+1, M-i):  # 상
            y = M - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

for i in range(N):
    for j in range(M):
        print(data[i][j], end=" ")
    print()