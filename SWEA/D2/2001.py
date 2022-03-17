import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    # print(arr)
    best = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    kill += int(arr[a][b])
            if kill >= best:
                best = kill

    print("#{} {}".format(test_case, best))