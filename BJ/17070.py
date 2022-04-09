# 골드5, 파이프 옮기기
# 동적 프로그래밍, 다이나믹 프로그래밍
# 그래프 이론
import sys
input = sys.stdin.readline

def solution():
    # 첫 위치가
    dp[0][0][1] = 1


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
dp[0][row][col] 가로
dp[1][row][col] 대각선
dp[2][row][col] 세로

solution()



# print(N)
# print(graph)
