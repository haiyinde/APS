N = int(input())
numbers = list(map(int, input().split()))
prime = 0
for num in numbers:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime += 1

print(prime)