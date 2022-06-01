N = int(input())
numbers = list(int(input()) for _ in range(N))

numbers.sort()

for num in numbers:
    print(num)