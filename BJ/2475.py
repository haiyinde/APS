numbers = list(map(int, input().split()))

total = 0
for num in numbers:
    total += num**2

result = total % 10

print(result)