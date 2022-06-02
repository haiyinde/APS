import sys
# 계수 정렬 => 메모리 초과
# Pypy3 : 메모리 초과 //  Python3 : 통과
N = int(input())
storage = [0] * 10000

# for num in numbers:
#     storage[num-1] += 1

for i in range(N):
    num = int(sys.stdin.readline())
    storage[num-1] += 1

for i in range(10000):
    if storage[i] != 0:
        for j in range(storage[i]):
            print(i+1)