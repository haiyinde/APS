import sys
sys.stdin = open("sample_input.txt", "r")

di = [0, 0, 1, -1]
dj = []

def climb(i, j):
    global difficulty, temp

    if temp < min(difficulty):
        difficulty = temp
        return

    if cliff[i][j] == 3:
        return
    else:
        for h in range(1, i+1):  # N : 암벽의 총 높이 / i+1 이동할 수 있는 총 높이
            if cliff[i+h][j] == 1:
                temp = h
                climb(i+h, j)


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # 암벽의 높이 N, 너비 M
    cliff = [list(map(int, input().split())) for _ in range(N)]
    difficulty = [N]  # 각 이동경로의 최대 높이 저장.
    temp = 0

    for i in range(N - 1, -1, -1):
        climb(i, 0)

    print("#{} {}".format(test_case, min(difficulty)))