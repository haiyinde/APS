#D2  
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    result = 0

    if N < M:
        for i in range(M-N+1):
            tmp = 0
            for j in range(N):
                tmp += Ai[j] * Bj[i+j]
            if tmp > result:
                result = tmp

    if N > M:
        for i in range(N-M+1):
            tmp = 0
            for j in range(M):
                tmp += Bj[j] * Ai[i+j]
            if tmp > result:
                result = tmp

    print("#{} {}".format(t, result))
