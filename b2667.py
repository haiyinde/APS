# DFS
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]  # 상 하 좌 우

N = int(input())  # 지도의 크기 N
housing_area = [list(map(int, input())) for _ in range(N)]
num = []

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:  # 범위를 벗어나면
        return False
    if housing_area[x][y] == 1:  # 집을 찾으면
        global count
        count += 1
        housing_area[x][y] = 0  # 0으로 바꾼다
        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]
            dfs(nx, ny)
        return True
    return False

count = 0
result = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])