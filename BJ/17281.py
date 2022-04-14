def solution():
    out = 0
    while out <= 2:
        for i in range(9):
            if data[0][i] == 0 or data[1][i] == 0:
            # if A[i] == 0 or B[i] == 0:
                out += 1


N = int(input())  # 이닝 수
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(N)]

solution()