import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())  # 앞마당의 길이 N 대회의 시간 M
a = list(map(int, input().split()))  # 수열 a
snowball = 1
loc = 0
biggest = -1

while M != 0 and loc < N:
    M -= 1
    loc += 1
    snowball += a[loc]

    loc += 2
    snowball = snowball//2 + a[loc]
