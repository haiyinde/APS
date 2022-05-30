N = int(input())
numbers = list(int(input()) for _ in range(N))

for i in range(N):
    for j in range(i+1, N):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for n in numbers:
    print(n)