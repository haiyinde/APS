# 계수 정렬 => 시간 초과
N = int(input())
numbers = list(int(input()) for _ in range(N))

storage = [0] * 10000

for num in numbers:
    storage[num-1] += 1

for i in range(10000):
    if storage[i] != 0:
        for j in range(storage[i]):
            print(i+1)