N = int(input())
numbers = list(map(str, range(1, N+1)))

for i in range(N):
    cnt = 0
    for s in numbers[i]:
        if s in ["3", "6", "9"]:
            cnt += 1
            numbers[i] = "-" * cnt

print(*numbers)