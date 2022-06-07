N = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
for i in range(1, N+1):
    total += sum(times[:i])

print(total)