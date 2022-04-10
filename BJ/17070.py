# 골드5, 파이프 옮기기
# 동적 프로그래밍, 다이나믹 프로그래밍
# 그래프 이론
import sys
input = sys.stdin.readline

def solution():
    # 주어진 첫 위치로 인해 0,1 위치의 가로로 끝나는 파이프의 갯수 1
    dp[0][0][1] = 1
    for i in range(2, N):   # 0,1 처리해줬으니 0,2부터 탐색하기
        if graph[0][i] == 0:  # 빈 공간이면
            dp[0][0][i] = dp[0][0][i-1]  # 이전 파이프의 가로 갯수

    for r in range(1, N):
        for c in range(1, N):
            # 대각선 파이프를 추가하는 과정 => 대각선 파이프의 경우 세 칸이 모두 비어있어야 한다.
            if graph[r][c] == 0 and graph[r][c-1] == 0 and graph[r-1][c] == 0:
                dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            # 가로 파이프 = 대각선 + 가로
            if graph[r][c] == 0:
                dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
            # 세로 파이프 = 대각선 + 세로
                dp[2][r][c] = dp[1][r-1][c] + dp[2][r-1][c]

    print(sum(dp[i][N-1][N-1] for i in range(3)))
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
# dp[0][row][col] 가로
# dp[1][row][col] 대각선
# dp[2][row][col] 세로

solution()
